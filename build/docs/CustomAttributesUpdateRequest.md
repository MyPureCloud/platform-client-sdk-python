# CustomAttributesUpdateRequest

## CustomAttributesUpdateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Unique identifier for the Custom Attributes record. IDs are created by users. | |
| **divisions** | list[str] | The list of division ids. Use [] if divisions aren&#39;t used (Unassigned Division). Omitting or setting to [] clears existing values on update. | [optional] |
| **schema_id** | str | The id of the schema that dictates which attributes can be included. Required for create, cannot be updated. | [optional] |
| **version** | int | The latest version of the Custom Attributes record. Optional for concurrency check on update. | [optional] |
| **custom_attributes** | dict(str, object) | The map of attribute values. | |



_PureCloudPlatformClientV2 255.0.0_
