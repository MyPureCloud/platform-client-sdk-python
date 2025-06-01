# JourneySegment

## JourneySegment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the segment. | |
| **is_active** | bool | Whether or not the segment is active. | |
| **display_name** | str | The display name of the segment. | |
| **version** | int | The version of the segment. | |
| **description** | str | A description of the segment. | [optional] |
| **color** | str | The hexadecimal color value of the segment. | |
| **scope** | str | The target entity that a segment applies to. | |
| **should_display_to_agent** | bool | Whether or not the segment should be displayed to agent/supervisor users. | |
| **context** | [Context](Context) | The context of the segment. | |
| **journey** | [Journey](Journey) | The pattern of rules defining the segment. | |
| **external_segment** | [ExternalSegment](ExternalSegment) | Details of an entity corresponding to this segment in an external system. | [optional] |
| **assignment_expiration_days** | int | Time, in days, from when the segment is assigned until it is automatically unassigned. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **created_date** | datetime | Timestamp indicating when the segment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **modified_date** | datetime | Timestamp indicating when the segment was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 230.0.0_
