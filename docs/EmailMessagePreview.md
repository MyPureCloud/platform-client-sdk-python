# EmailMessagePreview

## EmailMessagePreview

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **to** | [list[EmailAddress]](EmailAddress) | The recipients of the email message. | |
| **cc** | [list[EmailAddress]](EmailAddress) | The recipients that were copied on the email message. | [optional] |
| **bcc** | [list[EmailAddress]](EmailAddress) | The recipients that were blind copied on the email message. | [optional] |
| **pcFrom** | [EmailAddress](EmailAddress) | The sender of the email message. | |
| **reply_to** | [EmailAddress](EmailAddress) | The receiver of the reply email message. | [optional] |
| **subject** | str | The subject of the email message. | [optional] |
| **attachments** | [list[Attachment]](Attachment) | The attachments of the email message. | [optional] |
| **text_body_preview** | str | A truncated version of the textBody | [optional] |
| **time** | datetime | The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **history_included** | bool | Indicates whether the history of previous emails of the conversation is included within the email bodies of this message. | [optional] |
| **state** | str | The state of the current draft. | [optional] |
| **draft_type** | str | The type of draft that need to be treated. | [optional] |
| **email_size_bytes** | int | Indicates an estimation of the size of the current email as a whole, in its final, ready to be sent form. | [optional] |
| **max_email_size_bytes** | int | Indicates the maximum allowed size for an email to be send via SMTP server, based on the email domain configuration | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 210.0.0_
