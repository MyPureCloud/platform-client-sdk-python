# WorkitemQueryJobResponse

## WorkitemQueryJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **state** | str | The state of the query job | [optional] |
| **date_started** | datetime | The date the job was started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_finished** | datetime | The date the job finished. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **error** | [WorkitemQueryJobError](WorkitemQueryJobError) | The error associated with the query job, if the state is Failed | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
