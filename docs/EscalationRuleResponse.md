# EscalationRuleResponse

## EscalationRuleResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the escalation rule. | [optional] |
| **name** | str | The name of the escalation rule. | [optional] |
| **match_criteria** | str | The criteria that defines when a social media message should be escalated. | |
| **priority** | int | The priority of the escalation rule. | [optional] |
| **division_id** | str | The ID of the division the social escalation rule belongs to. | |
| **description** | str | A description of the social escalation rule. | [optional] |
| **date_created** | datetime | Timestamp indicating when the escalation rule was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Timestamp indicating when the escalation rule was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | The status of the escalation rule. | [optional] |
| **open_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for an open message escalation. | [optional] |
| **facebook_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for a Facebook message escalation. | [optional] |
| **instagram_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for an Instagram message escalation. | [optional] |
| **twitter_escalation** | [EscalationTarget](EscalationTarget) | The target integration configuration used for a X (formerly Twitter) message escalation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
