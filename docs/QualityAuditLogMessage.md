# QualityAuditLogMessage

## QualityAuditLogMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id of the audit message. | [optional] |
| **user_home_org_id** | str | Home Organization Id associated with this audit message. | [optional] |
| **user_trustee_org_id** | str | Trustee Organization Id if this audit message is from trustee access. | [optional] |
| **user** | [DomainEntityRef](DomainEntityRef) | User associated with this audit message. | [optional] |
| **client** | [AddressableEntityRef](AddressableEntityRef) | Client associated with this audit message. | [optional] |
| **remote_ips** | list[str] | List of IP addresses of systems that originated or handled the request. | [optional] |
| **service_name** | str | Name of the service that logged this audit message. | [optional] |
| **level** | str | The level of this audit message. | [optional] |
| **status** | str | The status of the action of this audit message. | [optional] |
| **event_date** | datetime | Date and time of when the audit message was logged. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **message_info** | [MessageInfo](MessageInfo) | Message describing the event being audited. | [optional] |
| **action** | str | Action that took place. | [optional] |
| **entity** | [DomainEntityRef](DomainEntityRef) | Entity that was impacted. | [optional] |
| **entity_type** | str | Type of the entity that was impacted. | [optional] |
| **property_changes** | [list[PropertyChange]](PropertyChange) | List of properties that were changed and changes made to those properties. | [optional] |
| **context** | dict(str, str) | Additional context for this message. | [optional] |



_PureCloudPlatformClientV2 217.0.0_