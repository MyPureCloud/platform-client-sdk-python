# OutgoingMessageRequest

## OutgoingMessageRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **bot_id** | str | The unique id of the bot. | |
| **bot_version** | str | The version of the bot. | |
| **bot_session_id** | str | The id of the session. This id will be used for an entire conversation with the bot (a series of back and forth between the bot until the bot has fulfilled its intent). | |
| **bot_state** | str | The state of the bot reported | |
| **language_code** | str | The language used for this message. EG &#39;en-us&#39; or &#39;es&#39;, etc; These language codes are W3C language identification tags (ISO 639-1 for the language name and ISO 3166 for the country code). | |
| **reply_messages** | [list[ReplyMessage]](ReplyMessage) | This is a list of messages to send back to the user, this field can be null or an empty list. | [optional] |
| **intent** | str | The name of the intent the bot is either processing or has processed, this will be blank if no intent could be detected. | [optional] |
| **confidence** | float | A value between 0 and 1.0 denoting the confidence of the discovered intent (if found) this is optional and if left null genesys assumes a confidence of 1.0 on success and 0 on fail. | [optional] |
| **error_info** | [ErrorInfo](ErrorInfo) | If the botState is Failed the bot can add this error object with more details about the error. | [optional] |
| **parameters** | dict(str, str) | This is a map of string-string key, value pairs containing optional fields that can be passed from the bot for custom behavior, tracking, etc, which can be used by the flow. | [optional] |
| **entities** | [list[BotEntityValue]](BotEntityValue) | A set of entity values that go along with the intent. | [optional] |



_PureCloudPlatformClientV2 246.0.0_
