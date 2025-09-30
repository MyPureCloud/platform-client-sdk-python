# BillingInvoice

## BillingInvoice

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **bill_to_customer** | [Customer](Customer) | The bill to customer. | [optional] |
| **ship_to_customer** | [Customer](Customer) | The ship to customer. | [optional] |
| **sold_to_customer** | [Customer](Customer) | The sold to customer. | [optional] |
| **date_invoiced** | date | Date when the invoice was issued. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **bill_to_address** | [InvoiceAddress](InvoiceAddress) | Details of the bill to address. | [optional] |
| **ship_to_address** | [InvoiceAddress](InvoiceAddress) | Details of the ship to address. | [optional] |
| **currency_iso_code** | str | Contains the ISO code for any currency allowed by the organization. | [optional] |
| **payment_status** | str | Status of the payment. | [optional] |
| **payment_terms** | str | Payment terms. | [optional] |
| **payment_link** | str | Payment link. | [optional] |
| **customer_po_number** | str | Purchase Order Number. | [optional] |
| **customer_invoice_type** | str | Type of the invoice. | [optional] |
| **amount** | float | Amount. | [optional] |



_PureCloudPlatformClientV2 239.0.0_
