# ConversationContentPaymentRequest

## ConversationContentPaymentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **payment_platform** | str | The payment platform being used (e.g. Apple Pay) | |
| **country_code** | str | The merchant&#39;s two-letter ISO 3166 country code. | |
| **currency_code** | str | The three-letter ISO 4217 currency code for the payment. | |
| **order_total** | float | The total price of the order. | |
| **line_items** | [list[ConversationContentLineItem]](ConversationContentLineItem) | The items that make up the order. | [optional] |
| **shipping_options** | [list[ConversationContentLineItem]](ConversationContentLineItem) | The available shipping options. | [optional] |
| **required_contact_fields** | [list[ConversationContentRequiredContactField]](ConversationContentRequiredContactField) | Contact fields required to complete the order. | [optional] |
| **received_message** | [ConversationContentReceivedReplyMessage](ConversationContentReceivedReplyMessage) | The message prompt to complete a payment transaction. | [optional] |
| **reply_message** | [ConversationContentReceivedReplyMessage](ConversationContentReceivedReplyMessage) | The reply message after the user has completed the payment transaction. | [optional] |



_PureCloudPlatformClientV2 235.0.0_
