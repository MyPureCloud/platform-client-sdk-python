---
title: WebChatMessage
---
## WebChatMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **conversation** | [**WebChatConversation**](WebChatConversation.html) | The identifier of the conversation | |
| **sender** | [**WebChatMemberInfo**](WebChatMemberInfo.html) | The member who sent the message | |
| **body** | **str** | The message body. | |
| **body_type** | **str** | The purpose of the message within the conversation, such as a standard text entry versus a greeting. | |
| **timestamp** | **datetime** | The timestamp of the message, in ISO-8601 format | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


