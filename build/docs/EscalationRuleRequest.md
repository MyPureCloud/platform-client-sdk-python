# EscalationRuleRequest

## EscalationRuleRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the escalation rule. | |
| **match_criteria** | str | The criteria that defines when a social media message should be escalated. | |
| **priority** | int | The priority of the escalation rule. The lower the number the higer the priority. Once a rule is matched others are skipped. | |
| **division_id** | str | The ID of the division the social escalation rule belongs to. | |
| **description** | str | A description of the social escalation rule. | [optional] |
| **status** | str | The status of the escalation rule. | [optional] |
| **open_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for an open message escalation. | [optional] |
| **facebook_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for a Facebook message escalation. | [optional] |
| **instagram_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for an Instagram message escalation. | [optional] |
| **twitter_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for a X (formerly Twitter) message escalation. | [optional] |



_PureCloudPlatformClientV2 237.0.0_
