# WhatsAppDefinition

## WhatsAppDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The messaging template name. | |
| **namespace** | str | The messaging template namespace. This field is deprecated. | [optional] |
| **language** | str | The messaging template language configured for this template. This is a WhatsApp specific value. For example, &#39;en_US&#39; | |
| **buttons** | [list[Button]](Button) | List of buttons to be included in the standard WhatsApp messages channel | [optional] |
| **message_footer** | [MessageFooter](MessageFooter) | Footer for the message in the standard WhatsApp messages channel | [optional] |
| **header** | [MessageHeader](MessageHeader) | Header for the message in the standard WhatsApp messages channel | [optional] |
| **integration_id** | str | WhatsApp integration ID for whatsApp carousels | [optional] |
| **category** | str | Category of whatsApp carousels template. | [optional] |
| **template_status** | str | Template status of whatsApp carousels template. | [optional] |
| **status_info** | [StatusInfo](StatusInfo) | Status information about the template | [optional] |
| **carousel** | [Carousel](Carousel) | Definition for whatsApp carousels template. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
