---
title: InboundRoute
---
## InboundRoute

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **pattern** | **str** | The search pattern that the mailbox name should match. | |
| **queue** | [**UriReference**](UriReference.html) | The queue to route the emails to. | [optional] |
| **priority** | **int** | The priority to use for routing. | [optional] |
| **skills** | [**list[UriReference]**](UriReference.html) | The skills to use for routing. | [optional] |
| **language** | [**UriReference**](UriReference.html) | The language to use for routing. | [optional] |
| **from_name** | **str** | The sender name to use for outgoing replies. | |
| **from_email** | **str** | The sender email to use for outgoing replies. | |
| **flow** | [**UriReference**](UriReference.html) | The flow to use for processing the email. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


