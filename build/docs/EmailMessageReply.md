# EmailMessageReply

## EmailMessageReply

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **to** | [list[EmailAddress]](EmailAddress) | The recipients of the email message. | |
| **cc** | [list[EmailAddress]](EmailAddress) | The recipients that were copied on the email message. | [optional] |
| **bcc** | [list[EmailAddress]](EmailAddress) | The recipients that were blind copied on the email message. | [optional] |
| **pcFrom** | [EmailAddress](EmailAddress) | The sender of the email message. | |
| **reply_to** | [EmailAddress](EmailAddress) | The receiver of the reply email message. | [optional] |
| **subject** | str | The subject of the email message. | [optional] |
| **attachments** | [list[Attachment]](Attachment) | The attachments of the email message. | [optional] |
| **text_body** | str | The text body of the email message. | |
| **html_body** | str | The html body of the email message. | [optional] |
| **time** | datetime | The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **history_included** | bool | Indicates whether the history of previous emails of the conversation is included within the email bodies of this message. | [optional] |
| **email_size_bytes** | int | Indicates an estimation of the size of the current email as a whole, in its final, ready to be sent form. | [optional] |
| **max_email_size_bytes** | int | Indicates the maximum allowed size for an email to be send via SMTP server, based on the email domain configuration | [optional] |



_PureCloudPlatformClientV2 246.0.0_
