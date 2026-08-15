# ScheduleBid

## ScheduleBid

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the schedule bid | |
| **name** | str | The name of the schedule bid | |
| **bid_window_start_date** | date | The bid start date when agents can start participating in schedule bidding relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **bid_window_end_date** | date | The bid end date relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **effective_date** | date | The date when schedule sets would be effective for schedule generation relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **status** | str | The state of the bid | |
| **bid_type** | str | The type of the bid | |
| **forecast** | [BuShortTermForecastWeekReference](BuShortTermForecastWeekReference) | The selected forecast used for schedule set generation for this bid | [optional] |
| **weeks_to_schedule** | int | The number of weeks to generate schedule sets through this bid | |
| **end_overrides_and_rotations** | bool | If true, all existing overrides, work plan rotations will be ended one day before effective date of this bid | |
| **agent_ranking_type** | str | The type of agent ranking selected for this bid | |
| **ranking_tiebreaker_type** | str | Ranking tiebreaker | |
| **published_date** | datetime | The date the schedule bid is published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | date | The end date until which schedule sets can be used for schedule generation. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **metadata** | [WorkPlanBidMetadata](WorkPlanBidMetadata) | The metadata of this bid | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 264.0.0_
