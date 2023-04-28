---
title: Evaluation
---
## Evaluation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **conversation** | [**ConversationReference**](ConversationReference.html) |  | [optional] |
| **evaluation_form** | [**EvaluationForm**](EvaluationForm.html) | Evaluation form used for evaluation. | [optional] |
| **evaluator** | [**User**](User.html) |  | [optional] |
| **agent** | [**User**](User.html) |  | [optional] |
| **calibration** | [**Calibration**](Calibration.html) |  | [optional] |
| **status** | **str** |  | [optional] |
| **answers** | [**EvaluationScoringSet**](EvaluationScoringSet.html) |  | [optional] |
| **agent_has_read** | **bool** |  | [optional] |
| **assignee** | [**User**](User.html) |  | [optional] |
| **release_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **assigned_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **changed_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **queue** | [**Queue**](Queue.html) |  | [optional] |
| **media_type** | **list[str]** | List of different communication types used in conversation. | [optional] |
| **rescore** | **bool** | Is only true when evaluation is re-scored. | [optional] |
| **conversation_date** | **datetime** | Date of conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation_end_date** | **datetime** | End date of conversation if it had completed before evaluation creation. Null if created before the conversation ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **never_release** | **bool** | Signifies if the evaluation is never to be released. This cannot be set true if release date is also set. | [optional] |
| **assigned** | **bool** | Set to false to unassign the evaluation. This cannot be set to false when assignee is also set. | [optional] |
| **date_assignee_changed** | **datetime** | Date when the assignee was last changed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **resource_id** | **str** | Only used for email evaluations. Will be null for all other evaluations. | [optional] |
| **resource_type** | **str** | The type of resource. Only used for email evaluations. Will be null for evaluations on all other resources. | [optional] |
| **redacted** | **bool** | Is only true when the user making the request does not have sufficient permissions to see evaluation | [optional] |
| **is_scoring_index** | **bool** |  | [optional] |
| **authorized_actions** | **list[str]** | List of user authorized actions on evaluation. Possible values: assign, edit, editScore, editAgentSignoff, delete, release, viewAudit | [optional] |
| **has_assistance_failed** | **bool** | Is true when evaluation assistance didn&#39;t execute successfully | [optional] |
| **evaluation_source** | [**EvaluationSource**](EvaluationSource.html) | The source that created the evaluation. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


