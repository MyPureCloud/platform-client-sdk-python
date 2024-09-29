# ApiUsageRow

## ApiUsageRow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **client_id** | str | Client Id associated with this query result | [optional] |
| **client_name** | str | Client Name associated with this query result | [optional] |
| **organization_id** | str | Organization Id associated with this query result | [optional] |
| **user_id** | str | User Id associated with this query result | [optional] |
| **template_uri** | str | Template Uri associated with this query result | [optional] |
| **http_method** | str | HTTP Method associated with this query result | [optional] |
| **status200** | int | Number of requests resulting in a 2xx HTTP status code | [optional] |
| **status300** | int | Number of requests resulting in a 3xx HTTP status code | [optional] |
| **status400** | int | Number of requests resulting in a 4xx HTTP status code | [optional] |
| **status500** | int | Number of requests resulting in a 5xx HTTP status code | [optional] |
| **status429** | int | Number of requests resulting in a 429 HTTP status code, this is a subset of the count returned with status400 | [optional] |
| **requests** | int | Total number of requests | [optional] |
| **date** | datetime | Date of requests, based on granularity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 212.0.0_
