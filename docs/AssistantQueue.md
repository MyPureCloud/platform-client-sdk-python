# AssistantQueue

## AssistantQueue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the queue. | |
| **media_types** | list[str] | List of media Types in which the assistant is activated for this queue. | |
| **assistant** | [Assistant](Assistant) | Assistant to which the queue is assigned. | [optional] |
| **date_created** | datetime | Date when the assistant queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the assistant queue was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 213.0.0_
