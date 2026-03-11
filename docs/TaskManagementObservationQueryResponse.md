# TaskManagementObservationQueryResponse

## TaskManagementObservationQueryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **results** | [list[TaskManagementObservationResult]](TaskManagementObservationResult) | Query results grouped by the specified dimensions supplied in the groupBy parameter. Each result contains metrics for a specific group combination. | [optional] |
| **details** | [TaskManagementObservationDetailContainer](TaskManagementObservationDetailContainer) | Details about entities contained in results. Provides expanded information when requested through the expands parameter. | [optional] |
| **cursors** | [Cursors](Cursors) | Cursor tokens to be used for navigating paginated results | [optional] |
| **next_uri** | str | A URI to the next page in the listing. | [optional] |



_PureCloudPlatformClientV2 253.0.0_
