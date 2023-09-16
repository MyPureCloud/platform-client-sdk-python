---
title: ChatMessageResponse
---
## ChatMessageResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The id of the message | |
| **date_created** | **datetime** | Message&#39;s created time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_modified** | **datetime** | Message&#39;s last updated time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **to_jid** | **str** | Jid of message&#39;s recipient (roomJid or userJid) | |
| **jid** | **str** | Jid of message&#39;s sender (userJid) | |
| **body** | **str** | Message&#39;s body | |
| **mentions** | **dict(str, str)** | Message&#39;s mentions | [optional] |
| **edited** | **bool** | If message was edited | [optional] |
| **attachment_deleted** | **bool** | If message&#39;s attachment was deleted | [optional] |
| **file_uri** | **str** | URI of file attachment | [optional] |
| **thread** | [**Entity**](Entity.html) | The id for a thread this message corresponds to | |
{: class="table table-striped"}


