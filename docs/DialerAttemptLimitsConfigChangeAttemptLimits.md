# DialerAttemptLimitsConfigChangeAttemptLimits

## DialerAttemptLimitsConfigChangeAttemptLimits

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **max_attempts_per_contact** | int |  | [optional] |
| **max_attempts_per_number** | int |  | [optional] |
| **time_zone_id** | str | The timezone is necessary to define when \&quot;today\&quot; starts and ends | [optional] |
| **reset_period** | str | After how long the number of attempts will be set back to 0 | [optional] |
| **recall_entries** | [dict(str, DialerAttemptLimitsConfigChangeRecallEntry)](DialerAttemptLimitsConfigChangeRecallEntry) | Configuration for recall attempts | [optional] |
| **breadth_first_recalls** | bool | Whether recalls are performed before considering other numbers (true) or after (false) | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 229.0.0_
