---
title: Group
---
## Group

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The group name. | |
| **description** | **str** |  | [optional] |
| **date_modified** | **datetime** | Last modified date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **member_count** | **int** | Number of members. | [optional] |
| **state** | **str** | Active, inactive, or deleted state. | [optional] |
| **version** | **int** | Current version for this resource. | [optional] |
| **type** | **str** | Type of group. | |
| **images** | [**list[UserImage]**](UserImage.html) |  | [optional] |
| **addresses** | [**list[GroupContact]**](GroupContact.html) |  | [optional] |
| **rules_visible** | **bool** | Are membership rules visible to the person requesting to view the group | |
| **visibility** | **str** | Who can view this group | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


