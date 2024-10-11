# RequestConfig

## RequestConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **request_url_template** | str | URL that may include placeholders for requests to 3rd party service. This value is read only for Function Integrations and will be set when a draft is created. | [optional] |
| **request_template** | str | Velocity template to define request body sent to 3rd party service. | [optional] |
| **request_template_uri** | str | URI to retrieve requestTemplate | [optional] |
| **request_type** | str | HTTP method to use for request | [optional] |
| **headers** | dict(str, str) | Headers to include in request in (Header Name, Value) pairs. | [optional] |



_PureCloudPlatformClientV2 213.0.0_
