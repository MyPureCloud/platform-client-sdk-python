# ScheduleBidGroup

## ScheduleBidGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the schedule bid group | |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this bid group belongs | |
| **agents** | [list[UserReference]](UserReference) | The agents who participate in this bid group | |
| **work_plans** | [list[WorkPlanReference]](WorkPlanReference) | The work plans used in this bid group | [optional] |
| **work_plan_rotations** | [list[BidGroupWorkPlanRotationResponse]](BidGroupWorkPlanRotationResponse) | The work plan rotations used in this bid group | [optional] |
| **planning_groups** | [list[PlanningGroupReference]](PlanningGroupReference) | The planning groups selected in this bid group | |
| **download_url** | str | The downloadUrl to fetch Schedule sets. It will be populated if the status of this bid is &#39;Optimized&#39; | [optional] |
| **download_template** | [BidGroupScheduleSet](BidGroupScheduleSet) | Schedule sets always come through downloadUrl, the schema included here is just for documentation | [optional] |



_PureCloudPlatformClientV2 265.0.0_
