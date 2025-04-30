# QueueConversationEventTopicWrapup

## QueueConversationEventTopicWrapup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **code** | str | The user configured wrap up code name. | [optional] |
| **notes** | str | Text entered by the agent to describe the call or disposition. | [optional] |
| **tags** | list[str] | List of tags selected by the agent to describe the call or disposition. | [optional] |
| **duration_seconds** | int | The length of time in seconds that the agent spent doing after call work., Note, the format of utc-millisec should be ignored, our code generator needs it to generate a Long for us internally | [optional] |
| **end_time** | datetime | The timestamp when the wrapup was finished. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
