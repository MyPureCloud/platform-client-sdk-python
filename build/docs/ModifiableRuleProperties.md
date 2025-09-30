# ModifiableRuleProperties

## ModifiableRuleProperties

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
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 239.0.0_
