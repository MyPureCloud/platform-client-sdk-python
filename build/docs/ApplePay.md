# ApplePay

## ApplePay

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **store_name** | str | The name of the store. | |
| **merchant_id** | str | The stores merchant identifier. | |
| **domain_name** | str | The domain name associated with the merchant account. | |
| **payment_capabilities** | list[str] | The payment capabilities supported by the merchant. | |
| **supported_payment_networks** | list[str] | The payment networks supported by the merchant. | |
| **payment_certificate_credential_id** | str | The Genesys credentialId the payment certificates are stored under. | |
| **payment_gateway_url** | str | The url used to process payments. | |
| **fallback_url** | str | The url opened in a web browser if the customers device is unable to make payments using Apple Pay. | [optional] |
| **shipping_method_update_url** | str | The url called when the customer changes the shipping method. | [optional] |
| **shipping_contact_update_url** | str | The url called when the customer changes their shipping address information. | [optional] |
| **payment_method_update_url** | str | The url called when the customer changes their payment method. | [optional] |
| **order_tracking_url** | str | The url called after completing the order to update the order information in your system | [optional] |



_PureCloudPlatformClientV2 245.0.0_
