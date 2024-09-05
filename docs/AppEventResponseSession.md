# AppEventResponseSession

## AppEventResponseSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the app session. | |
| **duration_in_seconds** | int | Indicates how long the customer has been in the app within this session. | |
| **event_count** | int | The count of all events recorded during this session. | |
| **screenview_count** | int | The count of all screen views recorded during this session. | |
| **referrer** | [Referrer](Referrer) | The referrer of the first event in the app session. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **created_date** | datetime | UTC timestamp of the session&#39;s first event, that is when the session starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 210.0.0_
