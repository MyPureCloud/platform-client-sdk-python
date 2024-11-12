# EvaluationScoringSet

## EvaluationScoringSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **total_score** | float | Score of all questions | [optional] |
| **total_critical_score** | float | Score of only the critical questions | [optional] |
| **total_non_critical_score** | float | Score of only the non-critical questions | [optional] |
| **question_group_scores** | [list[EvaluationQuestionGroupScore]](EvaluationQuestionGroupScore) |  | [optional] |
| **any_failed_kill_questions** | bool | Indicates that at least one fatal question was answered without having the highest score available for the question | [optional] |
| **comments** | str | Overall comments from the evaluator | [optional] |
| **private_comments** | str | Overall private comments from the evaluator | [optional] |
| **agent_comments** | str | Comments from the agent while reviewing evaluation results | [optional] |
| **transcript_topics** | [list[TranscriptTopic]](TranscriptTopic) | List of topics found within the conversation&#39;s transcripts | [optional] |



_PureCloudPlatformClientV2 216.0.0_
