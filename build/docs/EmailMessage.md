---
title: EmailMessage
---
## EmailMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **to** | [**list[EmailAddress]**](EmailAddress.html) | The recipients of the email message. | |
| **cc** | [**list[EmailAddress]**](EmailAddress.html) | The recipients that were copied on the email message. | [optional] |
| **bcc** | [**list[EmailAddress]**](EmailAddress.html) | The recipients that were blind copied on the email message. | [optional] |
| **pcFrom** | [**EmailAddress**](EmailAddress.html) | The sender of the email message. | |
| **subject** | **str** | The subject of the email message. | [optional] |
| **attachments** | [**list[Attachment]**](Attachment.html) | The attachments of the email message. | [optional] |
| **text_body** | **str** | The text body of the email message. | |
| **html_body** | **str** | The html body of the email message. | [optional] |
| **time** | **datetime** | The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **history_included** | **bool** | Indicates whether the history of previous emails of the conversation is included within the email bodies of this message. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


