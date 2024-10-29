# UserScheduleAdherence

## UserScheduleAdherence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **user** | [UserReference](UserReference) | The user for whom this status applies | [optional] |
| **business_unit** | [BusinessUnitReference](BusinessUnitReference) | The business unit to which this user belongs | [optional] |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this user belongs | [optional] |
| **team** | [TeamReference](TeamReference) | The team to which this user belongs | [optional] |
| **scheduled_activity_category** | str | Activity for which the user is scheduled | [optional] |
| **scheduled_activity_code** | [ActivityCodeSummary](ActivityCodeSummary) | Activity code for which the user is currently scheduled | [optional] |
| **system_presence** | str | Actual underlying system presence value | [optional] |
| **organization_secondary_presence_id** | str | Organization Secondary Presence Id. | [optional] |
| **routing_status** | str | Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue | [optional] |
| **actual_activity_category** | str | Activity in which the user is actually engaged | [optional] |
| **is_out_of_office** | bool | Whether the user is marked OutOfOffice | [optional] |
| **adherence_state** | str | The user&#39;s current adherence state | [optional] |
| **impact** | str | The impact of the user&#39;s current adherenceState | [optional] |
| **adherence_explanation** | [RealTimeAdherenceExplanation](RealTimeAdherenceExplanation) | Currently applicable explanation for the adherence state | [optional] |
| **time_of_adherence_change** | datetime | Time when the user entered the current adherenceState in ISO-8601 format | [optional] |
| **presence_update_time** | datetime | Time when presence was last updated. Used to calculate time in current status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **active_queues** | [list[QueueReference]](QueueReference) | The list of queues to which this user is joined | [optional] |
| **active_queues_modified_time** | datetime | Time when the list of active queues for this user was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **removed_from_management_unit** | bool | For notification purposes. Used to indicate that a user was removed from the management unit | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 215.0.0_
