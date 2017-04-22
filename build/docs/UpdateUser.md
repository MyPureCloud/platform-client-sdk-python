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
| **primary_contact_info** | [**list[Contact]**](Contact.html) |  | [optional] |
| **addresses** | [**list[Contact]**](Contact.html) | Email addresses and phone numbers for this user | [optional] |
| **title** | **str** |  | [optional] |
| **username** | **str** |  | [optional] |
| **manager** | **str** |  | [optional] |
| **images** | [**list[UserImage]**](UserImage.html) |  | [optional] |
| **version** | **int** | Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH. | [optional] |
| **profile_skills** | **list[str]** | Skills possessed by the user | [optional] |
| **locations** | [**list[Location]**](Location.html) | The user placement at each site location. | [optional] |
| **groups** | [**list[Group]**](Group.html) | The groups the user is a member of | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


