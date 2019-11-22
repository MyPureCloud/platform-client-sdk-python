---
title: ScimServiceProviderConfig
---
## ScimServiceProviderConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **documentation_uri** | **str** | The HTTP-addressable URL that points to the service provider&#39;s documentation. | [optional] |
| **patch** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | The \&quot;patch\&quot; configuration options. | [optional] |
| **filter** | [**ScimServiceProviderConfigFilterFeature**](ScimServiceProviderConfigFilterFeature.html) | The \&quot;filter\&quot; configuration options. | [optional] |
| **etag** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | The \&quot;etag\&quot; configuration options. | [optional] |
| **sort** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | The \&quot;sort\&quot; configuration options. | [optional] |
| **bulk** | [**ScimServiceProviderConfigBulkFeature**](ScimServiceProviderConfigBulkFeature.html) | The \&quot;bulk\&quot; configuration options. | [optional] |
| **change_password** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | The \&quot;changePassword\&quot; configuration options. | [optional] |
| **authentication_schemes** | [**list[ScimServiceProviderConfigAuthenticationScheme]**](ScimServiceProviderConfigAuthenticationScheme.html) | The list of supported authentication schemes. | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | Resource SCIM meta | [optional] |
{: class="table table-striped"}


