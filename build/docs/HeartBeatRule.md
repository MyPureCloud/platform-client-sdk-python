---
title: HeartBeatRule
---
## HeartBeatRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Name of the rule | |
| **sender_id** | **str** | The value that identifies the sender of the heartbeat. | |
| **heart_beat_timeout_in_minutes** | **int** | The number of minutes to wait before alerting missing heartbeats. | |
| **enabled** | **bool** | Indicates if the rule is enabled. | |
| **in_alarm** | **bool** | Indicates if the rule is in alarm state. | [optional] |
| **notification_users** | [**list[User]**](User.html) | The ids of users who will be notified of alarm state change. | |
| **alert_types** | **list[str]** | A collection of notification methods. | |
| **rule_type** | **str** | The type of system the will be generating the heartbeat. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


