---
title: WhatsAppIntegrationUpdateRequest
---
## WhatsAppIntegrationUpdateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | WhatsApp Integration name | [optional] |
| **action** | **str** | The action used to activate and then confirm a WhatsApp Integration. | |
| **authentication_method** | **str** | The authentication method used to confirm a WhatsApp Integration activation. If action is set to Activate, then authenticationMethod is a required field.  | [optional] |
| **confirmation_code** | **str** | The confirmation code sent by Whatsapp to you during the activation step. If action is set to Confirm, then confirmationCode is a required field. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


