# AuthorizationSettings

## AuthorizationSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **analysis_enabled** | bool | Boolean showing if organization is opted in or not to unused role/perm analysis | [optional] |
| **analysis_days** | int | Integer number of days to analyze user usage | [optional] |
| **date_last_calculated** | datetime | The date and time of the most recent unused role calculation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_last_active** | date | The date of the most recent org activity used for analysis. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 218.0.0_
