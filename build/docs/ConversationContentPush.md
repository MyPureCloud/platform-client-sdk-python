# ConversationContentPush

## ConversationContentPush

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **device_type** | str | The device type used to send the push notification | |
| **device_token_id** | str | Unique Id of the device token | |
| **device_token** | str | device token from the notification provider | |
| **failed_messages** | [list[ConversationPushFailedMessageReferences]](ConversationPushFailedMessageReferences) | MessageIds failed to be sent which trigger the push event | |
| **notification_message** | [ConversationPushNotificationMessageLabel](ConversationPushNotificationMessageLabel) | Title and body localized according to deployment | |
| **push_provider_integration** | [ConversationPushProviderIntegration](ConversationPushProviderIntegration) | Push provider integrations details configured on the deployment | |
| **expiration** | int | The time to live of the pushed message | |



_PureCloudPlatformClientV2 234.0.0_
