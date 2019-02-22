---
title: UpdateUser
---
## UpdateUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **chat** | [**Chat**](Chat.html) |  | [optional] |
| **department** | **str** |  | [optional] |
| **email** | **str** |  | [optional] |
| **primary_contact_info** | [**list[Contact]**](Contact.html) | The address(s) used for primary contact. Updates to the corresponding address in the addresses list will be reflected here. | [optional] |
| **addresses** | [**list[Contact]**](Contact.html) | Email address, phone number, and/or extension for this user. One entry is allowed per media type | [optional] |
| **title** | **str** |  | [optional] |
| **username** | **str** |  | [optional] |
| **manager** | **str** |  | [optional] |
| **images** | [**list[UserImage]**](UserImage.html) |  | [optional] |
| **version** | **int** | This value should be the current version of the user. The current version can be obtained with a GET on the user before doing a PATCH. | |
| **profile_skills** | **list[str]** | Profile skills possessed by the user | [optional] |
| **locations** | [**list[Location]**](Location.html) | The user placement at each site location. | [optional] |
| **groups** | [**list[Group]**](Group.html) | The groups the user is a member of | [optional] |
| **state** | **str** | The state of the user. This property can be used to restore a deleted user or transition between active and inactive. If specified, it is the only modifiable field. | [optional] |
| **acd_auto_answer** | **bool** | The value that denotes if acdAutoAnswer is set on the user | [optional] |
| **certifications** | **list[str]** |  | [optional] |
| **biography** | [**Biography**](Biography.html) |  | [optional] |
| **employer_info** | [**EmployerInfo**](EmployerInfo.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


