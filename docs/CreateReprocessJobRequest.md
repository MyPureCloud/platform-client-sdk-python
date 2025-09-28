# CreateReprocessJobRequest

## CreateReprocessJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name given for the job. | |
| **description** | str | The description of the job. | [optional] |
| **date_start** | datetime | The start date for the search criteria. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_end** | datetime | The end date for the search criteria. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **programs** | list[str] | A list of program IDs to filter conversations by. | |
| **media_types** | list[str] | The types of conversations to reprocess. | |
| **dialects** | list[str] | The dialects to filter by the conversations. | [optional] |



_PureCloudPlatformClientV2 238.0.0_
