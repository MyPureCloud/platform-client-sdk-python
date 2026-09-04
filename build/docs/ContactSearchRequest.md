# ContactSearchRequest

## ContactSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_number** | int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] |
| **page_size** | int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] |
| **division_ids** | list[str] | Which divisions to search, up to 50 | [optional] |
| **expand** | list[str] | Which fields, if any, to expand | [optional] |
| **operation** | [ContactSearchOperation](ContactSearchOperation) | Search operation to execute, currently supports {@code simpleSearch} only. | [optional] |



_PureCloudPlatformClientV2 266.0.0_
