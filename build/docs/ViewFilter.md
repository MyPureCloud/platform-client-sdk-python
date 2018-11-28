---
title: ViewFilter
---
## ViewFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_types** | **list[str]** | The media types are used to filter the view | [optional] |
| **queue_ids** | **list[str]** | The queue ids are used to filter the view | [optional] |
| **skill_ids** | **list[str]** | The skill ids are used to filter the view | [optional] |
| **skill_groups** | **list[str]** | The skill groups used to filter the view | [optional] |
| **language_ids** | **list[str]** | The language ids are used to filter the view | [optional] |
| **language_groups** | **list[str]** | The language groups used to filter the view | [optional] |
| **directions** | **list[str]** | The directions are used to filter the view | [optional] |
| **wrap_up_codes** | **list[str]** | The wrap up codes are used to filter the view | [optional] |
| **dnis_list** | **list[str]** | The dnis list is used to filter the view | [optional] |
| **filter_queues_by_user_ids** | **list[str]** | The user ids are used to fetch associated queues for the view | [optional] |
| **filter_users_by_queue_ids** | **list[str]** | The queue ids are used to fetch associated users for the view | [optional] |
| **user_ids** | **list[str]** | The user ids are used to filter the view | [optional] |
| **address_tos** | **list[str]** | The address To values are used to filter the view | [optional] |
| **address_froms** | **list[str]** | The address from values are used to filter the view | [optional] |
| **outbound_campaign_ids** | **list[str]** | The outbound campaign ids are used to filter the view | [optional] |
| **outbound_contact_list_ids** | **list[str]** | The outbound contact list ids are used to filter the view | [optional] |
| **contact_ids** | **list[str]** | The contact ids are used to filter the view | [optional] |
| **ani_list** | **list[str]** | The ani list ids are used to filter the view | [optional] |
| **durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The durations in milliseconds used to filter the view | [optional] |
| **evaluation_score** | [**NumericRange**](NumericRange.html) | The evaluationScore is used to filter the view | [optional] |
| **evaluation_critical_score** | [**NumericRange**](NumericRange.html) | The evaluationCriticalScore is used to filter the view | [optional] |
| **evaluation_form_ids** | **list[str]** | The evaluation form ids are used to filter the view | [optional] |
| **evaluated_agent_ids** | **list[str]** | The evaluated agent ids are used to filter the view | [optional] |
| **evaluator_ids** | **list[str]** | The evaluator ids are used to filter the view | [optional] |
| **transferred** | **bool** | Indicates filtering for transfers | [optional] |
| **abandoned** | **bool** | Indicates filtering for abandons | [optional] |
| **message_types** | **list[str]** | The message media types used to filter the view | [optional] |
| **division_ids** | **list[str]** | The divison Ids used to filter the view | [optional] |
| **survey_form_ids** | **list[str]** | The survey form ids used to filter the view | [optional] |
| **survey_total_score** | [**NumericRange**](NumericRange.html) | The survey total score used to filter the view | [optional] |
| **survey_nps_score** | [**NumericRange**](NumericRange.html) | The survey NPS score used to filter the view | [optional] |
| **show_secondary_status** | **bool** | Indicates if the Secondary Status should be shown | [optional] |
| **agent_duration_sort_order** | **str** | Provides the agent duration sort order | [optional] |
| **waiting_duration_sort_order** | **str** | Provides the waiting duration sort order | [optional] |
| **interacting_duration_sort_order** | **str** | Provides the interacting duration sort order | [optional] |
| **agent_name** | **str** | Displays the Agent name as provided by the user | [optional] |
| **skills_list** | **list[str]** | The list of skill strings as free form text | [optional] |
| **language_list** | **list[str]** | The list of language strings as free form text | [optional] |
| **mos** | [**NumericRange**](NumericRange.html) | The desired range for mos values | [optional] |
| **survey_question_group_score** | [**NumericRange**](NumericRange.html) | The survey question group score used to filter the view | [optional] |
| **survey_promoter_score** | [**NumericRange**](NumericRange.html) | The survey promoter score used to filter the view | [optional] |
{: class="table table-striped"}


