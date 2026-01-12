# BillingContract

## BillingContract

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **external_number** | str | Unique external number. | [optional] |
| **status** | str | The status of the contract. | [optional] |
| **commercial_model** | str | The type of commercial model. | [optional] |
| **purchase_order_numbers** | list[str] | List of po numbers periods for this contract. | [optional] |
| **bill_to_customer** | [Customer](Customer) | The bill to customer. | [optional] |
| **sold_to_customer** | [Customer](Customer) | The sold to customer. | [optional] |
| **end_customer** | [Customer](Customer) | The end customer. | [optional] |
| **date_start** | date | The start date of the contract. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end** | date | The end date of the contract. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_ramp_start** | date | the date when the first revenue or quantity in a ramped deal begins. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_ramp_end** | date | the date when the first revenue or quantity in a ramped deal ends. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **billing_periods** | [list[BillingContractPeriod]](BillingContractPeriod) | List of billing periods for the contract. | [optional] |
| **plans** | [list[BillingPlan]](BillingPlan) | The collection of prices for the related organizations. | [optional] |



_PureCloudPlatformClientV2 247.0.0_
