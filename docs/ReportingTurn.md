# ReportingTurn

## ReportingTurn

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_input** | str | The chosen user input associated with this reporting turn. | [optional] |
| **bot_prompts** | list[str] | The bot prompts associated with this reporting turn. | [optional] |
| **session_id** | str | The bot session ID that this reporting turn is grouped under. | [optional] |
| **ask_action** | [ReportingTurnAction](ReportingTurnAction) | The bot flow &#39;ask&#39; action associated with this reporting turn (e.g. AskForIntent). | [optional] |
| **intent** | [ReportingTurnIntent](ReportingTurnIntent) | The intent and associated slots detected during this reporting turn. | [optional] |
| **knowledge** | [ReportingTurnKnowledge](ReportingTurnKnowledge) | The knowledge data captured during this reporting turn. | [optional] |
| **knowledge_base_events** | [ReportingTurnKnowledgeEvents](ReportingTurnKnowledgeEvents) | The knowledge data captured during this reporting turn. | [optional] |
| **date_created** | datetime | Timestamp indicating when the original turn was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | Timestamp indicating when the original turn was completed. Note: The &#39;interval&#39; query param uses this timestamp to filter the output. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **ask_action_result** | str | Result of the bot flow &#39;ask&#39; action. | [optional] |
| **session_end_details** | [SessionEndDetails](SessionEndDetails) | The details related to end of bot flow session. | [optional] |
| **conversation** | [AddressableEntityRef](AddressableEntityRef) | The conversation details, across potentially multiple Bot Flow sessions. | [optional] |



_PureCloudPlatformClientV2 240.0.0_
