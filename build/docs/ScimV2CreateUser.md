---
title: ScimV2CreateUser
---
## ScimV2CreateUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **active** | **bool** | Indicates whether the user&#39;s administrative status is active. | [optional] |
| **user_name** | **str** | The user&#39;s Genesys Cloud email address. Must be unique. | |
| **display_name** | **str** | The display name of the user. | |
| **password** | **str** | The new password for the Genesys Cloud user. Does not return an existing password. When creating a user, if a password is not supplied, then a password will be randomly generated that is 40 characters in length and contains five characters from each of the password policy groups. | [optional] |
| **title** | **str** | The user&#39;s title. | [optional] |
| **phone_numbers** | [**list[ScimPhoneNumber]**](ScimPhoneNumber.html) | The list of the user&#39;s phone numbers. | [optional] |
| **emails** | [**list[ScimEmail]**](ScimEmail.html) | The list of the user&#39;s email addresses. | [optional] |
| **external_id** | **str** | The external ID of the user. Set by the provisioning client. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readWrite\&quot;. | [optional] |
| **groups** | [**list[ScimV2GroupReference]**](ScimV2GroupReference.html) | The list of groups that the user is a member of. This list is immutable per SCIM RFC and may only be updated using the GROUPS resource endpoint. | [optional] |
| **roles** | [**list[ScimUserRole]**](ScimUserRole.html) | The list of roles assigned to the user. | [optional] |
| **urnietfparamsscimschemasextensionenterprise2_0_user** | [**ScimV2EnterpriseUser**](ScimV2EnterpriseUser.html) | The URI of the schema for the enterprise user. | [optional] |
| **urnietfparamsscimschemasextensiongenesyspurecloud2_0_user** | [**ScimUserExtensions**](ScimUserExtensions.html) | The URI of the schema for the Genesys Cloud user. | [optional] |
{: class="table table-striped"}


