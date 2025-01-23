# InteractionStatsAlert

## InteractionStatsAlert

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Name of the rule that generated the alert | |
| **dimension** | str | The dimension of concern. | |
| **dimension_value** | str | The value of the dimension. | |
| **metric** | str | The metric to be assessed. | |
| **media_type** | str | The media type. | |
| **numeric_range** | str | The comparison descriptor used against the metric&#39;s value. | |
| **statistic** | str | The statistic of concern for the metric. | |
| **value** | float | The threshold value. | |
| **rule_id** | str | The id of the rule. | |
| **unread** | bool | Indicates if the alert has been read. | |
| **start_date** | datetime | The date/time the alert was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **end_date** | datetime | The date/time the owning rule exiting in alarm status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **notification_users** | [list[User]](User) | The ids of users who were notified of alarm state change. | |
| **alert_types** | list[str] | A collection of notification methods. | |
| **rule_uri** | str |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 220.0.0_
