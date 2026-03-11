# TaskManagementObservationQuery

## TaskManagementObservationQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **group_by** | list[str] | Dimension(s) to group by. Determines how the results will be grouped in the response. | |
| **metrics** | [list[TaskManagementQueryMetric]](TaskManagementQueryMetric) | List of metrics to be retrieved. Specifies which observational metrics should be included in the response. | |
| **filter** | [TaskManagementObservationQueryFilter](TaskManagementObservationQueryFilter) | Filter to return a subset of observations. | |
| **expands** | list[str] | List of properties to expand. Additional details about the objects returned in the results will be included in the response if supplied. | [optional] |



_PureCloudPlatformClientV2 253.0.0_
