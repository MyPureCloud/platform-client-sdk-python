# VoicemailMailboxInfo

## VoicemailMailboxInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **owner_type** | str | The owner type of the voicemail mailbox | [optional] |
| **usage_size_bytes** | int | The total number of bytes for all voicemail message audio recordings | [optional] |
| **total_count** | int | The total number of voicemail messages | [optional] |
| **unread_count** | int | The total number of voicemail messages marked as unread | [optional] |
| **deleted_count** | int | The total number of voicemail messages marked as deleted | [optional] |
| **created_date** | datetime | The date of the oldest voicemail message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_date** | datetime | The date of the most recent voicemail message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **newest_unread_date** | datetime | The date of the most recent unread voicemail message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **oldest_unread_date** | datetime | The date of the most oldest unread voicemail message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **newest_read_date** | datetime | The date of the most recent read voicemail message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **oldest_read_date** | datetime | The date of the most oldest read voicemail message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
