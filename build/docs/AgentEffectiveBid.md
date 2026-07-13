# AgentEffectiveBid

## AgentEffectiveBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the schedule bid | |
| **name** | str |  | [optional] |
| **effective_date** | date | The effective date of the bid relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **end_date** | date | The end date of the bid, relative to the business unit time zone in yyyy-MM-dd format. Null denotes an active schedule bid. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **download_url** | str | The download URL to fetch the list of schedule sets and the agents assigned to them | |
| **download_template** | [AgentAssignedScheduleSetList](AgentAssignedScheduleSetList) | This field will always be null. Effective schedule sets are returned through the download URL. The schema is included here for documentation purposes | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 262.0.0_
