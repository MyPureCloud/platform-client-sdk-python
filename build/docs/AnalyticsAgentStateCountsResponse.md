# AnalyticsAgentStateCountsResponse

## AnalyticsAgentStateCountsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **segment_counts** | [list[AgentStateSegmentTypeCount]](AgentStateSegmentTypeCount) | List of count by segment types | [optional] |
| **presence_counts** | [list[AgentStatePresenceCount]](AgentStatePresenceCount) | List of count by presences | [optional] |
| **routing_status_counts** | [list[AgentStateRoutingStatusCount]](AgentStateRoutingStatusCount) | List of count by routing statuses | [optional] |
| **is_out_of_office_counts** | [list[AgentStateIsOutOfOfficeCount]](AgentStateIsOutOfOfficeCount) | List of count by out of office states | [optional] |
| **adherence_state_counts** | [list[AgentStateAdherenceStateCount]](AgentStateAdherenceStateCount) | List of count by adherence state | [optional] |
| **scheduled_activity_category_counts** | [list[AgentStateActivityCategoryCount]](AgentStateActivityCategoryCount) | List of count by scheduled activity category | [optional] |
| **actual_activity_category_counts** | [list[AgentStateActivityCategoryCount]](AgentStateActivityCategoryCount) | List of count by actual activity category | [optional] |



_PureCloudPlatformClientV2 266.0.0_
