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
|[**get_learning_assignments**](LearningApi.html#get_learning_assignments) | List of Learning module Assignments|
|[**get_learning_assignments_me**](LearningApi.html#get_learning_assignments_me) | List of Learning Assignments assigned to current user|
|[**get_learning_module**](LearningApi.html#get_learning_module) | Get a learning module|
|[**get_learning_module_rule**](LearningApi.html#get_learning_module_rule) | Get a learning module rule|
|[**get_learning_module_version**](LearningApi.html#get_learning_module_version) | Get specific version of a published module|
|[**get_learning_modules**](LearningApi.html#get_learning_modules) | Get all learning modules of an organization|
|[**patch_learning_assignment**](LearningApi.html#patch_learning_assignment) | Update Learning Assignment|
|[**post_learning_assignments**](LearningApi.html#post_learning_assignments) | Create Learning Assignment|
|[**post_learning_assignments_bulkadd**](LearningApi.html#post_learning_assignments_bulkadd) | Add multiple learning assignments|
|[**post_learning_assignments_bulkremove**](LearningApi.html#post_learning_assignments_bulkremove) | Remove multiple Learning Assignments|
|[**post_learning_module_publish**](LearningApi.html#post_learning_module_publish) | Publish a Learning module|
|[**post_learning_modules**](LearningApi.html#post_learning_modules) | Create a new learning module|
|[**post_learning_rules_query**](LearningApi.html#post_learning_rules_query) | Get users for learning module rule|
|[**put_learning_module**](LearningApi.html#put_learning_module) | Update a learning module|
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
| **expand** | [**list[str]**](str.html)| Fields to expand in response | [optional] <br />**Values**: module, assessment, assessmentForm |
{: class="table table-striped"}

### Return type

[**LearningAssignment**](LearningAssignment.html)

<a name="get_learning_assignments"></a>

## [**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html) get_learning_assignments(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, user_id=user_id, types=types, states=states, expand=expand)



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
overdue = 'Any' # str | Specifies if only the non-overdue (overdue is \"False\") or overdue (overdue is \"True\") assignments are returned. If overdue is \"Any\" or if the overdue parameter is not supplied, all assignments are returned (optional) (default to Any)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'Desc' # str | Specifies result set sort order; if not specified, default sort order is descending (Desc) (optional) (default to Desc)
sort_by = 'sort_by_example' # str | Specifies which field to sort the results by, default sort is by recommendedCompletionDate (optional)
user_id = ['user_id_example'] # list[str] | Specifies the list of user IDs to be queried, up to 100 user IDs. (optional)
types = ['types_example'] # list[str] | Specifies the assignment types, currently not supported and will be ignored. For now, all learning assignments regardless of types will be returned (optional)
states = ['states_example'] # list[str] | Specifies the assignment states to filter by (optional)
expand = ['expand_example'] # list[str] | Specifies the expand option for returning additional information (optional)

try:
    # List of Learning module Assignments
    api_response = api_instance.get_learning_assignments(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, user_id=user_id, types=types, states=states, expand=expand)
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
| **overdue** | **str**| Specifies if only the non-overdue (overdue is \&quot;False\&quot;) or overdue (overdue is \&quot;True\&quot;) assignments are returned. If overdue is \&quot;Any\&quot; or if the overdue parameter is not supplied, all assignments are returned | [optional] [default to Any]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order; if not specified, default sort order is descending (Desc) | [optional] [default to Desc]<br />**Values**: Asc, Desc |
| **sort_by** | **str**| Specifies which field to sort the results by, default sort is by recommendedCompletionDate | [optional] <br />**Values**: RecommendedCompletionDate, DateModified |
| **user_id** | [**list[str]**](str.html)| Specifies the list of user IDs to be queried, up to 100 user IDs. | [optional]  |
| **types** | [**list[str]**](str.html)| Specifies the assignment types, currently not supported and will be ignored. For now, all learning assignments regardless of types will be returned | [optional] <br />**Values**: Informational, AssessedContent, Questionnaire |
| **states** | [**list[str]**](str.html)| Specifies the assignment states to filter by | [optional] <br />**Values**: Assigned, InProgress, Completed |
| **expand** | [**list[str]**](str.html)| Specifies the expand option for returning additional information | [optional] <br />**Values**: ModuleSummary |
{: class="table table-striped"}

### Return type

[**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html)

<a name="get_learning_assignments_me"></a>

## [**LearningAssignmentsDomainEntity**](LearningAssignmentsDomainEntity.html) get_learning_assignments_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, types=types, states=states, expand=expand)



List of Learning Assignments assigned to current user



Wraps GET /api/v2/learning/assignments/me 

Requires NO permissions: 


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
overdue = 'Any' # str | Specifies if only the non-overdue (overdue is \"False\") or overdue (overdue is \"True\") assignments are returned. If overdue is \"Any\" or if the overdue parameter is not supplied, all assignments are returned (optional) (default to Any)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'Desc' # str | Specifies result set sort order; if not specified, default sort order is descending (Desc) (optional) (default to Desc)
sort_by = 'sort_by_example' # str | Specifies which field to sort the results by, default sort is by recommendedCompletionDate (optional)
types = ['types_example'] # list[str] | Specifies the assignment types, currently not supported and will be ignored. For now, all learning assignments regardless of types will be returned (optional)
states = ['states_example'] # list[str] | Specifies the assignment states to filter by (optional)
expand = ['expand_example'] # list[str] | Specifies the expand option for returning additional information (optional)

try:
    # List of Learning Assignments assigned to current user
    api_response = api_instance.get_learning_assignments_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, types=types, states=states, expand=expand)
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
| **overdue** | **str**| Specifies if only the non-overdue (overdue is \&quot;False\&quot;) or overdue (overdue is \&quot;True\&quot;) assignments are returned. If overdue is \&quot;Any\&quot; or if the overdue parameter is not supplied, all assignments are returned | [optional] [default to Any]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order; if not specified, default sort order is descending (Desc) | [optional] [default to Desc]<br />**Values**: Asc, Desc |
| **sort_by** | **str**| Specifies which field to sort the results by, default sort is by recommendedCompletionDate | [optional] <br />**Values**: RecommendedCompletionDate, DateModified |
| **types** | [**list[str]**](str.html)| Specifies the assignment types, currently not supported and will be ignored. For now, all learning assignments regardless of types will be returned | [optional] <br />**Values**: Informational, AssessedContent, Questionnaire |
| **states** | [**list[str]**](str.html)| Specifies the assignment states to filter by | [optional] <br />**Values**: Assigned, InProgress, Completed |
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
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: assessmentForm |
{: class="table table-striped"}

### Return type

[**LearningModule**](LearningModule.html)

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
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: assessmentForm |
{: class="table table-striped"}

### Return type

[**LearningModule**](LearningModule.html)

<a name="get_learning_modules"></a>

## [**LearningModulesDomainEntityListing**](LearningModulesDomainEntityListing.html) get_learning_modules(is_archived=is_archived, types=types, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, search_term=search_term, expand=expand)



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
is_archived = false # bool | Archive status (optional) (default to false)
types = ['types_example'] # list[str] | Specifies the module types. (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ascending' # str | Sort order (optional) (default to ascending)
sort_by = 'name' # str | Sort by (optional) (default to name)
search_term = 'search_term_example' # str | Search Term (searchable by name) (optional)
expand = ['expand_example'] # list[str] | Fields to expand in response(case insensitive) (optional)

try:
    # Get all learning modules of an organization
    api_response = api_instance.get_learning_modules(is_archived=is_archived, types=types, page_size=page_size, page_number=page_number, sort_order=sort_order, sort_by=sort_by, search_term=search_term, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->get_learning_modules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **is_archived** | **bool**| Archive status | [optional] [default to false] |
| **types** | [**list[str]**](str.html)| Specifies the module types. | [optional] <br />**Values**: Informational, AssessedContent, Questionnaire |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to ascending]<br />**Values**: ascending, descending |
| **sort_by** | **str**| Sort by | [optional] [default to name]<br />**Values**: name |
| **search_term** | **str**| Search Term (searchable by name) | [optional]  |
| **expand** | [**list[str]**](str.html)| Fields to expand in response(case insensitive) | [optional] <br />**Values**: rule, summaryData |
{: class="table table-striped"}

### Return type

[**LearningModulesDomainEntityListing**](LearningModulesDomainEntityListing.html)

<a name="patch_learning_assignment"></a>

## [**LearningAssignment**](LearningAssignment.html) patch_learning_assignment(assignment_id, body=body)



Update Learning Assignment



Wraps PATCH /api/v2/learning/assignments/{assignmentId} 

Requires NO permissions: 


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

##  post_learning_assignments_bulkremove(body=body)



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
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | The IDs of the learning assignments to be removed (optional)

try:
    # Remove multiple Learning Assignments
    api_instance.post_learning_assignments_bulkremove(body=body)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_assignments_bulkremove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **list[str]**| The IDs of the learning assignments to be removed | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_learning_module_publish"></a>

## [**LearningModulePublishResponse**](LearningModulePublishResponse.html) post_learning_module_publish(module_id)



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

try:
    # Publish a Learning module
    api_response = api_instance.post_learning_module_publish(module_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningApi->post_learning_module_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| The ID of the learning module |  |
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

