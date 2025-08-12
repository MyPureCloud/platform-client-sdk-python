# UpdateServiceGoalTemplate

## UpdateServiceGoalTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the service goal template. | [optional] |
| **service_level** | [BuServiceLevel](BuServiceLevel) | Service level targets for this service goal template | [optional] |
| **average_speed_of_answer** | [BuAverageSpeedOfAnswer](BuAverageSpeedOfAnswer) | Average speed of answer targets for this service goal template | [optional] |
| **abandon_rate** | [BuAbandonRate](BuAbandonRate) | Abandon rate targets for this service goal template | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the service goal template | |
| **impact_override** | [ServiceGoalTemplateImpactOverride](ServiceGoalTemplateImpactOverride) | Settings controlling max percent increase and decrease of service goals for this service goal template | [optional] |



_PureCloudPlatformClientV2 235.0.0_
