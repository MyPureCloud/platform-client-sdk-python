# NluFeedbackResponse

## NluFeedbackResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **text** | str | The feedback text. | [optional] |
| **intents** | [list[IntentFeedback]](IntentFeedback) | Detected intent of the utterance | [optional] |
| **version** | [NluDomainVersion](NluDomainVersion) | The domain version of the feedback. | [optional] |
| **date_created** | datetime | The date when the feedback was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **language** | str | The language of the version to which feedback is linked, e.g. en-us, de-de | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
