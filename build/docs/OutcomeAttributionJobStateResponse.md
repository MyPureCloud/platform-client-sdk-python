# OutcomeAttributionJobStateResponse

## OutcomeAttributionJobStateResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **state** | str | State of job. | [optional] |
| **results_uri** | str | URI where the query results can be retrieved.  Populated when job has reached a terminal state, i.e. no longer Running. | [optional] |
| **percent_failed_threshold** | int | Optional percent failed threshold for validation errors; if reached will halt the job. Default is 5 percent, allowed values 0 to 100. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **created_date** | datetime | Date when the job was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 231.0.0_
