---
title: TestMessage
---
## TestMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | After the message has been sent, this is the value of the Message-ID email header. | [optional] |
| **to** | [**list[EmailAddress]**](EmailAddress.html) | The recipients of the email message. | |
| **pcFrom** | [**EmailAddress**](EmailAddress.html) | The sender of the email message. | |
| **subject** | **str** | The subject of the email message. | [optional] |
| **text_body** | **str** | The text body of the email message. | |
| **html_body** | **str** | The html body of the email message | [optional] |
| **time** | **datetime** | The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


