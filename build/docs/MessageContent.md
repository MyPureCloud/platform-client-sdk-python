---
title: MessageContent
---
## MessageContent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **content_type** | **str** | Type of this content element. If contentType = \&quot;Attachment\&quot; only one item is allowed. | |
| **location** | [**ContentLocation**](ContentLocation.html) | Location object | [optional] |
| **attachment** | [**ContentAttachment**](ContentAttachment.html) | Attachment object | [optional] |
| **quick_reply** | [**ContentQuickReply**](ContentQuickReply.html) | Quick reply object | [optional] |
| **button_response** | [**ContentButtonResponse**](ContentButtonResponse.html) | Button response object | [optional] |
| **generic** | [**ContentGeneric**](ContentGeneric.html) | Generic content object | [optional] |
| **list** | [**ContentList**](ContentList.html) | List content object | [optional] |
| **template** | [**ContentNotificationTemplate**](ContentNotificationTemplate.html) | Template notification object | [optional] |
| **reactions** | [**list[ContentReaction]**](ContentReaction.html) | A list of reactions | [optional] |
| **mention** | [**MessagingRecipient**](MessagingRecipient.html) | This is used to identify who the message is sent to, as well as who it was sent from. This information is channel specific - depends on capabilities to describe party by the platform | [optional] |
| **postback** | [**ContentPostback**](ContentPostback.html) | The postback object result of a user clicking in a button | [optional] |
{: class="table table-striped"}


