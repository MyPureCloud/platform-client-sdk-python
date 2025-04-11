# CommonRule

## CommonRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Name of the rule | |
| **description** | str | The description of the rule. | [optional] |
| **enabled** | bool | Indicates if the rule is enabled. | [optional] |
| **notifications** | [list[AlertNotification]](AlertNotification) | The alert notification types to trigger when alarm state changes as well as the users they will be sent to. | [optional] |
| **send_exiting_alarm_notifications** | bool | Indicates if the alert will send a notification when it is closed. | [optional] |
| **wait_between_notification_ms** | int | The amount of time in milliseconds to wait between notification. | [optional] |
| **conditions** | [CommonRuleConditions](CommonRuleConditions) | The set of metric conditions that would trigger an alert. | [optional] |
| **type** | str | The type of the rule. | |
| **in_alarm** | bool | Indicates if the rule is in alarm state. | [optional] |
| **user** | [UserReference](UserReference) | The entity that created the rule. | [optional] |
| **version** | int | The current version number of the rule. | [optional] |
| **date_created** | datetime | The creation date of the rule when the rule was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_last_modified** | datetime | The timestamp of the last update to the rule. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 226.0.0_
