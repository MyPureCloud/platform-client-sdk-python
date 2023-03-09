---
title: InfrastructureAsCodeApi
---

## PureCloudPlatformClientV2.InfrastructureAsCodeApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_infrastructureascode_job**](InfrastructureAsCodeApi.html#get_infrastructureascode_job) | Get job status and results|
|[**get_infrastructureascode_jobs**](InfrastructureAsCodeApi.html#get_infrastructureascode_jobs) | Get job history|
|[**post_infrastructureascode_jobs**](InfrastructureAsCodeApi.html#post_infrastructureascode_jobs) | Create a Job|
{: class="table table-striped"}

<a name="get_infrastructureascode_job"></a>

## [**InfrastructureascodeJob**](InfrastructureascodeJob.html) get_infrastructureascode_job(job_id, details=details)



Get job status and results

Get the execution status of a submitted job, optionally including results and error details.



Wraps GET /api/v2/infrastructureascode/jobs/{jobId} 

Requires ALL permissions: 

* infrastructureascode:job:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.InfrastructureAsCodeApi()
job_id = 'job_id_example' # str | Job ID
details = False # bool | Include details of execution, including job results or error information (optional) (default to False)

try:
    # Get job status and results
    api_response = api_instance.get_infrastructureascode_job(job_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureAsCodeApi->get_infrastructureascode_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Job ID |  |
| **details** | **bool**| Include details of execution, including job results or error information | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**InfrastructureascodeJob**](InfrastructureascodeJob.html)

<a name="get_infrastructureascode_jobs"></a>

## [**InfrastructureascodeJob**](InfrastructureascodeJob.html) get_infrastructureascode_jobs(max_results=max_results, include_errors=include_errors, sort_by=sort_by, sort_order=sort_order)



Get job history

Get a history of submitted jobs, optionally including error messages.



Wraps GET /api/v2/infrastructureascode/jobs 

Requires ANY permissions: 

* infrastructureascode:job:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.InfrastructureAsCodeApi()
max_results = 1 # int | Number of jobs to show (optional) (default to 1)
include_errors = False # bool | Include error messages (optional) (default to False)
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')

try:
    # Get job history
    api_response = api_instance.get_infrastructureascode_jobs(max_results=max_results, include_errors=include_errors, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureAsCodeApi->get_infrastructureascode_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **max_results** | **int**| Number of jobs to show | [optional] [default to 1] |
| **include_errors** | **bool**| Include error messages | [optional] [default to False] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;]<br />**Values**: id, dateSubmitted, submittedBy, status |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
{: class="table table-striped"}

### Return type

[**InfrastructureascodeJob**](InfrastructureascodeJob.html)

<a name="post_infrastructureascode_jobs"></a>

## [**InfrastructureascodeJob**](InfrastructureascodeJob.html) post_infrastructureascode_jobs(body)



Create a Job

Create and submit a job for remote execution or see job planning results.



Wraps POST /api/v2/infrastructureascode/jobs 

Requires ANY permissions: 

* infrastructureascode:job:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.InfrastructureAsCodeApi()
body = PureCloudPlatformClientV2.AcceleratorInput() # AcceleratorInput | 

try:
    # Create a Job
    api_response = api_instance.post_infrastructureascode_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureAsCodeApi->post_infrastructureascode_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AcceleratorInput**](AcceleratorInput.html)|  |  |
{: class="table table-striped"}

### Return type

[**InfrastructureascodeJob**](InfrastructureascodeJob.html)

