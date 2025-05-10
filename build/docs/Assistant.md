# Assistant

## Assistant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the assistant that will assist the agent. | |
| **date_created** | datetime | Date when the assistant was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the assistant was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the assistant. | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who last modified the assistant. | [optional] |
| **google_dialogflow_config** | [GoogleDialogflowConfig](GoogleDialogflowConfig) | (Deprecated: use the &#39;knowledgeSuggestionConfig&#39; for genesys knowledge suggestions) Configuration of Dialogflow used to assist the agent with transcriptions and knowledge suggestions. | [optional] |
| **transcription_config** | [TranscriptionConfig](TranscriptionConfig) | Configuration for speech transcription used to assist the agent. | |
| **knowledge_suggestion_config** | [KnowledgeSuggestionConfig](KnowledgeSuggestionConfig) | Configuration that defines how to produce knowledge suggestions. | |
| **state** | str | State of the assistant. | [optional] |
| **copilot** | [Copilot](Copilot) | Agent copilot configuration. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 228.0.0_
