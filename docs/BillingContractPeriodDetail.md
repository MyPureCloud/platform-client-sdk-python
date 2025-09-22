# BillingContractPeriodDetail

## BillingContractPeriodDetail

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **date_start** | date | The date when the Billing Period starts. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end** | date | The date when the Billing Period starts. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **status** | str | The type of address. | [optional] |
| **charges** | [list[BillingCharge]](BillingCharge) | Represents usage metrics including prepaid, actual, and overage quantities along with associated charges. | [optional] |
| **wallets** | [list[BillingWallet]](BillingWallet) | Represents usage metrics including prepaid, actual, and overage quantities along with associated charges. | [optional] |



_PureCloudPlatformClientV2 237.0.0_
