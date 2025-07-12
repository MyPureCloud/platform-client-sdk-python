# ConversationSummary

## ConversationSummary

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **text** | str | The text of the summary. | [optional] |
| **status** | str | The status of the conversation summary. | [optional] |
| **media_type** | str | The media type of the conversation. | [optional] |
| **language** | str | The language of the conversation. | [optional] |
| **predicted_wrapup_codes** | [list[ConversationSummaryWrapupCode]](ConversationSummaryWrapupCode) | The wrapup codes of the conversation summary. | [optional] |
| **edited_summary** | [ConversationEditedInput](ConversationEditedInput) | The edited summary of the conversation. | [optional] |
| **reason** | [ConversationSummaryReason](ConversationSummaryReason) | The reason of the conversation summary. | [optional] |
| **followup** | [ConversationSummaryFollowup](ConversationSummaryFollowup) | The followup of the conversation summary. | [optional] |
| **resolution** | [ConversationSummaryResolution](ConversationSummaryResolution) | The resolution of the conversation summary. | [optional] |
| **date_created** | datetime | The created date of the summary. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **id** | str | The id of the summary. | [optional] |
| **confidence** | float | The AI confidence value. | [optional] |
| **participants** | [list[AddressableEntityRef]](AddressableEntityRef) | The list of participants. | [optional] |



_PureCloudPlatformClientV2 233.0.0_
