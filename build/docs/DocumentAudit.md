---
title: DocumentAudit
---
## DocumentAudit

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **user** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **workspace** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **transaction_id** | **str** |  | [optional] |
| **transaction_initiator** | **bool** |  | [optional] |
| **application** | **str** |  | [optional] |
| **service_name** | **str** |  | [optional] |
| **level** | **str** |  | [optional] |
| **timestamp** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **status** | **str** |  | [optional] |
| **action_context** | **str** |  | [optional] |
| **action** | **str** |  | [optional] |
| **entity** | [**AuditEntityReference**](AuditEntityReference.html) |  | [optional] |
| **changes** | [**list[AuditChange]**](AuditChange.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


