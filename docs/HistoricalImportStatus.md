# HistoricalImportStatus

## HistoricalImportStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **request_id** | str | Request id of the historical import in the organization | [optional] |
| **date_import_ended** | datetime | The last day of the data you are importing. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_import_started** | datetime | The first day of the data you are importing. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | Status of the historical import in the organization. | [optional] |
| **error** | str | Error occured if the status of the import is failed | [optional] |
| **date_created** | datetime | Date in which the historical import is initiated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date in which the historical import is modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **active** | bool | Whether this historical import is active or not | [optional] |
| **type** | str | Whether this historical import is of type csv or json | [optional] |



_PureCloudPlatformClientV2 211.0.0_
