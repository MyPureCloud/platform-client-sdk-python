# CreateWebChatRequest

## CreateWebChatRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | str | The ID of the queue to use for routing the chat conversation. | |
| **provider** | str | The name of the provider that is sourcing the web chat. | |
| **skill_ids** | list[str] | The list of skill ID&#39;s to use for routing. | [optional] |
| **language_id** | str | The ID of the langauge to use for routing. | [optional] |
| **priority** | int | The priority to assign to the conversation for routing. | [optional] |
| **attributes** | dict(str, str) | The list of attributes to associate with the customer participant. | [optional] |
| **customer_name** | str | The name of the customer participating in the web chat. | [optional] |



_PureCloudPlatformClientV2 215.0.0_
