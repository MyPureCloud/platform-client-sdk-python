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
| **customer_first_callback_delivery_mode** | str | How customer-first callback agent reservation is applied for this callback. useAgentReservation forces reservation on; noAgentReservation forces it off; useQueueSetting uses the queue configuration. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
