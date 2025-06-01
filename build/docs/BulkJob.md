# BulkJob

## BulkJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **state** | str | The bulk job state. | [optional] |
| **action** | str | The bulk job action. This determines what the bulk job does, for example, terminate workitems. | [optional] |
| **total_count** | int | Total count of items to be processed in the bulk job. | [optional] |
| **successful_count** | int | Count of successfully processed items in the bulk job. | [optional] |
| **failed_count** | int | Count of failed processed items in the bulk job. | [optional] |
| **date_started** | datetime | The bulk job start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_finished** | datetime | The bulk job finished date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The bulk job modification date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 230.0.0_
