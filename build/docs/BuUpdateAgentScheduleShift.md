# BuUpdateAgentScheduleShift

## BuUpdateAgentScheduleShift

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the shift | [optional] |
| **start_date** | datetime | The start date of this shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_minutes** | int | The length of this shift in minutes | [optional] |
| **activities** | [list[BuAgentScheduleActivity]](BuAgentScheduleActivity) | The activities associated with this shift | [optional] |
| **manually_edited** | bool | Whether this shift was manually edited. This is only set by clients and is used for rescheduling | [optional] |
| **schedule** | [BuScheduleReference](BuScheduleReference) | The schedule to which this shift belongs | [optional] |
| **work_plan_id** | [ValueWrapperString](ValueWrapperString) | The ID of the work plan for which the work plan shift emanates from | [optional] |
| **work_plan_shift_id** | [ValueWrapperString](ValueWrapperString) | The ID of the work plan shift that was used in schedule generation | [optional] |
| **delete** | bool | Set to true to delete the shift from the agent&#39;s schedule | [optional] |



_PureCloudPlatformClientV2 239.0.0_
