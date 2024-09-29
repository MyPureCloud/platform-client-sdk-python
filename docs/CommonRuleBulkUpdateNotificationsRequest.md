# CommonRuleBulkUpdateNotificationsRequest

## CommonRuleBulkUpdateNotificationsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **rule_ids** | list[str] | The user supplied rules ids to be updated | |
| **properties** | [ModifiableRuleProperties](ModifiableRuleProperties) | The rule properties to be updated | [optional] |
| **types_to_add** | list[str] | Collection of alerting notification types to add for all entities in the rules | [optional] |
| **types_to_remove** | list[str] | Collection of alerting notification types to remove for all entities in the rules | [optional] |



_PureCloudPlatformClientV2 212.0.0_
