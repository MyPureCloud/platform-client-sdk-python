# JourneySegmentRequest

## JourneySegmentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **is_active** | bool | Whether or not the segment is active. | [optional] |
| **display_name** | str | The display name of the segment. | |
| **version** | int | The version of the segment. | [optional] |
| **description** | str | A description of the segment. | [optional] |
| **color** | str | The hexadecimal color value of the segment. | |
| **should_display_to_agent** | bool | Whether or not the segment should be displayed to agent/supervisor users. | [optional] |
| **context** | [RequestContext](RequestContext) | The context of the segment. | |
| **journey** | [RequestJourney](RequestJourney) | The pattern of rules defining the segment. | |
| **external_segment** | [RequestExternalSegment](RequestExternalSegment) | Details of an entity corresponding to this segment in an external system. | [optional] |
| **assignment_expiration_days** | int | Time, in days, from when the segment is assigned until it is automatically unassigned. | [optional] |



_PureCloudPlatformClientV2 233.0.0_
