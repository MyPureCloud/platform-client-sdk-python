---
title: CreateTriggerRequest
---
## CreateTriggerRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **target** | [**TriggerTarget**](TriggerTarget.html) | The target to invoke when a matching event is received | |
| **enabled** | **bool** | Boolean indicating if Trigger is enabled | |
| **match_criteria** | [**list[MatchCriteria]**](MatchCriteria.html) | The configuration for when a trigger is considered to be a match for an event. When not provided, all events will fire the trigger | [optional] |
| **name** | **str** | The name of the trigger | |
| **topic_name** | **str** | The topic that will cause the trigger to be invoked. Cannot be updated after creation. Valid topics can be found at /processautomation/triggers/topics  | |
| **event_ttl_seconds** | **int** | How long each event is meaningful after origination, in seconds. Events older than this threshold may be dropped if the platform is delayed in processing events. Unset means events are valid indefinitely. | [optional] |
| **description** | **str** | Description of the trigger. Can be up to 512 characters in length. | [optional] |
{: class="table table-striped"}


