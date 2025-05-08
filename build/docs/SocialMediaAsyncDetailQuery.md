# SocialMediaAsyncDetailQuery

## SocialMediaAsyncDetailQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **time_zone** | str | Time zone context used to calculate response intervals (this allows resolving DST changes). The interval offset is used even when timeZone is specified. Default is UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London | [optional] |
| **filter** | [SocialMediaQueryFilter](SocialMediaQueryFilter) | Behaves like a SQL WHERE clause. This is ANDed with the interval parameter. Expresses boolean logical predicates as well as dimensional filters | [optional] |
| **topic_ids** | list[str] | List of topicIds to query in | [optional] |
| **page_size** | int | The number of results per page | [optional] |
| **order** | str | Sorting of results based on time | [optional] |



_PureCloudPlatformClientV2 227.1.0_
