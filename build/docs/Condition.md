# Condition

## Condition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The type of the condition. | [optional] |
| **inverted** | bool | If true, inverts the result of evaluating this Condition. Default is false. | [optional] |
| **attribute_name** | str | An attribute name associated with this Condition. Required for a contactAttributeCondition. | [optional] |
| **value** | str | A value associated with this Condition. This could be text, a number, or a relative time. Not used for a DataActionCondition. | [optional] |
| **value_type** | str | The type of the value associated with this Condition. Not used for a DataActionCondition. | [optional] |
| **operator** | str | An operation with which to evaluate the Condition. Not used for a DataActionCondition. | [optional] |
| **codes** | list[str] | List of wrap-up code identifiers. Required for a wrapupCondition. | [optional] |
| **pcProperty** | str | A value associated with the property type of this Condition. Required for a contactPropertyCondition. | [optional] |
| **property_type** | str | The type of the property associated with this Condition. Required for a contactPropertyCondition. | [optional] |
| **data_action** | [DomainEntityRef](DomainEntityRef) | The Data Action to use for this condition. Required for a dataActionCondition. | [optional] |
| **data_not_found_resolution** | bool | The result of this condition if the data action returns a result indicating there was no data. Required for a DataActionCondition. | [optional] |
| **contact_id_field** | str | The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionCondition. | [optional] |
| **call_analysis_result_field** | str | The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionCondition. | [optional] |
| **agent_wrapup_field** | str | The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionCondition. | [optional] |
| **contact_column_to_data_action_field_mappings** | [list[ContactColumnToDataActionFieldMapping]](ContactColumnToDataActionFieldMapping) | A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionCondition. | [optional] |
| **predicates** | [list[DataActionConditionPredicate]](DataActionConditionPredicate) | A list of predicates defining the comparisons to use for this condition. Required for a dataActionCondition. | [optional] |



_PureCloudPlatformClientV2 227.1.0_
