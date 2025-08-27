# CommonAlert

## CommonAlert

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **user** | [UserReference](UserReference) | The user who created the rule that triggered the alert. | |
| **rule** | [AlertRuleProperties](AlertRuleProperties) | The properties of the rule that triggered the alert. | |
| **notifications** | [list[AlertNotification]](AlertNotification) | The collection of notification methods and the ids of users who were notified by those methods. | |
| **date_start** | datetime | The timestamp of when the alert was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_end** | datetime | The timestamp of when the alert ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **active** | bool | Indicates if an alert is currently active. | |
| **unread** | bool | Indicates if an alert has not been read. | |
| **wait_between_notification_ms** | int | The amount of time to wait between notification. Time is in milliseconds. | |
| **muted** | bool | Flag indicating if the alert is in a muted state. | |
| **snoozed** | bool | Flag indicating if the alert is in a snoozed state. | |
| **date_muted_until** | datetime | Timestamp of when the mute status of the alert should end. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_snoozed_until** | datetime | Timestamp of when the snooze status of the alert should end. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conditions** | [CommonRuleConditions](CommonRuleConditions) | The conditions that make up the rule. | |
| **conversation_id** | str | The id of the conversation instance that caused the alert to trigger. | [optional] |
| **alert_summary** | [AlertSummary](AlertSummary) | Summary of the alert status of the entities defined in the conditions.  Is set when rule has instance-based or team member based rule predicates | [optional] |
| **rule_uri** | str |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 236.0.0_
