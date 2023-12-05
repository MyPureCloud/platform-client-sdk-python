---
title: BotFlowSession
---
## BotFlowSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the bot session. | [optional] |
| **flow** | [**Entity**](Entity.html) | The flow associated to this bot session. | [optional] |
| **channel** | [**BotChannel**](BotChannel.html) | Channel-specific information that describes the message channel/provider. | [optional] |
| **language** | **str** | The initial language of operation for the session. | [optional] |
| **end_language** | **str** | The language of the session at the time the session ended | [optional] |
| **bot_result** | **str** | The reason for session termination. | [optional] |
| **bot_result_category** | **str** | The category of result for the session. | [optional] |
| **date_created** | **datetime** | Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation** | [**AddressableEntityRef**](AddressableEntityRef.html) | The conversation details, across potentially multiple Bot Flow sessions. | [optional] |
{: class="table table-striped"}


