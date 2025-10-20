# BillingWallet

## BillingWallet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the object. | [optional] |
| **organizations** | [list[NamedEntity]](NamedEntity) | A Genesys Cloud Organization and it&#39;s related plans. | [optional] |
| **product** | [BillingProduct](BillingProduct) | Represents the details of a product. | [optional] |
| **starting_balance** | float | The initial balance in the wallet. | [optional] |
| **ending_balance** | float | The final balance in the wallet after transactions. | [optional] |
| **balance_increase** | float | Total amount added to the wallet. | [optional] |
| **balance_decrease** | float | The amount removed from the wallet due to a contract change. | [optional] |
| **balance_consumption** | float | Total consumption deducted from the wallet. | [optional] |
| **balance_overage** | float | The amount exceeding a predefined balance threshold. | [optional] |
| **balance_overage_rate** | float | The rate charged for an overage.. | [optional] |
| **balance_overage_charge** | float | The amount to be charged. | [optional] |
| **balance_overage_currency** | str | The currency in which the overage charge is invoiced. | [optional] |
| **unit_of_measure** | str | The unit of measure for the wallet. | [optional] |



_PureCloudPlatformClientV2 241.0.0_
