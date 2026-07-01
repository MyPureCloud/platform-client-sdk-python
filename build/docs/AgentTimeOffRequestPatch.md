# AgentTimeOffRequestPatch

## AgentTimeOffRequestPatch

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **marked_as_read** | bool | Whether this request has been read by the agent | [optional] |
| **status** | str | The status of this time off request. Can only be canceled if the requested date has not already passed | [optional] |
| **notes** | str | Notes about the time off request. Can only be edited while the request is still pending | [optional] |
| **full_day_earliest_start_offset_minutes** | [ListWrapperInteger](ListWrapperInteger) | Earliest start offset in minutes for each full-day request date. Values may be null when time-off estimation is disabled or no estimate is available | [optional] |
| **full_day_latest_end_offset_minutes** | [ListWrapperInteger](ListWrapperInteger) | Latest end offset in minutes for each full-day request date. Values may be null when time-off estimation is disabled or no estimate is available | [optional] |



_PureCloudPlatformClientV2 261.0.0_
