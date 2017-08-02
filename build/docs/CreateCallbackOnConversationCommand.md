---
title: CreateCallbackOnConversationCommand
---
## CreateCallbackOnConversationCommand

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **script_id** | **str** | The identifier of the script to be used for the callback | [optional] |
| **queue_id** | **str** | The identifier of the queue to be used for the callback. Either queueId or routingData is required. | [optional] |
| **routing_data** | [**RoutingData**](RoutingData.html) | The routing data to be used for the callback. Either queueId or routingData is required. | [optional] |
| **callback_user_name** | **str** | The name of the party to be called back. | [optional] |
| **callback_numbers** | **list[str]** | A list of phone numbers for the callback. | |
| **callback_scheduled_time** | **datetime** | The scheduled date-time for the callback as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **country_code** | **str** | The country code to be associated with the callback numbers. | [optional] |
| **data** | **dict(str, str)** | A map of key-value pairs containing additional data that can be associated to the callback. These values will appear in the attributes property on the conversation participant. Example: { \&quot;notes\&quot;: \&quot;ready to close the deal!\&quot;, \&quot;customerPreferredName\&quot;: \&quot;Doc\&quot; } | [optional] |
{: class="table table-striped"}


