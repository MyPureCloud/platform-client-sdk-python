---
title: WhatsAppIntegration
---
## WhatsAppIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | A unique Integration Id. | |
| **name** | **str** | The name of the WhatsApp integration. | |
| **phone_number** | **str** | The phone number associated to the whatsApp integration. | |
| **status** | **str** | The status of the WhatsApp Integration | [optional] |
| **recipient** | [**DomainEntityRef**](DomainEntityRef.html) | The recipient associated to the WhatsApp Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | **datetime** | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that created this Integration | [optional] |
| **modified_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that last modified this Integration | [optional] |
| **version** | **int** | Version number required for updates. | |
| **activation_status_code** | **str** | The status code of WhatsApp Integration activation process | [optional] |
| **activation_error_info** | [**ErrorBody**](ErrorBody.html) | The error information of WhatsApp Integration activation process | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


