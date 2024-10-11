# DevelopmentActivity

## DevelopmentActivity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **date_completed** | datetime | Date that activity was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | User that created activity | [optional] |
| **date_created** | datetime | Date activity was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **percentage_score** | float | The user&#39;s percentage score for this activity | [optional] |
| **is_passed** | bool | True if the activity was passed | [optional] |
| **is_latest** | bool | True if this is the latest version of assignment assigned to the user | [optional] |
| **is_module_archived** | bool | True if the associated module is archived | [optional] |
| **archival_mode** | str | Module archive type | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **name** | str | The name of the activity | [optional] |
| **type** | str | The type of activity | [optional] |
| **status** | str | The status of the activity | [optional] |
| **date_due** | datetime | Due date for completion of the activity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **facilitator** | [UserReference](UserReference) | Facilitator of the activity | [optional] |
| **attendees** | [list[UserReference]](UserReference) | List of users attending the activity | [optional] |
| **is_overdue** | bool | Indicates if the activity is overdue | [optional] |



_PureCloudPlatformClientV2 213.0.0_
