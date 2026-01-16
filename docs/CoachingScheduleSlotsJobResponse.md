# CoachingScheduleSlotsJobResponse

## CoachingScheduleSlotsJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **attendee_ids** | list[str] | The attendee IDs to fetch the slots for. | [optional] |
| **facilitator_ids** | list[str] | The facilitator IDs to fetch the slots for. | [optional] |
| **length_in_minutes** | int | The length in minutes of the slots. | [optional] |
| **business_unit_id** | str | The Business Unit Id of the users. | [optional] |
| **activity_code_id** | str | The Activity Code Id of the slots. | [optional] |
| **results** | [list[CoachingScheduleSlotsJobResult]](CoachingScheduleSlotsJobResult) | The results of the job. | [optional] |
| **slots_type** | str | The type of slots fetched in the job. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_
