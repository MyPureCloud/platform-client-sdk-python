# InstagramIntegrationRequest

## InstagramIntegrationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Instagram Integration | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingRequestReference](MessagingSettingRequestReference) | Defines the message settings to be applied for this integration | [optional] |
| **page_access_token** | str | The long-lived Page Access Token of Instagram page.  See https://developers.facebook.com/docs/facebook-login/access-tokens.  When a pageAccessToken is provided, pageId and userAccessToken are not required. | [optional] |
| **user_access_token** | str | The short-lived User Access Token of Instagram user logged into Facebook app.  See https://developers.facebook.com/docs/facebook-login/access-tokens.  When userAccessToken is provided, pageId is mandatory.  When userAccessToken/pageId combination is provided, pageAccessToken is not required. | [optional] |
| **page_id** | str | The page ID of Instagram page. The pageId is required when userAccessToken is provided. | [optional] |
| **app_id** | str | The app ID of Facebook app. The appId is required when a customer wants to use their own approved Facebook app. | [optional] |
| **app_secret** | str | The app Secret of Facebook app. The appSecret is required when appId is provided. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 217.0.0_
