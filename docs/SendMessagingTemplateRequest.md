# SendMessagingTemplateRequest

## SendMessagingTemplateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **response_id** | str | Unique identifier for a Response Management response to fetch and apply pre-configured message content when sending outbound responses. | [optional] |
| **parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management response substitutions for the response&#39;s messaging template. (Deprecated) use bodyParameters instead. | [optional] |
| **header_parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management header parameter substitutions for the response&#39;s messaging template | [optional] |
| **body_parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management body parameter substitutions for the response&#39;s messaging template | [optional] |
| **button_url_parameters** | [list[TemplateParameter]](TemplateParameter) | A list of Response Management button url parameter substitutions for the response&#39;s messaging template | [optional] |
| **carousel_parameters** | [CarouselParameters](CarouselParameters) | Template parameters for carousel card components | [optional] |



_PureCloudPlatformClientV2 249.0.0_
