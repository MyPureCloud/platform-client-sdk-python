# TranscriptTopic

## TranscriptTopic

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the object. | [optional] |
| **topic_phrase** | str | The phrase which detected the topic.  | [optional] |
| **transcript_phrase** | str | The transcript phrase which detected the topic. | [optional] |
| **confidence** | int | The detection confidence of the topic. | [optional] |
| **start_time_milliseconds** | int | The start time of the topic phrase. | [optional] |
| **duration** | [TopicDuration](TopicDuration) |  | [optional] |
| **offset** | [TopicOffset](TopicOffset) | Location of the phrase | [optional] |
| **recording_location** | int | Location of the phrase in the recording in milliseconds | [optional] |



_PureCloudPlatformClientV2 230.0.0_
