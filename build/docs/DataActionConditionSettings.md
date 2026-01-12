# DataActionConditionSettings

## DataActionConditionSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **data_action_id** | str | The Data Action Id to use for this condition. | |
| **contact_id_field** | str | The input field from the data action that the contactId will be passed into. | [optional] |
| **data_not_found_resolution** | bool | The result of this condition if the data action returns a result indicating there was no data. | |
| **predicates** | [list[DigitalDataActionConditionPredicate]](DigitalDataActionConditionPredicate) | A list of predicates defining the comparisons to use for this condition. | [optional] |
| **contact_column_to_data_action_field_mappings** | [list[DataActionContactColumnFieldMapping]](DataActionContactColumnFieldMapping) | A list of mappings defining which contact data fields will be passed to which data action input fields. | [optional] |



_PureCloudPlatformClientV2 247.0.0_
