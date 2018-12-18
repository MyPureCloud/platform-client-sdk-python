---
title: DialerRulesetConfigChangeCondition
---
## DialerRulesetConfigChangeCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | [optional] |
| **inverted** | **bool** |  | [optional] |
| **attribute_name** | **str** |  | [optional] |
| **value** | **str** |  | [optional] |
| **value_type** | **str** |  | [optional] |
| **operator** | **str** |  | [optional] |
| **codes** | **list[str]** |  | [optional] |
| **property_type** | **str** |  | [optional] |
| **pcProperty** | **str** |  | [optional] |
| **contact_id_field** | **str** |  | [optional] |
| **call_analysis_result_field** | **str** |  | [optional] |
| **agent_wrapup_field** | **str** |  | [optional] |
| **contact_column_to_data_action_field_mappings** | [**list[DialerRulesetConfigChangeContactColumnToDataActionFieldMapping]**](DialerRulesetConfigChangeContactColumnToDataActionFieldMapping.html) |  | [optional] |
| **predicates** | [**list[DialerRulesetConfigChangeDataActionConditionPredicate]**](DialerRulesetConfigChangeDataActionConditionPredicate.html) |  | [optional] |
| **data_action** | [**DialerRulesetConfigChangeUriReference**](DialerRulesetConfigChangeUriReference.html) |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


