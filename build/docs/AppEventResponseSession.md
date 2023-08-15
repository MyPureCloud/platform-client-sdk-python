---
title: AppEventResponseSession
---
## AppEventResponseSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **duration_in_seconds** | **int** | Indicates how long the customer has been in the app within this session. | [optional] |
| **event_count** | **int** | The count of all events recorded during this session. | [optional] |
| **screenview_count** | **int** | The count of all screen views recorded during this session. | [optional] |
| **referrer** | [**Referrer**](Referrer.html) | The referrer of the first event in the app session. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | Date of the session&#39;s first event, that is when the session starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


