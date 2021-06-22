---
title: PerformanceProfile
---
## PerformanceProfile

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | A name for this performance profile | |
| **division** | [**Division**](Division.html) | The division for this performance profile associate to | [optional] |
| **description** | **str** | A description about this performance profile | |
| **metric_orders** | **list[str]** | Order of the associated metrics. The list should contain valid ids for metrics | |
| **date_created** | **datetime** | Creation date for this performance profile. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **reporting_intervals** | [**list[ReportingInterval]**](ReportingInterval.html) | The reporting interval periods for this performance profile | [optional] |
| **active** | **bool** | The flag for active profiles | [optional] |
| **max_leaderboard_rank_size** | **int** | The maximum rank size for the leaderboard. This counts the number of ranks can be retrieved in a leaderboard queries | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


