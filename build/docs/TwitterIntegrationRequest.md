---
title: TwitterIntegrationRequest
---
## TwitterIntegrationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the Twitter Integration | |
| **supported_content** | [**SupportedContentReference**](SupportedContentReference.html) | Defines the SupportedContent profile configured for an integration | [optional] |
| **access_token_key** | **str** | The Access Token Key from Twitter messenger | |
| **access_token_secret** | **str** | The Access Token Secret from Twitter messenger | |
| **consumer_key** | **str** | The Consumer Key from Twitter messenger | |
| **consumer_secret** | **str** | The Consumer Secret from Twitter messenger | |
| **tier** | **str** | The type of twitter account to be used for the integration | |
| **env_name** | **str** | The Twitter environment name, e.g.: env-beta (required for premium tier) | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


