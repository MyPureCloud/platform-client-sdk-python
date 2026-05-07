# Variable

## Variable

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the variable. | |
| **type** | str | The data type of the variable. | |
| **scope** | str | The scope that determines the variable&#39;s usage context within Guides runtime. | |
| **description** | str | The description of the variable used by Guides runtime for input/output handling. | [optional] |
| **validation** | object | The validation configuration for the variable. Optional - if not present, no validation is applied. | [optional] |
| **list_values** | object | The values configuration for List variables. Only applicable when type is &#39;List&#39;. | [optional] |
| **list_variables** | [list[Variable]](Variable) | The variables that the list result will be stored in. Only applicable when type is &#39;List&#39;. | [optional] |



_PureCloudPlatformClientV2 257.0.0_
