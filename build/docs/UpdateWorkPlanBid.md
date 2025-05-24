# UpdateWorkPlanBid

## UpdateWorkPlanBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the work plan bid | [optional] |
| **forecast** | [BuShortTermForecastWeekReference](BuShortTermForecastWeekReference) | The selected forecast in this work plan bid | [optional] |
| **bid_window_start_date** | date | The bid start date where agents start participate in work plan bidding in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **bid_window_end_date** | date | The bid end date in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **effective_date** | date | The date when agents will be assigned to the new work plan in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **agent_ranking_type** | str | The type of agent ranking selected for this bid | [optional] |
| **ranking_tiebreaker_type** | str | Ranking tiebreaker | [optional] |
| **work_plan_fields_visible_to_agents** | [ListWrapperAgentWorkPlanField](ListWrapperAgentWorkPlanField) | The work plan fields visible to agents whenever work plan preferences are made | [optional] |
| **status** | str | The state of the bid | [optional] |



_PureCloudPlatformClientV2 229.0.0_
