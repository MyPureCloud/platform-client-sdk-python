---
title: Range
---
## Range

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | Range type (NoEnd: without an end date. EndDate: with an end date. Numbered: with a specific number of occurrences) | |
| **end** | **str** | The end date time of the last occurrence of the range as an ISO-8601 string. Required for EndDate range type. | [optional] |
| **number_of_occurrences** | **int** | The number of times the schedule will be repeated, e.g: 2. Required to set for Numbered range type. | [optional] |
{: class="table table-striped"}


