# VoicemailsSearchResponse

## VoicemailsSearchResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **total** | int | The total number of results found | |
| **page_count** | int | The total number of pages | |
| **page_size** | int | The current page size | |
| **page_number** | int | The current page number | |
| **previous_page** | str | Q64 value for the previous page of results | [optional] |
| **current_page** | str | Q64 value for the current page of results | [optional] |
| **next_page** | str | Q64 value for the next page of results | [optional] |
| **types** | list[str] | Resource types the search was performed against | |
| **results** | [list[VoicemailMessage]](VoicemailMessage) | Search results | |



_PureCloudPlatformClientV2 217.0.0_
