# AnalyticsAgentStateAgentResponse

## AnalyticsAgentStateAgentResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | User Id - only returned if division is covered by agentStateNames permission | [optional] |
| **division_id** | str | Division Id | [optional] |
| **user_name** | str | User name - only returned if division is covered by agentStateNames permission | [optional] |
| **manager_id** | str | The user that this user reports to | [optional] |
| **session_count** | int | The count of sessions | [optional] |
| **sessions** | [list[AnalyticsAgentStateAgentSessionResult]](AnalyticsAgentStateAgentSessionResult) | List of sessions | [optional] |



_PureCloudPlatformClientV2 239.0.0_
