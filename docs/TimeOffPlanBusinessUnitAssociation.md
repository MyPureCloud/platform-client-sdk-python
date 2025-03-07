# TimeOffPlanBusinessUnitAssociation

## TimeOffPlanBusinessUnitAssociation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_units** | [list[ManagementUnitReference]](ManagementUnitReference) | Management units to which this time-off plan applies. This must not be set if staffingGroups is populated | [optional] |
| **staffing_groups** | [list[StaffingGroupReference]](StaffingGroupReference) | Staffing groups to which this time-off plan applies. This must not be set if managementUnits is populated | [optional] |



_PureCloudPlatformClientV2 223.0.0_
