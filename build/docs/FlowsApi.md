---
title: FlowsApi
---

## PureCloudPlatformClientV2.FlowsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_analytics_flows_aggregates_job**](FlowsApi.html#get_analytics_flows_aggregates_job) | Get status for async query for Flow aggregates|
|[**get_analytics_flows_aggregates_job_results**](FlowsApi.html#get_analytics_flows_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**post_analytics_flows_activity_query**](FlowsApi.html#post_analytics_flows_activity_query) | Query for flow activity observations|
|[**post_analytics_flows_aggregates_jobs**](FlowsApi.html#post_analytics_flows_aggregates_jobs) | Query for flow aggregates asynchronously|
|[**post_analytics_flows_aggregates_query**](FlowsApi.html#post_analytics_flows_aggregates_query) | Query for flow aggregates|
|[**post_analytics_flows_observations_query**](FlowsApi.html#post_analytics_flows_observations_query) | Query for flow observations|
{: class="table table-striped"}

<a name="get_analytics_flows_aggregates_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_flows_aggregates_job(job_id)



Get status for async query for Flow aggregates

get_analytics_flows_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/flows/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:flowAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for Flow aggregates
    api_response = api_instance.get_analytics_flows_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlowsApi->get_analytics_flows_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_flows_aggregates_job_results"></a>

## [**FlowAsyncAggregateQueryResponse**](FlowAsyncAggregateQueryResponse.html) get_analytics_flows_aggregates_job_results(job_id, cursor=cursor)



Fetch a page of results for an async aggregates query

get_analytics_flows_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/flows/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:flowAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_flows_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlowsApi->get_analytics_flows_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowAsyncAggregateQueryResponse**](FlowAsyncAggregateQueryResponse.html)

<a name="post_analytics_flows_activity_query"></a>

## [**FlowActivityResponse**](FlowActivityResponse.html) post_analytics_flows_activity_query(body, page_size=page_size, page_number=page_number)



Query for flow activity observations

Wraps POST /api/v2/analytics/flows/activity/query 

Requires ANY permissions: 

* analytics:flowObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
body = PureCloudPlatformClientV2.FlowActivityQuery() # FlowActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for flow activity observations
    api_response = api_instance.post_analytics_flows_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlowsApi->post_analytics_flows_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowActivityQuery**](FlowActivityQuery.html)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowActivityResponse**](FlowActivityResponse.html)

<a name="post_analytics_flows_aggregates_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_flows_aggregates_jobs(body)



Query for flow aggregates asynchronously

post_analytics_flows_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/flows/aggregates/jobs 

Requires ANY permissions: 

* analytics:flowAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
body = PureCloudPlatformClientV2.FlowAsyncAggregationQuery() # FlowAsyncAggregationQuery | query

try:
    # Query for flow aggregates asynchronously
    api_response = api_instance.post_analytics_flows_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlowsApi->post_analytics_flows_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowAsyncAggregationQuery**](FlowAsyncAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_flows_aggregates_query"></a>

## [**FlowAggregateQueryResponse**](FlowAggregateQueryResponse.html) post_analytics_flows_aggregates_query(body)



Query for flow aggregates

Wraps POST /api/v2/analytics/flows/aggregates/query 

Requires ANY permissions: 

* analytics:flowAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
body = PureCloudPlatformClientV2.FlowAggregationQuery() # FlowAggregationQuery | query

try:
    # Query for flow aggregates
    api_response = api_instance.post_analytics_flows_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlowsApi->post_analytics_flows_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowAggregationQuery**](FlowAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**FlowAggregateQueryResponse**](FlowAggregateQueryResponse.html)

<a name="post_analytics_flows_observations_query"></a>

## [**FlowObservationQueryResponse**](FlowObservationQueryResponse.html) post_analytics_flows_observations_query(body)



Query for flow observations

Wraps POST /api/v2/analytics/flows/observations/query 

Requires ANY permissions: 

* analytics:flowObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
body = PureCloudPlatformClientV2.FlowObservationQuery() # FlowObservationQuery | query

try:
    # Query for flow observations
    api_response = api_instance.post_analytics_flows_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlowsApi->post_analytics_flows_observations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowObservationQuery**](FlowObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**FlowObservationQueryResponse**](FlowObservationQueryResponse.html)

