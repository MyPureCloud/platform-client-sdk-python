# WorktypeVersion

## WorktypeVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Worktype. | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **description** | str | The description of the Worktype. | [optional] |
| **date_created** | datetime | The creation date of the Worktype. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The modified date of the Worktype. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **default_workbin** | [WorkbinReference](WorkbinReference) | The default Workbin for Workitems created from the Worktype. | [optional] |
| **default_status** | [WorkitemStatusReference](WorkitemStatusReference) | The default status for Workitems created from the Worktype. | [optional] |
| **statuses** | [list[WorkitemStatus]](WorkitemStatus) | The list of possible statuses for Workitems created from the Worktype. | [optional] |
| **default_duration_seconds** | int | The default duration in seconds for Workitems created from the Worktype. | [optional] |
| **default_expiration_seconds** | int | The default expiration time in seconds for Workitems created from the Worktype. | [optional] |
| **default_due_duration_seconds** | int | The default due duration in seconds for Workitems created from the Worktype. | [optional] |
| **default_priority** | int | The default priority for Workitems created from the Worktype. The valid range is between -25,000,000 and 25,000,000. | [optional] |
| **default_language** | [LanguageReference](LanguageReference) | The default language for Workitems created from the Worktype. | [optional] |
| **default_ttl_seconds** | int | The default time to time to live in seconds for Workitems created from the Worktype. | [optional] |
| **modified_by** | [UserReference](UserReference) | The id of the User who modified the Worktype. | [optional] |
| **default_queue** | [WorkitemQueueReference](WorkitemQueueReference) | The default queue for Workitems created from the Worktype. | [optional] |
| **default_skills** | [list[RoutingSkillReference]](RoutingSkillReference) | The default skills for Workitems created from the Worktype. | [optional] |
| **assignment_enabled** | bool | When set to true, Workitems will be sent to the queue of the Worktype as they are created. Default value is false. | [optional] |
| **schema** | [WorkitemSchema](WorkitemSchema) | The schema defining the custom attributes for Workitems created from the Worktype. | [optional] |
| **service_level_target** | int | The target service level for Workitems created from the Worktype. The default value is 100. | [optional] |
| **version** | int | Version | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 213.0.0_
