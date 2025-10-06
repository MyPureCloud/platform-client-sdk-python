# MeetingIdRecord

## MeetingIdRecord

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **ephemeral** | bool | Boolean flag for ephemeral status of the created record | |
| **conference_id** | str | The conferenceId used to generate a meetingId | [optional] |
| **date_expired** | datetime | Instant at which the meetingId record will no longer be considered active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
