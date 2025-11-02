# ShiftTradeSettings

## ShiftTradeSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether shift trading is enabled for this management unit | [optional] |
| **auto_review** | bool | Whether automatic shift trade review is enabled according to the rules defined in for this management unit | [optional] |
| **allow_direct_trades** | bool | Whether direct shift trades between agents are allowed | [optional] |
| **min_hours_in_future** | int | The minimum number of hours in the future shift trades are allowed | [optional] |
| **unequal_paid** | str | How to handle shift trades which involve unequal paid times | [optional] |
| **one_sided** | str | How to handle one-sided shift trades | [optional] |
| **weekly_min_paid_violations** | str | How to handle shift trades which result in violations of weekly minimum paid time constraint | [optional] |
| **weekly_max_paid_violations** | str | How to handle shift trades which result in violations of weekly maximum paid time constraint | [optional] |
| **requires_matching_queues** | bool | Whether to constrain shift trades to agents with matching queues | [optional] |
| **requires_matching_languages** | bool | Whether to constrain shift trades to agents with matching languages | [optional] |
| **requires_matching_skills** | bool | Whether to constrain shift trades to agents with matching skills | [optional] |
| **requires_matching_planning_groups** | bool | Whether to constrain shift trades to agents with matching planning groups | [optional] |
| **activity_category_rules** | [list[ShiftTradeActivityRule]](ShiftTradeActivityRule) | Rules that specify what to do with activity categories that are part of a shift defined in a trade | [optional] |
| **external_activity_rules** | [list[ShiftTradeExternalActivityRule]](ShiftTradeExternalActivityRule) | Rules that specify what to do with external activities that are part of a shift | [optional] |
| **external_activity_rule_ignores_activity_category_rule** | bool | Whether external activity rules ignore activity category rules | [optional] |
| **max_trade_span_weeks** | int | The maximum number of weeks a shift trade can span | [optional] |
| **max_trades_per_agent_per_week** | int | The maximum number of shift trades an agent can submit per week | [optional] |
| **min_minutes_between_shifts** | int | The minimum number of minutes between shifts | [optional] |
| **planning_period_min_paid_violations** | str | How to handle shift trades which result in violations of planning period minimum paid time constraint | [optional] |
| **planning_period_max_paid_violations** | str | How to handle shift trades which result in violations of planning period maximum paid time constraint | [optional] |
| **min_minutes_between_shifts_violations** | str | How to handle shift trades which result in violations of minimum number of minutes between shifts constraint | [optional] |



_PureCloudPlatformClientV2 242.0.0_
