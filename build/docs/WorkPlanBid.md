# WorkPlanBid

## WorkPlanBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the work plan bid | |
| **name** | str | The name of the work plan bid | |
| **forecast** | [BuShortTermForecastWeekReference](BuShortTermForecastWeekReference) | The selected forecast in this work plan bid | [optional] |
| **bid_window_start_date** | date | The bid start date where agents start participate in work plan bidding. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **bid_window_end_date** | date | The bid end date. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **effective_date** | date | The date when agents will be assigned to the new work plan. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **status** | str | The state of the bid | |
| **agent_ranking_type** | str | The type of agent ranking selected for this bid | |
| **ranking_tiebreaker_type** | str | Ranking tiebreaker | |
| **published_date** | datetime | The date the work plan bid published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **work_plan_fields_visible_to_agents** | list[str] | The work plan fields visible to agents whenever work plan preferences are made | |
| **metadata** | [WorkPlanBidMetadata](WorkPlanBidMetadata) | The meta data of this bid | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
