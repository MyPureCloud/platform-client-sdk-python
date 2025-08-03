# IncomingMessageRequest

## IncomingMessageRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **bot_id** | str | The unique id of the bot. | |
| **bot_name** | str | Name of the bot | |
| **bot_version** | str | The version of the bot. | |
| **integration_id** | str | The Integration Id for the bot&#39;s configuration | |
| **bot_session_id** | str | The id of the session. This id will be used for an entire conversation with the bot (a series of back and forth between the bot until the bot has fulfilled its intent). | |
| **automate_flow_exec_id** | str | Execution ID of the Automate Flow. | |
| **conversation_id** | str | Genesys conversation ID. | |
| **language_code** | str | Language code for the conversation (e.g., &#39;en-US&#39;). | |
| **input_message** | [InputMessage](InputMessage) | Message received from the user to send to the bot | |
| **messaging_platform_type** | str | Type of messaging platform being used | |
| **channels** | list[str] | The channels this bot is utilizing. | |
| **bot_session_timeout** | int | Timeout duration for bot session in minutes. | [optional] |
| **parameters** | dict(str, str) | This is a map of string-string key, value pairs containing optional fields that can be passed to the bot for custom behavior, tracking, etc. | [optional] |



_PureCloudPlatformClientV2 234.0.0_
