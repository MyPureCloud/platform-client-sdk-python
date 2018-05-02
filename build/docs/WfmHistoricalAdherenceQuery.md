---
title: WfmHistoricalAdherenceQuery
---
## WfmHistoricalAdherenceQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | **datetime** | Beginning of the date range to query in ISO-8601 format | |
| **end_date** | **datetime** | End of the date range to query in ISO-8601 format. If it is not set, end date will be set to current time | [optional] |
| **time_zone** | **str** | The time zone to use for returned results in olson format. If it is not set, the management unit time zone will be used to compute adherence | [optional] |
| **user_ids** | **list[str]** | The userIds to report on. If it is not set, adherence will be computed for all the users in management unit | [optional] |
| **include_exceptions** | **bool** | Whether user exceptions should be returned as part of the results | [optional] |
{: class="table table-striped"}


