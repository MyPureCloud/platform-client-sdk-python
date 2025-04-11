# AsyncUserDetailsQuery

## AsyncUserDetailsQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | Specifies the date and time range of data being queried. Conversations MUST have started within this time range to potentially be included within the result set. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **user_filters** | [list[UserDetailQueryFilter]](UserDetailQueryFilter) | Filters that target the users to retrieve data for | [optional] |
| **presence_filters** | [list[PresenceDetailQueryFilter]](PresenceDetailQueryFilter) | Filters that target system and organization presence-level data | [optional] |
| **routing_status_filters** | [list[RoutingStatusDetailQueryFilter]](RoutingStatusDetailQueryFilter) | Filters that target agent routing status-level data | [optional] |
| **order** | str | Sort the result set in ascending/descending order. Default is ascending | [optional] |
| **limit** | int | Specify number of results to be returned | [optional] |



_PureCloudPlatformClientV2 226.0.0_
