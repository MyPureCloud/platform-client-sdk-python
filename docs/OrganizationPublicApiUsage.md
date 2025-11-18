# OrganizationPublicApiUsage

## OrganizationPublicApiUsage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date** | date | The date of the usage. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **platform** | str | The platform the request(s) is/were made on. | [optional] |
| **http_method** | str | The http method of the request(s) | [optional] |
| **template_uri** | str | The templateUri of the request(s). | [optional] |
| **request_count** | int | The total number of requests. | [optional] |
| **status200** | int | The number of requests resulting in a 2xx HTTP status code. | [optional] |
| **status300** | int | The number of requests resulting in a 3xx HTTP status code. | [optional] |
| **status400** | int | The number of requests resulting in a 4xx HTTP status code. | [optional] |
| **status429** | int | The number of requests resulting in a 429 HTTP status code. | [optional] |
| **status500** | int | The number of requests resulting in a 5xx HTTP status code. | [optional] |
| **oauth_client** | [DomainEntityRef](DomainEntityRef) | The id of the oauthClient that made the request(s). | [optional] |
| **user** | [UserReference](UserReference) | The id of the user who made the request(s). | [optional] |



_PureCloudPlatformClientV2 243.0.0_
