# CoachingAppointmentResponse

## CoachingAppointmentResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of coaching appointment | [optional] |
| **description** | str | The description of coaching appointment | [optional] |
| **date_start** | datetime | The date/time the coaching appointment starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_in_minutes** | int | The duration of coaching appointment in minutes | [optional] |
| **status** | str | The status of coaching appointment | [optional] |
| **facilitator** | [UserReference](UserReference) | The facilitator of coaching appointment | [optional] |
| **attendees** | [list[UserReference]](UserReference) | The list of attendees attending the coaching | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the coaching appointment | [optional] |
| **date_created** | datetime | The date/time the coaching appointment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The last user to modify the coaching appointment | [optional] |
| **date_modified** | datetime | The date/time the coaching appointment was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversations** | [list[ConversationReference]](ConversationReference) | The list of conversations associated with coaching appointment. | [optional] |
| **documents** | [list[DocumentReference]](DocumentReference) | The list of documents associated with coaching appointment. | [optional] |
| **is_overdue** | bool | Whether the appointment is overdue. | [optional] |
| **wfm_schedule** | [WfmScheduleReference](WfmScheduleReference) | The Workforce Management schedule the appointment is associated with. | [optional] |
| **date_completed** | datetime | The date/time the coaching appointment was set to completed status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_links** | list[str] | The list of external links related to the appointment | [optional] |
| **location** | str | The location of the appointment | [optional] |
| **share_insights_data** | bool | Whether to share the insight data | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
