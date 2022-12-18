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
| **queue** | [**DomainEntityRef**](DomainEntityRef.html) | The queue to route the emails to. | [optional] |
| **priority** | **int** | The priority to use for routing. | [optional] |
| **skills** | [**list[DomainEntityRef]**](DomainEntityRef.html) | The skills to use for routing. | [optional] |
| **language** | [**DomainEntityRef**](DomainEntityRef.html) | The language to use for routing. | [optional] |
| **from_name** | **str** | The sender name to use for outgoing replies. | |
| **from_email** | **str** | The sender email to use for outgoing replies. | [optional] |
| **flow** | [**DomainEntityRef**](DomainEntityRef.html) | The flow to use for processing the email. | [optional] |
| **reply_email_address** | [**QueueEmailAddress**](QueueEmailAddress.html) | The route to use for email replies. | [optional] |
| **auto_bcc** | [**list[EmailAddress]**](EmailAddress.html) | The recipients that should be automatically blind copied on outbound emails associated with this InboundRoute. | [optional] |
| **spam_flow** | [**DomainEntityRef**](DomainEntityRef.html) | The flow to use for processing inbound emails that have been marked as spam. | [optional] |
| **signature** | [**Signature**](Signature.html) | The configuration for the canned response signature that will be appended to outbound emails sent via this route | [optional] |
| **history_inclusion** | **str** | The configuration to indicate how the history of a conversation has to be included in a draft | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


