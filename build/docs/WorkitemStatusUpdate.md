# WorkitemStatusUpdate

## WorkitemStatusUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the Status. Valid length between 3 and 256 characters. | [optional] |
| **destination_status_ids** | list[str] | A list of destination Statuses where a Workitem with this Status can transition to. If the list is empty Workitems with this Status can transition to all other Statuses defined on the Worktype. A Status can have a maximum of 24 destinations. | [optional] |
| **description** | str | The description of the Status. Maximum length of 512 characters. | [optional] |
| **default_destination_status_id** | str | Default destination status to which this Status will transition to if auto status transition enabled. | [optional] |
| **status_transition_delay_seconds** | int | Delay in seconds for auto status transition. Required if defaultDestinationStatusId is provided. | [optional] |
| **status_transition_time** | str | Time is represented as an ISO-8601 string without a timezone. For example: HH:mm:ss.SSS | [optional] |



_PureCloudPlatformClientV2 212.0.0_
