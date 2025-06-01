# WorkitemVersion

## WorkitemVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Workitem. | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **type** | [WorktypeReference](WorktypeReference) | The Worktype of the Workitem. | [optional] |
| **description** | str | The description of the Workitem. | [optional] |
| **language** | [LanguageReference](LanguageReference) | The language of the Workitem. | [optional] |
| **utilization_label** | [WorkitemUtilizationLabelReference](WorkitemUtilizationLabelReference) | The utilization label of the Workitem. | [optional] |
| **priority** | int | The priority of the Workitem. The valid range is between -25,000,000 and 25,000,000. | [optional] |
| **date_created** | datetime | The creation date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The modified date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_due** | datetime | The due date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_expires** | datetime | The expiry date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **duration_seconds** | int | The estimated duration in seconds to complete the workitem. | [optional] |
| **ttl** | int | The time to live of the Workitem in seconds. | [optional] |
| **status** | [WorkitemStatusReference](WorkitemStatusReference) | The current Status of the Workitem. | [optional] |
| **status_category** | str | The Category of the current Status of the Workitem. | [optional] |
| **date_status_changed** | datetime | The State change date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_closed** | datetime | The date the Workitem was closed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **workbin** | [WorkbinReference](WorkbinReference) | The Workbin that contains the Workitem. | [optional] |
| **reporter** | [UserReferenceWithName](UserReferenceWithName) | The reporter of the Workitem. | [optional] |
| **assignee** | [UserReferenceWithName](UserReferenceWithName) | The assignee of the Workitem. | [optional] |
| **external_contact** | [ExternalContactReference](ExternalContactReference) | The external contact of the Workitem. | [optional] |
| **external_tag** | str | The external tag of the Workitem. | [optional] |
| **modified_by** | [UserReference](UserReference) | The User who modified the Workitem. | [optional] |
| **queue** | [WorkitemQueueReference](WorkitemQueueReference) | The Workitems queue. | [optional] |
| **assignment_state** | str | The assignment state of the workitem. | [optional] |
| **date_assignment_state_changed** | datetime | The assignment state change date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **alert_timeout_seconds** | int | The duration in seconds before an alert will timeout. | [optional] |
| **skills** | [list[RoutingSkillReference]](RoutingSkillReference) | The skills of the Workitem. | [optional] |
| **preferred_agents** | [list[UserReference]](UserReference) | The preferred agents of the Workitem. | [optional] |
| **auto_status_transition** | bool | Set it to false to disable auto status transition. By default, it is enabled. | [optional] |
| **schema** | [WorkitemSchema](WorkitemSchema) | The schema defining the custom fields of the Workitem. The schema is inherited from the Workitems Worktype at creation time. | [optional] |
| **custom_fields** | dict(str, object) | Custom fields defined in the schema referenced by the Workitem. | [optional] |
| **auto_status_transition_detail** | [AutoStatusTransitionDetail](AutoStatusTransitionDetail) | Auto status transition details of Workitem. | [optional] |
| **scored_agents** | [list[WorkitemScoredAgent]](WorkitemScoredAgent) | A list of scored agents for the Workitem. | [optional] |
| **script** | [WorkitemScriptReference](WorkitemScriptReference) | The script that will be executed for the Workitem. | [optional] |
| **version** | int | Version | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 230.0.0_
