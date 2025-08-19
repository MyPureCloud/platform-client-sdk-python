# PaymentRequest

## PaymentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **payment_platform** | str | The payment platform being used (e.g. Apple Pay) | [optional] |
| **country_code** | str | The merchant&#39;s two-letter ISO 3166 country code. | [optional] |
| **currency_code** | str | The three-letter ISO 4217 currency code for the payment. | [optional] |
| **order_total** | float | The total price of the order. | |
| **line_items** | [list[PaymentLineItem]](PaymentLineItem) | The items that make up the order. | [optional] |
| **shipping_options** | [list[PaymentLineItem]](PaymentLineItem) | The available shipping options. | [optional] |



_PureCloudPlatformClientV2 235.1.0_
