# StatusChange

## StatusChange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_status_changed** | datetime | The date of this status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | The status the change request transitioned to | [optional] |
| **previous_status** | str | The status the change request transitioned from | [optional] |
| **namespace** | str | The namespace for the status change | [optional] |
| **message** | str | A short message describing the status change | [optional] |
| **reject_reason** | str | The reason for rejecting the limit override request | [optional] |



_PureCloudPlatformClientV2 249.0.0_
