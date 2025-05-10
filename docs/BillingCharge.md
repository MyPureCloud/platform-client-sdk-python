# BillingCharge

## BillingCharge

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **product** | [BillingProduct](BillingProduct) | Represents the details of a product. | [optional] |
| **organizations** | [list[NamedEntity]](NamedEntity) | List of plans within the organization. | [optional] |
| **getprepaid_quantity** | int | The quantity of usage that is prepaid. | [optional] |
| **getfairuse_quantity** | int | The quantity of usage allowed under fair use policies. | [optional] |
| **getactual_quantity** | int | The actual quantity of usage. | [optional] |
| **getoverage_quantity** | int | The quantity of usage that exceeds prepaid or fair use limits. | [optional] |
| **overage_rate** | float | The rate charged per unit of overage. | [optional] |
| **overage_charge** | float | The total charge for overage usage. | [optional] |
| **overage_currency** | str | The currency in which the overage charge is billed. | [optional] |



_PureCloudPlatformClientV2 228.0.0_
