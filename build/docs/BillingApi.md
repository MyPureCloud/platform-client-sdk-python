---
title: BillingApi
---

## PureCloudPlatformClientV2.BillingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_billing_reports_billableusage**](BillingApi.html#get_billing_reports_billableusage) | Get a report of the billable usages (e.g. licenses and devices utilized) for a given period.|
{: class="table table-striped"}

<a name="get_billing_reports_billableusage"></a>

## [**BillingUsageReport**](BillingUsageReport.html) get_billing_reports_billableusage(start_date, end_date)

Get a report of the billable usages (e.g. licenses and devices utilized) for a given period.



Wraps GET /api/v2/billing/reports/billableusage 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BillingApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ
end_date = '2013-10-20T19:20:30+01:00' # datetime | The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

try:
    # Get a report of the billable usages (e.g. licenses and devices utilized) for a given period.
    api_response = api_instance.get_billing_reports_billableusage(start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BillingApi->get_billing_reports_billableusage: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_date** | **datetime**| The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ |  |
| **end_date** | **datetime**| The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ |  |
{: class="table table-striped"}

### Return type

[**BillingUsageReport**](BillingUsageReport.html)

