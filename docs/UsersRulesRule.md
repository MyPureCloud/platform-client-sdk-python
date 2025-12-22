# UsersRulesRule

## UsersRulesRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | The description of the rule | [optional] |
| **type** | str | The type of the rule | [optional] |
| **criteria** | [list[UsersRulesCriteria]](UsersRulesCriteria) | The criteria of the rule | [optional] |
| **created_date** | datetime | The date/time the rule was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the rule | [optional] |
| **modified_date** | datetime | The date/time the rule was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The last user to modify the rule | [optional] |
| **last_run** | [UsersRulesLastRunMetadata](UsersRulesLastRunMetadata) | Information on the last run of the rule | [optional] |
| **recent_run_count** | int | The number of times the rule has run | [optional] |
| **dependent_count** | int | The number of dependents this rule has | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
