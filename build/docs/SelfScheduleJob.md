# SelfScheduleJob

## SelfScheduleJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **status** | str | The status of the job | |
| **activity_moves** | [list[SelfScheduleActivityMoveListItem]](SelfScheduleActivityMoveListItem) | The self-schedule activity moves, if status &#x3D;&#x3D; &#39;Complete&#39; | [optional] |
| **error** | [ErrorBody](ErrorBody) | Any error information, only set if the status &#x3D;&#x3D; &#39;Error&#39; | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 270.0.0_
