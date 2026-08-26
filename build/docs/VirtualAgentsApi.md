# VirtualAgentsApi

## PureCloudPlatformClientV2.VirtualAgentsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_agentic_virtualagent_jobs**](#delete_agentic_virtualagent_jobs) | Start the deletion of a virtualAgent.|
|[**get_agentic_virtualagent**](#get_agentic_virtualagent) | Get virtual agent.|
|[**get_agentic_virtualagent_job**](#get_agentic_virtualagent_job) | Get a virtualAgent job.|
|[**get_agentic_virtualagents**](#get_agentic_virtualagents) | Get all virtual agents.|
|[**patch_agentic_virtualagent**](#patch_agentic_virtualagent) | Update a virtual agent.|
|[**post_agentic_virtualagent_version_jobs**](#post_agentic_virtualagent_version_jobs) | Start the publishing of a virtual agent version.|
|[**post_agentic_virtualagents**](#post_agentic_virtualagents) | Create a virtual agent.|



## delete_agentic_virtualagent_jobs

> [**AgenticVirtualAgentJob**](AgenticVirtualAgentJob) delete_agentic_virtualagent_jobs(virtual_agent_id)


Start the deletion of a virtualAgent.

Wraps DELETE /api/v2/agentic/virtualagents/{virtualAgentId}/jobs 

Requires ALL permissions: 

* agentic:virtualAgentJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
virtual_agent_id = 'virtual_agent_id_example' # str | Virtual Agent ID

try:
    # Start the deletion of a virtualAgent.
    api_response = api_instance.delete_agentic_virtualagent_jobs(virtual_agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->delete_agentic_virtualagent_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **virtual_agent_id** | **str**| Virtual Agent ID |  |

### Return type

[**AgenticVirtualAgentJob**](AgenticVirtualAgentJob)


## get_agentic_virtualagent

> [**AgenticVirtualAgent**](AgenticVirtualAgent) get_agentic_virtualagent(virtual_agent_id)


Get virtual agent.

Wraps GET /api/v2/agentic/virtualagents/{virtualAgentId} 

Requires ALL permissions: 

* agentic:virtualAgent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
virtual_agent_id = 'virtual_agent_id_example' # str | Virtual Agent ID

try:
    # Get virtual agent.
    api_response = api_instance.get_agentic_virtualagent(virtual_agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->get_agentic_virtualagent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **virtual_agent_id** | **str**| Virtual Agent ID |  |

### Return type

[**AgenticVirtualAgent**](AgenticVirtualAgent)


## get_agentic_virtualagent_job

> [**AgenticVirtualAgentJob**](AgenticVirtualAgentJob) get_agentic_virtualagent_job(virtual_agent_id, job_id)


Get a virtualAgent job.

Wraps GET /api/v2/agentic/virtualagents/{virtualAgentId}/jobs/{jobId} 

Requires ALL permissions: 

* agentic:virtualAgentJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
virtual_agent_id = 'virtual_agent_id_example' # str | Virtual Agent ID
job_id = 'job_id_example' # str | jobId

try:
    # Get a virtualAgent job.
    api_response = api_instance.get_agentic_virtualagent_job(virtual_agent_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->get_agentic_virtualagent_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **virtual_agent_id** | **str**| Virtual Agent ID |  |
| **job_id** | **str**| jobId |  |

### Return type

[**AgenticVirtualAgentJob**](AgenticVirtualAgentJob)


## get_agentic_virtualagents

> [**AgenticVirtualAgentEntityListing**](AgenticVirtualAgentEntityListing) get_agentic_virtualagents(name=name, name_contains=name_contains, status=status, sort_by=sort_by, sort_order=sort_order, page_number=page_number, page_size=page_size)


Get all virtual agents.

Wraps GET /api/v2/agentic/virtualagents 

Requires ALL permissions: 

* agentic:virtualAgent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
name = 'name_example' # str | Filter by matching name - case insensitive. (optional)
name_contains = 'name_contains_example' # str | Filter by name contains - case insensitive. (optional)
status = 'status_example' # str | Filter by status. (optional)
sort_by = ''dateModified'' # str | Sort by. Default value dateModified. (optional) (default to 'dateModified')
sort_order = ''desc'' # str | Sort Order. Default value desc. (optional) (default to 'desc')
page_number = 1 # int | Page number. (optional) (default to 1)
page_size = 25 # int | Page size. The maximum page size is 100. (optional) (default to 25)

try:
    # Get all virtual agents.
    api_response = api_instance.get_agentic_virtualagents(name=name, name_contains=name_contains, status=status, sort_by=sort_by, sort_order=sort_order, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->get_agentic_virtualagents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Filter by matching name - case insensitive. | [optional]  |
| **name_contains** | **str**| Filter by name contains - case insensitive. | [optional]  |
| **status** | **str**| Filter by status. | [optional] <br />**Values**: Draft, Published |
| **sort_by** | **str**| Sort by. Default value dateModified. | [optional] [default to &#39;dateModified&#39;]<br />**Values**: dateModified, name, status |
| **sort_order** | **str**| Sort Order. Default value desc. | [optional] [default to &#39;desc&#39;]<br />**Values**: asc, desc |
| **page_number** | **int**| Page number. | [optional] [default to 1] |
| **page_size** | **int**| Page size. The maximum page size is 100. | [optional] [default to 25] |

### Return type

[**AgenticVirtualAgentEntityListing**](AgenticVirtualAgentEntityListing)


## patch_agentic_virtualagent

> [**AgenticVirtualAgent**](AgenticVirtualAgent) patch_agentic_virtualagent(virtual_agent_id, body)


Update a virtual agent.

Wraps PATCH /api/v2/agentic/virtualagents/{virtualAgentId} 

Requires ALL permissions: 

* agentic:virtualAgent:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
virtual_agent_id = 'virtual_agent_id_example' # str | Virtual Agent ID
body = PureCloudPlatformClientV2.UpdateAgenticVirtualAgent() # UpdateAgenticVirtualAgent | 

try:
    # Update a virtual agent.
    api_response = api_instance.patch_agentic_virtualagent(virtual_agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->patch_agentic_virtualagent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **virtual_agent_id** | **str**| Virtual Agent ID |  |
| **body** | [**UpdateAgenticVirtualAgent**](UpdateAgenticVirtualAgent)|  |  |

### Return type

[**AgenticVirtualAgent**](AgenticVirtualAgent)


## post_agentic_virtualagent_version_jobs

> [**AgenticVirtualAgentVersionPublishJob**](AgenticVirtualAgentVersionPublishJob) post_agentic_virtualagent_version_jobs(virtual_agent_id, version_id, body)


Start the publishing of a virtual agent version.

Wraps POST /api/v2/agentic/virtualagents/{virtualAgentId}/versions/{versionId}/jobs 

Requires ALL permissions: 

* agentic:virtualAgentVersionJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
virtual_agent_id = 'virtual_agent_id_example' # str | Virtual Agent ID
version_id = 'version_id_example' # str | Version ID
body = PureCloudPlatformClientV2.AgenticVirtualAgentVersionPublishJobRequest() # AgenticVirtualAgentVersionPublishJobRequest | 

try:
    # Start the publishing of a virtual agent version.
    api_response = api_instance.post_agentic_virtualagent_version_jobs(virtual_agent_id, version_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->post_agentic_virtualagent_version_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **virtual_agent_id** | **str**| Virtual Agent ID |  |
| **version_id** | **str**| Version ID |  |
| **body** | [**AgenticVirtualAgentVersionPublishJobRequest**](AgenticVirtualAgentVersionPublishJobRequest)|  |  |

### Return type

[**AgenticVirtualAgentVersionPublishJob**](AgenticVirtualAgentVersionPublishJob)


## post_agentic_virtualagents

> [**AgenticVirtualAgent**](AgenticVirtualAgent) post_agentic_virtualagents(body)


Create a virtual agent.

Wraps POST /api/v2/agentic/virtualagents 

Requires ALL permissions: 

* agentic:virtualAgent:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VirtualAgentsApi()
body = PureCloudPlatformClientV2.CreateAgenticVirtualAgent() # CreateAgenticVirtualAgent | 

try:
    # Create a virtual agent.
    api_response = api_instance.post_agentic_virtualagents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAgentsApi->post_agentic_virtualagents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateAgenticVirtualAgent**](CreateAgenticVirtualAgent)|  |  |

### Return type

[**AgenticVirtualAgent**](AgenticVirtualAgent)


_PureCloudPlatformClientV2 265.0.0_
