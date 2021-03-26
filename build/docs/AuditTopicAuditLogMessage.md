---
title: AuditTopicAuditLogMessage
---
## AuditTopicAuditLogMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **user_id** | **str** |  | [optional] |
| **user_home_org_id** | **str** |  | [optional] |
| **username** | [**AuditTopicDomainEntityRef**](AuditTopicDomainEntityRef.html) |  | [optional] |
| **user_display** | **str** |  | [optional] |
| **client_id** | [**AuditTopicAddressableEntityRef**](AuditTopicAddressableEntityRef.html) |  | [optional] |
| **remote_ip** | **list[str]** |  | [optional] |
| **service_name** | **str** |  | [optional] |
| **event_time** | **datetime** |  | [optional] |
| **message** | [**AuditTopicMessageInfo**](AuditTopicMessageInfo.html) |  | [optional] |
| **action** | **str** |  | [optional] |
| **entity_type** | **str** |  | [optional] |
| **entity** | [**AuditTopicDomainEntityRef**](AuditTopicDomainEntityRef.html) |  | [optional] |
| **property_changes** | [**list[AuditTopicPropertyChange]**](AuditTopicPropertyChange.html) |  | [optional] |
| **context** | **dict(str, str)** |  | [optional] |
{: class="table table-striped"}


