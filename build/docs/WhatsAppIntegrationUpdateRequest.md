---
title: WhatsAppIntegrationUpdateRequest
---
## WhatsAppIntegrationUpdateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | WhatsApp Integration name | [optional] |
| **supported_content** | [**SupportedContentReference**](SupportedContentReference.html) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [**MessagingSettingRequestReference**](MessagingSettingRequestReference.html) | Defines the message settings to be applied for this integration | [optional] |
| **action** | **str** | The action used to activate and then confirm a WhatsApp Integration. | [optional] |
| **authentication_method** | **str** | The authentication method used to confirm a WhatsApp Integration activation. If action is set to Activate, then authenticationMethod is a required field.  | [optional] |
| **confirmation_code** | **str** | The confirmation code sent by Whatsapp to you during the activation step. If action is set to Confirm, then confirmationCode is a required field. | [optional] |
| **phone_number** | **str** | Phone number to associate with the WhatsApp integration | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


