# WorkitemCommonCreate

## WorkitemCommonCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the Workitem. Valid length between 3 and 256 characters. | |
| **priority** | int | The priority of the Workitem. The valid range is between -25,000,000 and 25,000,000. | [optional] |
| **date_due** | datetime | The due date of the Workitem. Can not be greater than 365 days from the current time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_expires** | datetime | The expiry date of the Workitem. Can not be greater than 365 days from the current time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **duration_seconds** | int | The estimated duration in seconds to complete the Workitem. Maximum of 365 days. | [optional] |
| **ttl** | int | The epoch timestamp in seconds specifying the time to live for the Workitem. Can not be greater than 365 days from the current time. | [optional] |
| **status_id** | str | The ID of the Status of the Workitem. | [optional] |
| **workbin_id** | str | The ID of Workbin that contains the Workitem. | [optional] |
| **auto_status_transition** | bool | Set it to false to disable auto status transition. By default, it is enabled. | [optional] |
| **description** | str | The description of the Workitem. Maximum length of 512 characters. | [optional] |
| **type_id** | str | The ID of the Worktype of the Workitem. | |
| **custom_fields** | dict(str, object) | Custom fields defined in the schema referenced by the worktype of the workitem. | [optional] |
| **queue_id** | str | The ID of the Workitems queue. Must be a valid UUID. | [optional] |
| **assignee_id** | str | The ID of the assignee of the Workitem. Must be a valid UUID. | [optional] |
| **language_id** | str | The ID of language of the Workitem. Must be a valid UUID. | [optional] |
| **external_contact_id** | str | The ID of the external contact of the Workitem. Must be a valid UUID. | [optional] |
| **external_tag** | str | The external tag of the Workitem. | [optional] |
| **skill_ids** | list[str] | The skill IDs of the Workitem. Must be valid UUIDs. | [optional] |
| **script_id** | str | The ID of the Workitems script. Must be a valid UUID. | [optional] |



_PureCloudPlatformClientV2 226.0.0_
