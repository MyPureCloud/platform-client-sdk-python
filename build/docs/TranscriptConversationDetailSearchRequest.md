# TranscriptConversationDetailSearchRequest

## TranscriptConversationDetailSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | str | The sort order for results | [optional] |
| **sort_by** | str | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | int | The number of results per page | [optional] |
| **page_number** | int | The page of resources you want to retrieve | [optional] |
| **sort** | [list[SearchSort]](SearchSort) | Multi-value sort order, list of multiple sort values | [optional] |
| **types** | list[str] | Resource domain type to search | |
| **query** | [list[TranscriptConversationDetailSearchCriteria]](TranscriptConversationDetailSearchCriteria) | The search criteria | [optional] |



_PureCloudPlatformClientV2 218.0.0_
