# CreateCallbackOnConversationCommand

## CreateCallbackOnConversationCommand

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **script_id** | str | The identifier of the script to be used for the callback | [optional] |
| **queue_id** | str | The identifier of the queue to be used for the callback. Either queueId or routingData is required. | [optional] |
| **routing_data** | [RoutingData](RoutingData) | The routing data to be used for the callback. Either queueId or routingData is required. | [optional] |
| **callback_user_name** | str | The name of the party to be called back. | [optional] |
| **callback_numbers** | list[str] | A list of phone numbers for the callback. | |
| **callback_scheduled_time** | datetime | The scheduled date-time for the callback as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **country_code** | str | The country code to be associated with the callback numbers. | [optional] |
| **validate_callback_numbers** | bool | Whether or not to validate the callback numbers for phone number format. | [optional] |
| **data** | dict(str, str) | A map of key-value pairs containing additional data that can be associated to the callback. These values will appear in the attributes property on the conversation participant. Example: { \&quot;notes\&quot;: \&quot;ready to close the deal!\&quot;, \&quot;customerPreferredName\&quot;: \&quot;Doc\&quot; } | [optional] |
| **caller_id** | str | The phone number displayed to recipients when a phone call is placed as part of the callback. Must conform to the E.164 format. May be overridden by other settings in the system such as external trunk settings. Telco support for \&quot;callerId\&quot; varies. | [optional] |
| **caller_id_name** | str | The name displayed to recipients when a phone call is placed as part of the callback. May be overridden by other settings in the system such as external trunk settings. Telco support for \&quot;callerIdName\&quot; varies. | [optional] |



_PureCloudPlatformClientV2 248.0.0_
