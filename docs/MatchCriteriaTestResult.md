# MatchCriteriaTestResult

## MatchCriteriaTestResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **json_path** | str | The Goessner json path of the field to match | [optional] |
| **operator** | str | The type of operation to perform for matching check | [optional] |
| **value** | object | The value to match on. Only one of value and values can be included | [optional] |
| **values** | list[object] | The list of values to match on. Only one of value and values can be included | [optional] |
| **generated_json_path_condition** | str | The generated json path condition | [optional] |
| **match** | bool | Did the generated json path condition match | [optional] |
| **json_path_extraction** | [list[MatchTestResult]](MatchTestResult) | The json paths and their values that were compared | [optional] |



_PureCloudPlatformClientV2 230.0.0_
