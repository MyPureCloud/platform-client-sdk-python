---
title: UserActivityQuery
---
## UserActivityQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metrics** | [**list[UserActivityQueryMetric]**](UserActivityQueryMetric.html) | List of requested metrics | |
| **group_by** | **list[str]** | Dimension(s) to group by | |
| **filter** | [**UserActivityQueryFilter**](UserActivityQueryFilter.html) | Filter to return a subset of observations. Expresses boolean logical predicates as well as dimensional filters | [optional] |
| **order** | **str** | Sort the result set in ascending/descending order. Default is ascending | [optional] |
{: class="table table-striped"}


