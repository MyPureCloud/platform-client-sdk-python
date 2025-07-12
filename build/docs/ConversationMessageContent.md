# ConversationMessageContent

## ConversationMessageContent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **content_type** | str | Type of this content element. | |
| **location** | [ConversationContentLocation](ConversationContentLocation) | Location content. | [optional] |
| **attachment** | [ConversationContentAttachment](ConversationContentAttachment) | Attachment content. | [optional] |
| **quick_reply** | [ConversationContentQuickReply](ConversationContentQuickReply) | Quick reply content. | [optional] |
| **button_response** | [ConversationContentButtonResponse](ConversationContentButtonResponse) | Button response content. | [optional] |
| **template** | [ConversationContentNotificationTemplate](ConversationContentNotificationTemplate) | Template notification content. | [optional] |
| **story** | [ConversationContentStory](ConversationContentStory) | Ephemeral story content. | [optional] |
| **card** | [ConversationContentCard](ConversationContentCard) | Card content | [optional] |
| **carousel** | [ConversationContentCarousel](ConversationContentCarousel) | Carousel content | [optional] |
| **text** | [ConversationContentText](ConversationContentText) | Text content. | [optional] |
| **quick_reply_v2** | [ConversationContentQuickReplyV2](ConversationContentQuickReplyV2) | Quick reply V2 content. | [optional] |
| **reactions** | [list[ConversationContentReaction]](ConversationContentReaction) | A set of reactions to a message. | [optional] |
| **push** | [ConversationContentPush](ConversationContentPush) | Push content. | [optional] |



_PureCloudPlatformClientV2 233.0.0_
