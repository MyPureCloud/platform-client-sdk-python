# ResponseFilter

## ResponseFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Field to filter on. Allowed values are &#39;name&#39;, &#39;libraryId&#39;, &#39;text.contentType&#39;, &#39;messagingTemplate&#39; and &#39;responseType&#39; | |
| **operator** | str | Filter operation: IN, EQUALS, NOTEQUALS. | |
| **values** | list[str] | Values to filter on. If name is &#39;responseType&#39; then allowed values are &#39;CampaignSmsTemplate&#39;, &#39;CampaignEmailTemplate&#39;, &#39;Footer&#39; and &#39;Signature&#39; | |



_PureCloudPlatformClientV2 221.0.0_
