# WebDeployment

## WebDeployment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The deployment ID | [optional] |
| **name** | str | The deployment name | |
| **description** | str | The description of the config | [optional] |
| **allow_all_domains** | bool | Property indicates whether all domains are allowed or not. allowedDomains must be empty when this is set as true. | [optional] |
| **allowed_domains** | list[str] | The list of domains that are approved to use this deployment; the list will be added to CORS headers for ease of web use. | [optional] |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | The supported content profile for a deployment | [optional] |
| **snippet** | str | Javascript snippet used to load the config | [optional] |
| **date_created** | datetime | The date the deployment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date the deployment was most recently modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **last_modified_user** | [AddressableEntityRef](AddressableEntityRef) | A reference to the user who most recently modified the deployment | [optional] |
| **flow** | [WebDeploymentFlowEntityRef](WebDeploymentFlowEntityRef) | A reference to the inboundshortmessage flow used by this deployment | [optional] |
| **status** | str | The current status of the deployment | [optional] |
| **push_integrations** | [list[PushIntegration]](PushIntegration) | The push integration objects associated with the deployment | [optional] |
| **configuration** | [WebDeploymentConfigurationVersionEntityRef](WebDeploymentConfigurationVersionEntityRef) | The config version this deployment uses | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_
