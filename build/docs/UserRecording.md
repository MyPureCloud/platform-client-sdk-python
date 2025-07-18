# UserRecording

## UserRecording

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **content_uri** | str |  | [optional] |
| **workspace** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **conversation** | [Conversation](Conversation) |  | [optional] |
| **content_length** | int |  | [optional] |
| **duration_milliseconds** | int |  | [optional] |
| **thumbnails** | [list[DocumentThumbnail]](DocumentThumbnail) |  | [optional] |
| **read** | bool |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
