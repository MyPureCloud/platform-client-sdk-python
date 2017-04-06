---
title: RoutingStatusRule
---
## RoutingStatusRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Name of the rule | |
| **agent** | [**User**](User.html) | The agent whose routing status will be watched. | |
| **routing_status** | **str** | The routing status on which to alert. | |
| **routing_limit_in_seconds** | **int** | The number of seconds to wait before alerting based upon the agent&#39;s routing status. | |
| **enabled** | **bool** | Indicates if the rule is enabled. | |
| **in_alarm** | **bool** | Indicates if the rule is in alarm state. | [optional] |
| **notification_users** | [**list[User]**](User.html) | The ids of users who will be notified of alarm state change. | |
| **alert_types** | **list[str]** | A collection of notification methods. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


