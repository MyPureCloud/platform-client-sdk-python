# RecordingNotificationResponse

## RecordingNotificationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **originating_message_id** | str | Reference to the ID of the original outbound notification message this response is for (e.g. the Apple requestIdentifier). | [optional] |
| **reference_id** | str | The business context reference associated with the notification (e.g. order ID, case ID). May be empty if the provider does not return it. | [optional] |
| **notification_status** | str | The status of the notification response. | [optional] |
| **notification_text** | str | The localized display text of the user&#39;s response (e.g. \&quot;Yes\&quot;). | [optional] |



_PureCloudPlatformClientV2 266.0.0_
