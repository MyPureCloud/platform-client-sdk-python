# ConversationContentNotificationResponse

## ConversationContentNotificationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **originating_message_id** | str | Reference to the ID of the original outbound notification message this response is for (e.g. the Apple requestIdentifier). | |
| **reference_id** | str | The business context reference associated with the notification (e.g. order ID, case ID). May be empty if the provider does not return it. | [optional] |
| **notification_status** | str | The status of the notification response. | |
| **notification_text** | str | The localized display text of the user&#39;s response (e.g. \&quot;Yes\&quot;). | [optional] |



_PureCloudPlatformClientV2 257.0.0_
