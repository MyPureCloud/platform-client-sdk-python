# KnowledgeGuestSession

## KnowledgeGuestSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Session ID. | [optional] |
| **app** | [KnowledgeGuestSessionApp](KnowledgeGuestSessionApp) | The app where the session is started. | |
| **customer_id** | str | An arbitrary ID for the customer starting the session. Used to track multiple sessions started by the same customer. | |
| **page_url** | str | URL of the page where the session is started. | [optional] |
| **contexts** | [list[KnowledgeGuestSessionContext]](KnowledgeGuestSessionContext) | The session contexts. | [optional] |



_PureCloudPlatformClientV2 212.0.0_
