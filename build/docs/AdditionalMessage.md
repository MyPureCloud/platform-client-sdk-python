# AdditionalMessage

## AdditionalMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **text_body** | str | The body of the text message.  Maximum character counts are: SMS - 765 characters, other channels - 2000 characters. | |
| **media_ids** | list[str] | The media ids associated with the text message. See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage. | [optional] |
| **messaging_template** | [SendMessagingTemplateRequest](SendMessagingTemplateRequest) | The messaging template use to send a predefined canned response with the message | [optional] |



_PureCloudPlatformClientV2 230.0.0_
