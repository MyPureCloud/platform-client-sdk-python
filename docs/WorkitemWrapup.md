# WorkitemWrapup

## WorkitemWrapup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **workitem** | [WorkitemReference](WorkitemReference) | Workitem that the wrapup code has been added to. | [optional] |
| **wrapup_code** | [WrapupIdReference](WrapupIdReference) | The wrapup code used in the workitem. | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who added the wrapup code to the workitem. | [optional] |
| **user** | [UserReference](UserReference) | The user for whom wrapup code was added. This may be the same as modifiedBy. | [optional] |
| **date_modified** | datetime | The modified date of the Workitem when the wrapup code was added. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 220.0.0_
