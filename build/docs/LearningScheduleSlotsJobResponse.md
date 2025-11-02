# LearningScheduleSlotsJobResponse

## LearningScheduleSlotsJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **user_ids** | list[str] | The user IDs to fetch the slots for. | [optional] |
| **length_in_minutes** | int | The length in minutes of the slots. | [optional] |
| **business_unit_id** | str | The Business Unit Id of the users. | [optional] |
| **activity_code_id** | str | The Activity Code Id of the slots. | [optional] |
| **slots_type** | str | The type of slots fetched in the job. | [optional] |
| **results** | [list[LearningScheduleSlotsJobResult]](LearningScheduleSlotsJobResult) | The results of the job. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 242.0.0_
