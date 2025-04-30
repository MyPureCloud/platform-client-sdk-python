# WorktypeCreate

## WorktypeCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the Worktype. Valid length between 3 and 256 characters. | |
| **default_workbin_id** | str | The ID of the default Workbin for Workitems created from the Worktype. | |
| **default_duration_seconds** | int | The default duration in seconds for Workitems created from the Worktype. Maximum of 365 days. | [optional] |
| **default_expiration_seconds** | int | The default expiration time in seconds for Workitems created from the Worktype. Maximum of 365 days. | [optional] |
| **default_due_duration_seconds** | int | The default due duration in seconds for Workitems created from the Worktype. Maximum of 365 days. | [optional] |
| **default_priority** | int | The default priority for Workitems created from the Worktype. The valid range is between -25,000,000 and 25,000,000. | [optional] |
| **default_ttl_seconds** | int | The default time to time to live in seconds for Workitems created from the Worktype. The valid range is between 1 and 365 days. | [optional] |
| **assignment_enabled** | bool | When set to true, Workitems will be sent to the queue of the Worktype as they are created. Default value is false. | [optional] |
| **schema_id** | str | The ID of the custom attribute schema for Workitems created from the Worktype. Must be a valid UUID. | [optional] |
| **service_level_target** | int | The target service level for Workitems created from the Worktype. The default value is 100. | [optional] |
| **rule_settings** | [WorkitemRuleSettings](WorkitemRuleSettings) | Settings for the worktypes rules. | [optional] |
| **description** | str | The description of the Worktype. Maximum length of 512 characters. | [optional] |
| **division_id** | str | The ID of the division the Worktype belongs to. Defaults to the default Workbin division ID. The Worktype must be in the same division as its default Workbin. | [optional] |
| **disable_default_status_creation** | bool | Set to true to disable default status creation. Default statuses are created with the Worktype by default | [optional] |
| **schema_version** | int | The version of the Worktypes custom attribute schema. The latest schema version will be used if this property is not set. | [optional] |
| **default_queue_id** | str | The ID of the default queue for Workitems created from the Worktype. Must be a valid UUID. | [optional] |
| **default_language_id** | str | The ID of the default language for Workitems created from the Worktype. Must be a valid UUID. | [optional] |
| **default_skill_ids** | list[str] | The IDs of the default skills for Workitems created from the Worktype. Must be valid UUIDs. Maximum of 20 IDs | [optional] |
| **default_script_id** | str | The default script for Workitems created from the Worktype. Must be a valid UUID. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
