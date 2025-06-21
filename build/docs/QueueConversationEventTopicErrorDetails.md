# QueueConversationEventTopicErrorDetails

## QueueConversationEventTopicErrorDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | int | The HTTP status code for this message (400, 401, 403, 404, 500, etc. | [optional] |
| **code** | str | A code unique to this error. | [optional] |
| **message** | str | Friendly description of this error. | [optional] |
| **message_with_params** | str | This is the same as message except it uses template fields for variable replacement. For instance: &#39;User {username} was not found&#39; | [optional] |
| **message_params** | dict(str, str) | Used in conjunction with messageWithParams. These are the template parameters. For instance: UserParam.key &#x3D; &#39;username&#39;, UserParam.value &#x3D; &#39;john.doe&#39; | [optional] |
| **context_id** | str | The correlation Id or context Id for this message. If left blank the Public API will look at the HTTP response header &#39;ININ-Correlation-Id&#39; instead. | [optional] |
| **uri** | str |  | [optional] |



_PureCloudPlatformClientV2 231.0.0_
