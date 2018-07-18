---
title: OrgUser
---
## OrgUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **chat** | [**Chat**](Chat.html) |  | [optional] |
| **department** | **str** |  | [optional] |
| **email** | **str** |  | [optional] |
| **primary_contact_info** | [**list[Contact]**](Contact.html) | Auto populated from addresses. | [optional] |
| **addresses** | [**list[Contact]**](Contact.html) | Email addresses and phone numbers for this user | [optional] |
| **state** | **str** | The current state for this user. | [optional] |
| **title** | **str** |  | [optional] |
| **username** | **str** |  | [optional] |
| **manager** | [**User**](User.html) |  | [optional] |
| **images** | [**list[UserImage]**](UserImage.html) |  | [optional] |
| **version** | **int** | Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH. | |
| **routing_status** | [**RoutingStatus**](RoutingStatus.html) | ACD routing status | [optional] |
| **presence** | [**UserPresence**](UserPresence.html) | Active presence | [optional] |
| **conversation_summary** | [**UserConversationSummary**](UserConversationSummary.html) | Summary of conversion statistics for conversation types. | [optional] |
| **out_of_office** | [**OutOfOffice**](OutOfOffice.html) | Determine if out of office is enabled | [optional] |
| **geolocation** | [**Geolocation**](Geolocation.html) | Current geolocation position | [optional] |
| **station** | [**UserStations**](UserStations.html) | Effective, default, and last station information | [optional] |
| **authorization** | [**UserAuthorization**](UserAuthorization.html) | Roles and permissions assigned to the user | [optional] |
| **profile_skills** | **list[str]** | Skills possessed by the user | [optional] |
| **locations** | [**list[Location]**](Location.html) | The user placement at each site location. | [optional] |
| **groups** | [**list[Group]**](Group.html) | The groups the user is a member of | [optional] |
| **acd_auto_answer** | **bool** | acd auto answer | [optional] |
| **organization** | [**Organization**](Organization.html) |  | [optional] |
{: class="table table-striped"}


