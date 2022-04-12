---
title: LineIntegration
---
## LineIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | A unique Integration Id | |
| **name** | **str** | The name of the LINE Integration | |
| **supported_content** | [**SupportedContentReference**](SupportedContentReference.html) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [**MessagingSettingReference**](MessagingSettingReference.html) |  | [optional] |
| **channel_id** | **str** | The Channel Id from LINE messenger | |
| **webhook_uri** | **str** | The Webhook URI to be updated in LINE platform | |
| **status** | **str** | The status of the LINE Integration | [optional] |
| **recipient** | [**DomainEntityRef**](DomainEntityRef.html) | The recipient associated to the Line Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | **datetime** | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that created this Integration | [optional] |
| **modified_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that last modified this Integration | [optional] |
| **version** | **int** | Version number required for updates. | |
| **create_status** | **str** | Status of asynchronous create operation | [optional] |
| **create_error** | [**ErrorBody**](ErrorBody.html) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


