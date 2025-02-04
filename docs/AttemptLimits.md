# AttemptLimits

## AttemptLimits

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **max_attempts_per_contact** | int | The maximum number of times a contact can be called within the resetPeriod. Required if maxAttemptsPerNumber is not defined. | [optional] |
| **max_attempts_per_number** | int | The maximum number of times a phone number can be called within the resetPeriod. Required if maxAttemptsPerContact is not defined. | [optional] |
| **time_zone_id** | str | If the resetPeriod is TODAY, this specifies the timezone in which TODAY occurs. Required if the resetPeriod is TODAY. | [optional] |
| **reset_period** | str | After how long the number of attempts will be set back to 0. Defaults to NEVER. | [optional] |
| **recall_entries** | [dict(str, RecallEntry)](RecallEntry) | Configuration for recall attempts. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
