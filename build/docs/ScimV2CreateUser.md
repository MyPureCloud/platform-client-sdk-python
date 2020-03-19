---
title: ScimV2CreateUser
---
## ScimV2CreateUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **active** | **bool** | Indicates whether the user&#39;s administrative status is active. | [optional] |
| **user_name** | **str** | The user&#39;s PureCloud email address. Must be unique. | |
| **display_name** | **str** | The display name of the user. | |
| **password** | **str** | The new password for the PureCloud user. Does not return an existing password. | [optional] |
| **title** | **str** | The user&#39;s title. | [optional] |
| **phone_numbers** | [**list[ScimPhoneNumber]**](ScimPhoneNumber.html) | The list of the user&#39;s phone numbers. | [optional] |
| **emails** | [**list[ScimEmail]**](ScimEmail.html) | The list of the user&#39;s email addresses. | [optional] |
| **external_id** | **str** | The external ID of the user. Set by the provisioning client. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readWrite\&quot;. | [optional] |
| **groups** | [**list[ScimV2GroupReference]**](ScimV2GroupReference.html) | The list of groups that the user is a member of. | [optional] |
| **roles** | [**list[ScimUserRole]**](ScimUserRole.html) | The list of roles assigned to the user. | [optional] |
| **urnietfparamsscimschemasextensionenterprise2_0_user** | [**ScimV2EnterpriseUser**](ScimV2EnterpriseUser.html) | The URI of the schema for the enterprise user. | [optional] |
| **urnietfparamsscimschemasextensiongenesyspurecloud2_0_user** | [**ScimUserExtensions**](ScimUserExtensions.html) |  | [optional] |
{: class="table table-striped"}


