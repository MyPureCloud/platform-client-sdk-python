# UsersRulesDependent

## UsersRulesDependent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **rule_id** | str | The id of the rule | [optional] |
| **type_id** | str | The type id of the dependent | [optional] |
| **type** | str | The type of the dependent | [optional] |
| **created_date** | datetime | The date/time the dependent was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the dependent | [optional] |
| **last_run** | [UsersRulesLastRunMetadata](UsersRulesLastRunMetadata) | Information on the last run of the dependent | [optional] |
| **recent_run_count** | int | The number of times the rule has run | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 249.0.0_
