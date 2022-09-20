---
title: TestModeResults
---
## TestModeResults

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schema_validation** | [**TestSchemaOperation**](TestSchemaOperation.html) | Information about the validation of the schema of the event body passed in to test mode | [optional] |
| **target_validation** | [**TestTargetOperation**](TestTargetOperation.html) | Information about the validation of the trigger target | [optional] |
| **json_path_validation** | [**TestMatchesOperation**](TestMatchesOperation.html) | Information about the json path matching criteria | [optional] |
| **trigger_matches** | **bool** | Whether the trigger would have matched on the provided event body | [optional] |
{: class="table table-striped"}


