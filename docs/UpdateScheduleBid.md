# UpdateScheduleBid

## UpdateScheduleBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the schedule bid | [optional] |
| **forecast** | [BuShortTermForecastWeekReference](BuShortTermForecastWeekReference) | The selected forecast used for schedule set generation for this bid | [optional] |
| **bid_window_start_date** | date | The bid start date where agents start participating in schedule bidding relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **bid_window_end_date** | date | The bid end date relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **effective_date** | date | The date when schedule sets would be effective for schedule generation relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **weeks_to_schedule** | int | The number of weeks to generate schedule set through this bid | [optional] |
| **end_overrides_and_rotations** | bool | If true, all existing overrides, work plan rotations will be ended one day before effective date of this bid | [optional] |
| **agent_ranking_type** | str | The type of agent ranking selected for this bid | [optional] |
| **ranking_tiebreaker_type** | str | Ranking tiebreaker to be used | [optional] |
| **status** | str | The state of the bid | [optional] |



_PureCloudPlatformClientV2 265.0.0_
