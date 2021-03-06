---
title: FacebookIntegrationRequest
---
## FacebookIntegrationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the Facebook Integration | |
| **page_access_token** | **str** | The long-lived Page Access Token of a facebook page.  See https://developers.facebook.com/docs/facebook-login/access-tokens.  When a pageAccessToken is provided, pageId and userAccessToken are not required. | [optional] |
| **user_access_token** | **str** | The short-lived User Access Token of the facebook user logged into the facebook app.  See https://developers.facebook.com/docs/facebook-login/access-tokens.  When userAccessToken is provided, pageId is mandatory.  When userAccessToken/pageId combination is provided, pageAccessToken is not required. | [optional] |
| **page_id** | **str** | The page Id of a facebook page. The pageId is required when userAccessToken is provided. | [optional] |
| **app_id** | **str** | The app Id of a facebook app. The appId is required when a customer wants to use their own approved facebook app. | [optional] |
| **app_secret** | **str** | The app Secret of a facebook app. The appSecret is required when appId is provided. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


