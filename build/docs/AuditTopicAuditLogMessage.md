# AuditTopicAuditLogMessage

## AuditTopicAuditLogMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **user_id** | str |  | [optional] |
| **user_home_org_id** | str |  | [optional] |
| **username** | [AuditTopicDomainEntityRef](AuditTopicDomainEntityRef) |  | [optional] |
| **user_display** | str |  | [optional] |
| **client_id** | [AuditTopicAddressableEntityRef](AuditTopicAddressableEntityRef) |  | [optional] |
| **remote_ip** | list[str] |  | [optional] |
| **service_name** | str |  | [optional] |
| **level** | str |  | [optional] |
| **event_time** | datetime |  | [optional] |
| **message** | [AuditTopicMessageInfo](AuditTopicMessageInfo) |  | [optional] |
| **action** | str |  | [optional] |
| **entity_type** | str |  | [optional] |
| **entity** | [AuditTopicDomainEntityRef](AuditTopicDomainEntityRef) |  | [optional] |
| **property_changes** | [list[AuditTopicPropertyChange]](AuditTopicPropertyChange) |  | [optional] |
| **context** | dict(str, str) |  | [optional] |



_PureCloudPlatformClientV2 246.1.0_
