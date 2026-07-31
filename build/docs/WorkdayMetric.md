# WorkdayMetric

## WorkdayMetric

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metric** | [Metric](Metric) | Gamification metric | [optional] |
| **objective** | [Objective](Objective) | Current objective for this metric | [optional] |
| **points** | int | Gamification points earned for this metric | [optional] |
| **max_points** | int | The maximum Gamification points a user may earn for this metric | [optional] |
| **value** | float | Value of this metric | [optional] |
| **punctuality_events** | [list[PunctualityEvent]](PunctualityEvent) | List of schedule activity events for punctuality metrics | [optional] |
| **business_unit_id** | str | The id of the business unit associated with this metric, only returned for metrics with punctuality events | [optional] |
| **evaluation_details** | [list[QualityEvaluationScoreItem]](QualityEvaluationScoreItem) | List of evaluations for quality evaluation score metrics | [optional] |



_PureCloudPlatformClientV2 263.0.0_
