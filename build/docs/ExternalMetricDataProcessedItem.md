# ExternalMetricDataProcessedItem

## ExternalMetricDataProcessedItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | The user ID. Must provide either userId or userEmail, but not both. | [optional] |
| **user_email** | str | The user main email used in user&#39;s GenesysCloud account. Must provide either userId or userEmail, but not both. | [optional] |
| **metric_id** | str | The ID of the external metric definition | |
| **date_occurred** | date | The date of the metric data. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **value** | float | The value of the metric data. When value is null, the metric data will be deleted. | |
| **count** | int | The number of data points. The default value is 0 when type is Cumulative and the metric data already exists, otherwise 1. When total count reaches 0, the metric data will be deleted. | [optional] |
| **type** | str | The type of the metric data. The default value is Total. | [optional] |
| **total_value** | float | The total value of the metric data. | [optional] |
| **total_count** | int | The total number of data points. | [optional] |



_PureCloudPlatformClientV2 239.0.0_
