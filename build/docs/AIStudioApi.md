# AIStudioApi

## PureCloudPlatformClientV2.AIStudioApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_guide_jobs**](#delete_guide_jobs) | Start the deletion of a guide.|
|[**get_guide**](#get_guide) | Get guide.|
|[**get_guide_job**](#get_guide_job) | Get the specified guide deletion job.|
|[**get_guide_version**](#get_guide_version) | Get a guide version.|
|[**get_guide_version_job**](#get_guide_version_job) | Get the status of the publishing job for this guide version.|
|[**get_guides**](#get_guides) | Get all guides.|
|[**get_guides_job**](#get_guides_job) | Get the status of the guide content generation job.|
|[**patch_guide**](#patch_guide) | Update a guide.|
|[**patch_guide_version**](#patch_guide_version) | Update a guide version.|
|[**post_guide_version_jobs**](#post_guide_version_jobs) | Start the publishing of a guide version.|
|[**post_guide_versions**](#post_guide_versions) | Create a guide version.|
|[**post_guides**](#post_guides) | Create a guide.|
|[**post_guides_jobs**](#post_guides_jobs) | Start a guide content generation job.|



## delete_guide_jobs

> [**GuideJob**](GuideJob) delete_guide_jobs(guide_id)


Start the deletion of a guide.

delete_guide_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/guides/{guideId}/jobs 

Requires ALL permissions: 

* aiStudio:guideJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID

try:
    # Start the deletion of a guide.
    api_response = api_instance.delete_guide_jobs(guide_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->delete_guide_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |

### Return type

[**GuideJob**](GuideJob)


## get_guide

> [**Guide**](Guide) get_guide(guide_id)


Get guide.

get_guide is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/guides/{guideId} 

Requires ALL permissions: 

* aiStudio:guide:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID

try:
    # Get guide.
    api_response = api_instance.get_guide(guide_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->get_guide: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |

### Return type

[**Guide**](Guide)


## get_guide_job

> [**GuideJob**](GuideJob) get_guide_job(guide_id, job_id)


Get the specified guide deletion job.

get_guide_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/guides/{guideId}/jobs/{jobId} 

Requires ALL permissions: 

* aiStudio:guideJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
job_id = 'job_id_example' # str | jobId

try:
    # Get the specified guide deletion job.
    api_response = api_instance.get_guide_job(guide_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->get_guide_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **job_id** | **str**| jobId |  |

### Return type

[**GuideJob**](GuideJob)


## get_guide_version

> [**GuideVersion**](GuideVersion) get_guide_version(guide_id, version_id)


Get a guide version.

get_guide_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/guides/{guideId}/versions/{versionId} 

Requires ALL permissions: 

* aiStudio:guideVersion:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
version_id = 'version_id_example' # str | Version ID

try:
    # Get a guide version.
    api_response = api_instance.get_guide_version(guide_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->get_guide_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **version_id** | **str**| Version ID |  |

### Return type

[**GuideVersion**](GuideVersion)


## get_guide_version_job

> [**GuideVersionPublishJob**](GuideVersionPublishJob) get_guide_version_job(guide_id, version_id, job_id)


Get the status of the publishing job for this guide version.

get_guide_version_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/guides/{guideId}/versions/{versionId}/jobs/{jobId} 

Requires ALL permissions: 

* aiStudio:guideVersionJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
version_id = 'version_id_example' # str | Version ID
job_id = 'job_id_example' # str | jobId

try:
    # Get the status of the publishing job for this guide version.
    api_response = api_instance.get_guide_version_job(guide_id, version_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->get_guide_version_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **version_id** | **str**| Version ID |  |
| **job_id** | **str**| jobId |  |

### Return type

[**GuideVersionPublishJob**](GuideVersionPublishJob)


## get_guides

> [**GuideEntityListing**](GuideEntityListing) get_guides(name=name, name_contains=name_contains, status=status, sort_by=sort_by, sort_order=sort_order, page_number=page_number, page_size=page_size)


Get all guides.

get_guides is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/guides 

Requires ALL permissions: 

* aiStudio:guide:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
name = 'name_example' # str | Filter by matching name - case insensitive. (optional)
name_contains = 'name_contains_example' # str | Filter by name contains - case insensitive. (optional)
status = 'status_example' # str | Filter by status. (optional)
sort_by = ''dateModified'' # str | Sort by. Default value dateModified. (optional) (default to 'dateModified')
sort_order = ''desc'' # str | Sort Order. Default value desc. (optional) (default to 'desc')
page_number = 1 # int | Page number. (optional) (default to 1)
page_size = 25 # int | Page size. The maximum page size is 100. (optional) (default to 25)

try:
    # Get all guides.
    api_response = api_instance.get_guides(name=name, name_contains=name_contains, status=status, sort_by=sort_by, sort_order=sort_order, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->get_guides: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Filter by matching name - case insensitive. | [optional]  |
| **name_contains** | **str**| Filter by name contains - case insensitive. | [optional]  |
| **status** | **str**| Filter by status. | [optional] <br />**Values**: Published, Draft |
| **sort_by** | **str**| Sort by. Default value dateModified. | [optional] [default to &#39;dateModified&#39;]<br />**Values**: dateModified, name, status |
| **sort_order** | **str**| Sort Order. Default value desc. | [optional] [default to &#39;desc&#39;]<br />**Values**: asc, desc |
| **page_number** | **int**| Page number. | [optional] [default to 1] |
| **page_size** | **int**| Page size. The maximum page size is 100. | [optional] [default to 25] |

### Return type

[**GuideEntityListing**](GuideEntityListing)


## get_guides_job

> [**GuideContentGenerationJob**](GuideContentGenerationJob) get_guides_job(job_id)


Get the status of the guide content generation job.

get_guides_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/guides/jobs/{jobId} 

Requires ALL permissions: 

* aiStudio:guideJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get the status of the guide content generation job.
    api_response = api_instance.get_guides_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->get_guides_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**GuideContentGenerationJob**](GuideContentGenerationJob)


## patch_guide

> [**Guide**](Guide) patch_guide(guide_id, body)


Update a guide.

patch_guide is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/guides/{guideId} 

Requires ALL permissions: 

* aiStudio:guide:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
body = PureCloudPlatformClientV2.UpdateGuide() # UpdateGuide | 

try:
    # Update a guide.
    api_response = api_instance.patch_guide(guide_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->patch_guide: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **body** | [**UpdateGuide**](UpdateGuide)|  |  |

### Return type

[**Guide**](Guide)


## patch_guide_version

> [**GuideVersion**](GuideVersion) patch_guide_version(guide_id, version_id, body)


Update a guide version.

patch_guide_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/guides/{guideId}/versions/{versionId} 

Requires ALL permissions: 

* aiStudio:guideVersion:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
version_id = 'version_id_example' # str | Version ID
body = PureCloudPlatformClientV2.UpdateGuideVersion() # UpdateGuideVersion | 

try:
    # Update a guide version.
    api_response = api_instance.patch_guide_version(guide_id, version_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->patch_guide_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **version_id** | **str**| Version ID |  |
| **body** | [**UpdateGuideVersion**](UpdateGuideVersion)|  |  |

### Return type

[**GuideVersion**](GuideVersion)


## post_guide_version_jobs

> [**GuideVersionPublishJob**](GuideVersionPublishJob) post_guide_version_jobs(guide_id, version_id, body)


Start the publishing of a guide version.

post_guide_version_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/guides/{guideId}/versions/{versionId}/jobs 

Requires ALL permissions: 

* aiStudio:guideVersionJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
version_id = 'version_id_example' # str | Version ID
body = PureCloudPlatformClientV2.GuideVersionPublishJobRequest() # GuideVersionPublishJobRequest | 

try:
    # Start the publishing of a guide version.
    api_response = api_instance.post_guide_version_jobs(guide_id, version_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->post_guide_version_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **version_id** | **str**| Version ID |  |
| **body** | [**GuideVersionPublishJobRequest**](GuideVersionPublishJobRequest)|  |  |

### Return type

[**GuideVersionPublishJob**](GuideVersionPublishJob)


## post_guide_versions

> [**GuideVersion**](GuideVersion) post_guide_versions(guide_id, body=body)


Create a guide version.

post_guide_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/guides/{guideId}/versions 

Requires ALL permissions: 

* aiStudio:guideVersion:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
guide_id = 'guide_id_example' # str | Guide ID
body = PureCloudPlatformClientV2.CreateGuideVersion() # CreateGuideVersion |  (optional)

try:
    # Create a guide version.
    api_response = api_instance.post_guide_versions(guide_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->post_guide_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **guide_id** | **str**| Guide ID |  |
| **body** | [**CreateGuideVersion**](CreateGuideVersion)|  | [optional]  |

### Return type

[**GuideVersion**](GuideVersion)


## post_guides

> [**Guide**](Guide) post_guides(body)


Create a guide.

post_guides is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/guides 

Requires ALL permissions: 

* aiStudio:guide:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
body = PureCloudPlatformClientV2.CreateGuide() # CreateGuide | 

try:
    # Create a guide.
    api_response = api_instance.post_guides(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->post_guides: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateGuide**](CreateGuide)|  |  |

### Return type

[**Guide**](Guide)


## post_guides_jobs

> [**GuideContentGenerationJob**](GuideContentGenerationJob) post_guides_jobs(body)


Start a guide content generation job.

post_guides_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/guides/jobs 

Requires ALL permissions: 

* aiStudio:guideJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AIStudioApi()
body = PureCloudPlatformClientV2.GenerateGuideContentRequest() # GenerateGuideContentRequest | 

try:
    # Start a guide content generation job.
    api_response = api_instance.post_guides_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIStudioApi->post_guides_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GenerateGuideContentRequest**](GenerateGuideContentRequest)|  |  |

### Return type

[**GuideContentGenerationJob**](GuideContentGenerationJob)


_PureCloudPlatformClientV2 235.0.0_
