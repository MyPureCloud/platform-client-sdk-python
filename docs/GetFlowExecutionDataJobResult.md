# GetFlowExecutionDataJobResult

## GetFlowExecutionDataJobResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **entities** | [list[ExecutionDataEntity]](ExecutionDataEntity) | On jobState &#x3D; Success this field will be populated with the list of results of files for download. | [optional] |
| **job_state** | str | The state of the backend process to prep the files for download. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 220.0.0_
