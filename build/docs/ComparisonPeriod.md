# ComparisonPeriod

## ComparisonPeriod

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **kpi** | str | Key Performance Indicator optimised during the comparison period. | [optional] |
| **date_started** | datetime | Start date of the comparison period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_ended** | datetime | End date of the comparison period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **percentage_benefit** | float | The percentage benefit on this queue for the duration of the comparison period | [optional] |
| **kpi_results** | [list[KpiResult]](KpiResult) | KPI results for each metric | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 222.0.0_
