# CoachingNotification

## CoachingNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the appointment for this notification. | [optional] |
| **marked_as_read** | bool | Indicates if notification is read or unread | [optional] |
| **action_type** | str | Action causing the notification. | [optional] |
| **relationship** | str | The relationship of this user to this notification&#39;s appointment | [optional] |
| **date_start** | datetime | The start time of the appointment relating to this notification. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_in_minutes** | int | The duration of the appointment on this notification | [optional] |
| **status** | str | The status of the appointment for this notification | [optional] |
| **user** | [UserReference](UserReference) | The user of this notification | [optional] |
| **appointment** | [CoachingAppointmentResponse](CoachingAppointmentResponse) | The appointment | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 238.0.0_
