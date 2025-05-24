# ResponseConfig

## ResponseConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **translation_map** | dict(str, str) | Map &#39;attribute name&#39; and &#39;JSON path&#39; pairs used to extract data from REST response. | [optional] |
| **translation_map_defaults** | dict(str, str) | Map &#39;attribute name&#39; and &#39;default value&#39; pairs used as fallback values if JSON path extraction fails for specified key. | [optional] |
| **success_template** | str | Velocity template to build response to return from Action. | [optional] |
| **success_template_uri** | str | URI to retrieve success template. | [optional] |



_PureCloudPlatformClientV2 229.0.0_
