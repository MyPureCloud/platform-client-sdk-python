# Trigger

## Trigger

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the trigger | [optional] |
| **topic_name** | str | The topic that will cause the trigger to be invoked | [optional] |
| **target** | [TriggerTarget](TriggerTarget) | The target to invoke when a matching event is received | [optional] |
| **version** | int | Version of this trigger | [optional] |
| **enabled** | bool | Whether or not the trigger is enabled | [optional] |
| **match_criteria** | [list[MatchCriteria]](MatchCriteria) | The configuration for when a trigger is considered to be a match for an event | [optional] |
| **event_ttl_seconds** | int | Optional length of time that events are meaningful after origination. Events older than this threshold may be dropped if the platform is delayed in processing events. Unset means events are valid indefinitely, otherwise must be set to at least 10 seconds. Only one of eventTTLSeconds or delayBySeconds can be set. | [optional] |
| **delay_by_seconds** | int | Optional delay invoking target after trigger fires. Must be in the range of 60 to 900 seconds. Only one of eventTTLSeconds or delayBySeconds can be set. | [optional] |
| **description** | str | Description of the trigger. Can be up to 512 characters in length. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
