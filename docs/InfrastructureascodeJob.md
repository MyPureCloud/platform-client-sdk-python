# InfrastructureascodeJob

## InfrastructureascodeJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **dry_run** | bool | Whether or not the job was a dry run | |
| **accelerator_id** | str | Accelerator associated with the job | [optional] |
| **date_submitted** | datetime | Date and time on which job was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **submitted_by** | [UserReference](UserReference) | User who submitted the job | [optional] |
| **status** | str | Job status | [optional] |
| **error_info** | [ErrorInfo](ErrorInfo) | Information about errors, if any | [optional] |
| **results** | str | The output results of the terraform job | [optional] |
| **rollback_results** | str | The results of rolling back the job if there were errors.  Not returned if job was successful. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
