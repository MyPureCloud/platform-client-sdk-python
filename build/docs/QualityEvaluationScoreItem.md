# QualityEvaluationScoreItem

## QualityEvaluationScoreItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **evaluation_id** | str | The id of evaluation | [optional] |
| **conversation_id** | str | The id of conversation | [optional] |
| **conversation_date** | datetime | The date of conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation_end_date** | datetime | The end date of conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **form_name** | str | The name of form | [optional] |
| **points** | int | Gamification points earned for this metric | [optional] |
| **evaluation_score** | float | The quality score of evaluation as a percentage | [optional] |
| **max_points** | int | The maximum Gamification points a user may earn for this metric | [optional] |
| **media_types** | list[str] | A list of media types for the metric | [optional] |



_PureCloudPlatformClientV2 224.0.0_
