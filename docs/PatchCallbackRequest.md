# PatchCallbackRequest

## PatchCallbackRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **conversation_id** | str | The conversationId. | |
| **queue_id** | str | The identifier of the queue to be used for the callback. | [optional] |
| **agent_id** | str | The agentId. | |
| **callback_scheduled_time** | datetime | The scheduled date-time for the callback. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **country_code** | str | The countryCode | [optional] |
| **callback_numbers** | list[str] | The callbackNumbers | [optional] |
| **validate_callback_numbers** | bool | validateCallbackNumbers | [optional] |



_PureCloudPlatformClientV2 242.0.0_
