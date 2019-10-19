---
title: ScimServiceProviderConfig
---
## ScimServiceProviderConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **documentation_uri** | **str** | The HTTP-addressable URL that points to the service provider&#39;s documentation. | [optional] |
| **patch** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | \&quot;patch\&quot; configuration options. | [optional] |
| **filter** | [**ScimServiceProviderConfigFilterFeature**](ScimServiceProviderConfigFilterFeature.html) | \&quot;filter\&quot; configuration options. | [optional] |
| **etag** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | \&quot;ETag\&quot; configuration options. | [optional] |
| **sort** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | \&quot;sort\&quot; configuration options. | [optional] |
| **bulk** | [**ScimServiceProviderConfigBulkFeature**](ScimServiceProviderConfigBulkFeature.html) | \&quot;bulk\&quot; configuration options. | [optional] |
| **change_password** | [**ScimServiceProviderConfigSimpleFeature**](ScimServiceProviderConfigSimpleFeature.html) | \&quot;changePassword\&quot; configuration options. | [optional] |
| **authentication_schemes** | [**list[ScimServiceProviderConfigAuthenticationScheme]**](ScimServiceProviderConfigAuthenticationScheme.html) | The list of supported authentication schemes. | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | Resource SCIM meta | [optional] |
{: class="table table-striped"}


