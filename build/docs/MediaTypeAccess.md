# MediaTypeAccess

## MediaTypeAccess

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **inbound** | [list[MediaType]](MediaType) | List of media types allowed for inbound messages from customers. If inbound messages from a customer contain media that is not in this list, the media will be dropped from the outbound message. | [optional] |
| **outbound** | [list[MediaType]](MediaType) | List of media types allowed for outbound messages to customers. If an outbound message is sent that contains media that is not in this list, the message will not be sent. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
