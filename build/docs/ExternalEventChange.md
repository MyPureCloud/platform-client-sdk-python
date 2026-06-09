# ExternalEventChange

## ExternalEventChange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **change_category** | str | The category of the change | [optional] |
| **schema_id** | str | The unique identifier for the schema | [optional] |
| **event_name** | str | The name of the event | [optional] |
| **date_detected** | datetime | The timestamp when the change was detected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **system_status** | str | The status of the change | [optional] |
| **error_code** | str | A code representing the error, only present for ERROR category changes | [optional] |
| **error_description** | str | A description of the error, only present for ERROR category changes | [optional] |



_PureCloudPlatformClientV2 259.0.0_
