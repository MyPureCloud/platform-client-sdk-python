# AdditionalMessage

## AdditionalMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **text_body** | str | The body of the text message.  Maximum character counts are: SMS - 765 characters, other channels - 2000 characters. | |
| **media_ids** | list[str] | The media ids associated with the text message. See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage. | [optional] |
| **messaging_template** | [SendMessagingTemplateRequest](SendMessagingTemplateRequest) | Pre-defined message templates for structured communications. Supports various template types including WhatsApp business messaging template and form | [optional] |



_PureCloudPlatformClientV2 245.0.0_
