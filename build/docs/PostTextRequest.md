---
title: PostTextRequest
---
## PostTextRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **bot_id** | **str** | ID of the bot to send the text to. | |
| **bot_alias** | **str** | Alias/Version of the bot | [optional] |
| **integration_id** | **str** | the integration service id for the bot&#39;s credentials | |
| **bot_session_id** | **str** | GUID for this bot&#39;s session | |
| **post_text_message** | [**PostTextMessage**](PostTextMessage.html) | Message to send to the bot | |
| **language_code** | **str** | The launguage code the bot will run under | [optional] |
| **bot_session_timeout_minutes** | **int** | Override timeout for the bot session. This should be greater than 10 minutes. | [optional] |
| **bot_channels** | **list[str]** | The channels this bot is utilizing | [optional] |
| **bot_correlation_id** | **str** | Id for tracking the activity - this will be returned in the response | [optional] |
| **messaging_platform_type** | **str** | If the channels list contains a &#39;Messaging&#39; item and the messaging platform is known, include it here to get accurate analytics | [optional] |
| **amazon_lex_request** | [**AmazonLexRequest**](AmazonLexRequest.html) |  | [optional] |
| **google_dialogflow** | [**GoogleDialogflowCustomSettings**](GoogleDialogflowCustomSettings.html) |  | [optional] |
{: class="table table-striped"}


