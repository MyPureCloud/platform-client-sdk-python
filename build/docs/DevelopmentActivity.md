---
title: DevelopmentActivity
---
## DevelopmentActivity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **date_completed** | **datetime** | Date that activity was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **created_by** | [**UserReference**](UserReference.html) | User that created activity | [optional] |
| **date_created** | **datetime** | Date activity was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **name** | **str** | The name of the activity | [optional] |
| **type** | **str** | The type of activity | [optional] |
| **status** | **str** | The status of the activity | [optional] |
| **date_due** | **datetime** | Due date for completion of the activity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **facilitator** | [**UserReference**](UserReference.html) | Facilitator of the activity | [optional] |
| **attendees** | [**list[UserReference]**](UserReference.html) | List of users attending the activity | [optional] |
| **is_overdue** | **bool** | Indicates if the activity is overdue | [optional] |
{: class="table table-striped"}


