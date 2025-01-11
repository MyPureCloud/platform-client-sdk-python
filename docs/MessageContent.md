# MessageContent

## MessageContent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **content_type** | str | Type of this content element. | |
| **location** | [ContentLocation](ContentLocation) | Location content. | [optional] |
| **attachment** | [ContentAttachment](ContentAttachment) | Attachment content. | [optional] |
| **quick_reply** | [ContentQuickReply](ContentQuickReply) | Quick reply content. | [optional] |
| **button_response** | [ContentButtonResponse](ContentButtonResponse) | Button response content. | [optional] |
| **generic** | [ContentGeneric](ContentGeneric) | Generic content (Deprecated). | [optional] |
| **list** | [ContentList](ContentList) | List content (Deprecated). | [optional] |
| **template** | [ContentNotificationTemplate](ContentNotificationTemplate) | Template notification content. | [optional] |
| **reactions** | [list[ContentReaction]](ContentReaction) | A set of reactions to a message. | [optional] |
| **mention** | [MessagingRecipient](MessagingRecipient) | Mention content. | [optional] |
| **postback** | [ContentPostback](ContentPostback) | Structured message postback (Deprecated). | [optional] |
| **story** | [ContentStory](ContentStory) | Ephemeral story content. | [optional] |
| **card** | [ContentCard](ContentCard) | Card content | [optional] |
| **carousel** | [ContentCarousel](ContentCarousel) | Carousel content | [optional] |
| **text** | [ContentText](ContentText) | Text content. | [optional] |
| **quick_reply_v2** | [ContentQuickReplyV2](ContentQuickReplyV2) | Quick reply V2 content. | [optional] |



_PureCloudPlatformClientV2 219.1.0_
