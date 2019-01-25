---
title: WebChatDeployment
---
## WebChatDeployment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **description** | **str** |  | [optional] |
| **authentication_required** | **bool** |  | [optional] |
| **authentication_url** | **str** | URL for third party service authenticating web chat clients. See https://github.com/MyPureCloud/authenticated-web-chat-server-examples | [optional] |
| **disabled** | **bool** |  | [optional] |
| **web_chat_config** | [**WebChatConfig**](WebChatConfig.html) |  | [optional] |
| **allowed_domains** | **list[str]** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


