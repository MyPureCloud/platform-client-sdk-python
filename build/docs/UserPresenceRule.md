---
title: UserPresenceRule
---
## UserPresenceRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Name of the rule | |
| **presence_user** | [**User**](User.html) | The user whose presence will be watched. | |
| **presence_type** | **str** | Indicates to which presence type the presence value belongs. | |
| **presence_value** | **str** | The Org&#39;s UUID or Systems enum constance indicating the presence of concern. | |
| **presence_limit_in_seconds** | **int** | The number of seconds to wait before alerting based upon the user&#39;s presence. | |
| **enabled** | **bool** | Indicates if the rule is enabled. | |
| **in_alarm** | **bool** | Indicates if the rule is in alarm state. | [optional] |
| **notification_users** | [**list[User]**](User.html) | The ids of users who will be notified of alarm state change. | |
| **alert_types** | **list[str]** | A collection of notification methods. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


