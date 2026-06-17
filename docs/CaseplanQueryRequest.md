# CaseplanQueryRequest

## CaseplanQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Filter by Caseplan name (case-insensitive, partial match). Omitting name returns all Caseplans (subject to pagination). | [optional] |
| **name_search_type** | str | Type of name search to perform. Default is BEGINS_WITH. | [optional] |
| **page_size** | int | Number of results per page. Maximum is 200. Default is 25. | [optional] |
| **after** | str | Cursor for pagination. Use the \&quot;after\&quot; value from the previous response. | [optional] |
| **division_ids** | list[str] | Divisions to filter by. Accepts a list of UUIDs and/or &#39;*&#39;. | [optional] |



_PureCloudPlatformClientV2 260.0.0_
