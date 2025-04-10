# UserStation

## UserStation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this station | [optional] |
| **name** | str |  | [optional] |
| **type** | str |  | [optional] |
| **associated_user** | [User](User) |  | [optional] |
| **associated_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **default_user** | [User](User) |  | [optional] |
| **provider_info** | dict(str, str) | Provider-specific info for this station, e.g. { \&quot;edgeGroupId\&quot;: \&quot;ffe7b15c-a9cc-4f4c-88f5-781327819a49\&quot; } | [optional] |
| **web_rtc_call_appearances** | int | The number of call appearances on the station. | [optional] |



_PureCloudPlatformClientV2 225.0.0_
