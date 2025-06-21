# WebChatDeployment

## WebChatDeployment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str |  | [optional] |
| **authentication_required** | bool |  | [optional] |
| **authentication_url** | str | URL for third party service authenticating web chat clients. See https://github.com/MyPureCloud/authenticated-web-chat-server-examples | [optional] |
| **disabled** | bool |  | [optional] |
| **web_chat_config** | [WebChatConfig](WebChatConfig) |  | [optional] |
| **allowed_domains** | list[str] |  | [optional] |
| **flow** | [DomainEntityRef](DomainEntityRef) | The URI of the Inbound Chat Flow to run when new chats are initiated under this Deployment. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 231.0.0_
