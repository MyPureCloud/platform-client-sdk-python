---
title: AuditLogMessage
---
## AuditLogMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Id of the audit message. | [optional] |
| **user** | [**DomainEntityRef**](DomainEntityRef.html) | User associated with this audit message. | [optional] |
| **client** | [**AddressableEntityRef**](AddressableEntityRef.html) | Client associated with this audit message. | [optional] |
| **remote_ip** | **list[str]** | List of IP addresses of systems that originated or handled the request. | [optional] |
| **service_name** | **str** | Name of the service that logged this audit message. | [optional] |
| **event_date** | **datetime** | Date and time of when the audit message was logged. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **message** | [**MessageInfo**](MessageInfo.html) | Message describing the event being audited. | [optional] |
| **action** | **str** | Action that took place. | [optional] |
| **entity** | [**DomainEntityRef**](DomainEntityRef.html) | Entity that was impacted. | [optional] |
| **entity_type** | **str** | Type of the entity that was impacted. | [optional] |
| **property_changes** | [**list[PropertyChange]**](PropertyChange.html) | List of properties that were changed and changes made to those properties. | [optional] |
| **context** | **dict(str, str)** | Additional context for this message. | [optional] |
{: class="table table-striped"}


