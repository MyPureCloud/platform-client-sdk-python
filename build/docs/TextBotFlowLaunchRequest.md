---
title: TextBotFlowLaunchRequest
---
## TextBotFlowLaunchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **flow** | [**TextBotFlow**](TextBotFlow.html) | Specifies which Bot Flow to launch. | |
| **external_session_id** | **str** | The ID of the external session that is associated with the bot flow. | |
| **conversation_id** | **str** | A conversation ID to associate with the bot flow, if available. | [optional] |
| **input_data** | [**TextBotInputOutputData**](TextBotInputOutputData.html) | Input values to the flow. Valid values are defined by the flow&#39;s input JSON schema. | [optional] |
| **channel** | [**TextBotChannel**](TextBotChannel.html) | Channel information relevant to the bot flow. | |
{: class="table table-striped"}


