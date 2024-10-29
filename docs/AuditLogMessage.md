# AuditLogMessage

## AuditLogMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id of the audit message. | [optional] |
| **user_home_org_id** | str | Home Organization Id associated with this audit message. | [optional] |
| **user** | [DomainEntityRef](DomainEntityRef) | User associated with this audit message. | [optional] |
| **client** | [AddressableEntityRef](AddressableEntityRef) | Client associated with this audit message. | [optional] |
| **remote_ip** | list[str] | List of IP addresses of systems that originated or handled the request. | [optional] |
| **service_name** | str | Name of the service that logged this audit message. | [optional] |
| **level** | str | Level of this audit message, USER or SYSTEM. | [optional] |
| **event_date** | datetime | Date and time of when the audit message was logged. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **message** | [MessageInfo](MessageInfo) | Message describing the event being audited. | [optional] |
| **action** | str | Action that took place. | [optional] |
| **entity** | [DomainEntityRef](DomainEntityRef) | Entity that was impacted. | [optional] |
| **entity_type** | str | Type of the entity that was impacted. | [optional] |
| **status** | str | Status of the event being audited | [optional] |
| **application** | str | Name of the application used to perform the audit&#39;s action | [optional] |
| **initiating_action** | [InitiatingAction](InitiatingAction) | Id and action of the audit initiating the transaction | [optional] |
| **transaction_initiator** | bool | Whether the current audit is the initiator of the transaction | [optional] |
| **property_changes** | [list[PropertyChange]](PropertyChange) | List of properties that were changed and changes made to those properties. | [optional] |
| **context** | dict(str, str) | Additional context for this message. | [optional] |
| **entity_changes** | [list[EntityChange]](EntityChange) | List of entities that were changed and changes made to those entities. | [optional] |



_PureCloudPlatformClientV2 215.0.0_
