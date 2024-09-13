# GoogleDialogflowCustomSettings

## GoogleDialogflowCustomSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **environment** | str | If set this environment will be used to initiate the dialogflow bot, otherwise the default configuration will be used.  See https://cloud.google.com/dialogflow/docs/agents-versions | [optional] |
| **event_name** | str | If set this eventName will be used to initiate the dialogflow bot rather than language processing on the input text.  See https://cloud.google.com/dialogflow/es/docs/events-overview | [optional] |
| **webhook_query_parameters** | dict(str, str) | Parameters passed to the fulfillment webhook of the bot (if any). | [optional] |
| **event_input_parameters** | dict(str, str) | Parameters passed to the event input of the bot. | [optional] |



_PureCloudPlatformClientV2 211.0.0_
