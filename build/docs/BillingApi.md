---
title: BillingApi
---

## PureCloudPlatformClientV2.BillingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_billing_reports_billableusage**](BillingApi.html#get_billing_reports_billableusage) | Get a report of the billable license usages|
|[**get_billing_trusteebillingoverview_trustor_org_id**](BillingApi.html#get_billing_trusteebillingoverview_trustor_org_id) | Get the billing overview for an organization that is managed by a partner.|
{: class="table table-striped"}

<a name="get_billing_reports_billableusage"></a>

## [**BillingUsageReport**](BillingUsageReport.html) get_billing_reports_billableusage(start_date, end_date)



Get a report of the billable license usages

Report is of the billable usages (e.g. licenses and devices utilized) for a given period. If response's status is InProgress, wait a few seconds, then try the same request again.

Wraps GET /api/v2/billing/reports/billableusage 

Requires ANY permissions: 

* billing:subscription:read
* billing:subscription:view
* billing:subscription:create
* billing:subscription:add

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
start_date = '2013-10-20T19:20:30+01:00' # datetime | The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ
end_date = '2013-10-20T19:20:30+01:00' # datetime | The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

try:
    # Get a report of the billable license usages
    api_response = api_instance.get_billing_reports_billableusage(start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BillingApi->get_billing_reports_billableusage: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_date** | **datetime**| The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ |  |
| **end_date** | **datetime**| The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ |  |
{: class="table table-striped"}

### Return type

[**BillingUsageReport**](BillingUsageReport.html)

<a name="get_billing_trusteebillingoverview_trustor_org_id"></a>

## [**TrusteeBillingOverview**](TrusteeBillingOverview.html) get_billing_trusteebillingoverview_trustor_org_id(trustor_org_id, billing_period_index=billing_period_index)



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
    print "Exception when calling BillingApi->get_billing_trusteebillingoverview_trustor_org_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| The organization ID of the trustor (customer) organization. |  |
| **billing_period_index** | **int**| 0 for active period (overview data may change until period closes). 1 for prior completed billing period. 2 for two billing cycles prior, and so on. | [optional] [default to 0] |
{: class="table table-striped"}

### Return type

[**TrusteeBillingOverview**](TrusteeBillingOverview.html)

