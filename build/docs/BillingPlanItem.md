# BillingPlanItem

## BillingPlanItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **item_number** | str | Item number. | [optional] |
| **name** | str | Name of the item. | [optional] |
| **type** | str | Type of the item. | [optional] |
| **function** | str | Function of the item. | [optional] |
| **description** | str | Detailed description of the item. | [optional] |
| **date_charged_through** | date | The date through which a customer has been billed for the charge. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **currency_iso_code** | str | Contains the ISO code for any currency allowed by the organization. | [optional] |
| **discount_amount** | float | The amount of the discount. | [optional] |
| **date_effective_start** | date | The date when the Address became effective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_effective_end** | date | The date when the Address became effective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **overage_price** | float | The price for units over the allowed amount. | [optional] |
| **price** | float | The price associated with the item expressed as a decimal. | [optional] |
| **quantity** | int | The quantity of units. | [optional] |
| **unit_of_measure** | str | The unit of measure for the wallet. | [optional] |



_PureCloudPlatformClientV2 235.1.0_
