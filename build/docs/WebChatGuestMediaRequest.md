# WebChatGuestMediaRequest

## WebChatGuestMediaRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **types** | list[str] | The types of media being requested. | |
| **state** | str | The state of the media request, one of PENDING|ACCEPTED|DECLINED|TIMEDOUT|CANCELLED|ERRORED. | |
| **communication_id** | str | The ID of the new media communication, if applicable. | [optional] |
| **security_key** | str | The security information related to a media request. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_
