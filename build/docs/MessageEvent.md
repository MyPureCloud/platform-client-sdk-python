# MessageEvent

## MessageEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_type** | str | Type of this event element | |
| **co_browse** | [EventCoBrowse](EventCoBrowse) | CoBrowse event. | [optional] |
| **typing** | [EventTyping](EventTyping) | Typing event. | [optional] |
| **presence** | [EventPresence](EventPresence) | Presence event. | [optional] |
| **video** | [EventVideo](EventVideo) | Video event. | [optional] |
| **reactions** | [list[ContentReaction]](ContentReaction) | A list of reactions to a message. | [optional] |



_PureCloudPlatformClientV2 224.0.0_
