# ArchitectJobMessageDetail

## ArchitectJobMessageDetail

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The kind of information carried by this entry, which determines which of the other properties are set. | [optional] |
| **url** | str | The URL of the request. | [optional] |
| **method** | str | The HTTP method of the request. | [optional] |
| **request_body** | str | The body of the request, reported as sent and without redaction. Omitted when the request had no body, so it is absent for ordinary GET lookups and present for calls such as POST searches. Truncated to 4096 characters with a &#x60;...&lt;truncated N chars&gt;&#x60; suffix when longer. | [optional] |
| **status_code** | int | The HTTP status code of the response. Set only when a response was received, and never alongside errorCode. | [optional] |
| **status_message** | str | The HTTP status message of the response. Set only when a response was received, and never alongside errorMessage. | [optional] |
| **correlation_id** | str | The Genesys Cloud correlation id of the response, to quote when escalating to Genesys Cloud support. Set only when a response was received. | [optional] |
| **response_body** | str | The body of the response, reported as received and without redaction. Because entries are captured for requests that succeeded as well, this can carry data returned by a lookup that was unrelated to the failure. Omitted when the response had no body. Truncated to 4096 characters with a &#x60;...&lt;truncated N chars&gt;&#x60; suffix when longer. | [optional] |
| **error_code** | str | The transport error code, such as ECONNRESET. Set only when the request failed before any HTTP response was received, and never alongside statusCode. | [optional] |
| **error_message** | str | The transport error message. Set only when the request failed before any HTTP response was received, and never alongside statusMessage. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
