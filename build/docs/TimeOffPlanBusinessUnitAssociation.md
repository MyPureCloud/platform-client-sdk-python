---
title: TimeOffPlanBusinessUnitAssociation
---
## TimeOffPlanBusinessUnitAssociation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_units** | [**list[ManagementUnitReference]**](ManagementUnitReference.html) | Management units to which this time-off plan applies. This must not be set if staffingGroups is populated | [optional] |
| **staffing_groups** | [**list[StaffingGroupReference]**](StaffingGroupReference.html) | Staffing groups to which this time-off plan applies. This must not be set if managementUnits is populated | [optional] |
{: class="table table-striped"}


