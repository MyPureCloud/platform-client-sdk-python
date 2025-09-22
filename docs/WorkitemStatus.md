# WorkitemStatus

## WorkitemStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **category** | str | The Category of the Status. | [optional] |
| **destination_statuses** | [list[WorkitemStatusReference]](WorkitemStatusReference) | The Statuses the Status can transition to. | [optional] |
| **description** | str | The description of the Status. | [optional] |
| **default_destination_status** | [WorkitemStatusReference](WorkitemStatusReference) | Default destination status to which this Status will transition to if auto status transition enabled. | [optional] |
| **status_transition_delay_seconds** | int | Delay in seconds for auto status transition | [optional] |
| **status_transition_time** | str | Time is represented as an ISO-8601 string without a timezone. For example: HH:mm:ss.SSS | [optional] |
| **worktype** | [WorktypeReference](WorktypeReference) | The Worktype containing the Status. | [optional] |
| **auto_terminate_workitem** | bool | Terminate workitem on selection of status. Applicable only for statuses in the Closed category. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 237.0.0_
