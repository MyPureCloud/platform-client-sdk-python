# PostTextResponse

## PostTextResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **bot_state** | str | The state of the bot after completion of the request | |
| **reply_messages** | [list[PostTextMessage]](PostTextMessage) | The list of messages to respond with, if any | [optional] |
| **intent_name** | str | The name of the intent the bot is either processing or has processed, this will be blank if no intent could be detected. | [optional] |
| **slots** | dict(str, str) | Data parameters detected and filled by the bot. | [optional] |
| **bot_correlation_id** | str | The optional ID specified in the request | [optional] |
| **amazon_lex** | dict(str, object) | Raw data response from AWS (if called) | [optional] |
| **google_dialog_flow** | dict(str, object) | Raw data response from Google Dialogflow (if called) | [optional] |
| **genesys_dialog_engine** | dict(str, object) | Raw data response from Genesys&#39; Dialogengine (if called) | [optional] |
| **genesys_bot_connector** | dict(str, object) | Raw data response from Genesys&#39; BotConnector (if called) | [optional] |
| **nuance_mix_dlg** | dict(str, object) | Raw data response from Nuance Mix Dlg (if called) | [optional] |



_PureCloudPlatformClientV2 217.0.0_
