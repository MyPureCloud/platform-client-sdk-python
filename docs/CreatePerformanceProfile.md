# CreatePerformanceProfile

## CreatePerformanceProfile

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | A name for this performance profile | |
| **division** | [WritableDivision](WritableDivision) | The associated division for this Performance Profile | |
| **description** | str | A description about this performance profile | |
| **metric_orders** | list[str] | Order of the associated metrics. The list should contain valid ids for metrics | [optional] |
| **date_created** | datetime | Creation date for this performance profile. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **reporting_intervals** | [list[ReportingInterval]](ReportingInterval) | The reporting interval periods for this performance profile | |
| **active** | bool | The flag for active profiles | |
| **member_count** | int | The number of members in this performance profile | [optional] |
| **max_leaderboard_rank_size** | int | The maximum rank size for the leaderboard. This counts the number of ranks can be retrieved in a leaderboard queries | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 228.0.0_
