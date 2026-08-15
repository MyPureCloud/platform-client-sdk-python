# EngagementFilter

## EngagementFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operator** | str | The comparison operator for engagement metric filtering. | |
| **pcFrom** | int | The inclusive lower bound of the engagement metric count. Required when operator is Between, not allowed otherwise. | [optional] |
| **to** | int | The inclusive upper bound of the engagement metric count. Required when operator is Between, not allowed otherwise. | [optional] |
| **value** | int | The engagement metric count to compare against. Required for every operator except Between, not allowed for Between. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
