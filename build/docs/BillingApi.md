# BillingApi

## PureCloudPlatformClientV2.BillingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_billing_contract**](#get_billing_contract) | Get billing contract|
|[**get_billing_contract_billingperiod**](#get_billing_contract_billingperiod) | Get contract billing period|
|[**get_billing_contracts**](#get_billing_contracts) | Get billing contracts|
|[**get_billing_contracts_invoice_document**](#get_billing_contracts_invoice_document) | Get invoice document|
|[**get_billing_contracts_invoice_lines**](#get_billing_contracts_invoice_lines) | Get invoice lines|
|[**get_billing_contracts_invoices**](#get_billing_contracts_invoices) | Get invoices|
|[**get_billing_reports_billableusage**](#get_billing_reports_billableusage) | Get a report of the billable license usages|
|[**get_billing_trusteebillingoverview_trustor_org_id**](#get_billing_trusteebillingoverview_trustor_org_id) | Get the billing overview for an organization that is managed by a partner.|



## get_billing_contract

> [**BillingContract**](BillingContract) get_billing_contract(contract_id)


Get billing contract

Retrieve a single contract from the system.

get_billing_contract is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/billing/contracts/{contractId} 

Requires ANY permissions: 

* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
contract_id = 'contract_id_example' # str | The contract number.

try:
    # Get billing contract
    api_response = api_instance.get_billing_contract(contract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_contract: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contract_id** | **str**| The contract number. |  |

### Return type

[**BillingContract**](BillingContract)


## get_billing_contract_billingperiod

> [**BillingContractPeriodDetail**](BillingContractPeriodDetail) get_billing_contract_billingperiod(contract_id, billing_period_id)


Get contract billing period

Fetch the billing information for a given Organization by billing period.

get_billing_contract_billingperiod is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/billing/contracts/{contractId}/billingperiods/{billingPeriodId} 

Requires ANY permissions: 

* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
contract_id = 'contract_id_example' # str | The contract number.
billing_period_id = 'billing_period_id_example' # str | The Billing Period Id for the Org.

try:
    # Get contract billing period
    api_response = api_instance.get_billing_contract_billingperiod(contract_id, billing_period_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_contract_billingperiod: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contract_id** | **str**| The contract number. |  |
| **billing_period_id** | **str**| The Billing Period Id for the Org. |  |

### Return type

[**BillingContractPeriodDetail**](BillingContractPeriodDetail)


## get_billing_contracts

> [**BillingContractListing**](BillingContractListing) get_billing_contracts(before=before, after=after, page_size=page_size, date_start=date_start, date_end=date_end, status=status, external_number=external_number)


Get billing contracts

Retrieve a list of contracts stored in the system.

get_billing_contracts is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/billing/contracts 

Requires ANY permissions: 

* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
date_start = '2013-10-20' # date | Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
status = 'status_example' # str | Filter by the status of contracts (optional)
external_number = 'external_number_example' # str | Filter by the unique external number. (optional)

try:
    # Get billing contracts
    api_response = api_instance.get_billing_contracts(before=before, after=after, page_size=page_size, date_start=date_start, date_end=date_end, status=status, external_number=external_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_contracts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **date_start** | **date**| Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **status** | **str**| Filter by the status of contracts | [optional] <br />**Values**: Active, Inactive |
| **external_number** | **str**| Filter by the unique external number. | [optional]  |

### Return type

[**BillingContractListing**](BillingContractListing)


## get_billing_contracts_invoice_document

> [**UrlResponse**](UrlResponse) get_billing_contracts_invoice_document(invoice_id)


Get invoice document

Fetch the document for a specific invoice.

get_billing_contracts_invoice_document is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/billing/contracts/invoices/{invoiceId}/document 

Requires ANY permissions: 

* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
invoice_id = 'invoice_id_example' # str | invoiceId

try:
    # Get invoice document
    api_response = api_instance.get_billing_contracts_invoice_document(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_contracts_invoice_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **invoice_id** | **str**| invoiceId |  |

### Return type

[**UrlResponse**](UrlResponse)


## get_billing_contracts_invoice_lines

> [**BillingInvoiceItemListing**](BillingInvoiceItemListing) get_billing_contracts_invoice_lines(invoice_id, before=before, after=after, page_size=page_size)


Get invoice lines

Fetch a list of all bills for the specified account.

get_billing_contracts_invoice_lines is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/billing/contracts/invoices/{invoiceId}/lines 

Requires ANY permissions: 

* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
invoice_id = 'invoice_id_example' # str | invoiceId
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get invoice lines
    api_response = api_instance.get_billing_contracts_invoice_lines(invoice_id, before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_contracts_invoice_lines: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **invoice_id** | **str**| invoiceId |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**BillingInvoiceItemListing**](BillingInvoiceItemListing)


## get_billing_contracts_invoices

> [**BillingInvoiceListing**](BillingInvoiceListing) get_billing_contracts_invoices(before=before, after=after, page_size=page_size, date_start=date_start, date_end=date_end, payment_status=payment_status)


Get invoices

Retrieve a list of invoices stored in the system.

get_billing_contracts_invoices is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/billing/contracts/invoices 

Requires ANY permissions: 

* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
date_start = '2013-10-20' # date | Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
payment_status = 'payment_status_example' # str | Payment Status (optional)

try:
    # Get invoices
    api_response = api_instance.get_billing_contracts_invoices(before=before, after=after, page_size=page_size, date_start=date_start, date_end=date_end, payment_status=payment_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_contracts_invoices: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **date_start** | **date**| Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **payment_status** | **str**| Payment Status | [optional] <br />**Values**: Paid, UnPaid |

### Return type

[**BillingInvoiceListing**](BillingInvoiceListing)


## get_billing_reports_billableusage

> [**BillingUsageReport**](BillingUsageReport) get_billing_reports_billableusage(start_date, end_date)


Get a report of the billable license usages

Report is of the billable usages (e.g. licenses and devices utilized) for a given period. If response's status is InProgress, wait a few seconds, then try the same request again.

Wraps GET /api/v2/billing/reports/billableusage 

Requires ANY permissions: 

* billing:subscription:read
* billing:subscription:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
end_date = '2013-10-20T19:20:30+01:00' # datetime | The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

try:
    # Get a report of the billable license usages
    api_response = api_instance.get_billing_reports_billableusage(start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_reports_billableusage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_date** | **datetime**| The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **end_date** | **datetime**| The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |

### Return type

[**BillingUsageReport**](BillingUsageReport)


## get_billing_trusteebillingoverview_trustor_org_id

> [**TrusteeBillingOverview**](TrusteeBillingOverview) get_billing_trusteebillingoverview_trustor_org_id(trustor_org_id, billing_period_index=billing_period_index)


Get the billing overview for an organization that is managed by a partner.

Tax Disclaimer: Prices returned by this API do not include applicable taxes. It is the responsibility of the customer to pay all taxes that are appropriate in their jurisdiction. See the PureCloud API Documentation in the Developer Center for more information about this API: https://developer.mypurecloud.com/api/rest/v2/

Wraps GET /api/v2/billing/trusteebillingoverview/{trustorOrgId} 

Requires ANY permissions: 

* affiliateOrganization:clientBilling:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
trustor_org_id = 'trustor_org_id_example' # str | The organization ID of the trustor (customer) organization.
billing_period_index = 0 # int | 0 for active period (overview data may change until period closes). 1 for prior completed billing period. 2 for two billing cycles prior, and so on. (optional) (default to 0)

try:
    # Get the billing overview for an organization that is managed by a partner.
    api_response = api_instance.get_billing_trusteebillingoverview_trustor_org_id(trustor_org_id, billing_period_index=billing_period_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_trusteebillingoverview_trustor_org_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| The organization ID of the trustor (customer) organization. |  |
| **billing_period_index** | **int**| 0 for active period (overview data may change until period closes). 1 for prior completed billing period. 2 for two billing cycles prior, and so on. | [optional] [default to 0] |

### Return type

[**TrusteeBillingOverview**](TrusteeBillingOverview)


_PureCloudPlatformClientV2 245.0.0_
