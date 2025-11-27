# OrganizationPublicApiUsageQueryRequest

## OrganizationPublicApiUsageQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | Specify the interval to query on. Start and end are inclusive. Start date cannot be more than a year ago. End date cannot be more than 90 days after the start. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **granularity** | str | Specify the granularity to aggregate the data to. | [optional] |
| **sort_by** | [list[UsageQuerySortBy]](UsageQuerySortBy) | Specify how to sort the returned data. | [optional] |
| **metrics** | list[str] | Specify which metrics you want returned (all will be returned by default). | [optional] |
| **template_uris** | list[str] | Specify if you only want a subset of templateUris represented in the query. | [optional] |
| **http_methods** | list[str] | Specify if you only want a subset of httpMethods represented in the query. | [optional] |
| **platforms** | list[str] | Specify if you only want a subset of platforms represented in the query. | [optional] |
| **group_by** | list[str] | Specify how to aggregate the data (by default the data is not aggregated). | [optional] |
| **user_ids** | list[str] | Specify if you only want a subset of userIds represented in the query. | [optional] |
| **oauth_client_ids** | list[str] | Specify if you only want a subset of oauthClientIds represented in the query. | [optional] |



_PureCloudPlatformClientV2 245.0.0_
