# StaffingGroupAllocationsResponseTemplate

## StaffingGroupAllocationsResponseTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **staffing_group_allocations** | [list[StaffingGroupAllocation]](StaffingGroupAllocation) | List of staffing group allocations | |
| **months** | [list[YearMonth]](YearMonth) | The list of months covered by this capacity plan, formatted as yyyy-MM | [optional] |
| **planning_group_allocations** | [list[CapacityPlanningPlanningGroupAllocation]](CapacityPlanningPlanningGroupAllocation) | The planning group allocations | [optional] |
| **capacity_plan_metrics_summary** | [CapacityPlanMetricsSummary](CapacityPlanMetricsSummary) | The total summary of staffing allocation metrics for this capacity plan, for the selected granularity | [optional] |



_PureCloudPlatformClientV2 257.1.0_
