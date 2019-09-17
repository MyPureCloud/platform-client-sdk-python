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
| **display_name** | **str** | The display name for the user. | |
| **password** | **str** | A new password for a PureCloud user. Does not return an existing password. | [optional] |
| **title** | **str** | The user&#39;s title. | [optional] |
| **phone_numbers** | [**list[ScimPhoneNumber]**](ScimPhoneNumber.html) | A list of the user&#39;s phone numbers. | [optional] |
| **emails** | [**list[ScimEmail]**](ScimEmail.html) | A list of the user&#39;s email addresses. | [optional] |
| **photos** | [**list[Photo]**](Photo.html) | A list of the user&#39;s photos. | [optional] |
| **external_id** | **str** | The external ID of the user. Set by the provisioning client. caseExact is set to true. mutability is set to readWrite. | [optional] |
| **groups** | [**list[ScimV2GroupReference]**](ScimV2GroupReference.html) | A list of groups that the user is a member of. | [optional] |
| **roles** | **list[str]** | A list of roles assigned to the user. | [optional] |
| **urnietfparamsscimschemasextensionenterprise2_0_user** | [**ScimV2EnterpriseUser**](ScimV2EnterpriseUser.html) |  | [optional] |
{: class="table table-striped"}


