# LexBotAlias

## LexBotAlias

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **bot** | [LexBot](LexBot) | The Lex bot this is an alias for | [optional] |
| **bot_version** | str | The version of the Lex bot this alias points at | [optional] |
| **status** | str | The status of the Lex bot alias | |
| **failure_reason** | str | If the status is FAILED, Amazon Lex explains why it failed to build the bot | [optional] |
| **language** | str | The target language of the Lex bot | [optional] |
| **intents** | [list[LexIntent]](LexIntent) | An array of Intents associated with this bot alias | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 212.0.0_
