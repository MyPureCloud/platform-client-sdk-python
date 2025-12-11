# InfrastructureAsCodeApi

## PureCloudPlatformClientV2.InfrastructureAsCodeApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_infrastructureascode_accelerator**](#get_infrastructureascode_accelerator) | Get information about an accelerator|
|[**get_infrastructureascode_accelerators**](#get_infrastructureascode_accelerators) | Get a list of available accelerators|
|[**get_infrastructureascode_job**](#get_infrastructureascode_job) | Get job status and results|
|[**get_infrastructureascode_jobs**](#get_infrastructureascode_jobs) | Get job history|
|[**post_infrastructureascode_jobs**](#post_infrastructureascode_jobs) | Create a Job|



## get_infrastructureascode_accelerator

> [**AcceleratorSpecification**](AcceleratorSpecification) get_infrastructureascode_accelerator(accelerator_id, preferred_language=preferred_language)


Get information about an accelerator

Get the complete metadata specification for an accelerator, including requirements and parameters.

Wraps GET /api/v2/infrastructureascode/accelerators/{acceleratorId} 

Requires ANY permissions: 

* infrastructureascode:accelerator:view

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
accelerator_id = 'accelerator_id_example' # str | Accelerator ID
preferred_language = ''en-US'' # str | Preferred Language (optional) (default to 'en-US')

try:
    # Get information about an accelerator
    api_response = api_instance.get_infrastructureascode_accelerator(accelerator_id, preferred_language=preferred_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureAsCodeApi->get_infrastructureascode_accelerator: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accelerator_id** | **str**| Accelerator ID |  |
| **preferred_language** | **str**| Preferred Language | [optional] [default to &#39;en-US&#39;]<br />**Values**: ar, cs, da, de, en-US, es, fi, fr, it, iw, ko, ja, nl, no, pl, pt-BR, pt-PT, sv, th, tr, zh-CN, zh-TW |

### Return type

[**AcceleratorSpecification**](AcceleratorSpecification)


## get_infrastructureascode_accelerators

> [**AcceleratorList**](AcceleratorList) get_infrastructureascode_accelerators(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, description=description, origin=origin, type=type, classification=classification, tags=tags)


Get a list of available accelerators

Search for accelerators that can be run.

Wraps GET /api/v2/infrastructureascode/accelerators 

Requires ANY permissions: 

* infrastructureascode:accelerator:view

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
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
name = 'name_example' # str | Filter by name (optional)
description = 'description_example' # str | Filter by description (optional)
origin = 'origin_example' # str | Filter by origin (optional)
type = 'type_example' # str | Filter by type (optional)
classification = 'classification_example' # str | Filter by classification (optional)
tags = 'tags_example' # str | Filter by tags (optional)

try:
    # Get a list of available accelerators
    api_response = api_instance.get_infrastructureascode_accelerators(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, description=description, origin=origin, type=type, classification=classification, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureAsCodeApi->get_infrastructureascode_accelerators: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **name** | **str**| Filter by name | [optional]  |
| **description** | **str**| Filter by description | [optional]  |
| **origin** | **str**| Filter by origin | [optional] <br />**Values**: community, partner, genesys |
| **type** | **str**| Filter by type | [optional] <br />**Values**: module, accelerator, blueprint |
| **classification** | **str**| Filter by classification | [optional]  |
| **tags** | **str**| Filter by tags | [optional]  |

### Return type

[**AcceleratorList**](AcceleratorList)


## get_infrastructureascode_job

> [**InfrastructureascodeJob**](InfrastructureascodeJob) get_infrastructureascode_job(job_id, details=details)


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

### Return type

[**InfrastructureascodeJob**](InfrastructureascodeJob)


## get_infrastructureascode_jobs

> [**InfrastructureascodeJob**](InfrastructureascodeJob) get_infrastructureascode_jobs(max_results=max_results, include_errors=include_errors, sort_by=sort_by, sort_order=sort_order, accelerator_id=accelerator_id, submitted_by=submitted_by, status=status)


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
sort_by = ''dateSubmitted'' # str | Sort by (optional) (default to 'dateSubmitted')
sort_order = ''desc'' # str | Sort order (optional) (default to 'desc')
accelerator_id = 'accelerator_id_example' # str | Find only jobs associated with this accelerator (optional)
submitted_by = 'submitted_by_example' # str | Find only jobs submitted by this user (optional)
status = 'status_example' # str | Find only jobs in this state (optional)

try:
    # Get job history
    api_response = api_instance.get_infrastructureascode_jobs(max_results=max_results, include_errors=include_errors, sort_by=sort_by, sort_order=sort_order, accelerator_id=accelerator_id, submitted_by=submitted_by, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureAsCodeApi->get_infrastructureascode_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **max_results** | **int**| Number of jobs to show | [optional] [default to 1] |
| **include_errors** | **bool**| Include error messages | [optional] [default to False] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;dateSubmitted&#39;]<br />**Values**: id, dateSubmitted, submittedBy, acceleratorId, status |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;desc&#39;]<br />**Values**: asc, desc |
| **accelerator_id** | **str**| Find only jobs associated with this accelerator | [optional]  |
| **submitted_by** | **str**| Find only jobs submitted by this user | [optional]  |
| **status** | **str**| Find only jobs in this state | [optional] <br />**Values**: Created, Queued, Running, Complete, Failed, Incomplete |

### Return type

[**InfrastructureascodeJob**](InfrastructureascodeJob)


## post_infrastructureascode_jobs

> [**InfrastructureascodeJob**](InfrastructureascodeJob) post_infrastructureascode_jobs(body)


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
| **body** | [**AcceleratorInput**](AcceleratorInput)|  |  |

### Return type

[**InfrastructureascodeJob**](InfrastructureascodeJob)


_PureCloudPlatformClientV2 246.0.0_
