---
title: RoutingStatusAlert
---
## RoutingStatusAlert

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Name of the rule | |
| **agent** | [**User**](User.html) | The agent whose routing status will be watched. | |
| **routing_status** | **str** | The routing status on which to alert. | |
| **routing_limit_in_seconds** | **int** | The number of seconds to wait before alerting based upon the agent&#39;s routing status. | |
| **rule_id** | **str** | The id of the rule. | |
| **start_date** | **datetime** | The date/time the alert was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **end_date** | **datetime** | The date/time the owning rule exiting in alarm status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **notification_users** | [**list[User]**](User.html) | The ids of users who were notified of alarm state change. | |
| **alert_types** | **list[str]** | A collection of notification methods. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


