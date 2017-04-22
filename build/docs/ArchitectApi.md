---
title: ArchitectApi
---

## PureCloudPlatformClientV2.ArchitectApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_architect_prompt**](ArchitectApi.html#delete_architect_prompt) | Delete specified user prompt|
|[**delete_architect_prompt_resource**](ArchitectApi.html#delete_architect_prompt_resource) | Delete specified user prompt resource|
|[**delete_architect_prompts**](ArchitectApi.html#delete_architect_prompts) | Batch-delete a list of prompts|
|[**delete_architect_systemprompt_resource**](ArchitectApi.html#delete_architect_systemprompt_resource) | Delete a system prompt resource override.|
|[**delete_flow**](ArchitectApi.html#delete_flow) | Delete flow|
|[**delete_flows**](ArchitectApi.html#delete_flows) | Batch-delete a list of flows|
|[**get_architect_dependencytracking**](ArchitectApi.html#get_architect_dependencytracking) | Get Dependency Tracking objects that have a given display name|
|[**get_architect_dependencytracking_build**](ArchitectApi.html#get_architect_dependencytracking_build) | Get Dependency Tracking build status for an organization|
|[**get_architect_dependencytracking_consumedresources**](ArchitectApi.html#get_architect_dependencytracking_consumedresources) | Get resources that are consumed by a given Dependency Tracking object|
|[**get_architect_dependencytracking_consumingresources**](ArchitectApi.html#get_architect_dependencytracking_consumingresources) | Get resources that consume a given Dependency Tracking object|
|[**get_architect_dependencytracking_deletedresourceconsumers**](ArchitectApi.html#get_architect_dependencytracking_deletedresourceconsumers) | Get Dependency Tracking objects that consume deleted resources|
|[**get_architect_dependencytracking_object**](ArchitectApi.html#get_architect_dependencytracking_object) | Get a Dependency Tracking object|
|[**get_architect_dependencytracking_type**](ArchitectApi.html#get_architect_dependencytracking_type) | Get a Dependency Tracking type.|
|[**get_architect_dependencytracking_types**](ArchitectApi.html#get_architect_dependencytracking_types) | Get Dependency Tracking types.|
|[**get_architect_dependencytracking_updatedresourceconsumers**](ArchitectApi.html#get_architect_dependencytracking_updatedresourceconsumers) | Get Dependency Tracking objects that depend on updated resources|
|[**get_architect_prompt**](ArchitectApi.html#get_architect_prompt) | Get specified user prompt|
|[**get_architect_prompt_resource**](ArchitectApi.html#get_architect_prompt_resource) | Get specified user prompt resource|
|[**get_architect_prompt_resources**](ArchitectApi.html#get_architect_prompt_resources) | Get a pageable list of user prompt resources|
|[**get_architect_prompts**](ArchitectApi.html#get_architect_prompts) | Get a pageable list of user prompts|
|[**get_architect_systemprompt**](ArchitectApi.html#get_architect_systemprompt) | Get a system prompt|
|[**get_architect_systemprompt_resource**](ArchitectApi.html#get_architect_systemprompt_resource) | Get a system prompt resource.|
|[**get_architect_systemprompt_resources**](ArchitectApi.html#get_architect_systemprompt_resources) | Get system prompt resources.|
|[**get_architect_systemprompts**](ArchitectApi.html#get_architect_systemprompts) | Get System Prompts|
|[**get_flow**](ArchitectApi.html#get_flow) | Get flow|
|[**get_flow_latestconfiguration**](ArchitectApi.html#get_flow_latestconfiguration) | Get the latest configuration for flow|
|[**get_flow_version**](ArchitectApi.html#get_flow_version) | Get flow version|
|[**get_flow_version_configuration**](ArchitectApi.html#get_flow_version_configuration) | Create flow version configuration|
|[**get_flow_versions**](ArchitectApi.html#get_flow_versions) | Get flow version list|
|[**get_flows**](ArchitectApi.html#get_flows) | Get a pageable list of flows, filtered by query parameters|
|[**post_architect_dependencytracking_build**](ArchitectApi.html#post_architect_dependencytracking_build) | Rebuild Dependency Tracking data for an organization|
|[**post_architect_prompt_resources**](ArchitectApi.html#post_architect_prompt_resources) | Create a new user prompt resource|
|[**post_architect_prompts**](ArchitectApi.html#post_architect_prompts) | Create a new user prompt|
|[**post_architect_systemprompt_resources**](ArchitectApi.html#post_architect_systemprompt_resources) | Create system prompt resource override.|
|[**post_flow_versions**](ArchitectApi.html#post_flow_versions) | Create flow version|
|[**post_flows**](ArchitectApi.html#post_flows) | Create flow|
|[**post_flows_actions_checkin**](ArchitectApi.html#post_flows_actions_checkin) | Check-in flow|
|[**post_flows_actions_checkout**](ArchitectApi.html#post_flows_actions_checkout) | Check-out flow|
|[**post_flows_actions_deactivate**](ArchitectApi.html#post_flows_actions_deactivate) | Deactivate flow|
|[**post_flows_actions_publish**](ArchitectApi.html#post_flows_actions_publish) | Publish flow|
|[**post_flows_actions_revert**](ArchitectApi.html#post_flows_actions_revert) | Revert flow|
|[**post_flows_actions_unlock**](ArchitectApi.html#post_flows_actions_unlock) | Unlock flow|
|[**put_architect_prompt**](ArchitectApi.html#put_architect_prompt) | Update specified user prompt|
|[**put_architect_prompt_resource**](ArchitectApi.html#put_architect_prompt_resource) | Update specified user prompt resource|
|[**put_architect_systemprompt_resource**](ArchitectApi.html#put_architect_systemprompt_resource) | Updates a system prompt resource override.|
|[**put_flow**](ArchitectApi.html#put_flow) | Update flow|
{: class="table table-striped"}

<a name="delete_architect_prompt"></a>

##  delete_architect_prompt(prompt_id, all_resources=all_resources)

Delete specified user prompt



Wraps DELETE /api/v2/architect/prompts/{promptId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
all_resources = true # bool | Whether or not to delete all the prompt resources (optional)

try:
    # Delete specified user prompt
    api_instance.delete_architect_prompt(prompt_id, all_resources=all_resources)
except ApiException as e:
    print "Exception when calling ArchitectApi->delete_architect_prompt: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **all_resources** | **bool**| Whether or not to delete all the prompt resources | [optional] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_prompt_resource"></a>

##  delete_architect_prompt_resource(prompt_id, language_code)

Delete specified user prompt resource



Wraps DELETE /api/v2/architect/prompts/{promptId}/resources/{languageCode} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Delete specified user prompt resource
    api_instance.delete_architect_prompt_resource(prompt_id, language_code)
except ApiException as e:
    print "Exception when calling ArchitectApi->delete_architect_prompt_resource: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **language_code** | **str**| Language | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_prompts"></a>

## [**Operation**](Operation.html) delete_architect_prompts(id)

Batch-delete a list of prompts

Multiple IDs can be specified, in which case all specified prompts will be deleted.  Asynchronous.  Notification topic: v2.architect.prompts.{promptId}

Wraps DELETE /api/v2/architect/prompts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = ['id_example'] # list[str] | List of Prompt IDs

try:
    # Batch-delete a list of prompts
    api_response = api_instance.delete_architect_prompts(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->delete_architect_prompts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| List of Prompt IDs | |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="delete_architect_systemprompt_resource"></a>

##  delete_architect_systemprompt_resource(prompt_id, language_code)

Delete a system prompt resource override.



Wraps DELETE /api/v2/architect/systemprompts/{promptId}/resources/{languageCode} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Delete a system prompt resource override.
    api_instance.delete_architect_systemprompt_resource(prompt_id, language_code)
except ApiException as e:
    print "Exception when calling ArchitectApi->delete_architect_systemprompt_resource: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **language_code** | **str**| Language | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_flow"></a>

##  delete_flow(flow_id)

Delete flow



Wraps DELETE /api/v2/flows/{flowId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID

try:
    # Delete flow
    api_instance.delete_flow(flow_id)
except ApiException as e:
    print "Exception when calling ArchitectApi->delete_flow: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_flows"></a>

## [**Operation**](Operation.html) delete_flows(id)

Batch-delete a list of flows

Multiple IDs can be specified, in which case all specified flows will be deleted.  Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps DELETE /api/v2/flows 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = ['id_example'] # list[str] | List of Flow IDs

try:
    # Batch-delete a list of flows
    api_response = api_instance.delete_flows(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->delete_flows: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| List of Flow IDs | |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="get_architect_dependencytracking"></a>

## [**DependencyObjectEntityListing**](DependencyObjectEntityListing.html) get_architect_dependencytracking(name, page_number=page_number, page_size=page_size, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type)

Get Dependency Tracking objects that have a given display name



Wraps GET /api/v2/architect/dependencytracking 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
name = 'name_example' # str | Object name to search for
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
object_type = ['object_type_example'] # list[str] | Object type(s) to search for (optional)
consumed_resources = true # bool | Include resources each result item consumes (optional)
consuming_resources = true # bool | Include resources that consume each result item (optional)
consumed_resource_type = ['consumed_resource_type_example'] # list[str] | Types of consumed resources to return, if consumed resources are requested (optional)
consuming_resource_type = ['consuming_resource_type_example'] # list[str] | Types of consuming resources to return, if consuming resources are requested (optional)

try:
    # Get Dependency Tracking objects that have a given display name
    api_response = api_instance.get_architect_dependencytracking(name, page_number=page_number, page_size=page_size, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Object name to search for | |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **object_type** | [**list[str]**](str.html)| Object type(s) to search for | [optional] |
| **consumed_resources** | **bool**| Include resources each result item consumes | [optional] |
| **consuming_resources** | **bool**| Include resources that consume each result item | [optional] |
| **consumed_resource_type** | [**list[str]**](str.html)| Types of consumed resources to return, if consumed resources are requested | [optional] |
| **consuming_resource_type** | [**list[str]**](str.html)| Types of consuming resources to return, if consuming resources are requested | [optional] |
{: class="table table-striped"}

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing.html)

<a name="get_architect_dependencytracking_build"></a>

## [**DependencyStatus**](DependencyStatus.html) get_architect_dependencytracking_build()

Get Dependency Tracking build status for an organization



Wraps GET /api/v2/architect/dependencytracking/build 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()

try:
    # Get Dependency Tracking build status for an organization
    api_response = api_instance.get_architect_dependencytracking_build()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_build: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**DependencyStatus**](DependencyStatus.html)

<a name="get_architect_dependencytracking_consumedresources"></a>

## [**ConsumedResourcesEntityListing**](ConsumedResourcesEntityListing.html) get_architect_dependencytracking_consumedresources(id, version, object_type, resource_type=resource_type)

Get resources that are consumed by a given Dependency Tracking object



Wraps GET /api/v2/architect/dependencytracking/consumedresources 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = 'id_example' # str | Consuming object ID
version = 'version_example' # str | Consuming object version
object_type = 'object_type_example' # str | Consuming object type
resource_type = ['resource_type_example'] # list[str] | Types of consumed resources to show (optional)

try:
    # Get resources that are consumed by a given Dependency Tracking object
    api_response = api_instance.get_architect_dependencytracking_consumedresources(id, version, object_type, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_consumedresources: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | **str**| Consuming object ID | |
| **version** | **str**| Consuming object version | |
| **object_type** | **str**| Consuming object type | |
| **resource_type** | [**list[str]**](str.html)| Types of consumed resources to show | [optional] |
{: class="table table-striped"}

### Return type

[**ConsumedResourcesEntityListing**](ConsumedResourcesEntityListing.html)

<a name="get_architect_dependencytracking_consumingresources"></a>

## [**ConsumingResourcesEntityListing**](ConsumingResourcesEntityListing.html) get_architect_dependencytracking_consumingresources(id, object_type, resource_type=resource_type)

Get resources that consume a given Dependency Tracking object



Wraps GET /api/v2/architect/dependencytracking/consumingresources 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = 'id_example' # str | Consumed object ID
object_type = 'object_type_example' # str | Consumed object type (only versioned object types are valid)
resource_type = ['resource_type_example'] # list[str] | Types of consuming resources to show (optional)

try:
    # Get resources that consume a given Dependency Tracking object
    api_response = api_instance.get_architect_dependencytracking_consumingresources(id, object_type, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_consumingresources: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | **str**| Consumed object ID | |
| **object_type** | **str**| Consumed object type (only versioned object types are valid) | |
| **resource_type** | [**list[str]**](str.html)| Types of consuming resources to show | [optional] |
{: class="table table-striped"}

### Return type

[**ConsumingResourcesEntityListing**](ConsumingResourcesEntityListing.html)

<a name="get_architect_dependencytracking_deletedresourceconsumers"></a>

## [**DependencyObjectEntityListing**](DependencyObjectEntityListing.html) get_architect_dependencytracking_deletedresourceconsumers(name=name, object_type=object_type, flow_filter=flow_filter, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)

Get Dependency Tracking objects that consume deleted resources



Wraps GET /api/v2/architect/dependencytracking/deletedresourceconsumers 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
name = 'name_example' # str | Name to search for (optional)
object_type = ['object_type_example'] # list[str] | Object type(s) to search for (optional)
flow_filter = 'flow_filter_example' # str | Show only checkedIn or published flows (optional)
consumed_resources = false # bool | Return consumed resources? (optional) (default to false)
consumed_resource_type = ['consumed_resource_type_example'] # list[str] | Resource type(s) to return (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get Dependency Tracking objects that consume deleted resources
    api_response = api_instance.get_architect_dependencytracking_deletedresourceconsumers(name=name, object_type=object_type, flow_filter=flow_filter, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_deletedresourceconsumers: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Name to search for | [optional] |
| **object_type** | [**list[str]**](str.html)| Object type(s) to search for | [optional] |
| **flow_filter** | **str**| Show only checkedIn or published flows | [optional] |
| **consumed_resources** | **bool**| Return consumed resources? | [optional] [default to false]|
| **consumed_resource_type** | [**list[str]**](str.html)| Resource type(s) to return | [optional] |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing.html)

<a name="get_architect_dependencytracking_object"></a>

## [**DependencyObject**](DependencyObject.html) get_architect_dependencytracking_object(id, version=version, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type)

Get a Dependency Tracking object



Wraps GET /api/v2/architect/dependencytracking/object 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = 'id_example' # str | Object ID
version = 'version_example' # str | Object version (optional)
object_type = 'object_type_example' # str | Object type (optional)
consumed_resources = true # bool | Include resources this item consumes (optional)
consuming_resources = true # bool | Include resources that consume this item (optional)
consumed_resource_type = ['consumed_resource_type_example'] # list[str] | Types of consumed resources to return, if consumed resources are requested (optional)
consuming_resource_type = ['consuming_resource_type_example'] # list[str] | Types of consuming resources to return, if consuming resources are requested (optional)

try:
    # Get a Dependency Tracking object
    api_response = api_instance.get_architect_dependencytracking_object(id, version=version, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_object: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | **str**| Object ID | |
| **version** | **str**| Object version | [optional] |
| **object_type** | **str**| Object type | [optional] |
| **consumed_resources** | **bool**| Include resources this item consumes | [optional] |
| **consuming_resources** | **bool**| Include resources that consume this item | [optional] |
| **consumed_resource_type** | [**list[str]**](str.html)| Types of consumed resources to return, if consumed resources are requested | [optional] |
| **consuming_resource_type** | [**list[str]**](str.html)| Types of consuming resources to return, if consuming resources are requested | [optional] |
{: class="table table-striped"}

### Return type

[**DependencyObject**](DependencyObject.html)

<a name="get_architect_dependencytracking_type"></a>

## [**DependencyType**](DependencyType.html) get_architect_dependencytracking_type(type_id)

Get a Dependency Tracking type.



Wraps GET /api/v2/architect/dependencytracking/types/{typeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
type_id = 'type_id_example' # str | Type ID

try:
    # Get a Dependency Tracking type.
    api_response = api_instance.get_architect_dependencytracking_type(type_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_type: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type_id** | **str**| Type ID | |
{: class="table table-striped"}

### Return type

[**DependencyType**](DependencyType.html)

<a name="get_architect_dependencytracking_types"></a>

## [**DependencyTypeEntityListing**](DependencyTypeEntityListing.html) get_architect_dependencytracking_types(page_number=page_number, page_size=page_size)

Get Dependency Tracking types.



Wraps GET /api/v2/architect/dependencytracking/types 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get Dependency Tracking types.
    api_response = api_instance.get_architect_dependencytracking_types(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_types: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**DependencyTypeEntityListing**](DependencyTypeEntityListing.html)

<a name="get_architect_dependencytracking_updatedresourceconsumers"></a>

## [**DependencyObjectEntityListing**](DependencyObjectEntityListing.html) get_architect_dependencytracking_updatedresourceconsumers(name=name, object_type=object_type, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)

Get Dependency Tracking objects that depend on updated resources



Wraps GET /api/v2/architect/dependencytracking/updatedresourceconsumers 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
name = 'name_example' # str | Name to search for (optional)
object_type = ['object_type_example'] # list[str] | Object type(s) to search for (optional)
consumed_resources = false # bool | Return consumed resources? (optional) (default to false)
consumed_resource_type = ['consumed_resource_type_example'] # list[str] | Resource type(s) to return (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get Dependency Tracking objects that depend on updated resources
    api_response = api_instance.get_architect_dependencytracking_updatedresourceconsumers(name=name, object_type=object_type, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_dependencytracking_updatedresourceconsumers: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Name to search for | [optional] |
| **object_type** | [**list[str]**](str.html)| Object type(s) to search for | [optional] |
| **consumed_resources** | **bool**| Return consumed resources? | [optional] [default to false]|
| **consumed_resource_type** | [**list[str]**](str.html)| Resource type(s) to return | [optional] |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing.html)

<a name="get_architect_prompt"></a>

## [**Prompt**](Prompt.html) get_architect_prompt(prompt_id)

Get specified user prompt



Wraps GET /api/v2/architect/prompts/{promptId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID

try:
    # Get specified user prompt
    api_response = api_instance.get_architect_prompt(prompt_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_prompt: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
{: class="table table-striped"}

### Return type

[**Prompt**](Prompt.html)

<a name="get_architect_prompt_resource"></a>

## [**PromptAsset**](PromptAsset.html) get_architect_prompt_resource(prompt_id, language_code)

Get specified user prompt resource



Wraps GET /api/v2/architect/prompts/{promptId}/resources/{languageCode} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Get specified user prompt resource
    api_response = api_instance.get_architect_prompt_resource(prompt_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_prompt_resource: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **language_code** | **str**| Language | |
{: class="table table-striped"}

### Return type

[**PromptAsset**](PromptAsset.html)

<a name="get_architect_prompt_resources"></a>

## [**PromptAssetEntityListing**](PromptAssetEntityListing.html) get_architect_prompt_resources(prompt_id, page_number=page_number, page_size=page_size)

Get a pageable list of user prompt resources

The returned list is pageable, and query parameters can be used for filtering.

Wraps GET /api/v2/architect/prompts/{promptId}/resources 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a pageable list of user prompt resources
    api_response = api_instance.get_architect_prompt_resources(prompt_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_prompt_resources: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**PromptAssetEntityListing**](PromptAssetEntityListing.html)

<a name="get_architect_prompts"></a>

## [**PromptEntityListing**](PromptEntityListing.html) get_architect_prompts(page_number=page_number, page_size=page_size, name=name, description=description, name_or_description=name_or_description)

Get a pageable list of user prompts

The returned list is pageable, and query parameters can be used for filtering.  Multiple names can be specified, in which case all matching prompts will be returned, and no other filters will be evaluated.

Wraps GET /api/v2/architect/prompts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)

try:
    # Get a pageable list of user prompts
    api_response = api_instance.get_architect_prompts(page_number=page_number, page_size=page_size, name=name, description=description, name_or_description=name_or_description)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_prompts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **name** | **str**| Name | [optional] |
| **description** | **str**| Description | [optional] |
| **name_or_description** | **str**| Name or description | [optional] |
{: class="table table-striped"}

### Return type

[**PromptEntityListing**](PromptEntityListing.html)

<a name="get_architect_systemprompt"></a>

## [**SystemPrompt**](SystemPrompt.html) get_architect_systemprompt(prompt_id)

Get a system prompt



Wraps GET /api/v2/architect/systemprompts/{promptId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | promptId

try:
    # Get a system prompt
    api_response = api_instance.get_architect_systemprompt(prompt_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_systemprompt: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| promptId | |
{: class="table table-striped"}

### Return type

[**SystemPrompt**](SystemPrompt.html)

<a name="get_architect_systemprompt_resource"></a>

## [**SystemPromptAsset**](SystemPromptAsset.html) get_architect_systemprompt_resource(prompt_id, language_code)

Get a system prompt resource.



Wraps GET /api/v2/architect/systemprompts/{promptId}/resources/{languageCode} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Get a system prompt resource.
    api_response = api_instance.get_architect_systemprompt_resource(prompt_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_systemprompt_resource: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **language_code** | **str**| Language | |
{: class="table table-striped"}

### Return type

[**SystemPromptAsset**](SystemPromptAsset.html)

<a name="get_architect_systemprompt_resources"></a>

## [**SystemPromptAssetEntityListing**](SystemPromptAssetEntityListing.html) get_architect_systemprompt_resources(prompt_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order)

Get system prompt resources.



Wraps GET /api/v2/architect/systemprompts/{promptId}/resources 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)

try:
    # Get system prompt resources.
    api_response = api_instance.get_architect_systemprompt_resources(prompt_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_systemprompt_resources: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **sort_by** | **str**| Sort by | [optional] [default to id]|
| **sort_order** | **str**| Sort order | [optional] [default to asc]|
{: class="table table-striped"}

### Return type

[**SystemPromptAssetEntityListing**](SystemPromptAssetEntityListing.html)

<a name="get_architect_systemprompts"></a>

## [**SystemPromptEntityListing**](SystemPromptEntityListing.html) get_architect_systemprompts(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, description=description, name_or_description=name_or_description)

Get System Prompts



Wraps GET /api/v2/architect/systemprompts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)

try:
    # Get System Prompts
    api_response = api_instance.get_architect_systemprompts(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, description=description, name_or_description=name_or_description)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_architect_systemprompts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **sort_by** | **str**| Sort by | [optional] [default to id]|
| **sort_order** | **str**| Sort order | [optional] [default to asc]|
| **name** | **str**| Name | [optional] |
| **description** | **str**| Description | [optional] |
| **name_or_description** | **str**| Name or description | [optional] |
{: class="table table-striped"}

### Return type

[**SystemPromptEntityListing**](SystemPromptEntityListing.html)

<a name="get_flow"></a>

## [**Flow**](Flow.html) get_flow(flow_id, deleted=deleted)

Get flow



Wraps GET /api/v2/flows/{flowId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
deleted = false # bool | Include deleted flows (optional) (default to false)

try:
    # Get flow
    api_response = api_instance.get_flow(flow_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_flow: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **deleted** | **bool**| Include deleted flows | [optional] [default to false]|
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="get_flow_latestconfiguration"></a>

## object** get_flow_latestconfiguration(flow_id, deleted=deleted)

Get the latest configuration for flow



Wraps GET /api/v2/flows/{flowId}/latestconfiguration 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
deleted = false # bool | Include deleted flows (optional) (default to false)

try:
    # Get the latest configuration for flow
    api_response = api_instance.get_flow_latestconfiguration(flow_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_flow_latestconfiguration: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **deleted** | **bool**| Include deleted flows | [optional] [default to false]|
{: class="table table-striped"}

### Return type

**object**

<a name="get_flow_version"></a>

## [**FlowVersion**](FlowVersion.html) get_flow_version(flow_id, version_id, deleted=deleted)

Get flow version



Wraps GET /api/v2/flows/{flowId}/versions/{versionId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
version_id = 'version_id_example' # str | Version ID
deleted = 'deleted_example' # str | Include deleted flows (optional)

try:
    # Get flow version
    api_response = api_instance.get_flow_version(flow_id, version_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_flow_version: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **version_id** | **str**| Version ID | |
| **deleted** | **str**| Include deleted flows | [optional] |
{: class="table table-striped"}

### Return type

[**FlowVersion**](FlowVersion.html)

<a name="get_flow_version_configuration"></a>

## object** get_flow_version_configuration(flow_id, version_id, deleted=deleted)

Create flow version configuration



Wraps GET /api/v2/flows/{flowId}/versions/{versionId}/configuration 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
version_id = 'version_id_example' # str | Version ID
deleted = 'deleted_example' # str | Include deleted flows (optional)

try:
    # Create flow version configuration
    api_response = api_instance.get_flow_version_configuration(flow_id, version_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_flow_version_configuration: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **version_id** | **str**| Version ID | |
| **deleted** | **str**| Include deleted flows | [optional] |
{: class="table table-striped"}

### Return type

**object**

<a name="get_flow_versions"></a>

## [**FlowVersionEntityListing**](FlowVersionEntityListing.html) get_flow_versions(flow_id, page_number=page_number, page_size=page_size, deleted=deleted)

Get flow version list



Wraps GET /api/v2/flows/{flowId}/versions 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
deleted = true # bool | Include deleted flows (optional)

try:
    # Get flow version list
    api_response = api_instance.get_flow_versions(flow_id, page_number=page_number, page_size=page_size, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_flow_versions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **deleted** | **bool**| Include deleted flows | [optional] |
{: class="table table-striped"}

### Return type

[**FlowVersionEntityListing**](FlowVersionEntityListing.html)

<a name="get_flows"></a>

## [**FlowEntityListing**](FlowEntityListing.html) get_flows(type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, publish_version_id=publish_version_id, editable_by=editable_by, locked_by=locked_by, secure=secure, deleted=deleted, include_schemas=include_schemas)

Get a pageable list of flows, filtered by query parameters

Multiple IDs can be specified, in which case all matching flows will be returned, and no other parameters will be evaluated.

Wraps GET /api/v2/flows 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
type = 'type_example' # str | Type
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
publish_version_id = 'publish_version_id_example' # str | Publish version ID (optional)
editable_by = 'editable_by_example' # str | Editable by (optional)
locked_by = 'locked_by_example' # str | Locked by (optional)
secure = 'secure_example' # str | Secure (optional)
deleted = false # bool | Include deleted (optional) (default to false)
include_schemas = false # bool | Include variable schemas (optional) (default to false)

try:
    # Get a pageable list of flows, filtered by query parameters
    api_response = api_instance.get_flows(type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, publish_version_id=publish_version_id, editable_by=editable_by, locked_by=locked_by, secure=secure, deleted=deleted, include_schemas=include_schemas)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->get_flows: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Type | |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **sort_by** | **str**| Sort by | [optional] [default to id]|
| **sort_order** | **str**| Sort order | [optional] [default to asc]|
| **id** | [**list[str]**](str.html)| ID | [optional] |
| **name** | **str**| Name | [optional] |
| **description** | **str**| Description | [optional] |
| **name_or_description** | **str**| Name or description | [optional] |
| **publish_version_id** | **str**| Publish version ID | [optional] |
| **editable_by** | **str**| Editable by | [optional] |
| **locked_by** | **str**| Locked by | [optional] |
| **secure** | **str**| Secure | [optional] |
| **deleted** | **bool**| Include deleted | [optional] [default to false]|
| **include_schemas** | **bool**| Include variable schemas | [optional] [default to false]|
{: class="table table-striped"}

### Return type

[**FlowEntityListing**](FlowEntityListing.html)

<a name="post_architect_dependencytracking_build"></a>

##  post_architect_dependencytracking_build()

Rebuild Dependency Tracking data for an organization

Asynchronous.  Notification topic: v2.architect.dependencytracking.build

Wraps POST /api/v2/architect/dependencytracking/build 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()

try:
    # Rebuild Dependency Tracking data for an organization
    api_instance.post_architect_dependencytracking_build()
except ApiException as e:
    print "Exception when calling ArchitectApi->post_architect_dependencytracking_build: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_architect_prompt_resources"></a>

## [**PromptAsset**](PromptAsset.html) post_architect_prompt_resources(prompt_id, body=body)

Create a new user prompt resource



Wraps POST /api/v2/architect/prompts/{promptId}/resources 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
body = PureCloudPlatformClientV2.PromptAssetCreate() # PromptAssetCreate |  (optional)

try:
    # Create a new user prompt resource
    api_response = api_instance.post_architect_prompt_resources(prompt_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_architect_prompt_resources: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **body** | [**PromptAssetCreate**](PromptAssetCreate.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**PromptAsset**](PromptAsset.html)

<a name="post_architect_prompts"></a>

## [**Prompt**](Prompt.html) post_architect_prompts(body=body)

Create a new user prompt



Wraps POST /api/v2/architect/prompts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.Prompt() # Prompt |  (optional)

try:
    # Create a new user prompt
    api_response = api_instance.post_architect_prompts(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_architect_prompts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Prompt**](Prompt.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**Prompt**](Prompt.html)

<a name="post_architect_systemprompt_resources"></a>

## [**SystemPromptAsset**](SystemPromptAsset.html) post_architect_systemprompt_resources(prompt_id, body=body)

Create system prompt resource override.



Wraps POST /api/v2/architect/systemprompts/{promptId}/resources 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
body = PureCloudPlatformClientV2.SystemPromptAsset() # SystemPromptAsset |  (optional)

try:
    # Create system prompt resource override.
    api_response = api_instance.post_architect_systemprompt_resources(prompt_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_architect_systemprompt_resources: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **body** | [**SystemPromptAsset**](SystemPromptAsset.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**SystemPromptAsset**](SystemPromptAsset.html)

<a name="post_flow_versions"></a>

## [**FlowVersion**](FlowVersion.html) post_flow_versions(flow_id, body=body)

Create flow version



Wraps POST /api/v2/flows/{flowId}/versions 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
body = NULL # object |  (optional)

try:
    # Create flow version
    api_response = api_instance.post_flow_versions(flow_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flow_versions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **body** | **object**|  | [optional] |
{: class="table table-striped"}

### Return type

[**FlowVersion**](FlowVersion.html)

<a name="post_flows"></a>

## [**Flow**](Flow.html) post_flows(body=body)

Create flow



Wraps POST /api/v2/flows 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.Flow() # Flow |  (optional)

try:
    # Create flow
    api_response = api_instance.post_flows(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Flow**](Flow.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_checkin"></a>

## [**Flow**](Flow.html) post_flows_actions_checkin(flow)

Check-in flow

Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps POST /api/v2/flows/actions/checkin 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Check-in flow
    api_response = api_instance.post_flows_actions_checkin(flow)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows_actions_checkin: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID | |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_checkout"></a>

## [**Flow**](Flow.html) post_flows_actions_checkout(flow)

Check-out flow



Wraps POST /api/v2/flows/actions/checkout 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Check-out flow
    api_response = api_instance.post_flows_actions_checkout(flow)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows_actions_checkout: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID | |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_deactivate"></a>

## [**Flow**](Flow.html) post_flows_actions_deactivate(flow)

Deactivate flow



Wraps POST /api/v2/flows/actions/deactivate 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Deactivate flow
    api_response = api_instance.post_flows_actions_deactivate(flow)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows_actions_deactivate: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID | |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_publish"></a>

## [**Operation**](Operation.html) post_flows_actions_publish(flow, version=version)

Publish flow

Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps POST /api/v2/flows/actions/publish 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID
version = 'version_example' # str | version (optional)

try:
    # Publish flow
    api_response = api_instance.post_flows_actions_publish(flow, version=version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows_actions_publish: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID | |
| **version** | **str**| version | [optional] |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="post_flows_actions_revert"></a>

## [**Flow**](Flow.html) post_flows_actions_revert(flow)

Revert flow



Wraps POST /api/v2/flows/actions/revert 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Revert flow
    api_response = api_instance.post_flows_actions_revert(flow)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows_actions_revert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID | |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_unlock"></a>

## [**Flow**](Flow.html) post_flows_actions_unlock(flow)

Unlock flow

Allows for unlocking a flow in the case where there is no flow configuration available, and thus a check-in will not unlock the flow. The user must have Architect Admin permissions to perform this action.

Wraps POST /api/v2/flows/actions/unlock 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Unlock flow
    api_response = api_instance.post_flows_actions_unlock(flow)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->post_flows_actions_unlock: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID | |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="put_architect_prompt"></a>

## [**Prompt**](Prompt.html) put_architect_prompt(prompt_id, body=body)

Update specified user prompt



Wraps PUT /api/v2/architect/prompts/{promptId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
body = PureCloudPlatformClientV2.Prompt() # Prompt |  (optional)

try:
    # Update specified user prompt
    api_response = api_instance.put_architect_prompt(prompt_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->put_architect_prompt: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **body** | [**Prompt**](Prompt.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**Prompt**](Prompt.html)

<a name="put_architect_prompt_resource"></a>

## [**PromptAsset**](PromptAsset.html) put_architect_prompt_resource(prompt_id, language_code, body=body)

Update specified user prompt resource



Wraps PUT /api/v2/architect/prompts/{promptId}/resources/{languageCode} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.PromptAsset() # PromptAsset |  (optional)

try:
    # Update specified user prompt resource
    api_response = api_instance.put_architect_prompt_resource(prompt_id, language_code, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->put_architect_prompt_resource: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **language_code** | **str**| Language | |
| **body** | [**PromptAsset**](PromptAsset.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**PromptAsset**](PromptAsset.html)

<a name="put_architect_systemprompt_resource"></a>

## [**SystemPromptAsset**](SystemPromptAsset.html) put_architect_systemprompt_resource(prompt_id, language_code, body=body)

Updates a system prompt resource override.



Wraps PUT /api/v2/architect/systemprompts/{promptId}/resources/{languageCode} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.SystemPromptAsset() # SystemPromptAsset |  (optional)

try:
    # Updates a system prompt resource override.
    api_response = api_instance.put_architect_systemprompt_resource(prompt_id, language_code, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->put_architect_systemprompt_resource: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID | |
| **language_code** | **str**| Language | |
| **body** | [**SystemPromptAsset**](SystemPromptAsset.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**SystemPromptAsset**](SystemPromptAsset.html)

<a name="put_flow"></a>

## [**Flow**](Flow.html) put_flow(flow_id, body=body)

Update flow



Wraps PUT /api/v2/flows/{flowId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
body = PureCloudPlatformClientV2.Flow() # Flow |  (optional)

try:
    # Update flow
    api_response = api_instance.put_flow(flow_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ArchitectApi->put_flow: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID | |
| **body** | [**Flow**](Flow.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

