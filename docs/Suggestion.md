# Suggestion

## Suggestion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **type** | str | The type of the documents for which the suggestion is. | [optional] |
| **faq** | [Faq](Faq) | The Faq from the knowledgebase that was provided as the suggestion. | [optional] |
| **article** | [Article](Article) | The article from the knowledgebase that was provided as the suggestion. | [optional] |
| **date_created** | datetime | Date when the suggestion was created. For example: yyyy-MM-ddTHH:mm:ss.SSZ. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **answer_record_id** | str | The ID of the knowledge search that provided the suggestion. | [optional] |
| **trigger_type** | str | The trigger type of the suggestion. | [optional] |
| **context** | [SuggestionContext](SuggestionContext) | The conversation context in which the suggestion was raised. | [optional] |
| **state** | str | The state of the suggestion. | [optional] |
| **knowledge_search** | [SuggestionKnowledgeSearch](SuggestionKnowledgeSearch) | The suggested knowledge search result that was provided as the suggestion. | [optional] |
| **knowledge_article** | [SuggestionKnowledgeArticle](SuggestionKnowledgeArticle) | The suggested knowledge article that was provided as the suggestion. | [optional] |
| **canned_response** | [SuggestionCannedResponse](SuggestionCannedResponse) | The suggested canned response that was provided as the suggestion. | [optional] |
| **script** | [SuggestionScript](SuggestionScript) | The suggested script that was provided as the suggestion. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **conversation** | [AddressableEntityRef](AddressableEntityRef) | The conversation that the suggestions correspond to. | [optional] |
| **assistant** | [AddressableEntityRef](AddressableEntityRef) | The assistant that was used to provide the suggestions. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
