# MergeInfo

## MergeInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | The status of a merge operation being taken against a cluster | [optional] |
| **error** | [MergeError](MergeError) | Error details about a failed merge. Only present if the status of the merge is ManualFailed or AutoFailed | [optional] |
| **date_merged** | datetime | The date the merge was attempted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 266.0.0_
