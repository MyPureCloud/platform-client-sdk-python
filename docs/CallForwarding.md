# CallForwarding

## CallForwarding

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **user** | [User](User) |  | [optional] |
| **enabled** | bool | Whether or not CallForwarding is enabled | [optional] |
| **phone_number** | str | This property is deprecated. Please use the calls property | [optional] |
| **calls** | [list[CallRoute]](CallRoute) | An ordered list of CallRoutes to be executed when CallForwarding is enabled | [optional] |
| **voicemail** | str | The type of voicemail to use with the callForwarding configuration | [optional] |
| **modified_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 217.0.0_
