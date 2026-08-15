# SummaryGenerationConfig

## SummaryGenerationConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Copilot generated summary is enabled. | |
| **summary_setting** | [SummarySettingEntity](SummarySettingEntity) | Configured summary setting object. | [optional] |
| **retention_seconds** | int | Summary retention time in seconds. Can only be modified on the parent assistant. | [optional] |
| **on_demand_summary_config** | [OnDemandSummaryConfig](OnDemandSummaryConfig) | On-demand summary configuration. | [optional] |
| **model_config** | [ModelConfig](ModelConfig) | Model configuration for summarization. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
