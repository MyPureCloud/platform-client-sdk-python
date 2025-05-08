# Leaderboard

## Leaderboard

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **division** | [Division](Division) | The targeted division for this leaderboard | [optional] |
| **metric** | [AddressableEntityRef](AddressableEntityRef) | The metric id if the leaderboard is about a specific metric | [optional] |
| **date_start_workday** | date | Start workday used as the date range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end_workday** | date | End workday used as the date range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **leaders** | [list[LeaderboardItem]](LeaderboardItem) | The list of leaders generated. | [optional] |
| **user_rank** | [LeaderboardItem](LeaderboardItem) | The requesting user&#39;s rank | [optional] |
| **performance_profile** | [AddressableEntityRef](AddressableEntityRef) | The targeted performance profile for the average points | [optional] |



_PureCloudPlatformClientV2 227.1.0_
