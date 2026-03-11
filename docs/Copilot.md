# Copilot

## Copilot

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Copilot is enabled. | [optional] |
| **live_on_queue** | bool | Copilot is live on selected queue. | |
| **default_language** | str | Copilot default language, e.g. [en-US, es-US, es-ES]. Once set, it can not be modified. | |
| **knowledge_answer_config** | [KnowledgeAnswerConfig](KnowledgeAnswerConfig) | Deprecated: Please use AutoSearchConfig and ManualSearchConfig fields instead. | [optional] |
| **summary_generation_config** | [SummaryGenerationConfig](SummaryGenerationConfig) | Copilot generated summary configuration. | [optional] |
| **wrapup_code_prediction_config** | [WrapupCodePredictionConfig](WrapupCodePredictionConfig) | Copilot generated wrapup code prediction configuration. | [optional] |
| **answer_generation_config** | [AnswerGenerationConfig](AnswerGenerationConfig) | Deprecated: Please use AutoSearchConfig and ManualSearchConfig fields instead. | [optional] |
| **nlu_engine_type** | str | Language understanding engine type. | [optional] |
| **nlu_config** | [NluConfig](NluConfig) | NLU configuration. | [optional] |
| **rule_engine_config** | [RuleEngineConfig](RuleEngineConfig) | Rule engine configuration. | [optional] |
| **auto_search_config** | [AutoSearchConfig](AutoSearchConfig) | Auto search configuration. | [optional] |
| **manual_search_config** | [ManualSearchConfig](ManualSearchConfig) | Manual Search configuration. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 253.0.0_
