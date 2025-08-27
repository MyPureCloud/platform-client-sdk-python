# FlowPaths

## FlowPaths

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **category** | str | Category (use case) of the paths within a given domain. | |
| **date_start** | datetime | Start date of the date range included in the flow paths data. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_end** | datetime | End date of the date range included in the flow paths data. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **elements** | [dict(str, FlowPathsElement)](FlowPathsElement) | Unique element identifiers and their corresponding elements in the trie data structure representing the paths. | |



_PureCloudPlatformClientV2 236.0.0_
