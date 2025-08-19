# IntradayPlanningGroupRequest

## IntradayPlanningGroupRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **business_unit_date** | date | Requested date in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **categories** | list[str] | The metric categories | |
| **planning_group_ids** | list[str] | The IDs of the planning groups for which to fetch data.  Omitting or passing an empty list will return all available planning groups | [optional] |
| **interval_length_minutes** | int | The period/interval in minutes for which to aggregate the data. Required, defaults to 15 | [optional] |



_PureCloudPlatformClientV2 235.1.0_
