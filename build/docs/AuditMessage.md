---
title: AuditMessage
---
## AuditMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | AuditMessage ID. | |
| **user** | [**AuditUser**](AuditUser.html) |  | [optional] |
| **correlation_id** | **str** | Correlation ID. | [optional] |
| **transaction_id** | **str** | Transaction ID. | [optional] |
| **transaction_initiator** | **bool** | Whether or not this audit can be considered the initiator of the transaction it is a part of. | [optional] |
| **application** | **str** | The application through which the action of this AuditMessage was initiated. | [optional] |
| **service_name** | **str** | The name of the service which sent this AuditMessage. | |
| **level** | **str** | The level of this audit. USER or SYSTEM. | |
| **timestamp** | **str** | The time at which the action of this AuditMessage was initiated. | [optional] |
| **received_timestamp** | **str** | The time at which this AuditMessage was received. | |
| **status** | **str** | The status of the action of this AuditMessage | |
| **action_context** | **str** | The context of a system-level action | [optional] |
| **action** | **str** | A string representing the action that took place | [optional] |
| **changes** | [**list[Change]**](Change.html) | Details about any changes that occurred in this audit | [optional] |
| **entity** | [**AuditEntity**](AuditEntity.html) |  | [optional] |
| **service_context** | [**ServiceContext**](ServiceContext.html) | The service-specific context associated with this AuditMessage. | [optional] |
{: class="table table-striped"}


