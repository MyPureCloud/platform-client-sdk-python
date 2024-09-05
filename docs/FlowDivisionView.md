# FlowDivisionView

## FlowDivisionView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The flow identifier | [optional] |
| **name** | str | The flow name | |
| **division** | [WritableDivision](WritableDivision) | The division to which this entity belongs. | [optional] |
| **type** | str |  | [optional] |
| **description** | str | the flow description | [optional] |
| **input_schema** | [JsonSchemaDocument](JsonSchemaDocument) | json schema describing the inputs for the flow | [optional] |
| **output_schema** | [JsonSchemaDocument](JsonSchemaDocument) | json schema describing the outputs for the flow | [optional] |
| **supported_languages** | [list[SupportedLanguage]](SupportedLanguage) | List of supported languages for the published version of the flow. | [optional] |
| **published_version** | [FlowVersion](FlowVersion) | published version information if there is a published version | [optional] |
| **debug_version** | [FlowVersion](FlowVersion) | debug version information if there is a debug version | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 210.0.0_
