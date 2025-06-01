# SendMessagingTemplateRequest

## SendMessagingTemplateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **response_id** | str | A Response Management response identifier for a messaging template defined response | [optional] |
| **parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management response substitutions for the response&#39;s messaging template. (Deprecated) use bodyParameters instead. | [optional] |
| **header_parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management header parameter substitutions for the response&#39;s messaging template | [optional] |
| **body_parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management body parameter substitutions for the response&#39;s messaging template | [optional] |
| **button_url_parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management button url parameter substitutions for the response&#39;s messaging template | [optional] |



_PureCloudPlatformClientV2 230.0.0_
