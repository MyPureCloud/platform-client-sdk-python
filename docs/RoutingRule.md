# RoutingRule

## RoutingRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operator** | str | matching operator.  MEETS_THRESHOLD matches any agent with a score at or above the rule&#39;s threshold.  ANY matches all specified agents, regardless of score. | [optional] |
| **threshold** | int | threshold required for routing attempt (generally an agent score).  may be null for operator ANY. | [optional] |
| **wait_seconds** | float | seconds to wait in this rule before moving to the next | [optional] |



_PureCloudPlatformClientV2 237.0.0_
