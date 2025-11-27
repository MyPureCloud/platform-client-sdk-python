# OrganizationPublicApiUsageResultsResponse

## OrganizationPublicApiUsageResultsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str |  | [optional] |
| **query_status** | str | The status of the query. | |
| **error_body** | [ErrorBody](ErrorBody) | The reason for the failure. This will only be present if the query is in a FAILURE state but may not be included even if the state is FAILURE | [optional] |
| **next_uri** | str | The uri to get the next set of results. Will only be included if there is another page to retrieve. | [optional] |
| **entities** | [list[OrganizationPublicApiUsage]](OrganizationPublicApiUsage) | The results of the query. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 245.0.0_
