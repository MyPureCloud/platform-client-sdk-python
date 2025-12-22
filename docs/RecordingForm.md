# RecordingForm

## RecordingForm

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **introduction** | [RecordingIntroduction](RecordingIntroduction) | The introduction component, used to give an intro into what the form entails. | [optional] |
| **form_pages** | [list[RecordingFormPage]](RecordingFormPage) | Form pages. | [optional] |
| **received_message** | [ReceivedReplyMessage](ReceivedReplyMessage) | Defines the initial prompt message structure containing title and subtitle fields that are displayed to the end user when a form requires completion. | [optional] |
| **reply_message** | [ReceivedReplyMessage](ReceivedReplyMessage) | The reply message after the user has filled out the form received. | [optional] |
| **response** | [list[RecordingFormResponseComponent]](RecordingFormResponseComponent) | Content of the payload included in the Form response. | [optional] |
| **originating_message_id** | str | Reference to the id of the original message. | [optional] |
| **canned_response_id** | str | The id of the canned response which was used to create the form. | [optional] |



_PureCloudPlatformClientV2 246.1.0_
