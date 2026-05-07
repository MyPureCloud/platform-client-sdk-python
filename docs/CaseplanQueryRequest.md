# CaseplanQueryRequest

## CaseplanQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Filter by caseplan name (case-insensitive, partial match). Omitting name returns all caseplans (subject to pagination). | [optional] |
| **page_size** | int | Number of results per page. Maximum is 200. Default is 25. | [optional] |
| **after** | str | Cursor for pagination. Use the \&quot;after\&quot; value from the previous response. | [optional] |
| **division_ids** | list[str] | Divisions to filter by. Accepts a list of UUIDs and/or &#39;*&#39;. | [optional] |



_PureCloudPlatformClientV2 257.0.0_
