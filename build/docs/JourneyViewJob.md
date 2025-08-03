# JourneyViewJob

## JourneyViewJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **date_created** | datetime | Timestamp of execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_completed** | datetime | Timestamp of completion. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **status** | str | The status of the job | |
| **journey_view** | [JourneyView](JourneyView) | The journey view for which the job is executed | |
| **date_completion_estimated** | datetime | Timestamp for the estimated time of completion. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **estimated_completion_margin** | int | Margin of error of the estimated time of completion | |
| **user_id** | str | Id of the user who submitted the request | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 234.0.0_
