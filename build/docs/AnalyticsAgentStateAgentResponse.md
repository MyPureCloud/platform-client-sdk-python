# AnalyticsAgentStateAgentResponse

## AnalyticsAgentStateAgentResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | User Id - only returned if division is covered by agentStateNames permission | [optional] |
| **division_id** | str | Division Id | [optional] |
| **user_name** | str | User name - only returned if division is covered by agentStateNames permission | [optional] |
| **manager_id** | str | The user that this user reports to | [optional] |
| **session_count** | int | The count of sessions | [optional] |
| **sessions** | [list[AnalyticsAgentStateAgentSessionResult]](AnalyticsAgentStateAgentSessionResult) | List of sessions | [optional] |
| **system_presence** | str | The user&#39;s system presence | [optional] |
| **organization_presence_id** | str | The identifier for the user&#39;s organization presence | [optional] |
| **presence_date** | datetime | The timestamp for when the user&#39;s presence began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **routing_status** | str | The user&#39;s routing status | [optional] |
| **routing_status_date** | datetime | The timestamp for when the user&#39;s routing status began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **is_out_of_office** | bool | Whether the user is out of office | [optional] |
| **management_unit_id** | str | The id of the user&#39;s management unit | [optional] |
| **business_unit_id** | str | The id of the user&#39;s business unit | [optional] |
| **adherence_state** | str | The user&#39;s adherence state | [optional] |
| **adherence_impact** | str | The user&#39;s adherence impact | [optional] |
| **adherence_date** | datetime | The timestamp for when the user&#39;s adherence state began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **scheduled_activity_code_id** | str | The id of the user&#39;s scheduled activity code | [optional] |
| **scheduled_activity_category** | str | The user&#39;s scheduled activity category | [optional] |
| **actual_activity_category** | str | The user&#39;s actual activity category | [optional] |



_PureCloudPlatformClientV2 266.0.0_
