# DialerRulesetConfigChangeCondition

## DialerRulesetConfigChangeCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **data_action** | [DialerRulesetConfigChangeUriReference](DialerRulesetConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **type** | str | The type of the condition | [optional] |
| **inverted** | bool | Indicates whether to evaluate for the opposite of the stated condition; default is false | [optional] |
| **attribute_name** | str | An attribute name associated with the condition (applies only to certain rule conditions) | [optional] |
| **value** | str | A value associated with the condition | [optional] |
| **value_type** | str | Determines the type of the value associated with the condition | [optional] |
| **operator** | str | An operation type for condition evaluation | [optional] |
| **codes** | list[str] | List of wrap-up code identifiers (used only in conditions of type &#39;wrapupCondition&#39;) | [optional] |
| **property_type** | str | Determines the type of the property associated with the condition | [optional] |
| **pcProperty** | str | A value associated with the property type of this condition | [optional] |
| **data_not_found_resolution** | bool | The result of this condition if the data action returns a result indicating there was no data. Required for a DataActionCondition. | [optional] |
| **contact_id_field** | str | The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionCondition. | [optional] |
| **call_analysis_result_field** | str | The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionCondition. | [optional] |
| **agent_wrapup_field** | str | The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionCondition. | [optional] |
| **contact_column_to_data_action_field_mappings** | [list[DialerRulesetConfigChangeContactColumnToDataActionFieldMapping]](DialerRulesetConfigChangeContactColumnToDataActionFieldMapping) | A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionCondition. | [optional] |
| **predicates** | [list[DialerRulesetConfigChangeDataActionConditionPredicate]](DialerRulesetConfigChangeDataActionConditionPredicate) | A list of predicates defining the comparisons to use for this condition. Required for a dataActionCondition. | [optional] |



_PureCloudPlatformClientV2 214.0.0_
