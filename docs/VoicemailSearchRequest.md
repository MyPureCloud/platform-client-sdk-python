# VoicemailSearchRequest

## VoicemailSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | str | The sort order for results | [optional] |
| **sort_by** | str | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | int | The number of results per page | [optional] |
| **page_number** | int | The page of resources you want to retrieve | [optional] |
| **sort** | [list[SearchSort]](SearchSort) | Multi-value sort order, list of multiple sort values | [optional] |
| **expand** | list[str] | Provides more details about a specified resource | [optional] |
| **query** | [list[VoicemailSearchCriteria]](VoicemailSearchCriteria) |  | [optional] |



_PureCloudPlatformClientV2 211.1.0_
