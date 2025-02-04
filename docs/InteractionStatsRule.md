# InteractionStatsRule

## InteractionStatsRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Name of the rule | |
| **dimension** | str | The dimension of concern. | |
| **dimension_value** | str | The value of the dimension. | |
| **metric** | str | The metric to be assessed. | |
| **media_type** | str | The media type. | |
| **numeric_range** | str | The comparison descriptor used against the metric&#39;s value. | |
| **statistic** | str | The statistic of concern for the metric. | |
| **value** | float | The threshold value. | |
| **enabled** | bool | Indicates if the rule is enabled. | |
| **in_alarm** | bool | Indicates if the rule is in alarm state. | [optional] |
| **notification_users** | [list[User]](User) | The ids of users who will be notified of alarm state change. | |
| **alert_types** | list[str] | A collection of notification methods. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
