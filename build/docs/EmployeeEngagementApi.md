---
title: EmployeeEngagementApi
---

## PureCloudPlatformClientV2.EmployeeEngagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_employeeengagement_celebration**](EmployeeEngagementApi.html#delete_employeeengagement_celebration) | Deletes a celebration|
|[**get_employeeengagement_celebrations**](EmployeeEngagementApi.html#get_employeeengagement_celebrations) | Get all celebrations|
|[**get_employeeengagement_recognition**](EmployeeEngagementApi.html#get_employeeengagement_recognition) | Gets a single recognition|
|[**patch_employeeengagement_celebration**](EmployeeEngagementApi.html#patch_employeeengagement_celebration) | Set a state for a celebration|
|[**post_employeeengagement_recognitions**](EmployeeEngagementApi.html#post_employeeengagement_recognitions) | Creates a recognition|
{: class="table table-striped"}

<a name="delete_employeeengagement_celebration"></a>

##  delete_employeeengagement_celebration(celebration_id)



Deletes a celebration

Wraps DELETE /api/v2/employeeengagement/celebrations/{celebrationId} 

Requires ANY permissions: 

* engagement:celebration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmployeeEngagementApi()
celebration_id = 'celebration_id_example' # str | The ID of the celebration

try:
    # Deletes a celebration
    api_instance.delete_employeeengagement_celebration(celebration_id)
except ApiException as e:
    print("Exception when calling EmployeeEngagementApi->delete_employeeengagement_celebration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **celebration_id** | **str**| The ID of the celebration |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_employeeengagement_celebrations"></a>

## [**GetCelebrationListing**](GetCelebrationListing.html) get_employeeengagement_celebrations(page_number=page_number, page_size=page_size)



Get all celebrations

Wraps GET /api/v2/employeeengagement/celebrations 

Requires ANY permissions: 

* engagement:celebration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmployeeEngagementApi()
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)

try:
    # Get all celebrations
    api_response = api_instance.get_employeeengagement_celebrations(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeEngagementApi->get_employeeengagement_celebrations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**GetCelebrationListing**](GetCelebrationListing.html)

<a name="get_employeeengagement_recognition"></a>

## [**Recognition**](Recognition.html) get_employeeengagement_recognition(recognition_id)



Gets a single recognition

Wraps GET /api/v2/employeeengagement/recognitions/{recognitionId} 

Requires ANY permissions: 

* engagement:recognition:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmployeeEngagementApi()
recognition_id = 'recognition_id_example' # str | The Recognition ID

try:
    # Gets a single recognition
    api_response = api_instance.get_employeeengagement_recognition(recognition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeEngagementApi->get_employeeengagement_recognition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recognition_id** | **str**| The Recognition ID |  |
{: class="table table-striped"}

### Return type

[**Recognition**](Recognition.html)

<a name="patch_employeeengagement_celebration"></a>

##  patch_employeeengagement_celebration(celebration_id, body)



Set a state for a celebration

Wraps PATCH /api/v2/employeeengagement/celebrations/{celebrationId} 

Requires ANY permissions: 

* engagement:celebration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmployeeEngagementApi()
celebration_id = 'celebration_id_example' # str | The ID of the celebration
body = PureCloudPlatformClientV2.CelebrationStateParam() # CelebrationStateParam | Patch Celebration state

try:
    # Set a state for a celebration
    api_instance.patch_employeeengagement_celebration(celebration_id, body)
except ApiException as e:
    print("Exception when calling EmployeeEngagementApi->patch_employeeengagement_celebration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **celebration_id** | **str**| The ID of the celebration |  |
| **body** | [**CelebrationStateParam**](CelebrationStateParam.html)| Patch Celebration state |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_employeeengagement_recognitions"></a>

## [**RecognitionBase**](RecognitionBase.html) post_employeeengagement_recognitions(body)



Creates a recognition

Wraps POST /api/v2/employeeengagement/recognitions 

Requires ANY permissions: 

* engagement:recognition:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmployeeEngagementApi()
body = PureCloudPlatformClientV2.CreateRecognition() # CreateRecognition | Create Recognition

try:
    # Creates a recognition
    api_response = api_instance.post_employeeengagement_recognitions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeEngagementApi->post_employeeengagement_recognitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateRecognition**](CreateRecognition.html)| Create Recognition |  |
{: class="table table-striped"}

### Return type

[**RecognitionBase**](RecognitionBase.html)

