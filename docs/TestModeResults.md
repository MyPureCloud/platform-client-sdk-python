# TestModeResults

## TestModeResults

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schema_validation** | [TestSchemaOperation](TestSchemaOperation) | Information about the validation of the schema of the event body passed in to test mode | [optional] |
| **target_validation** | [TestTargetOperation](TestTargetOperation) | Information about the validation of the trigger target | [optional] |
| **json_path_validation** | [TestMatchesOperation](TestMatchesOperation) | Information about the json path matching criteria | [optional] |
| **trigger_matches** | bool | Whether the trigger would have matched on the provided event body | [optional] |



_PureCloudPlatformClientV2 223.0.0_
