# WidgetDeployment

## WidgetDeployment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | A human-readable description of this Deployment. | [optional] |
| **authentication_required** | bool | When true, the customer members starting a chat must be authenticated by supplying their JWT to the create operation. | [optional] |
| **disabled** | bool | When true, all create chat operations using this Deployment will be rejected. | [optional] |
| **flow** | [DomainEntityRef](DomainEntityRef) | The URI of the Inbound Chat Flow to run when new chats are initiated under this Deployment. | [optional] |
| **allowed_domains** | list[str] | The list of domains that are approved to use this Deployment; the list will be added to CORS headers for ease of web use. | [optional] |
| **client_type** | str | The type of display widget for which this Deployment is configured, which controls the administrator settings shown. | [optional] |
| **client_config** | [WidgetClientConfig](WidgetClientConfig) | The client configuration options that should be made available to the clients of this Deployment. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 230.0.0_
