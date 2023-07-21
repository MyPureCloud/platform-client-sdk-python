---
title: ActionMap
---
## ActionMap

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **version** | **int** | The version of the action map. | [optional] |
| **is_active** | **bool** | Whether the action map is active. | [optional] |
| **display_name** | **str** | Display name of the action map. | |
| **trigger_with_segments** | **list[str]** | Trigger action map if any segment in the list is assigned to a given customer. | |
| **trigger_with_event_conditions** | [**list[EventCondition]**](EventCondition.html) | List of event conditions that must be satisfied to trigger the action map. | [optional] |
| **trigger_with_outcome_probability_conditions** | [**list[OutcomeProbabilityCondition]**](OutcomeProbabilityCondition.html) | Probability conditions for outcomes that must be satisfied to trigger the action map. | [optional] |
| **trigger_with_outcome_percentile_conditions** | [**list[OutcomePercentileCondition]**](OutcomePercentileCondition.html) | (deprecated - use triggerWithOutcomeQuantileConditions instead) Percentile conditions for outcomes that must be satisfied to trigger the action map. | [optional] |
| **trigger_with_outcome_quantile_conditions** | [**list[OutcomeQuantileCondition]**](OutcomeQuantileCondition.html) | Quantile conditions for outcomes that must be satisfied to trigger the action map. | [optional] |
| **page_url_conditions** | [**list[UrlCondition]**](UrlCondition.html) | URL conditions that a page must match for web actions to be displayable. | |
| **activation** | [**Activation**](Activation.html) | Type of activation. | [optional] |
| **weight** | **int** | Weight of the action map with higher number denoting higher weight. | [optional] |
| **action** | [**ActionMapAction**](ActionMapAction.html) | The action that will be executed if this action map is triggered. | [optional] |
| **action_map_schedule_groups** | [**ActionMapScheduleGroups**](ActionMapScheduleGroups.html) | The action map&#39;s associated schedule groups. | [optional] |
| **ignore_frequency_cap** | **bool** | Override organization-level frequency cap and always offer web engagements from this action map. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | Timestamp indicating when the action map was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_date** | **datetime** | Timestamp indicating when the action map was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **start_date** | **datetime** | Timestamp at which the action map is scheduled to start firing. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | **datetime** | Timestamp at which the action map is scheduled to stop firing. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


