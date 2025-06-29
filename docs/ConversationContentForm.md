# ConversationContentForm

## ConversationContentForm

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **introduction** | [ConversationContentIntroduction](ConversationContentIntroduction) | The intro component, used to give an intro into what the form entails | [optional] |
| **form_pages** | [list[ConversationFormPage]](ConversationFormPage) | Form pages | [optional] |
| **received_message** | [ConversationContentReceivedReplyMessage](ConversationContentReceivedReplyMessage) | The message prompt to fill out the form received. | [optional] |
| **reply_message** | [ConversationContentReceivedReplyMessage](ConversationContentReceivedReplyMessage) | The reply message after the user has filled out the form received. | [optional] |
| **show_summary** | bool | Show summary at end of form submission. | [optional] |
| **response** | [list[ConversationFormResponseComponent]](ConversationFormResponseComponent) | Content of the payload included in the Form response. | [optional] |
| **originating_message_id** | str | Reference to the ID of the original message. | [optional] |
| **canned_response_id** | str | The id of the canned response which was used to create the form. | |



_PureCloudPlatformClientV2 232.0.0_
