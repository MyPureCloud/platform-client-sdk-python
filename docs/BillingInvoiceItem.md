# BillingInvoiceItem

## BillingInvoiceItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **product** | [BillingProduct](BillingProduct) | Represents the details of a product. | [optional] |
| **description** | str | Line Item Description. | [optional] |
| **date_transacted** | date | Invoice transaction date. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_start** | date | Invoice start date. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end** | date | Invoice end date. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **organization** | [NamedEntity](NamedEntity) | A Genesys Cloud Organization. | [optional] |
| **quantity** | int | Quantity of the item. | [optional] |
| **unit_of_measure** | str | Unit of Measure. | [optional] |
| **amount** | float | Amount. | [optional] |



_PureCloudPlatformClientV2 229.0.0_
