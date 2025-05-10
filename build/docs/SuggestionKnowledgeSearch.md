# SuggestionKnowledgeSearch

## SuggestionKnowledgeSearch

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **title** | str | The article title. | [optional] |
| **snippets** | list[str] | Snippets of text from the article matching the query. | [optional] |
| **confidence** | float | Value between 0 and 1. 1 corresponds to very confident, 0 to not confident at all. | [optional] |
| **search_id** | str | The search id. | [optional] |
| **document** | [AddressableEntityRef](AddressableEntityRef) | The article matching the query. | [optional] |
| **version** | [AddressableEntityRef](AddressableEntityRef) | The version of the article. | [optional] |
| **knowledge_answer** | [SuggestionKnowledgeAnswer](SuggestionKnowledgeAnswer) | The most relevant answer within a searched article for the searched query | [optional] |
| **variations** | [list[AddressableEntityRef]](AddressableEntityRef) | Variations of the article. | [optional] |



_PureCloudPlatformClientV2 228.0.0_
