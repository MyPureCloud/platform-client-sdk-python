---
title: HeartBeatAlert
---
## HeartBeatAlert

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Name of the rule | |
| **sender_id** | **str** | The value that identifies the sender of the heartbeat. | |
| **heart_beat_timeout_in_minutes** | **int** | The number of minutes to wait before alerting missing heartbeats. | |
| **rule_id** | **str** | The id of the rule. | |
| **start_date** | **datetime** | The date/time the alert was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **end_date** | **datetime** | The date/time the owning rule exiting in alarm status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **notification_users** | [**list[User]**](User.html) | The ids of users who were notified of alarm state change. | |
| **alert_types** | **list[str]** | A collection of notification methods. | |
| **rule_type** | **str** | The type of heartbeat rule that generated the alert | |
| **rule_uri** | **str** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


