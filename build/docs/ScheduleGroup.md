---
title: ScheduleGroup
---
## ScheduleGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** | The resource&#39;s description. | [optional] |
| **version** | **int** | The current version of the resource. | [optional] |
| **date_created** | **datetime** | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the resource. | [optional] |
| **created_by** | **str** | The ID of the user that created the resource. | [optional] |
| **state** | **str** | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the resource. | [optional] |
| **created_by_app** | **str** | The application that created the resource. | [optional] |
| **time_zone** | **str** | The timezone the schedules are a part of.  This is not a schedule property to allow a schedule to be used in multiple timezones. | [optional] |
| **open_schedules** | [**list[UriReference]**](UriReference.html) | The schedules defining the hours an organization is open. | [optional] |
| **closed_schedules** | [**list[UriReference]**](UriReference.html) | The schedules defining the hours an organization is closed. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

