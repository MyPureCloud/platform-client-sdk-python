# AutoStatusTransitionDetail

## AutoStatusTransitionDetail

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **next_status** | [WorkitemStatusReference](WorkitemStatusReference) | Next status of auto status transition. | [optional] |
| **date_of_transition** | datetime | Date at which auto status transition occurs. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **error_details** | [TaskManagementErrorDetails](TaskManagementErrorDetails) | This property will be set if auto status transition is failed. | [optional] |



_PureCloudPlatformClientV2 221.0.0_
