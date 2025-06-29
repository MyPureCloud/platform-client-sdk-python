# AlertRequest

## AlertRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The action being taken on the alert. | |
| **date_start** | datetime | The start date of the mute/snooze period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_end** | datetime | The end date of the mute/snooze period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **unread** | [UnreadFields](UnreadFields) | The fields need for an unread update requests | [optional] |
| **valid_request** | bool |  | [optional] |



_PureCloudPlatformClientV2 232.0.0_
