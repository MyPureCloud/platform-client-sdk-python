# CallableTimeSet

## CallableTimeSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the CallableTimeSet. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **callable_times** | [list[CallableTime]](CallableTime) | The list of CallableTimes for which it is acceptable to place outbound calls. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_
