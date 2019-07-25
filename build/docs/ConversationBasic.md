---
title: ConversationBasic
---
## ConversationBasic

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **start_time** | **datetime** | The time when the conversation started. This will be the time when the first participant joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **end_time** | **datetime** | The time when the conversation ended. This will be the time when the last participant left the conversation, or null when the conversation is still active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **divisions** | [**list[ConversationDivisionMembership]**](ConversationDivisionMembership.html) | Identifiers of divisions associated with this conversation | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **participants** | [**list[ParticipantBasic]**](ParticipantBasic.html) |  | [optional] |
{: class="table table-striped"}


