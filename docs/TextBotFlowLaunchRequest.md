# TextBotFlowLaunchRequest

## TextBotFlowLaunchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **flow** | [TextBotFlow](TextBotFlow) | Specifies which Bot Flow to launch. | |
| **external_session_id** | str | The ID of the external session that is associated with the bot flow. | |
| **conversation_id** | str | A conversation ID to associate with the bot flow, if available. | [optional] |
| **input_data** | [TextBotInputOutputData](TextBotInputOutputData) | Input values to the flow. Valid values are defined by the flow&#39;s input JSON schema. | [optional] |
| **channel** | [TextBotChannel](TextBotChannel) | Channel information relevant to the bot flow. | |
| **language** | str | The language that the bot will use in the session. Validated against list of supported languages and if the value is omitted or is invalid, the default language will be used. | [optional] |



_PureCloudPlatformClientV2 218.0.0_
