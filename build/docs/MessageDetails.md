---
title: MessageDetails
---
## MessageDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message_id** | **str** | UUID identifying the message media. | [optional] |
| **message_uri** | **str** | A URI for this message entity. | [optional] |
| **message_status** | **str** | Indicates the delivery status of the message. | [optional] |
| **message_segment_count** | **int** | The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits. | [optional] |
| **message_time** | **datetime** | The time when the message was sent or received. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
{: class="table table-striped"}


