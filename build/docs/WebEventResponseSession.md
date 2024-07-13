---
title: WebEventResponseSession
---
## WebEventResponseSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **duration_in_seconds** | **int** | Indicates how long the customer has been on the site within this session. | |
| **event_count** | **int** | The count of all events recorded during this session. | |
| **pageview_count** | **int** | The count of all pageviews performed during this session. | |
| **referrer** | [**Referrer**](Referrer.html) | The referrer of the first event in the web session. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | Date of the session&#39;s first event, that is when the session starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
{: class="table table-striped"}


