---
title: LearningApi
---

## PureCloudPlatformClientV2.LearningApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_learning_assignment**](LearningApi.html#delete_learning_assignment) | Delete a learning assignment|
|[**delete_learning_module**](LearningApi.html#delete_learning_module) | Delete a learning module|
|[**get_learning_assignment**](LearningApi.html#get_learning_assignment) | Get Learning Assignment|
|[**get_learning_assignment_step**](LearningApi.html#get_learning_assignment_step) | Get Learning Assignment Step|
|[**get_learning_assignments**](LearningApi.html#get_learning_assignments) | List of Learning module Assignments|
|[**get_learning_assignments_me**](LearningApi.html#get_learning_assignments_me) | List of Learning Assignments assigned to current user|
|[**get_learning_module**](LearningApi.html#get_learning_module) | Get a learning module|
|[**get_learning_module_job**](LearningApi.html#get_learning_module_job) | Get a specific Learning Module job status|
|[**get_learning_module_preview**](LearningApi.html#get_learning_module_preview) | Get a learning module preview|
|[**get_learning_module_rule**](LearningApi.html#get_learning_module_rule) | Get a learning module rule|
|[**get_learning_module_version**](LearningApi.html#get_learning_module_version) | Get specific version of a published module|
|[**get_learning_modules**](LearningApi.html#get_learning_modules) | Get all learning modules of an organization|
|[**get_learning_modules_assignments**](LearningApi.html#get_learning_modules_assignments) | Get all learning modules of an organization including assignments for a specific user|
|[**get_learning_modules_coverart_cover_art_id**](LearningApi.html#get_learning_modules_coverart_cover_art_id) | Get a specific Learning Module cover art using ID|
|[**get_learning_scorm_scorm_id**](LearningApi.html#get_learning_scorm_scorm_id) | Get Learning SCORM Result|
|[**patch_learning_assignment**](LearningApi.html#patch_learning_assignment) | Update Learning Assignment|
|[**patch_learning_assignment_reschedule**](LearningApi.html#patch_learning_assignment_reschedule) | Reschedule Learning Assignment|
|[**patch_learning_assignment_step**](LearningApi.html#patch_learning_assignment_step) | Update Learning Assignment Step|
|[**patch_learning_module_user_assignments**](LearningApi.html#patch_learning_module_user_assignments) | Update an external assignment for a specific user|
|[**post_learning_assessments_scoring**](LearningApi.html#post_learning_assessments_scoring) | Score learning assessment for preview|
|[**post_learning_assignment_reassign**](LearningApi.html#post_learning_assignment_reassign) | Reassign Learning Assignment|
|[**post_learning_assignment_reset**](LearningApi.html#post_learning_assignment_reset) | Reset Learning Assignment|
|[**post_learning_assignments**](LearningApi.html#post_learning_assignments) | Create Learning Assignment|
|[**post_learning_assignments_aggregates_query**](LearningApi.html#post_learning_assignments_aggregates_query) | Retrieve aggregated assignment data|
|[**post_learning_assignments_bulkadd**](LearningApi.html#post_learning_assignments_bulkadd) | Add multiple learning assignments|
|[**post_learning_assignments_bulkremove**](LearningApi.html#post_learning_assignments_bulkremove) | Remove multiple Learning Assignments|
|[**post_learning_module_jobs**](LearningApi.html#post_learning_module_jobs) | Starts a specified operation on learning module|
|[**post_learning_module_publish**](LearningApi.html#post_learning_module_publish) | Publish a Learning module|
|[**post_learning_modules**](LearningApi.html#post_learning_modules) | Create a new learning module|
|[**post_learning_rules_query**](LearningApi.html#post_learning_rules_query) | Get users for learning module rule|
|[**post_learning_scheduleslots_query**](LearningApi.html#post_learning_scheduleslots_query) | Get list of possible slots where a learning activity can be scheduled.|
|[**post_learning_scorm**](LearningApi.html#post_learning_scorm) | Create a SCORM package upload request|
|[**put_learning_module**](LearningApi.html#put_learning_module) | Update a learning module|
|[**put_learning_module_preview**](LearningApi.html#put_learning_module_preview) | Update a learning module preview|
|[**put_learning_module_rule**](LearningApi.html#put_learning_module_rule) | Update a learning module rule|
{: class="table table-striped"}

<a name="delete_learning_assignment"></a>

##  delete_learning_assignment(assignment_id)



Delete a learning assignment

Wraps DELETE /api/v2/learning/assignments/{assignmentId} 

Requires ANY permissions: 

* learning:assignment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The Learning Assignment ID

try:
    # Delete a learning assignment
    api_instance.delete_learning_assignment(assignment_id)
except ApiException as e:
    print("Exception when calling LearningApi->delete_learning_assignment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The Learning Assignment ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_learning_module"></a>

##  delete_learning_module(module_id)



Delete a learning module

This will delete a learning module if it is unpublished or it will delete a published and archived learning module

Wraps DELETE /api/v2/learning/modules/{moduleId} 

Requires ANY permissions: 

* learning:module:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module

try:
    # Delete a learning module
    api_instance.delete_learning_module(module_id)
except ApiException as e:
    print("Exception when calling LearningApi->delete_learning_module: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_learning_assignment"></a>

## [**LearningAssignment**](LearningAssignment.html) get_learning_assignment(assignment_id, expand=expand)



Get Learning Assignment

Permission not required if you are the assigned user of the learning assignment

Wraps GET /api/v2/learning/assignments/{assignmentId} 

Requires ANY permissions: 

* learning:assignment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The ID of Learning Assignment
expand = ['expand_example'] # list[str] | Fields to expand in response (optional)

try:
    # Get Learning Assignment
    api_response = api_instance.get_learning_assignment(assignment_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_assignment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The ID of Learning Assignment |  |
| **expand** | [**list[str]**](str.html)| Fields to expand in response | [optional] <br />**Values**: module, assessment, assessmentForm, module.coverArt, step, step.moduleStep |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="get_learning_assignment_step"></a>

## [**LearningAssignmentStep**](LearningAssignmentStep.html) get_learning_assignment_step(assignment_id, step_id, shareable_content_object_id=shareable_content_object_id, default_shareable_content_object=default_shareable_content_object, expand=expand)



Get Learning Assignment Step

Permission not required if you are the assigned user of the learning assignment

Wraps GET /api/v2/learning/assignments/{assignmentId}/steps/{stepId} 

Requires ANY permissions: 

* learning:assignment:viewOwn

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The ID of Learning Assignment
step_id = 'step_id_example' # str | The ID of Learning Assignment Step
shareable_content_object_id = 'shareable_content_object_id_example' # str | The ID of SCO to load (optional)
default_shareable_content_object = 'default_shareable_content_object_example' # str | The default SCO to retrieve (optional)
expand = ['expand_example'] # list[str] | Fields to expand in response (optional)

try:
    # Get Learning Assignment Step
    api_response = api_instance.get_learning_assignment_step(assignment_id, step_id, shareable_content_object_id=shareable_content_object_id, default_shareable_content_object=default_shareable_content_object, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_assignment_step: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The ID of Learning Assignment |  |
| **step_id** | **str**| The ID of Learning Assignment Step |  |
| **shareable_content_object_id** | **str**| The ID of SCO to load | [optional]  |
| **default_shareable_content_object** | **str**| The default SCO to retrieve | [optional] <br />**Values**: First, Last, Next |
| **expand** | [**list[str]**](str.html)| Fields to expand in response | [optional] <br />**Values**: moduleStep |
{: class="table table-striped"}

### Return type

[**LearningAssignmentStep**](LearningAssignmentStep.html)

<a name="get_learning_assignments"></a>

## [**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html) get_learning_assignments(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, pcPass=pcPass, min_percentage_score=min_percentage_score, max_percentage_score=max_percentage_score, sort_order=sort_order, sort_by=sort_by, user_id=user_id, types=types, states=states, expand=expand)



List of Learning module Assignments

Either moduleId or user value is required

Wraps GET /api/v2/learning/assignments 

Requires ANY permissions: 

* learning:assignment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | Specifies the ID of the learning module. Fetch assignments for learning module ID (optional)
interval = 'interval_example' # str | Specifies the range of dueDates to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = ''Any'' # str | Specifies if only the non-overdue (overdue is \"False\") or overdue (overdue is \"True\") assignments are returned. If overdue is \"Any\" or if the overdue parameter is not supplied, all assignments are returned (optional) (default to 'Any')
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
pcPass = ''Any'' # str | Specifies if only the failed (pass is \"False\") or passed (pass is \"True\") assignments (completed with assessment)are returned. If pass is \"Any\" or if the pass parameter is not supplied, all assignments are returned (optional) (default to 'Any')
min_percentage_score = 3.4 # float | The minimum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) (optional)
max_percentage_score = 3.4 # float | The maximum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) (optional)
sort_order = ''Desc'' # str | Specifies result set sort order; if not specified, default sort order is descending (Desc) (optional) (default to 'Desc')
sort_by = 'sort_by_example' # str | Specifies which field to sort the results by, default sort is by recommendedCompletionDate (optional)
user_id = ['user_id_example'] # list[str] | Specifies the list of user IDs to be queried, up to 100 user IDs. (optional)
types = ['types_example'] # list[str] | Specifies the module types to filter by (optional)
states = ['states_example'] # list[str] | Specifies the assignment states to filter by (optional)
expand = ['expand_example'] # list[str] | Specifies the expand option for returning additional information (optional)

try:
    # List of Learning module Assignments
    api_response = api_instance.get_learning_assignments(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, pcPass=pcPass, min_percentage_score=min_percentage_score, max_percentage_score=max_percentage_score, sort_order=sort_order, sort_by=sort_by, user_id=user_id, types=types, states=states, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_assignments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| Specifies the ID of the learning module. Fetch assignments for learning module ID | [optional]  |
| **interval** | **str**| Specifies the range of dueDates to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if only the non-overdue (overdue is \&quot;False\&quot;) or overdue (overdue is \&quot;True\&quot;) assignments are returned. If overdue is \&quot;Any\&quot; or if the overdue parameter is not supplied, all assignments are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **pcPass** | **str**| Specifies if only the failed (pass is \&quot;False\&quot;) or passed (pass is \&quot;True\&quot;) assignments (completed with assessment)are returned. If pass is \&quot;Any\&quot; or if the pass parameter is not supplied, all assignments are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **min_percentage_score** | **float**| The minimum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) | [optional]  |
| **max_percentage_score** | **float**| The maximum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) | [optional]  |
| **sort_order** | **str**| Specifies result set sort order; if not specified, default sort order is descending (Desc) | [optional] [default to &#39;Desc&#39;]<br />**Values**: Asc, Desc |
| **sort_by** | **str**| Specifies which field to sort the results by, default sort is by recommendedCompletionDate | [optional] <br />**Values**: RecommendedCompletionDate, DateModified |
| **user_id** | [**list[str]**](str.html)| Specifies the list of user IDs to be queried, up to 100 user IDs. | [optional]  |
| **types** | [**list[str]**](str.html)| Specifies the module types to filter by | [optional] <br />**Values**: Informational, AssessedContent, Assessment, External |
| **states** | [**list[str]**](str.html)| Specifies the assignment states to filter by | [optional] <br />**Values**: Assigned, InProgress, Completed, NotCompleted, InvalidSchedule |
| **expand** | [**list[str]**](str.html)| Specifies the expand option for returning additional information | [optional] <br />**Values**: ModuleSummary |
{: class="table table-striped"}

### Return type

[**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html)

<a name="get_learning_assignments_me"></a>

## [**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html) get_learning_assignments_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, pcPass=pcPass, min_percentage_score=min_percentage_score, max_percentage_score=max_percentage_score, sort_order=sort_order, sort_by=sort_by, types=types, states=states, expand=expand)



List of Learning Assignments assigned to current user

Wraps GET /api/v2/learning/assignments/me 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | Specifies the ID of the learning module. Fetch assignments for learning module ID (optional)
interval = 'interval_example' # str | Specifies the range of dueDates to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = ''Any'' # str | Specifies if only the non-overdue (overdue is \"False\") or overdue (overdue is \"True\") assignments are returned. If overdue is \"Any\" or if the overdue parameter is not supplied, all assignments are returned (optional) (default to 'Any')
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
pcPass = ''Any'' # str | Specifies if only the failed (pass is \"False\") or passed (pass is \"True\") assignments (completed with assessment)are returned. If pass is \"Any\" or if the pass parameter is not supplied, all assignments are returned (optional) (default to 'Any')
min_percentage_score = 3.4 # float | The minimum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) (optional)
max_percentage_score = 3.4 # float | The maximum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) (optional)
sort_order = ''Desc'' # str | Specifies result set sort order; if not specified, default sort order is descending (Desc) (optional) (default to 'Desc')
sort_by = 'sort_by_example' # str | Specifies which field to sort the results by, default sort is by recommendedCompletionDate (optional)
types = ['types_example'] # list[str] | Specifies the module types to filter by (optional)
states = ['states_example'] # list[str] | Specifies the assignment states to filter by (optional)
expand = ['expand_example'] # list[str] | Specifies the expand option for returning additional information (optional)

try:
    # List of Learning Assignments assigned to current user
    api_response = api_instance.get_learning_assignments_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, pcPass=pcPass, min_percentage_score=min_percentage_score, max_percentage_score=max_percentage_score, sort_order=sort_order, sort_by=sort_by, types=types, states=states, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_assignments_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| Specifies the ID of the learning module. Fetch assignments for learning module ID | [optional]  |
| **interval** | **str**| Specifies the range of dueDates to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if only the non-overdue (overdue is \&quot;False\&quot;) or overdue (overdue is \&quot;True\&quot;) assignments are returned. If overdue is \&quot;Any\&quot; or if the overdue parameter is not supplied, all assignments are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **pcPass** | **str**| Specifies if only the failed (pass is \&quot;False\&quot;) or passed (pass is \&quot;True\&quot;) assignments (completed with assessment)are returned. If pass is \&quot;Any\&quot; or if the pass parameter is not supplied, all assignments are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **min_percentage_score** | **float**| The minimum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) | [optional]  |
| **max_percentage_score** | **float**| The maximum assessment score for an assignment (completed with assessment) to be included in the results (inclusive) | [optional]  |
| **sort_order** | **str**| Specifies result set sort order; if not specified, default sort order is descending (Desc) | [optional] [default to &#39;Desc&#39;]<br />**Values**: Asc, Desc |
| **sort_by** | **str**| Specifies which field to sort the results by, default sort is by recommendedCompletionDate | [optional] <br />**Values**: RecommendedCompletionDate, DateModified |
| **types** | [**list[str]**](str.html)| Specifies the module types to filter by | [optional] <br />**Values**: Informational, AssessedContent, Assessment, External |
| **states** | [**list[str]**](str.html)| Specifies the assignment states to filter by | [optional] <br />**Values**: Assigned, InProgress, Completed, NotCompleted, InvalidSchedule |
| **expand** | [**list[str]**](str.html)| Specifies the expand option for returning additional information | [optional] <br />**Values**: ModuleSummary |
{: class="table table-striped"}

### Return type

[**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html)

<a name="get_learning_module"></a>

## [**LearningModule**](LearningModule.html) get_learning_module(module_id, expand=expand)



Get a learning module

Wraps GET /api/v2/learning/modules/{moduleId} 

Requires ANY permissions: 

* learning:module:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
expand = ['expand_example'] # list[str] | Fields to expand in response(case insensitive) (optional)

try:
    # Get a learning module
    api_response = api_instance.get_learning_module(module_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_module: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: assessmentForm, coverArt |
{: class="table table-striped"}

### Return type

[**LearningModule**](LearningModule.html)

<a name="get_learning_module_job"></a>

## [**LearningModuleJobResponse**](LearningModuleJobResponse.html) get_learning_module_job(module_id, job_id)



Get a specific Learning Module job status

Wraps GET /api/v2/learning/modules/{moduleId}/jobs/{jobId} 

Requires ANY permissions: 

* learning:module:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
job_id = 'job_id_example' # str | The ID of the learning module job

try:
    # Get a specific Learning Module job status
    api_response = api_instance.get_learning_module_job(module_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_module_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **job_id** | **str**| The ID of the learning module job |  |
{: class="table table-striped"}

### Return type

[**LearningModuleJobResponse**](LearningModuleJobResponse.html)

<a name="get_learning_module_preview"></a>

## [**LearningModulePreviewGetResponse**](LearningModulePreviewGetResponse.html) get_learning_module_preview(module_id)



Get a learning module preview

Wraps GET /api/v2/learning/modules/{moduleId}/preview 

Requires ANY permissions: 

* learning:module:preview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module

try:
    # Get a learning module preview
    api_response = api_instance.get_learning_module_preview(module_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_module_preview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
{: class="table table-striped"}

### Return type

[**LearningModulePreviewGetResponse**](LearningModulePreviewGetResponse.html)

<a name="get_learning_module_rule"></a>

## [**LearningModuleRule**](LearningModuleRule.html) get_learning_module_rule(module_id)



Get a learning module rule

Wraps GET /api/v2/learning/modules/{moduleId}/rule 

Requires ANY permissions: 

* learning:rule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module

try:
    # Get a learning module rule
    api_response = api_instance.get_learning_module_rule(module_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_module_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
{: class="table table-striped"}

### Return type

[**LearningModuleRule**](LearningModuleRule.html)

<a name="get_learning_module_version"></a>

## [**LearningModule**](LearningModule.html) get_learning_module_version(module_id, version_id, expand=expand)



Get specific version of a published module

Wraps GET /api/v2/learning/modules/{moduleId}/versions/{versionId} 

Requires ANY permissions: 

* learning:module:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
version_id = 'version_id_example' # str | The version of learning module
expand = ['expand_example'] # list[str] | Fields to expand in response(case insensitive) (optional)

try:
    # Get specific version of a published module
    api_response = api_instance.get_learning_module_version(module_id, version_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_module_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **version_id** | **str**| The version of learning module |  |
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: assessmentForm, coverArt |
{: class="table table-striped"}

### Return type

[**LearningModule**](LearningModule.html)

<a name="get_learning_modules"></a>

## [**LearningModulesDomainEntityListing**](LearningModulesDomainEntityListing.html) get_learning_modules(is_archived=is_archived, types=types, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, search_term=search_term, expand=expand, is_published=is_published, statuses=statuses, external_ids=external_ids)



Get all learning modules of an organization

Wraps GET /api/v2/learning/modules 

Requires ANY permissions: 

* learning:module:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
is_archived = False # bool | Archive status (optional) (default to False)
types = ['types_example'] # list[str] | Specifies the module types. (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
search_term = 'search_term_example' # str | Search Term (searchable by name) (optional)
expand = ['expand_example'] # list[str] | Fields to expand in response(case insensitive) (optional)
is_published = ''Any'' # str | Specifies if only the Unpublished (isPublished is \"False\") or Published (isPublished is \"True\") modules are returned. If isPublished is \"Any\" or omitted, both types are returned (optional) (default to 'Any')
statuses = ['statuses_example'] # list[str] | Specifies the module statuses to filter by (optional)
external_ids = ['external_ids_example'] # list[str] | Specifies the module external IDs to filter by. Only one ID is allowed (optional)

try:
    # Get all learning modules of an organization
    api_response = api_instance.get_learning_modules(is_archived=is_archived, types=types, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, search_term=search_term, expand=expand, is_published=is_published, statuses=statuses, external_ids=external_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_modules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **is_archived** | **bool**| Archive status | [optional] [default to False] |
| **types** | [**list[str]**](str.html)| Specifies the module types. | [optional] <br />**Values**: Informational, AssessedContent, Assessment, External |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;]<br />**Values**: name, createddate, percentpassed, averagescore |
| **search_term** | **str**| Search Term (searchable by name) | [optional]  |
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: rule, summaryData |
| **is_published** | **str**| Specifies if only the Unpublished (isPublished is \&quot;False\&quot;) or Published (isPublished is \&quot;True\&quot;) modules are returned. If isPublished is \&quot;Any\&quot; or omitted, both types are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **statuses** | [**list[str]**](str.html)| Specifies the module statuses to filter by | [optional] <br />**Values**: Unpublished, Published, Archived |
| **external_ids** | [**list[str]**](str.html)| Specifies the module external IDs to filter by. Only one ID is allowed | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningModulesDomainEntityListing**](LearningModulesDomainEntityListing.html)

<a name="get_learning_modules_assignments"></a>

## [**AssignedLearningModuleDomainEntityListing**](AssignedLearningModuleDomainEntityListing.html) get_learning_modules_assignments(user_ids, page_size=page_size, page_number=page_number, search_term=search_term, overdue=overdue, assignment_states=assignment_states, expand=expand)



Get all learning modules of an organization including assignments for a specific user

Wraps GET /api/v2/learning/modules/assignments 

Requires ALL permissions: 

* learning:module:view
* learning:assignment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
user_ids = ['user_ids_example'] # list[str] | The IDs of the users to include
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
search_term = 'search_term_example' # str | Search Term (searches by name and description) (optional)
overdue = ''Any'' # str | Specifies if only modules with overdue/not overdue (overdue is \"True\" or \"False\") assignments are returned. If overdue is \"Any\" or omitted, both are returned and can including modules that are unassigned. (optional) (default to 'Any')
assignment_states = ['assignment_states_example'] # list[str] | Specifies the assignment states to return. (optional)
expand = ['expand_example'] # list[str] | Fields to expand in response(case insensitive) (optional)

try:
    # Get all learning modules of an organization including assignments for a specific user
    api_response = api_instance.get_learning_modules_assignments(user_ids, page_size=page_size, page_number=page_number, search_term=search_term, overdue=overdue, assignment_states=assignment_states, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_modules_assignments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_ids** | [**list[str]**](str.html)| The IDs of the users to include |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **search_term** | **str**| Search Term (searches by name and description) | [optional]  |
| **overdue** | **str**| Specifies if only modules with overdue/not overdue (overdue is \&quot;True\&quot; or \&quot;False\&quot;) assignments are returned. If overdue is \&quot;Any\&quot; or omitted, both are returned and can including modules that are unassigned. | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **assignment_states** | [**list[str]**](str.html)| Specifies the assignment states to return. | [optional] <br />**Values**: NotAssigned, Assigned, InProgress, Completed, InvalidSchedule |
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: coverArt |
{: class="table table-striped"}

### Return type

[**AssignedLearningModuleDomainEntityListing**](AssignedLearningModuleDomainEntityListing.html)

<a name="get_learning_modules_coverart_cover_art_id"></a>

## [**LearningModuleCoverArtResponse**](LearningModuleCoverArtResponse.html) get_learning_modules_coverart_cover_art_id(cover_art_id)



Get a specific Learning Module cover art using ID

Wraps GET /api/v2/learning/modules/coverart/{coverArtId} 

Requires ANY permissions: 

* learning:coverart:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
cover_art_id = 'cover_art_id_example' # str | Key identifier for the cover art

try:
    # Get a specific Learning Module cover art using ID
    api_response = api_instance.get_learning_modules_coverart_cover_art_id(cover_art_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_modules_coverart_cover_art_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cover_art_id** | **str**| Key identifier for the cover art |  |
{: class="table table-striped"}

### Return type

[**LearningModuleCoverArtResponse**](LearningModuleCoverArtResponse.html)

<a name="get_learning_scorm_scorm_id"></a>

## [**LearningScormResponse**](LearningScormResponse.html) get_learning_scorm_scorm_id(scorm_id)



Get Learning SCORM Result

Wraps GET /api/v2/learning/scorm/{scormId} 

Requires ANY permissions: 

* learning:scorm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
scorm_id = 'scorm_id_example' # str | The ID of the SCORM package

try:
    # Get Learning SCORM Result
    api_response = api_instance.get_learning_scorm_scorm_id(scorm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_scorm_scorm_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **scorm_id** | **str**| The ID of the SCORM package |  |
{: class="table table-striped"}

### Return type

[**LearningScormResponse**](LearningScormResponse.html)

<a name="patch_learning_assignment"></a>

## [**LearningAssignment**](LearningAssignment.html) patch_learning_assignment(assignment_id, body=body)



Update Learning Assignment

Wraps PATCH /api/v2/learning/assignments/{assignmentId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The ID of Learning Assignment
body = PureCloudPlatformClientV2.LearningAssignmentUpdate() # LearningAssignmentUpdate | The Learning Assignment to be updated (optional)

try:
    # Update Learning Assignment
    api_response = api_instance.patch_learning_assignment(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->patch_learning_assignment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The ID of Learning Assignment |  |
| **body** | [**LearningAssignmentUpdate**](LearningAssignmentUpdate.html)| The Learning Assignment to be updated | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="patch_learning_assignment_reschedule"></a>

## [**LearningAssignment**](LearningAssignment.html) patch_learning_assignment_reschedule(assignment_id, body=body)



Reschedule Learning Assignment

Wraps PATCH /api/v2/learning/assignments/{assignmentId}/reschedule 

Requires ANY permissions: 

* learning:assignment:reschedule

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The ID of Learning Assignment
body = PureCloudPlatformClientV2.LearningAssignmentReschedule() # LearningAssignmentReschedule | The Learning assignment reschedule model (optional)

try:
    # Reschedule Learning Assignment
    api_response = api_instance.patch_learning_assignment_reschedule(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->patch_learning_assignment_reschedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The ID of Learning Assignment |  |
| **body** | [**LearningAssignmentReschedule**](LearningAssignmentReschedule.html)| The Learning assignment reschedule model | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="patch_learning_assignment_step"></a>

## [**LearningAssignmentStep**](LearningAssignmentStep.html) patch_learning_assignment_step(assignment_id, step_id, body=body)



Update Learning Assignment Step

Permission not required if you are the assigned user of the learning assignment

Wraps PATCH /api/v2/learning/assignments/{assignmentId}/steps/{stepId} 

Requires ANY permissions: 

* learning:assignment:editOwn

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The ID of Learning Assignment
step_id = 'step_id_example' # str | The ID of Learning Assignment Step
body = PureCloudPlatformClientV2.LearningAssignmentStep() # LearningAssignmentStep | The Learning Assignment Step to be updated (optional)

try:
    # Update Learning Assignment Step
    api_response = api_instance.patch_learning_assignment_step(assignment_id, step_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->patch_learning_assignment_step: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The ID of Learning Assignment |  |
| **step_id** | **str**| The ID of Learning Assignment Step |  |
| **body** | [**LearningAssignmentStep**](LearningAssignmentStep.html)| The Learning Assignment Step to be updated | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningAssignmentStep**](LearningAssignmentStep.html)

<a name="patch_learning_module_user_assignments"></a>

## [**LearningAssignment**](LearningAssignment.html) patch_learning_module_user_assignments(module_id, user_id, body)



Update an external assignment for a specific user

Wraps PATCH /api/v2/learning/modules/{moduleId}/users/{userId}/assignments 

Requires ALL permissions: 

* learning:externalAssignment:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | Key identifier for the module
user_id = 'user_id_example' # str | Key identifier for the user
body = PureCloudPlatformClientV2.LearningAssignmentExternalUpdate() # LearningAssignmentExternalUpdate | The learning request for updating the assignment

try:
    # Update an external assignment for a specific user
    api_response = api_instance.patch_learning_module_user_assignments(module_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->patch_learning_module_user_assignments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| Key identifier for the module |  |
| **user_id** | **str**| Key identifier for the user |  |
| **body** | [**LearningAssignmentExternalUpdate**](LearningAssignmentExternalUpdate.html)| The learning request for updating the assignment |  |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="post_learning_assessments_scoring"></a>

## [**AssessmentScoringSet**](AssessmentScoringSet.html) post_learning_assessments_scoring(body)



Score learning assessment for preview

Wraps POST /api/v2/learning/assessments/scoring 

Requires ANY permissions: 

* learning:module:view
* learning:module:add
* learning:module:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = PureCloudPlatformClientV2.LearningAssessmentScoringRequest() # LearningAssessmentScoringRequest | Assessment form and answers to score

try:
    # Score learning assessment for preview
    api_response = api_instance.post_learning_assessments_scoring(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assessments_scoring: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningAssessmentScoringRequest**](LearningAssessmentScoringRequest.html)| Assessment form and answers to score |  |
{: class="table table-striped"}

### Return type

[**AssessmentScoringSet**](AssessmentScoringSet.html)

<a name="post_learning_assignment_reassign"></a>

## [**LearningAssignment**](LearningAssignment.html) post_learning_assignment_reassign(assignment_id)



Reassign Learning Assignment

This will reassign the state of the assignment to 'Assigned' and update the assignment to the latest version of the module

Wraps POST /api/v2/learning/assignments/{assignmentId}/reassign 

Requires ANY permissions: 

* learning:assignment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The Learning Assignment ID

try:
    # Reassign Learning Assignment
    api_response = api_instance.post_learning_assignment_reassign(assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignment_reassign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The Learning Assignment ID |  |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="post_learning_assignment_reset"></a>

## [**LearningAssignment**](LearningAssignment.html) post_learning_assignment_reset(assignment_id)



Reset Learning Assignment

This will reset the state of the assignment to 'Assigned' and remove the version of Learning module associated with the assignment

Wraps POST /api/v2/learning/assignments/{assignmentId}/reset 

Requires ANY permissions: 

* learning:assignment:reset

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
assignment_id = 'assignment_id_example' # str | The Learning Assignment ID

try:
    # Reset Learning Assignment
    api_response = api_instance.post_learning_assignment_reset(assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignment_reset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assignment_id** | **str**| The Learning Assignment ID |  |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="post_learning_assignments"></a>

## [**LearningAssignment**](LearningAssignment.html) post_learning_assignments(body=body)



Create Learning Assignment

Wraps POST /api/v2/learning/assignments 

Requires ANY permissions: 

* learning:assignment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = PureCloudPlatformClientV2.LearningAssignmentCreate() # LearningAssignmentCreate | The Learning Assignment to be created (optional)

try:
    # Create Learning Assignment
    api_response = api_instance.post_learning_assignments(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningAssignmentCreate**](LearningAssignmentCreate.html)| The Learning Assignment to be created | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="post_learning_assignments_aggregates_query"></a>

## [**LearningAssignmentAggregateResponse**](LearningAssignmentAggregateResponse.html) post_learning_assignments_aggregates_query(body)



Retrieve aggregated assignment data

Wraps POST /api/v2/learning/assignments/aggregates/query 

Requires ANY permissions: 

* learning:assignment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = PureCloudPlatformClientV2.LearningAssignmentAggregateParam() # LearningAssignmentAggregateParam | Aggregate Request

try:
    # Retrieve aggregated assignment data
    api_response = api_instance.post_learning_assignments_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignments_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningAssignmentAggregateParam**](LearningAssignmentAggregateParam.html)| Aggregate Request |  |
{: class="table table-striped"}

### Return type

[**LearningAssignmentAggregateResponse**](LearningAssignmentAggregateResponse.html)

<a name="post_learning_assignments_bulkadd"></a>

## [**LearningAssignmentBulkAddResponse**](LearningAssignmentBulkAddResponse.html) post_learning_assignments_bulkadd(body=body)



Add multiple learning assignments

Wraps POST /api/v2/learning/assignments/bulkadd 

Requires ANY permissions: 

* learning:assignment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = [PureCloudPlatformClientV2.LearningAssignmentItem()] # list[LearningAssignmentItem] | The learning assignments to be created (optional)

try:
    # Add multiple learning assignments
    api_response = api_instance.post_learning_assignments_bulkadd(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignments_bulkadd: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[LearningAssignmentItem]**](LearningAssignmentItem.html)| The learning assignments to be created | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningAssignmentBulkAddResponse**](LearningAssignmentBulkAddResponse.html)

<a name="post_learning_assignments_bulkremove"></a>

## [**LearningAssignmentBulkRemoveResponse**](LearningAssignmentBulkRemoveResponse.html) post_learning_assignments_bulkremove(body=body)



Remove multiple Learning Assignments

Wraps POST /api/v2/learning/assignments/bulkremove 

Requires ANY permissions: 

* learning:assignment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = ['body_example'] # list[str] | The IDs of the learning assignments to be removed (optional)

try:
    # Remove multiple Learning Assignments
    api_response = api_instance.post_learning_assignments_bulkremove(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignments_bulkremove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[str]**](str.html)| The IDs of the learning assignments to be removed | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningAssignmentBulkRemoveResponse**](LearningAssignmentBulkRemoveResponse.html)

<a name="post_learning_module_jobs"></a>

## [**LearningModuleJobResponse**](LearningModuleJobResponse.html) post_learning_module_jobs(module_id, body)



Starts a specified operation on learning module

This will initiate operation specified in the request body for a learning module

Wraps POST /api/v2/learning/modules/{moduleId}/jobs 

Requires ANY permissions: 

* learning:module:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
body = PureCloudPlatformClientV2.LearningModuleJobRequest() # LearningModuleJobRequest | The learning module job request

try:
    # Starts a specified operation on learning module
    api_response = api_instance.post_learning_module_jobs(module_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_module_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **body** | [**LearningModuleJobRequest**](LearningModuleJobRequest.html)| The learning module job request |  |
{: class="table table-striped"}

### Return type

[**LearningModuleJobResponse**](LearningModuleJobResponse.html)

<a name="post_learning_module_publish"></a>

## [**LearningModulePublishResponse**](LearningModulePublishResponse.html) post_learning_module_publish(module_id, body=body)



Publish a Learning module

Wraps POST /api/v2/learning/modules/{moduleId}/publish 

Requires ANY permissions: 

* learning:module:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
body = PureCloudPlatformClientV2.LearningModulePublishRequest() # LearningModulePublishRequest | The request body (optional)

try:
    # Publish a Learning module
    api_response = api_instance.post_learning_module_publish(module_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_module_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **body** | [**LearningModulePublishRequest**](LearningModulePublishRequest.html)| The request body | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningModulePublishResponse**](LearningModulePublishResponse.html)

<a name="post_learning_modules"></a>

## [**LearningModule**](LearningModule.html) post_learning_modules(body)



Create a new learning module

This will create a new unpublished learning module with the specified fields.

Wraps POST /api/v2/learning/modules 

Requires ANY permissions: 

* learning:module:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = PureCloudPlatformClientV2.LearningModuleRequest() # LearningModuleRequest | The learning module to be created

try:
    # Create a new learning module
    api_response = api_instance.post_learning_modules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_modules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningModuleRequest**](LearningModuleRequest.html)| The learning module to be created |  |
{: class="table table-striped"}

### Return type

[**LearningModule**](LearningModule.html)

<a name="post_learning_rules_query"></a>

## [**LearningAssignmentUserListing**](LearningAssignmentUserListing.html) post_learning_rules_query(page_size, page_number, body)



Get users for learning module rule

This will get the users who matches the given rule.

Wraps POST /api/v2/learning/rules/query 

Requires ANY permissions: 

* learning:rule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
page_size = 50 # int | Page size (default to 50)
page_number = 1 # int | Page number (default to 1)
body = PureCloudPlatformClientV2.LearningAssignmentUserQuery() # LearningAssignmentUserQuery | The learning module rule to fetch users

try:
    # Get users for learning module rule
    api_response = api_instance.post_learning_rules_query(page_size, page_number, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_rules_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [default to 50] |
| **page_number** | **int**| Page number | [default to 1] |
| **body** | [**LearningAssignmentUserQuery**](LearningAssignmentUserQuery.html)| The learning module rule to fetch users |  |
{: class="table table-striped"}

### Return type

[**LearningAssignmentUserListing**](LearningAssignmentUserListing.html)

<a name="post_learning_scheduleslots_query"></a>

## [**LearningScheduleSlotsQueryResponse**](LearningScheduleSlotsQueryResponse.html) post_learning_scheduleslots_query(body)



Get list of possible slots where a learning activity can be scheduled.

Wraps POST /api/v2/learning/scheduleslots/query 

Requires ANY permissions: 

* learning:scheduleSlot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = PureCloudPlatformClientV2.LearningScheduleSlotsQueryRequest() # LearningScheduleSlotsQueryRequest | The slot search request

try:
    # Get list of possible slots where a learning activity can be scheduled.
    api_response = api_instance.post_learning_scheduleslots_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_scheduleslots_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningScheduleSlotsQueryRequest**](LearningScheduleSlotsQueryRequest.html)| The slot search request |  |
{: class="table table-striped"}

### Return type

[**LearningScheduleSlotsQueryResponse**](LearningScheduleSlotsQueryResponse.html)

<a name="post_learning_scorm"></a>

## [**LearningScormUploadResponse**](LearningScormUploadResponse.html) post_learning_scorm(body=body)



Create a SCORM package upload request

Wraps POST /api/v2/learning/scorm 

Requires ANY permissions: 

* learning:scorm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
body = PureCloudPlatformClientV2.LearningScormUploadRequest() # LearningScormUploadRequest | The SCORM package to be uploaded (optional)

try:
    # Create a SCORM package upload request
    api_response = api_instance.post_learning_scorm(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_scorm: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningScormUploadRequest**](LearningScormUploadRequest.html)| The SCORM package to be uploaded | [optional]  |
{: class="table table-striped"}

### Return type

[**LearningScormUploadResponse**](LearningScormUploadResponse.html)

<a name="put_learning_module"></a>

## [**LearningModule**](LearningModule.html) put_learning_module(module_id, body)



Update a learning module

This will update the name, description, completion time in days and inform steps for a learning module

Wraps PUT /api/v2/learning/modules/{moduleId} 

Requires ANY permissions: 

* learning:module:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
body = PureCloudPlatformClientV2.LearningModuleRequest() # LearningModuleRequest | The learning module to be updated

try:
    # Update a learning module
    api_response = api_instance.put_learning_module(module_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->put_learning_module: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **body** | [**LearningModuleRequest**](LearningModuleRequest.html)| The learning module to be updated |  |
{: class="table table-striped"}

### Return type

[**LearningModule**](LearningModule.html)

<a name="put_learning_module_preview"></a>

## [**LearningModulePreviewUpdateResponse**](LearningModulePreviewUpdateResponse.html) put_learning_module_preview(module_id, body)



Update a learning module preview

This will update a learning module preview

Wraps PUT /api/v2/learning/modules/{moduleId}/preview 

Requires ANY permissions: 

* learning:module:preview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
body = PureCloudPlatformClientV2.LearningModulePreviewUpdateRequest() # LearningModulePreviewUpdateRequest | The learning module to be updated

try:
    # Update a learning module preview
    api_response = api_instance.put_learning_module_preview(module_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->put_learning_module_preview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **body** | [**LearningModulePreviewUpdateRequest**](LearningModulePreviewUpdateRequest.html)| The learning module to be updated |  |
{: class="table table-striped"}

### Return type

[**LearningModulePreviewUpdateResponse**](LearningModulePreviewUpdateResponse.html)

<a name="put_learning_module_rule"></a>

## [**LearningModuleRule**](LearningModuleRule.html) put_learning_module_rule(module_id, body)



Update a learning module rule

This will update a learning module rule with the specified fields.

Wraps PUT /api/v2/learning/modules/{moduleId}/rule 

Requires ANY permissions: 

* learning:rule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LearningApi()
module_id = 'module_id_example' # str | The ID of the learning module
body = PureCloudPlatformClientV2.LearningModuleRule() # LearningModuleRule | The learning module rule to be updated

try:
    # Update a learning module rule
    api_response = api_instance.put_learning_module_rule(module_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->put_learning_module_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
| **body** | [**LearningModuleRule**](LearningModuleRule.html)| The learning module rule to be updated |  |
{: class="table table-striped"}

### Return type

[**LearningModuleRule**](LearningModuleRule.html)

