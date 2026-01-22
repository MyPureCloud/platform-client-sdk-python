# AgentScoringRule

## AgentScoringRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **program_id** | str | The program ID that this rule belongs to. When provided in request body, this value is ignored in favor of the path parameter. | [optional] |
| **sampling_type** | str | Sampling type setting. Valid values: All, Percentage | |
| **sampling_percentage** | float | Percentage of interactions to evaluate (0.01-100.00). Required when samplingType is Percentage, null when All. | [optional] |
| **submission_type** | str | Submission type for evaluations. Valid values: Automated, Manual | |
| **evaluation_form_context_id** | str | The evaluation form contextID to use for scoring. | |
| **enabled** | bool | Whether the rule is enabled. | |
| **published** | bool | Whether the rule is published. | [optional] |
| **evaluator** | [AddressableEntityRef](AddressableEntityRef) | The evaluator for evaluations created by this rule. | [optional] |
| **date_created** | datetime | Date when the rule was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the rule was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 249.0.0_
