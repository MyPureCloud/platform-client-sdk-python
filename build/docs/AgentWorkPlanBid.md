# AgentWorkPlanBid

## AgentWorkPlanBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the work plan bid | |
| **name** | str |  | [optional] |
| **bid_window_start_date** | date | The date when agents can start participating in work plan bidding. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **bid_window_end_date** | date | The inclusive end date of a bid window. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **effective_date** | date | The date when agents will be assigned to the new work plan. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **status** | str | The state of the bid | |
| **work_plan_fields_visible_to_agents** | list[str] | The work plan fields visible to agents whenever work plan preferences are made | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 216.0.0_
