---
title: ImportShortTermForecastRequest
---
## ImportShortTermForecastRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **file_name** | **str** | The file name, if applicable, this data was extracted from (display purposes only) | [optional] |
| **description** | **str** | Description for the imported forecast.  Pass an empty string for no description | |
| **route_group_list** | [**RouteGroupList**](RouteGroupList.html) | The raw data to import | |
| **partial_upload_ids** | **list[str]** | IDs of partial uploads to include in this imported forecast.  Only relevant for large forecasts | [optional] |
{: class="table table-striped"}


