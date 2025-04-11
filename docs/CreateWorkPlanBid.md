# CreateWorkPlanBid

## CreateWorkPlanBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the work plan bid | |
| **forecast** | [BuShortTermForecastWeekReference](BuShortTermForecastWeekReference) | The selected forecast in this work plan bid | [optional] |
| **bid_window_start_date** | date | The bid start date where agents start participate in work plan bidding in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **bid_window_end_date** | date | The bid end date in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **effective_date** | date | The date when agents will be assigned to the new work plan in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **agent_ranking_type** | str | The type of agent ranking selected for this bid | |
| **ranking_tiebreaker_type** | str | Ranking tiebreaker to be used | |
| **work_plan_fields_visible_to_agents** | list[str] | The work plan fields visible to agents whenever work plan preferences are made | |



_PureCloudPlatformClientV2 226.0.0_
