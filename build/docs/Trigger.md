---
title: Trigger
---
## Trigger

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the trigger | [optional] |
| **topic_name** | **str** | The topic that will cause the trigger to be invoked | [optional] |
| **target** | [**TriggerTarget**](TriggerTarget.html) | The target to invoke when a matching event is received | [optional] |
| **version** | **int** | Version of this trigger | [optional] |
| **enabled** | **bool** | Whether or not the trigger is enabled | [optional] |
| **match_criteria** | [**list[MatchCriteria]**](MatchCriteria.html) | The configuration for when a trigger is considered to be a match for an event | [optional] |
| **event_ttl_seconds** | **int** | How long each event is meaningful after origination, in seconds. Events older than this threshold may be dropped if the platform is delayed in processing events. Unset means events are valid indefinitely. | [optional] |
| **description** | **str** | Description of the trigger. Can be up to 512 characters in length. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


