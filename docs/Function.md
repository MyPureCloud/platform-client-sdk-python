# Function

## Function

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Function identifier. | [optional] |
| **name** | str | Function name. This is automatically created based on the Action Id. | [optional] |
| **description** | str | Description of the function. Limit 255 characters. | |
| **date_created** | datetime | Date and time function was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **zip_id** | str | Zip file identifier. | [optional] |
| **handler** | str | Handler entry point into zip file to execute function. Should be path within upload function package to the invocation module without language extension, followed by a period and then exported invocation method name. e.g. &#39;src/index.handler&#39; | |
| **runtime** | str | Runtime required for execution. Valid runtimes change over time as versions are deprecated. Use /api/v2/integrations/actions/functions/runtimes for current list. | |
| **timeout_seconds** | int | Execution timeout to apply to function. Value is in seconds. Range allowed 1 to 15. Default value 15 seconds. | [optional] |



_PureCloudPlatformClientV2 238.0.0_
