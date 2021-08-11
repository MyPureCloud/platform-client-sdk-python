---
title: JourneyEventsSettings
---
## JourneyEventsSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** | Whether or not journey event collection is enabled. | [optional] |
| **excluded_query_parameters** | **list[str]** | List of parameters to be excluded from the query string. | [optional] |
| **should_keep_url_fragment** | **bool** | Whether or not to keep the URL fragment. | [optional] |
| **search_query_parameters** | **list[str]** | List of query parameters used for search (e.g. &#39;q&#39;). | [optional] |
| **pageview_config** | **str** | Controls how the pageview events are tracked. | [optional] |
| **click_events** | [**list[SelectorEventTrigger]**](SelectorEventTrigger.html) | Tracks when and where a visitor clicks on a webpage. | [optional] |
| **forms_track_events** | [**list[FormsTrackTrigger]**](FormsTrackTrigger.html) | Controls how the form submitted and form abandoned events are tracked after a visitor interacts with a form element. | [optional] |
| **idle_events** | [**list[IdleEventTrigger]**](IdleEventTrigger.html) | Tracks when and where a visitor becomes inactive on a webpage. | [optional] |
| **in_viewport_events** | [**list[SelectorEventTrigger]**](SelectorEventTrigger.html) | Tracks when elements become visible or hidden on screen. | [optional] |
| **scroll_depth_events** | [**list[ScrollPercentageEventTrigger]**](ScrollPercentageEventTrigger.html) | Tracks when a visitor scrolls to a specific percentage of a webpage. | [optional] |
{: class="table table-striped"}


