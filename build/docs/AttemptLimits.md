---
title: AttemptLimits
---
## AttemptLimits

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **max_attempts_per_contact** | **int** |  | [optional] |
| **max_attempts_per_number** | **int** |  | [optional] |
| **time_zone_id** | **str** | The timezone is necessary to define when \&quot;today\&quot; starts and ends | [optional] |
| **reset_period** | **str** | After how long the number of attempts will be set back to 0 | [optional] |
| **recall_entries** | [**dict(str, RecallEntry)**](RecallEntry.html) | Configuration for recall attempts | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


