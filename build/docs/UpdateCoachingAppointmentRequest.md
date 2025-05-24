# UpdateCoachingAppointmentRequest

## UpdateCoachingAppointmentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of coaching appointment. | [optional] |
| **description** | str | The description of coaching appointment. | [optional] |
| **date_start** | datetime | The date/time the coaching appointment starts. Times will be rounded down to the minute. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_in_minutes** | int | The duration of coaching appointment in minutes. | [optional] |
| **conversation_ids** | list[str] | IDs of conversations associated with this coaching appointment. | [optional] |
| **document_ids** | list[str] | IDs of documents associated with this coaching appointment. | [optional] |
| **status** | str | The status of the coaching appointment. | [optional] |
| **wfm_schedule** | [WfmScheduleReference](WfmScheduleReference) | The Workforce Management schedule the appointment is associated with. | [optional] |
| **external_links** | list[str] | The list of external links related to the appointment | [optional] |
| **location** | str | The location of the appointment | [optional] |
| **share_insights_data** | bool | Whether to share the insight data | [optional] |



_PureCloudPlatformClientV2 229.0.0_
