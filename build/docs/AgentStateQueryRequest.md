# AgentStateQueryRequest

## AgentStateQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_filter** | [AgentStateUserFilter](AgentStateUserFilter) | Filters that target user-level data | [optional] |
| **session_filter** | [AgentStateSessionFilter](AgentStateSessionFilter) | Filters that target session-level data | [optional] |
| **user_order_by** | str | Search user order dimension names; default to userName | [optional] |
| **user_order** | str | Search user order direction; default to asc | [optional] |
| **session_order_by** | str | Search session order dimension names; default to segmentStart | [optional] |
| **session_order** | str | Search session order direction; default to asc | [optional] |



_PureCloudPlatformClientV2 248.0.0_
