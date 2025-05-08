# HistoryListing

## HistoryListing

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **complete** | bool |  | [optional] |
| **user** | [User](User) |  | [optional] |
| **client** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **error_message** | str |  | [optional] |
| **error_code** | str |  | [optional] |
| **error_details** | [list[Detail]](Detail) |  | [optional] |
| **error_message_params** | dict(str, str) |  | [optional] |
| **action_name** | str | Action name | [optional] |
| **action_status** | str | Action status | [optional] |
| **name** | str |  | [optional] |
| **description** | str |  | [optional] |
| **system** | bool |  | [optional] |
| **started** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **completed** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **page_size** | int |  | [optional] |
| **page_number** | int |  | [optional] |
| **total** | int |  | [optional] |
| **entities** | [list[HistoryEntry]](HistoryEntry) |  | [optional] |
| **page_count** | int |  | [optional] |



_PureCloudPlatformClientV2 227.1.0_
