# LexV2BotAlias

## LexV2BotAlias

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **region** | str | The Lex V2 bot region | |
| **alias_id** | str | The Lex V2 bot alias Id | |
| **bot** | [LexV2Bot](LexV2Bot) | The Lex V2 bot this is an alias for | [optional] |
| **bot_version** | str | The version of the Lex V2 bot this alias points at | [optional] |
| **status** | str | The status of the Lex V2 bot alias | [optional] |
| **language** | str | The target language of the Lex V2 bot | [optional] |
| **intents** | [list[LexV2Intent]](LexV2Intent) | An array of Intents associated with this bot alias | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 219.1.0_
