---
title: ConversationMessageContent
---
## ConversationMessageContent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **content_type** | **str** | Type of this content element. If contentType = \&quot;Attachment\&quot; only one item is allowed. | |
| **location** | [**ConversationContentLocation**](ConversationContentLocation.html) | Location content. | [optional] |
| **story** | [**ConversationContentStory**](ConversationContentStory.html) | Ephemeral story content. | [optional] |
| **attachment** | [**ConversationContentAttachment**](ConversationContentAttachment.html) | Attachment content. | [optional] |
| **quick_reply** | [**ConversationContentQuickReply**](ConversationContentQuickReply.html) | Quick reply content. | [optional] |
| **template** | [**ConversationContentNotificationTemplate**](ConversationContentNotificationTemplate.html) | Template notification content. | [optional] |
| **button_response** | [**ConversationContentButtonResponse**](ConversationContentButtonResponse.html) | Button response content. | [optional] |
| **generic** | [**ConversationContentGeneric**](ConversationContentGeneric.html) | Generic Template Object | [optional] |
| **card** | [**ConversationContentCard**](ConversationContentCard.html) | Card (Generic Template) Object | [optional] |
| **carousel** | [**ConversationContentCarousel**](ConversationContentCarousel.html) | Carousel (Multiple Generic Template) Object | [optional] |
{: class="table table-striped"}


