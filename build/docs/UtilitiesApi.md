---
title: UtilitiesApi
---

## PureCloudPlatformClientV2.UtilitiesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_date**](UtilitiesApi.html#get_date) | Get the current system date/time|
|[**get_timezones**](UtilitiesApi.html#get_timezones) | Get time zones list|
|[**post_certificate_details**](UtilitiesApi.html#post_certificate_details) | Returns the information about an X509 PEM encoded certificate or certificate chain.|
{: class="table table-striped"}

<a name="get_date"></a>

## [**ServerDate**](ServerDate.html)get_date()

Get the current system date/time



Wraps GET /api/v2/date 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UtilitiesApi()

try:
    # Get the current system date/time
    api_response = api_instance.get_date()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UtilitiesApi->get_date: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ServerDate**](ServerDate.html)

<a name="get_timezones"></a>

## [**TimeZoneEntityListing**](TimeZoneEntityListing.html)get_timezones(page_size=page_size, page_number=page_number)

Get time zones list



Wraps GET /api/v2/timezones 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UtilitiesApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get time zones list
    api_response = api_instance.get_timezones(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UtilitiesApi->get_timezones: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
{: class="table table-striped"}

### Return type

[**TimeZoneEntityListing**](TimeZoneEntityListing.html)

<a name="post_certificate_details"></a>

## [**ParsedCertificate**](ParsedCertificate.html)post_certificate_details(body)

Returns the information about an X509 PEM encoded certificate or certificate chain.



Wraps POST /api/v2/certificate/details 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UtilitiesApi()
body = PureCloudPlatformClientV2.Certificate() # Certificate | Certificate

try:
    # Returns the information about an X509 PEM encoded certificate or certificate chain.
    api_response = api_instance.post_certificate_details(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UtilitiesApi->post_certificate_details: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Certificate**](Certificate.html)| Certificate | |
{: class="table table-striped"}

### Return type

[**ParsedCertificate**](ParsedCertificate.html)

