---
title: ArchitectApi
---

## PureCloudPlatformClientV2.ArchitectApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_architect_emergencygroup**](ArchitectApi.html#delete_architect_emergencygroup) | Deletes a emergency group by ID|
|[**delete_architect_ivr**](ArchitectApi.html#delete_architect_ivr) | Delete an IVR Config.|
|[**delete_architect_prompt**](ArchitectApi.html#delete_architect_prompt) | Delete specified user prompt|
|[**delete_architect_prompt_resource**](ArchitectApi.html#delete_architect_prompt_resource) | Delete specified user prompt resource|
|[**delete_architect_prompt_resource_audio**](ArchitectApi.html#delete_architect_prompt_resource_audio) | Delete specified user prompt resource audio|
|[**delete_architect_prompts**](ArchitectApi.html#delete_architect_prompts) | Batch-delete a list of prompts|
|[**delete_architect_schedule**](ArchitectApi.html#delete_architect_schedule) | Delete a schedule by id|
|[**delete_architect_schedulegroup**](ArchitectApi.html#delete_architect_schedulegroup) | Deletes a schedule group by ID|
|[**delete_architect_systemprompt_resource**](ArchitectApi.html#delete_architect_systemprompt_resource) | Delete a system prompt resource override.|
|[**delete_flow**](ArchitectApi.html#delete_flow) | Delete flow|
|[**delete_flows**](ArchitectApi.html#delete_flows) | Batch-delete a list of flows|
|[**delete_flows_datatable**](ArchitectApi.html#delete_flows_datatable) | deletes a specific datatable by id|
|[**delete_flows_datatable_row**](ArchitectApi.html#delete_flows_datatable_row) | Delete a row entry|
|[**delete_flows_milestone**](ArchitectApi.html#delete_flows_milestone) | Delete a flow milestone.|
|[**get_architect_dependencytracking**](ArchitectApi.html#get_architect_dependencytracking) | Get Dependency Tracking objects that have a given display name|
|[**get_architect_dependencytracking_build**](ArchitectApi.html#get_architect_dependencytracking_build) | Get Dependency Tracking build status for an organization|
|[**get_architect_dependencytracking_consumedresources**](ArchitectApi.html#get_architect_dependencytracking_consumedresources) | Get resources that are consumed by a given Dependency Tracking object|
|[**get_architect_dependencytracking_consumingresources**](ArchitectApi.html#get_architect_dependencytracking_consumingresources) | Get resources that consume a given Dependency Tracking object|
|[**get_architect_dependencytracking_deletedresourceconsumers**](ArchitectApi.html#get_architect_dependencytracking_deletedresourceconsumers) | Get Dependency Tracking objects that consume deleted resources|
|[**get_architect_dependencytracking_object**](ArchitectApi.html#get_architect_dependencytracking_object) | Get a Dependency Tracking object|
|[**get_architect_dependencytracking_type**](ArchitectApi.html#get_architect_dependencytracking_type) | Get a Dependency Tracking type.|
|[**get_architect_dependencytracking_types**](ArchitectApi.html#get_architect_dependencytracking_types) | Get Dependency Tracking types.|
|[**get_architect_dependencytracking_updatedresourceconsumers**](ArchitectApi.html#get_architect_dependencytracking_updatedresourceconsumers) | Get Dependency Tracking objects that depend on updated resources|
|[**get_architect_emergencygroup**](ArchitectApi.html#get_architect_emergencygroup) | Gets a emergency group by ID|
|[**get_architect_emergencygroups**](ArchitectApi.html#get_architect_emergencygroups) | Get a list of emergency groups.|
|[**get_architect_ivr**](ArchitectApi.html#get_architect_ivr) | Get an IVR config.|
|[**get_architect_ivrs**](ArchitectApi.html#get_architect_ivrs) | Get IVR configs.|
|[**get_architect_prompt**](ArchitectApi.html#get_architect_prompt) | Get specified user prompt|
|[**get_architect_prompt_history_history_id**](ArchitectApi.html#get_architect_prompt_history_history_id) | Get generated prompt history|
|[**get_architect_prompt_resource**](ArchitectApi.html#get_architect_prompt_resource) | Get specified user prompt resource|
|[**get_architect_prompt_resources**](ArchitectApi.html#get_architect_prompt_resources) | Get a pageable list of user prompt resources|
|[**get_architect_prompts**](ArchitectApi.html#get_architect_prompts) | Get a pageable list of user prompts|
|[**get_architect_schedule**](ArchitectApi.html#get_architect_schedule) | Get a schedule by ID|
|[**get_architect_schedulegroup**](ArchitectApi.html#get_architect_schedulegroup) | Gets a schedule group by ID|
|[**get_architect_schedulegroups**](ArchitectApi.html#get_architect_schedulegroups) | Get a list of schedule groups.|
|[**get_architect_schedules**](ArchitectApi.html#get_architect_schedules) | Get a list of schedules.|
|[**get_architect_systemprompt**](ArchitectApi.html#get_architect_systemprompt) | Get a system prompt|
|[**get_architect_systemprompt_history_history_id**](ArchitectApi.html#get_architect_systemprompt_history_history_id) | Get generated prompt history|
|[**get_architect_systemprompt_resource**](ArchitectApi.html#get_architect_systemprompt_resource) | Get a system prompt resource.|
|[**get_architect_systemprompt_resources**](ArchitectApi.html#get_architect_systemprompt_resources) | Get system prompt resources.|
|[**get_architect_systemprompts**](ArchitectApi.html#get_architect_systemprompts) | Get System Prompts|
|[**get_flow**](ArchitectApi.html#get_flow) | Get flow|
|[**get_flow_history_history_id**](ArchitectApi.html#get_flow_history_history_id) | Get generated flow history|
|[**get_flow_latestconfiguration**](ArchitectApi.html#get_flow_latestconfiguration) | Get the latest configuration for flow|
|[**get_flow_version**](ArchitectApi.html#get_flow_version) | Get flow version|
|[**get_flow_version_configuration**](ArchitectApi.html#get_flow_version_configuration) | Create flow version configuration|
|[**get_flow_versions**](ArchitectApi.html#get_flow_versions) | Get flow version list|
|[**get_flows**](ArchitectApi.html#get_flows) | Get a pageable list of flows, filtered by query parameters|
|[**get_flows_datatable**](ArchitectApi.html#get_flows_datatable) | Returns a specific datatable by id|
|[**get_flows_datatable_export_job**](ArchitectApi.html#get_flows_datatable_export_job) | Returns the state information about an export job|
|[**get_flows_datatable_import_job**](ArchitectApi.html#get_flows_datatable_import_job) | Returns the state information about an import job|
|[**get_flows_datatable_import_jobs**](ArchitectApi.html#get_flows_datatable_import_jobs) | Get all recent import jobs|
|[**get_flows_datatable_row**](ArchitectApi.html#get_flows_datatable_row) | Returns a specific row for the datatable|
|[**get_flows_datatable_rows**](ArchitectApi.html#get_flows_datatable_rows) | Returns the rows for the datatable with the given id|
|[**get_flows_datatables**](ArchitectApi.html#get_flows_datatables) | Retrieve a list of datatables for the org|
|[**get_flows_divisionviews**](ArchitectApi.html#get_flows_divisionviews) | Get a pageable list of basic flow information objects filterable by query parameters.|
|[**get_flows_execution**](ArchitectApi.html#get_flows_execution) | Get a flow execution&#39;s details. Flow execution details are available for several days after the flow is started.|
|[**get_flows_milestone**](ArchitectApi.html#get_flows_milestone) | Get a flow milestone|
|[**get_flows_milestones**](ArchitectApi.html#get_flows_milestones) | Get a pageable list of flow milestones, filtered by query parameters|
|[**get_flows_outcome**](ArchitectApi.html#get_flows_outcome) | Get a flow outcome|
|[**get_flows_outcomes**](ArchitectApi.html#get_flows_outcomes) | Get a pageable list of flow outcomes, filtered by query parameters|
|[**post_architect_dependencytracking_build**](ArchitectApi.html#post_architect_dependencytracking_build) | Rebuild Dependency Tracking data for an organization|
|[**post_architect_emergencygroups**](ArchitectApi.html#post_architect_emergencygroups) | Creates a new emergency group|
|[**post_architect_ivrs**](ArchitectApi.html#post_architect_ivrs) | Create IVR config.|
|[**post_architect_prompt_history**](ArchitectApi.html#post_architect_prompt_history) | Generate prompt history|
|[**post_architect_prompt_resources**](ArchitectApi.html#post_architect_prompt_resources) | Create a new user prompt resource|
|[**post_architect_prompts**](ArchitectApi.html#post_architect_prompts) | Create a new user prompt|
|[**post_architect_schedulegroups**](ArchitectApi.html#post_architect_schedulegroups) | Creates a new schedule group|
|[**post_architect_schedules**](ArchitectApi.html#post_architect_schedules) | Create a new schedule.|
|[**post_architect_systemprompt_history**](ArchitectApi.html#post_architect_systemprompt_history) | Generate system prompt history|
|[**post_architect_systemprompt_resources**](ArchitectApi.html#post_architect_systemprompt_resources) | Create system prompt resource override.|
|[**post_flow_versions**](ArchitectApi.html#post_flow_versions) | Create flow version|
|[**post_flows**](ArchitectApi.html#post_flows) | Create flow|
|[**post_flows_actions_checkin**](ArchitectApi.html#post_flows_actions_checkin) | Check-in flow|
|[**post_flows_actions_checkout**](ArchitectApi.html#post_flows_actions_checkout) | Check-out flow|
|[**post_flows_actions_deactivate**](ArchitectApi.html#post_flows_actions_deactivate) | Deactivate flow|
|[**post_flows_actions_publish**](ArchitectApi.html#post_flows_actions_publish) | Publish flow|
|[**post_flows_actions_revert**](ArchitectApi.html#post_flows_actions_revert) | Revert flow|
|[**post_flows_actions_unlock**](ArchitectApi.html#post_flows_actions_unlock) | Unlock flow|
|[**post_flows_datatable_export_jobs**](ArchitectApi.html#post_flows_datatable_export_jobs) | Begin an export process for exporting all rows from a datatable|
|[**post_flows_datatable_import_jobs**](ArchitectApi.html#post_flows_datatable_import_jobs) | Begin an import process for importing rows into a datatable|
|[**post_flows_datatable_rows**](ArchitectApi.html#post_flows_datatable_rows) | Create a new row entry for the datatable.|
|[**post_flows_datatables**](ArchitectApi.html#post_flows_datatables) | Create a new datatable with the specified json-schema definition|
|[**post_flows_executions**](ArchitectApi.html#post_flows_executions) | Launch an instance of a flow definition, for flow types that support it such as the &#39;workflow&#39; type.|
|[**post_flows_milestones**](ArchitectApi.html#post_flows_milestones) | Create a flow milestone|
|[**post_flows_outcomes**](ArchitectApi.html#post_flows_outcomes) | Create a flow outcome|
|[**put_architect_emergencygroup**](ArchitectApi.html#put_architect_emergencygroup) | Updates a emergency group by ID|
|[**put_architect_ivr**](ArchitectApi.html#put_architect_ivr) | Update an IVR Config.|
|[**put_architect_prompt**](ArchitectApi.html#put_architect_prompt) | Update specified user prompt|
|[**put_architect_prompt_resource**](ArchitectApi.html#put_architect_prompt_resource) | Update specified user prompt resource|
|[**put_architect_schedule**](ArchitectApi.html#put_architect_schedule) | Update schedule by ID|
|[**put_architect_schedulegroup**](ArchitectApi.html#put_architect_schedulegroup) | Updates a schedule group by ID|
|[**put_architect_systemprompt_resource**](ArchitectApi.html#put_architect_systemprompt_resource) | Updates a system prompt resource override.|
|[**put_flow**](ArchitectApi.html#put_flow) | Update flow|
|[**put_flows_datatable**](ArchitectApi.html#put_flows_datatable) | Updates a specific datatable by id|
|[**put_flows_datatable_row**](ArchitectApi.html#put_flows_datatable_row) | Update a row entry|
|[**put_flows_milestone**](ArchitectApi.html#put_flows_milestone) | Updates a flow milestone|
|[**put_flows_outcome**](ArchitectApi.html#put_flows_outcome) | Updates a flow outcome|
{: class="table table-striped"}

<a name="delete_architect_emergencygroup"></a>

##  delete_architect_emergencygroup(emergency_group_id)



Deletes a emergency group by ID



Wraps DELETE /api/v2/architect/emergencygroups/{emergencyGroupId} 

Requires ANY permissions: 

* routing:emergencyGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
emergency_group_id = 'emergency_group_id_example' # str | Emergency group ID

try:
    # Deletes a emergency group by ID
    api_instance.delete_architect_emergencygroup(emergency_group_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_emergencygroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **emergency_group_id** | **str**| Emergency group ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_ivr"></a>

##  delete_architect_ivr(ivr_id)



Delete an IVR Config.



Wraps DELETE /api/v2/architect/ivrs/{ivrId} 

Requires ANY permissions: 

* routing:callRoute:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
ivr_id = 'ivr_id_example' # str | IVR id

try:
    # Delete an IVR Config.
    api_instance.delete_architect_ivr(ivr_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_ivr: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ivr_id** | **str**| IVR id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_prompt"></a>

##  delete_architect_prompt(prompt_id, all_resources=all_resources)



Delete specified user prompt



Wraps DELETE /api/v2/architect/prompts/{promptId} 

Requires ALL permissions: 

* architect:userPrompt:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
all_resources = true # bool | Whether or not to delete all the prompt resources (optional)

try:
    # Delete specified user prompt
    api_instance.delete_architect_prompt(prompt_id, all_resources=all_resources)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_prompt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **all_resources** | **bool**| Whether or not to delete all the prompt resources | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_prompt_resource"></a>

##  delete_architect_prompt_resource(prompt_id, language_code)



Delete specified user prompt resource



Wraps DELETE /api/v2/architect/prompts/{promptId}/resources/{languageCode} 

Requires ALL permissions: 

* architect:userPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Delete specified user prompt resource
    api_instance.delete_architect_prompt_resource(prompt_id, language_code)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_prompt_resource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_prompt_resource_audio"></a>

##  delete_architect_prompt_resource_audio(prompt_id, language_code)



Delete specified user prompt resource audio



Wraps DELETE /api/v2/architect/prompts/{promptId}/resources/{languageCode}/audio 

Requires ALL permissions: 

* architect:userPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Delete specified user prompt resource audio
    api_instance.delete_architect_prompt_resource_audio(prompt_id, language_code)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_prompt_resource_audio: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_prompts"></a>

## [**Operation**](Operation.html) delete_architect_prompts(id)



Batch-delete a list of prompts

Multiple IDs can be specified, in which case all specified prompts will be deleted.  Asynchronous.  Notification topic: v2.architect.prompts.{promptId}

Wraps DELETE /api/v2/architect/prompts 

Requires ALL permissions: 

* architect:userPrompt:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = ['id_example'] # list[str] | List of Prompt IDs

try:
    # Batch-delete a list of prompts
    api_response = api_instance.delete_architect_prompts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_prompts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| List of Prompt IDs |  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="delete_architect_schedule"></a>

##  delete_architect_schedule(schedule_id)



Delete a schedule by id



Wraps DELETE /api/v2/architect/schedules/{scheduleId} 

Requires ANY permissions: 

* routing:schedule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Delete a schedule by id
    api_instance.delete_architect_schedule(schedule_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_schedulegroup"></a>

##  delete_architect_schedulegroup(schedule_group_id)



Deletes a schedule group by ID



Wraps DELETE /api/v2/architect/schedulegroups/{scheduleGroupId} 

Requires ANY permissions: 

* routing:scheduleGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
schedule_group_id = 'schedule_group_id_example' # str | Schedule group ID

try:
    # Deletes a schedule group by ID
    api_instance.delete_architect_schedulegroup(schedule_group_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_schedulegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_group_id** | **str**| Schedule group ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_architect_systemprompt_resource"></a>

##  delete_architect_systemprompt_resource(prompt_id, language_code)



Delete a system prompt resource override.



Wraps DELETE /api/v2/architect/systemprompts/{promptId}/resources/{languageCode} 

Requires ALL permissions: 

* architect:systemPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language

try:
    # Delete a system prompt resource override.
    api_instance.delete_architect_systemprompt_resource(prompt_id, language_code)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_systemprompt_resource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_flow"></a>

##  delete_flow(flow_id)



Delete flow



Wraps DELETE /api/v2/flows/{flowId} 

Requires ANY permissions: 

* architect:flow:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID

try:
    # Delete flow
    api_instance.delete_flow(flow_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flow: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_flows"></a>

## [**Operation**](Operation.html) delete_flows(id)



Batch-delete a list of flows

Multiple IDs can be specified, in which case all specified flows will be deleted.  Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps DELETE /api/v2/flows 

Requires ANY permissions: 

* architect:flow:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = ['id_example'] # list[str] | List of Flow IDs

try:
    # Batch-delete a list of flows
    api_response = api_instance.delete_flows(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| List of Flow IDs |  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="delete_flows_datatable"></a>

##  delete_flows_datatable(datatable_id, force=force)



deletes a specific datatable by id

Deletes an entire datatable (including the schema and data) with a given datatableId

Wraps DELETE /api/v2/flows/datatables/{datatableId} 

Requires ANY permissions: 

* architect:datatable:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
force = false # bool | force delete, even if in use (optional) (default to false)

try:
    # deletes a specific datatable by id
    api_instance.delete_flows_datatable(datatable_id, force=force)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flows_datatable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **force** | **bool**| force delete, even if in use | [optional] [default to false] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_flows_datatable_row"></a>

##  delete_flows_datatable_row(datatable_id, row_id)



Delete a row entry

Deletes a row with a given rowId (the value of the key field).

Wraps DELETE /api/v2/flows/datatables/{datatableId}/rows/{rowId} 

Requires ANY permissions: 

* architect:datatable:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
row_id = 'row_id_example' # str | the key for the row

try:
    # Delete a row entry
    api_instance.delete_flows_datatable_row(datatable_id, row_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flows_datatable_row: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **row_id** | **str**| the key for the row |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_flows_milestone"></a>

## [**Empty**](Empty.html) delete_flows_milestone(milestone_id)



Delete a flow milestone.



Wraps DELETE /api/v2/flows/milestones/{milestoneId} 

Requires ALL permissions: 

* architect:flowMilestone:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
milestone_id = 'milestone_id_example' # str | flow milestone ID

try:
    # Delete a flow milestone.
    api_response = api_instance.delete_flows_milestone(milestone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flows_milestone: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **milestone_id** | **str**| flow milestone ID |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="get_architect_dependencytracking"></a>

## [**DependencyObjectEntityListing**](DependencyObjectEntityListing.html) get_architect_dependencytracking(name, page_number=page_number, page_size=page_size, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type)



Get Dependency Tracking objects that have a given display name



Wraps GET /api/v2/architect/dependencytracking 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_dependencytracking: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Object name to search for |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **object_type** | [**list[str]**](str.html)| Object type(s) to search for | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **consumed_resources** | **bool**| Include resources each result item consumes | [optional]  |
| **consuming_resources** | **bool**| Include resources that consume each result item | [optional]  |
| **consumed_resource_type** | [**list[str]**](str.html)| Types of consumed resources to return, if consumed resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **consuming_resource_type** | [**list[str]**](str.html)| Types of consuming resources to return, if consuming resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
{: class="table table-striped"}

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing.html)

<a name="get_architect_dependencytracking_build"></a>

## [**DependencyStatus**](DependencyStatus.html) get_architect_dependencytracking_build()



Get Dependency Tracking build status for an organization



Wraps GET /api/v2/architect/dependencytracking/build 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()

try:
    # Get Dependency Tracking build status for an organization
    api_response = api_instance.get_architect_dependencytracking_build()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_build: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**DependencyStatus**](DependencyStatus.html)

<a name="get_architect_dependencytracking_consumedresources"></a>

## [**ConsumedResourcesEntityListing**](ConsumedResourcesEntityListing.html) get_architect_dependencytracking_consumedresources(id, version, object_type, resource_type=resource_type, page_number=page_number, page_size=page_size)



Get resources that are consumed by a given Dependency Tracking object



Wraps GET /api/v2/architect/dependencytracking/consumedresources 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = 'id_example' # str | Consuming object ID
version = 'version_example' # str | Consuming object version
object_type = 'object_type_example' # str | Consuming object type.  Only versioned types are allowed here.
resource_type = ['resource_type_example'] # list[str] | Types of consumed resources to show (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get resources that are consumed by a given Dependency Tracking object
    api_response = api_instance.get_architect_dependencytracking_consumedresources(id, version, object_type, resource_type=resource_type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_consumedresources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | **str**| Consuming object ID |  |
| **version** | **str**| Consuming object version |  |
| **object_type** | **str**| Consuming object type.  Only versioned types are allowed here. | <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **resource_type** | [**list[str]**](str.html)| Types of consumed resources to show | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ConsumedResourcesEntityListing**](ConsumedResourcesEntityListing.html)

<a name="get_architect_dependencytracking_consumingresources"></a>

## [**ConsumingResourcesEntityListing**](ConsumingResourcesEntityListing.html) get_architect_dependencytracking_consumingresources(id, object_type, resource_type=resource_type, version=version, page_number=page_number, page_size=page_size, flow_filter=flow_filter)



Get resources that consume a given Dependency Tracking object



Wraps GET /api/v2/architect/dependencytracking/consumingresources 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
id = 'id_example' # str | Consumed object ID
object_type = 'object_type_example' # str | Consumed object type
resource_type = ['resource_type_example'] # list[str] | Types of consuming resources to show.  Only versioned types are allowed here. (optional)
version = 'version_example' # str | Object version (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
flow_filter = 'flow_filter_example' # str | Show only checkedIn or published flows (optional)

try:
    # Get resources that consume a given Dependency Tracking object
    api_response = api_instance.get_architect_dependencytracking_consumingresources(id, object_type, resource_type=resource_type, version=version, page_number=page_number, page_size=page_size, flow_filter=flow_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_consumingresources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | **str**| Consumed object ID |  |
| **object_type** | **str**| Consumed object type | <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **resource_type** | [**list[str]**](str.html)| Types of consuming resources to show.  Only versioned types are allowed here. | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **version** | **str**| Object version | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **flow_filter** | **str**| Show only checkedIn or published flows | [optional] <br />**Values**: checkedIn, published |
{: class="table table-striped"}

### Return type

[**ConsumingResourcesEntityListing**](ConsumingResourcesEntityListing.html)

<a name="get_architect_dependencytracking_deletedresourceconsumers"></a>

## [**DependencyObjectEntityListing**](DependencyObjectEntityListing.html) get_architect_dependencytracking_deletedresourceconsumers(name=name, object_type=object_type, flow_filter=flow_filter, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)



Get Dependency Tracking objects that consume deleted resources



Wraps GET /api/v2/architect/dependencytracking/deletedresourceconsumers 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_deletedresourceconsumers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Name to search for | [optional]  |
| **object_type** | [**list[str]**](str.html)| Object type(s) to search for | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **flow_filter** | **str**| Show only checkedIn or published flows | [optional] <br />**Values**: checkedIn, published |
| **consumed_resources** | **bool**| Return consumed resources? | [optional] [default to false] |
| **consumed_resource_type** | [**list[str]**](str.html)| Resource type(s) to return | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing.html)

<a name="get_architect_dependencytracking_object"></a>

## [**DependencyObject**](DependencyObject.html) get_architect_dependencytracking_object(id, version=version, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type, consumed_resource_request=consumed_resource_request)



Get a Dependency Tracking object



Wraps GET /api/v2/architect/dependencytracking/object 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
consumed_resource_request = true # bool | Indicate that this is going to look up a consumed resource object (optional)

try:
    # Get a Dependency Tracking object
    api_response = api_instance.get_architect_dependencytracking_object(id, version=version, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type, consumed_resource_request=consumed_resource_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_object: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | **str**| Object ID |  |
| **version** | **str**| Object version | [optional]  |
| **object_type** | **str**| Object type | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **consumed_resources** | **bool**| Include resources this item consumes | [optional]  |
| **consuming_resources** | **bool**| Include resources that consume this item | [optional]  |
| **consumed_resource_type** | [**list[str]**](str.html)| Types of consumed resources to return, if consumed resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **consuming_resource_type** | [**list[str]**](str.html)| Types of consuming resources to return, if consuming resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **consumed_resource_request** | **bool**| Indicate that this is going to look up a consumed resource object | [optional]  |
{: class="table table-striped"}

### Return type

[**DependencyObject**](DependencyObject.html)

<a name="get_architect_dependencytracking_type"></a>

## [**DependencyType**](DependencyType.html) get_architect_dependencytracking_type(type_id)



Get a Dependency Tracking type.



Wraps GET /api/v2/architect/dependencytracking/types/{typeId} 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
type_id = 'type_id_example' # str | Type ID

try:
    # Get a Dependency Tracking type.
    api_response = api_instance.get_architect_dependencytracking_type(type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_type: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type_id** | **str**| Type ID |  |
{: class="table table-striped"}

### Return type

[**DependencyType**](DependencyType.html)

<a name="get_architect_dependencytracking_types"></a>

## [**DependencyTypeEntityListing**](DependencyTypeEntityListing.html) get_architect_dependencytracking_types(page_number=page_number, page_size=page_size)



Get Dependency Tracking types.



Wraps GET /api/v2/architect/dependencytracking/types 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_types: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**DependencyTypeEntityListing**](DependencyTypeEntityListing.html)

<a name="get_architect_dependencytracking_updatedresourceconsumers"></a>

## [**DependencyObjectEntityListing**](DependencyObjectEntityListing.html) get_architect_dependencytracking_updatedresourceconsumers(name=name, object_type=object_type, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)



Get Dependency Tracking objects that depend on updated resources



Wraps GET /api/v2/architect/dependencytracking/updatedresourceconsumers 

Requires ALL permissions: 

* architect:dependencyTracking:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_dependencytracking_updatedresourceconsumers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **name** | **str**| Name to search for | [optional]  |
| **object_type** | [**list[str]**](str.html)| Object type(s) to search for | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **consumed_resources** | **bool**| Return consumed resources? | [optional] [default to false] |
| **consumed_resource_type** | [**list[str]**](str.html)| Resource type(s) to return | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, BOTCONNECTORBOT, BOTCONNECTORBOTVERSION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GROUP, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, IVRCONFIGURATION, LANGUAGE, LEXBOT, LEXBOTALIAS, NLUDOMAIN, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, WIDGET, WORKFLOW |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing.html)

<a name="get_architect_emergencygroup"></a>

## [**EmergencyGroup**](EmergencyGroup.html) get_architect_emergencygroup(emergency_group_id)



Gets a emergency group by ID



Wraps GET /api/v2/architect/emergencygroups/{emergencyGroupId} 

Requires ANY permissions: 

* routing:emergencyGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
emergency_group_id = 'emergency_group_id_example' # str | Emergency group ID

try:
    # Gets a emergency group by ID
    api_response = api_instance.get_architect_emergencygroup(emergency_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_emergencygroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **emergency_group_id** | **str**| Emergency group ID |  |
{: class="table table-striped"}

### Return type

[**EmergencyGroup**](EmergencyGroup.html)

<a name="get_architect_emergencygroups"></a>

## [**EmergencyGroupListing**](EmergencyGroupListing.html) get_architect_emergencygroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)



Get a list of emergency groups.



Wraps GET /api/v2/architect/emergencygroups 

Requires ANY permissions: 

* routing:emergencyGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'name' # str | Sort by (optional) (default to name)
sort_order = 'ASC' # str | Sort order (optional) (default to ASC)
name = 'name_example' # str | Name of the Emergency Group to filter by. (optional)

try:
    # Get a list of emergency groups.
    api_response = api_instance.get_architect_emergencygroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_emergencygroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
| **sort_order** | **str**| Sort order | [optional] [default to ASC] |
| **name** | **str**| Name of the Emergency Group to filter by. | [optional]  |
{: class="table table-striped"}

### Return type

[**EmergencyGroupListing**](EmergencyGroupListing.html)

<a name="get_architect_ivr"></a>

## [**IVR**](IVR.html) get_architect_ivr(ivr_id)



Get an IVR config.



Wraps GET /api/v2/architect/ivrs/{ivrId} 

Requires ANY permissions: 

* routing:callRoute:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
ivr_id = 'ivr_id_example' # str | IVR id

try:
    # Get an IVR config.
    api_response = api_instance.get_architect_ivr(ivr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_ivr: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ivr_id** | **str**| IVR id |  |
{: class="table table-striped"}

### Return type

[**IVR**](IVR.html)

<a name="get_architect_ivrs"></a>

## [**IVREntityListing**](IVREntityListing.html) get_architect_ivrs(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)



Get IVR configs.



Wraps GET /api/v2/architect/ivrs 

Requires ANY permissions: 

* routing:callRoute:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'name' # str | Sort by (optional) (default to name)
sort_order = 'ASC' # str | Sort order (optional) (default to ASC)
name = 'name_example' # str | Name of the IVR to filter by. (optional)

try:
    # Get IVR configs.
    api_response = api_instance.get_architect_ivrs(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_ivrs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
| **sort_order** | **str**| Sort order | [optional] [default to ASC] |
| **name** | **str**| Name of the IVR to filter by. | [optional]  |
{: class="table table-striped"}

### Return type

[**IVREntityListing**](IVREntityListing.html)

<a name="get_architect_prompt"></a>

## [**Prompt**](Prompt.html) get_architect_prompt(prompt_id)



Get specified user prompt



Wraps GET /api/v2/architect/prompts/{promptId} 

Requires ALL permissions: 

* architect:userPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID

try:
    # Get specified user prompt
    api_response = api_instance.get_architect_prompt(prompt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_prompt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
{: class="table table-striped"}

### Return type

[**Prompt**](Prompt.html)

<a name="get_architect_prompt_history_history_id"></a>

## [**HistoryListing**](HistoryListing.html) get_architect_prompt_history_history_id(prompt_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)



Get generated prompt history



Wraps GET /api/v2/architect/prompts/{promptId}/history/{historyId} 

Requires ALL permissions: 

* architect:userPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
history_id = 'history_id_example' # str | History request ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_order = 'desc' # str | Sort order (optional) (default to desc)
sort_by = 'timestamp' # str | Sort by (optional) (default to timestamp)
action = ['action_example'] # list[str] | Flow actions to include (omit to include all) (optional)

try:
    # Get generated prompt history
    api_response = api_instance.get_architect_prompt_history_history_id(prompt_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_prompt_history_history_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **history_id** | **str**| History request ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_order** | **str**| Sort order | [optional] [default to desc] |
| **sort_by** | **str**| Sort by | [optional] [default to timestamp]<br />**Values**: action, timestamp, user |
| **action** | [**list[str]**](str.html)| Flow actions to include (omit to include all) | [optional] <br />**Values**: checkin, checkout, create, deactivate, debug, delete, publish, revert, save |
{: class="table table-striped"}

### Return type

[**HistoryListing**](HistoryListing.html)

<a name="get_architect_prompt_resource"></a>

## [**PromptAsset**](PromptAsset.html) get_architect_prompt_resource(prompt_id, language_code)



Get specified user prompt resource



Wraps GET /api/v2/architect/prompts/{promptId}/resources/{languageCode} 

Requires ALL permissions: 

* architect:userPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_prompt_resource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
{: class="table table-striped"}

### Return type

[**PromptAsset**](PromptAsset.html)

<a name="get_architect_prompt_resources"></a>

## [**PromptAssetEntityListing**](PromptAssetEntityListing.html) get_architect_prompt_resources(prompt_id, page_number=page_number, page_size=page_size)



Get a pageable list of user prompt resources

The returned list is pageable, and query parameters can be used for filtering.

Wraps GET /api/v2/architect/prompts/{promptId}/resources 

Requires ALL permissions: 

* architect:userPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_prompt_resources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**PromptAssetEntityListing**](PromptAssetEntityListing.html)

<a name="get_architect_prompts"></a>

## [**PromptEntityListing**](PromptEntityListing.html) get_architect_prompts(page_number=page_number, page_size=page_size, name=name, description=description, name_or_description=name_or_description, sort_by=sort_by, sort_order=sort_order)



Get a pageable list of user prompts

The returned list is pageable, and query parameters can be used for filtering.  Multiple names can be specified, in which case all matching prompts will be returned, and no other filters will be evaluated.

Wraps GET /api/v2/architect/prompts 

Requires ALL permissions: 

* architect:userPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = ['name_example'] # list[str] | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)

try:
    # Get a pageable list of user prompts
    api_response = api_instance.get_architect_prompts(page_number=page_number, page_size=page_size, name=name, description=description, name_or_description=name_or_description, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_prompts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | [**list[str]**](str.html)| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
{: class="table table-striped"}

### Return type

[**PromptEntityListing**](PromptEntityListing.html)

<a name="get_architect_schedule"></a>

## [**Schedule**](Schedule.html) get_architect_schedule(schedule_id)



Get a schedule by ID



Wraps GET /api/v2/architect/schedules/{scheduleId} 

Requires ANY permissions: 

* routing:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Get a schedule by ID
    api_response = api_instance.get_architect_schedule(schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

[**Schedule**](Schedule.html)

<a name="get_architect_schedulegroup"></a>

## [**ScheduleGroup**](ScheduleGroup.html) get_architect_schedulegroup(schedule_group_id)



Gets a schedule group by ID



Wraps GET /api/v2/architect/schedulegroups/{scheduleGroupId} 

Requires ANY permissions: 

* routing:scheduleGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
schedule_group_id = 'schedule_group_id_example' # str | Schedule group ID

try:
    # Gets a schedule group by ID
    api_response = api_instance.get_architect_schedulegroup(schedule_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedulegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_group_id** | **str**| Schedule group ID |  |
{: class="table table-striped"}

### Return type

[**ScheduleGroup**](ScheduleGroup.html)

<a name="get_architect_schedulegroups"></a>

## [**ScheduleGroupEntityListing**](ScheduleGroupEntityListing.html) get_architect_schedulegroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, schedule_ids=schedule_ids)



Get a list of schedule groups.



Wraps GET /api/v2/architect/schedulegroups 

Requires ANY permissions: 

* routing:scheduleGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'name' # str | Sort by (optional) (default to name)
sort_order = 'ASC' # str | Sort order (optional) (default to ASC)
name = 'name_example' # str | Name of the Schedule Group to filter by. (optional)
schedule_ids = 'schedule_ids_example' # str | A comma-delimited list of Schedule IDs to filter by. (optional)

try:
    # Get a list of schedule groups.
    api_response = api_instance.get_architect_schedulegroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, schedule_ids=schedule_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedulegroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
| **sort_order** | **str**| Sort order | [optional] [default to ASC] |
| **name** | **str**| Name of the Schedule Group to filter by. | [optional]  |
| **schedule_ids** | **str**| A comma-delimited list of Schedule IDs to filter by. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScheduleGroupEntityListing**](ScheduleGroupEntityListing.html)

<a name="get_architect_schedules"></a>

## [**ScheduleEntityListing**](ScheduleEntityListing.html) get_architect_schedules(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)



Get a list of schedules.



Wraps GET /api/v2/architect/schedules 

Requires ANY permissions: 

* routing:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'name' # str | Sort by (optional) (default to name)
sort_order = 'ASC' # str | Sort order (optional) (default to ASC)
name = 'name_example' # str | Name of the Schedule to filter by. (optional)

try:
    # Get a list of schedules.
    api_response = api_instance.get_architect_schedules(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
| **sort_order** | **str**| Sort order | [optional] [default to ASC] |
| **name** | **str**| Name of the Schedule to filter by. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScheduleEntityListing**](ScheduleEntityListing.html)

<a name="get_architect_systemprompt"></a>

## [**SystemPrompt**](SystemPrompt.html) get_architect_systemprompt(prompt_id)



Get a system prompt



Wraps GET /api/v2/architect/systemprompts/{promptId} 

Requires ALL permissions: 

* architect:systemPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | promptId

try:
    # Get a system prompt
    api_response = api_instance.get_architect_systemprompt(prompt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_systemprompt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| promptId |  |
{: class="table table-striped"}

### Return type

[**SystemPrompt**](SystemPrompt.html)

<a name="get_architect_systemprompt_history_history_id"></a>

## [**HistoryListing**](HistoryListing.html) get_architect_systemprompt_history_history_id(prompt_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)



Get generated prompt history



Wraps GET /api/v2/architect/systemprompts/{promptId}/history/{historyId} 

Requires ALL permissions: 

* architect:systemPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | promptId
history_id = 'history_id_example' # str | History request ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_order = 'desc' # str | Sort order (optional) (default to desc)
sort_by = 'timestamp' # str | Sort by (optional) (default to timestamp)
action = ['action_example'] # list[str] | Flow actions to include (omit to include all) (optional)

try:
    # Get generated prompt history
    api_response = api_instance.get_architect_systemprompt_history_history_id(prompt_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_systemprompt_history_history_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| promptId |  |
| **history_id** | **str**| History request ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_order** | **str**| Sort order | [optional] [default to desc] |
| **sort_by** | **str**| Sort by | [optional] [default to timestamp]<br />**Values**: action, timestamp, user |
| **action** | [**list[str]**](str.html)| Flow actions to include (omit to include all) | [optional] <br />**Values**: checkin, checkout, create, deactivate, debug, delete, publish, revert, save |
{: class="table table-striped"}

### Return type

[**HistoryListing**](HistoryListing.html)

<a name="get_architect_systemprompt_resource"></a>

## [**SystemPromptAsset**](SystemPromptAsset.html) get_architect_systemprompt_resource(prompt_id, language_code)



Get a system prompt resource.



Wraps GET /api/v2/architect/systemprompts/{promptId}/resources/{languageCode} 

Requires ALL permissions: 

* architect:systemPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_systemprompt_resource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
{: class="table table-striped"}

### Return type

[**SystemPromptAsset**](SystemPromptAsset.html)

<a name="get_architect_systemprompt_resources"></a>

## [**SystemPromptAssetEntityListing**](SystemPromptAssetEntityListing.html) get_architect_systemprompt_resources(prompt_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order)



Get system prompt resources.



Wraps GET /api/v2/architect/systemprompts/{promptId}/resources 

Requires ALL permissions: 

* architect:systemPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_systemprompt_resources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
{: class="table table-striped"}

### Return type

[**SystemPromptAssetEntityListing**](SystemPromptAssetEntityListing.html)

<a name="get_architect_systemprompts"></a>

## [**SystemPromptEntityListing**](SystemPromptEntityListing.html) get_architect_systemprompts(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, description=description, name_or_description=name_or_description)



Get System Prompts



Wraps GET /api/v2/architect/systemprompts 

Requires ALL permissions: 

* architect:systemPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->get_architect_systemprompts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
{: class="table table-striped"}

### Return type

[**SystemPromptEntityListing**](SystemPromptEntityListing.html)

<a name="get_flow"></a>

## [**Flow**](Flow.html) get_flow(flow_id, deleted=deleted)



Get flow



Wraps GET /api/v2/flows/{flowId} 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
deleted = false # bool | Deleted flows (optional) (default to false)

try:
    # Get flow
    api_response = api_instance.get_flow(flow_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **deleted** | **bool**| Deleted flows | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="get_flow_history_history_id"></a>

## [**HistoryListing**](HistoryListing.html) get_flow_history_history_id(flow_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)



Get generated flow history



Wraps GET /api/v2/flows/{flowId}/history/{historyId} 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
history_id = 'history_id_example' # str | History request ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_order = 'desc' # str | Sort order (optional) (default to desc)
sort_by = 'timestamp' # str | Sort by (optional) (default to timestamp)
action = ['action_example'] # list[str] | Flow actions to include (omit to include all) (optional)

try:
    # Get generated flow history
    api_response = api_instance.get_flow_history_history_id(flow_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_history_history_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **history_id** | **str**| History request ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_order** | **str**| Sort order | [optional] [default to desc] |
| **sort_by** | **str**| Sort by | [optional] [default to timestamp]<br />**Values**: action, timestamp, user |
| **action** | [**list[str]**](str.html)| Flow actions to include (omit to include all) | [optional] <br />**Values**: checkin, checkout, create, deactivate, debug, delete, publish, revert, save |
{: class="table table-striped"}

### Return type

[**HistoryListing**](HistoryListing.html)

<a name="get_flow_latestconfiguration"></a>

## object** get_flow_latestconfiguration(flow_id, deleted=deleted)



Get the latest configuration for flow



Wraps GET /api/v2/flows/{flowId}/latestconfiguration 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
deleted = false # bool | Deleted flows (optional) (default to false)

try:
    # Get the latest configuration for flow
    api_response = api_instance.get_flow_latestconfiguration(flow_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_latestconfiguration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **deleted** | **bool**| Deleted flows | [optional] [default to false] |
{: class="table table-striped"}

### Return type

**object**

<a name="get_flow_version"></a>

## [**FlowVersion**](FlowVersion.html) get_flow_version(flow_id, version_id, deleted=deleted)



Get flow version



Wraps GET /api/v2/flows/{flowId}/versions/{versionId} 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
version_id = 'version_id_example' # str | Version ID
deleted = 'deleted_example' # str | Deleted flows (optional)

try:
    # Get flow version
    api_response = api_instance.get_flow_version(flow_id, version_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **version_id** | **str**| Version ID |  |
| **deleted** | **str**| Deleted flows | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowVersion**](FlowVersion.html)

<a name="get_flow_version_configuration"></a>

## object** get_flow_version_configuration(flow_id, version_id, deleted=deleted)



Create flow version configuration



Wraps GET /api/v2/flows/{flowId}/versions/{versionId}/configuration 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
version_id = 'version_id_example' # str | Version ID
deleted = 'deleted_example' # str | Deleted flows (optional)

try:
    # Create flow version configuration
    api_response = api_instance.get_flow_version_configuration(flow_id, version_id, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_version_configuration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **version_id** | **str**| Version ID |  |
| **deleted** | **str**| Deleted flows | [optional]  |
{: class="table table-striped"}

### Return type

**object**

<a name="get_flow_versions"></a>

## [**FlowVersionEntityListing**](FlowVersionEntityListing.html) get_flow_versions(flow_id, page_number=page_number, page_size=page_size, deleted=deleted)



Get flow version list



Wraps GET /api/v2/flows/{flowId}/versions 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
deleted = true # bool | Include Deleted flows (optional)

try:
    # Get flow version list
    api_response = api_instance.get_flow_versions(flow_id, page_number=page_number, page_size=page_size, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **deleted** | **bool**| Include Deleted flows | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowVersionEntityListing**](FlowVersionEntityListing.html)

<a name="get_flows"></a>

## [**FlowEntityListing**](FlowEntityListing.html) get_flows(type=type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, publish_version_id=publish_version_id, editable_by=editable_by, locked_by=locked_by, locked_by_client_id=locked_by_client_id, secure=secure, deleted=deleted, include_schemas=include_schemas, published_after=published_after, published_before=published_before, division_id=division_id)



Get a pageable list of flows, filtered by query parameters

If one or more IDs are specified, the search will fetch flows that match the given ID(s) and not use any additional supplied query parameters in the search.

Wraps GET /api/v2/flows 

Requires ANY permissions: 

* architect:flow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
type = ['type_example'] # list[str] | Type (optional)
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
locked_by_client_id = 'locked_by_client_id_example' # str | Locked by client ID (optional)
secure = 'secure_example' # str | Secure (optional)
deleted = false # bool | Include deleted (optional) (default to false)
include_schemas = false # bool | Include variable schemas (optional) (default to false)
published_after = '2015-01-01T12:00:00-0600, 2015-01-01T18:00:00Z, 2015-01-01T12:00:00.000-0600, 2015-01-01T18:00:00.000Z, 2015-01-01' # str | Published after (optional)
published_before = '2015-01-01T12:00:00-0600, 2015-01-01T18:00:00Z, 2015-01-01T12:00:00.000-0600, 2015-01-01T18:00:00.000Z, 2015-01-01' # str | Published before (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)

try:
    # Get a pageable list of flows, filtered by query parameters
    api_response = api_instance.get_flows(type=type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, publish_version_id=publish_version_id, editable_by=editable_by, locked_by=locked_by, locked_by_client_id=locked_by_client_id, secure=secure, deleted=deleted, include_schemas=include_schemas, published_after=published_after, published_before=published_before, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | [**list[str]**](str.html)| Type | [optional] <br />**Values**: bot, commonmodule, inboundcall, inboundchat, inboundemail, inboundshortmessage, outboundcall, inqueuecall, speech, securecall, surveyinvite, workflow |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
| **id** | [**list[str]**](str.html)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **publish_version_id** | **str**| Publish version ID | [optional]  |
| **editable_by** | **str**| Editable by | [optional]  |
| **locked_by** | **str**| Locked by | [optional]  |
| **locked_by_client_id** | **str**| Locked by client ID | [optional]  |
| **secure** | **str**| Secure | [optional] <br />**Values**: any, checkedin, published |
| **deleted** | **bool**| Include deleted | [optional] [default to false] |
| **include_schemas** | **bool**| Include variable schemas | [optional] [default to false] |
| **published_after** | **str**| Published after | [optional]  |
| **published_before** | **str**| Published before | [optional]  |
| **division_id** | [**list[str]**](str.html)| division ID(s) | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowEntityListing**](FlowEntityListing.html)

<a name="get_flows_datatable"></a>

## [**DataTable**](DataTable.html) get_flows_datatable(datatable_id, expand=expand)



Returns a specific datatable by id

Given a datatableId returns the datatable object and schema associated with it.

Wraps GET /api/v2/flows/datatables/{datatableId} 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
expand = 'expand_example' # str | Expand instructions for the result (optional)

try:
    # Returns a specific datatable by id
    api_response = api_instance.get_flows_datatable(datatable_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **expand** | **str**| Expand instructions for the result | [optional] <br />**Values**: schema |
{: class="table table-striped"}

### Return type

[**DataTable**](DataTable.html)

<a name="get_flows_datatable_export_job"></a>

## [**DataTableExportJob**](DataTableExportJob.html) get_flows_datatable_export_job(datatable_id, export_job_id)



Returns the state information about an export job

Returns the state information about an export job.

Wraps GET /api/v2/flows/datatables/{datatableId}/export/jobs/{exportJobId} 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
export_job_id = 'export_job_id_example' # str | id of export job

try:
    # Returns the state information about an export job
    api_response = api_instance.get_flows_datatable_export_job(datatable_id, export_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatable_export_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **export_job_id** | **str**| id of export job |  |
{: class="table table-striped"}

### Return type

[**DataTableExportJob**](DataTableExportJob.html)

<a name="get_flows_datatable_import_job"></a>

## [**DataTableImportJob**](DataTableImportJob.html) get_flows_datatable_import_job(datatable_id, import_job_id)



Returns the state information about an import job

Returns the state information about an import job.

Wraps GET /api/v2/flows/datatables/{datatableId}/import/jobs/{importJobId} 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
import_job_id = 'import_job_id_example' # str | id of import job

try:
    # Returns the state information about an import job
    api_response = api_instance.get_flows_datatable_import_job(datatable_id, import_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatable_import_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **import_job_id** | **str**| id of import job |  |
{: class="table table-striped"}

### Return type

[**DataTableImportJob**](DataTableImportJob.html)

<a name="get_flows_datatable_import_jobs"></a>

## [**EntityListing**](EntityListing.html) get_flows_datatable_import_jobs(datatable_id, page_number=page_number, page_size=page_size)



Get all recent import jobs

Get all recent import jobs

Wraps GET /api/v2/flows/datatables/{datatableId}/import/jobs 

Requires ANY permissions: 

* architect:datatable:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get all recent import jobs
    api_response = api_instance.get_flows_datatable_import_jobs(datatable_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatable_import_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**EntityListing**](EntityListing.html)

<a name="get_flows_datatable_row"></a>

## [**dict(str, object)**](dict.html) get_flows_datatable_row(datatable_id, row_id, showbrief=showbrief)



Returns a specific row for the datatable

Given a datatableId and a rowId (the value of the key field) this will return the full row contents for that rowId.

Wraps GET /api/v2/flows/datatables/{datatableId}/rows/{rowId} 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
row_id = 'row_id_example' # str | The key for the row
showbrief = true # bool | if true returns just the key field for the row (optional) (default to true)

try:
    # Returns a specific row for the datatable
    api_response = api_instance.get_flows_datatable_row(datatable_id, row_id, showbrief=showbrief)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatable_row: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **row_id** | **str**| The key for the row |  |
| **showbrief** | **bool**| if true returns just the key field for the row | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

<a name="get_flows_datatable_rows"></a>

## [**DataTableRowEntityListing**](DataTableRowEntityListing.html) get_flows_datatable_rows(datatable_id, page_number=page_number, page_size=page_size, showbrief=showbrief)



Returns the rows for the datatable with the given id

Returns all of the rows for the datatable with the given datatableId.  By default this will just be a truncated list returning the key for each row. Set showBrief to false to return all of the row contents.

Wraps GET /api/v2/flows/datatables/{datatableId}/rows 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
showbrief = true # bool | If true returns just the key value of the row (optional) (default to true)

try:
    # Returns the rows for the datatable with the given id
    api_response = api_instance.get_flows_datatable_rows(datatable_id, page_number=page_number, page_size=page_size, showbrief=showbrief)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatable_rows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **showbrief** | **bool**| If true returns just the key value of the row | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**DataTableRowEntityListing**](DataTableRowEntityListing.html)

<a name="get_flows_datatables"></a>

## [**DataTablesDomainEntityListing**](DataTablesDomainEntityListing.html) get_flows_datatables(expand=expand, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order)



Retrieve a list of datatables for the org

Returns a metadata list of the datatables associated with this org, including datatableId, name and description.

Wraps GET /api/v2/flows/datatables 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
expand = 'expand_example' # str | Expand instructions for the result (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'ascending' # str | Sort order (optional) (default to ascending)

try:
    # Retrieve a list of datatables for the org
    api_response = api_instance.get_flows_datatables(expand=expand, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatables: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | **str**| Expand instructions for the result | [optional] <br />**Values**: schema |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id]<br />**Values**: id, name |
| **sort_order** | **str**| Sort order | [optional] [default to ascending] |
{: class="table table-striped"}

### Return type

[**DataTablesDomainEntityListing**](DataTablesDomainEntityListing.html)

<a name="get_flows_divisionviews"></a>

## [**FlowDivisionViewEntityListing**](FlowDivisionViewEntityListing.html) get_flows_divisionviews(type=type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, publish_version_id=publish_version_id, published_after=published_after, published_before=published_before, division_id=division_id, include_schemas=include_schemas)



Get a pageable list of basic flow information objects filterable by query parameters.

This returns a simplified version of /flow consisting of name and type. If one or more IDs are specified, the search will fetch flows that match the given ID(s) and not use any additional supplied query parameters in the search.

Wraps GET /api/v2/flows/divisionviews 

Requires ALL permissions: 

* architect:flow:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
type = ['type_example'] # list[str] | Type (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
publish_version_id = 'publish_version_id_example' # str | Publish version ID (optional)
published_after = '2015-01-01T12:00:00-0600, 2015-01-01T18:00:00Z, 2015-01-01T12:00:00.000-0600, 2015-01-01T18:00:00.000Z, 2015-01-01' # str | Published after (optional)
published_before = '2015-01-01T12:00:00-0600, 2015-01-01T18:00:00Z, 2015-01-01T12:00:00.000-0600, 2015-01-01T18:00:00.000Z, 2015-01-01' # str | Published before (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)
include_schemas = false # bool | Include variable schemas (optional) (default to false)

try:
    # Get a pageable list of basic flow information objects filterable by query parameters.
    api_response = api_instance.get_flows_divisionviews(type=type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, publish_version_id=publish_version_id, published_after=published_after, published_before=published_before, division_id=division_id, include_schemas=include_schemas)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | [**list[str]**](str.html)| Type | [optional] <br />**Values**: bot, commonmodule, inboundcall, inboundchat, inboundemail, inboundshortmessage, outboundcall, inqueuecall, speech, securecall, surveyinvite, workflow |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
| **id** | [**list[str]**](str.html)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **publish_version_id** | **str**| Publish version ID | [optional]  |
| **published_after** | **str**| Published after | [optional]  |
| **published_before** | **str**| Published before | [optional]  |
| **division_id** | [**list[str]**](str.html)| division ID(s) | [optional]  |
| **include_schemas** | **bool**| Include variable schemas | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**FlowDivisionViewEntityListing**](FlowDivisionViewEntityListing.html)

<a name="get_flows_execution"></a>

## [**FlowRuntimeExecution**](FlowRuntimeExecution.html) get_flows_execution(flow_execution_id)



Get a flow execution's details. Flow execution details are available for several days after the flow is started.



Wraps GET /api/v2/flows/executions/{flowExecutionId} 

Requires ANY permissions: 

* architect:flowExecution:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_execution_id = 'flow_execution_id_example' # str | flow execution ID

try:
    # Get a flow execution's details. Flow execution details are available for several days after the flow is started.
    api_response = api_instance.get_flows_execution(flow_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_execution: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_execution_id** | **str**| flow execution ID |  |
{: class="table table-striped"}

### Return type

[**FlowRuntimeExecution**](FlowRuntimeExecution.html)

<a name="get_flows_milestone"></a>

## [**FlowMilestone**](FlowMilestone.html) get_flows_milestone(milestone_id)



Get a flow milestone

Returns a specified flow milestone

Wraps GET /api/v2/flows/milestones/{milestoneId} 

Requires ALL permissions: 

* architect:flowMilestone:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
milestone_id = 'milestone_id_example' # str | flow milestone ID

try:
    # Get a flow milestone
    api_response = api_instance.get_flows_milestone(milestone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_milestone: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **milestone_id** | **str**| flow milestone ID |  |
{: class="table table-striped"}

### Return type

[**FlowMilestone**](FlowMilestone.html)

<a name="get_flows_milestones"></a>

## [**FlowMilestoneListing**](FlowMilestoneListing.html) get_flows_milestones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description)



Get a pageable list of flow milestones, filtered by query parameters

Multiple IDs can be specified, in which case all matching flow milestones will be returned, and no other parameters will be evaluated.

Wraps GET /api/v2/flows/milestones 

Requires ALL permissions: 

* architect:flowMilestone:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)

try:
    # Get a pageable list of flow milestones, filtered by query parameters
    api_response = api_instance.get_flows_milestones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_milestones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
| **id** | [**list[str]**](str.html)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowMilestoneListing**](FlowMilestoneListing.html)

<a name="get_flows_outcome"></a>

## [**FlowOutcome**](FlowOutcome.html) get_flows_outcome(flow_outcome_id)



Get a flow outcome

Returns a specified flow outcome

Wraps GET /api/v2/flows/outcomes/{flowOutcomeId} 

Requires ALL permissions: 

* architect:flowOutcome:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_outcome_id = 'flow_outcome_id_example' # str | flow outcome ID

try:
    # Get a flow outcome
    api_response = api_instance.get_flows_outcome(flow_outcome_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_outcome: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_outcome_id** | **str**| flow outcome ID |  |
{: class="table table-striped"}

### Return type

[**FlowOutcome**](FlowOutcome.html)

<a name="get_flows_outcomes"></a>

## [**FlowOutcomeListing**](FlowOutcomeListing.html) get_flows_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description)



Get a pageable list of flow outcomes, filtered by query parameters

Multiple IDs can be specified, in which case all matching flow outcomes will be returned, and no other parameters will be evaluated.

Wraps GET /api/v2/flows/outcomes 

Requires ALL permissions: 

* architect:flowOutcome:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'id' # str | Sort by (optional) (default to id)
sort_order = 'asc' # str | Sort order (optional) (default to asc)
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)

try:
    # Get a pageable list of flow outcomes, filtered by query parameters
    api_response = api_instance.get_flows_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_outcomes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to id] |
| **sort_order** | **str**| Sort order | [optional] [default to asc] |
| **id** | [**list[str]**](str.html)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowOutcomeListing**](FlowOutcomeListing.html)

<a name="post_architect_dependencytracking_build"></a>

##  post_architect_dependencytracking_build()



Rebuild Dependency Tracking data for an organization

Asynchronous.  Notification topic: v2.architect.dependencytracking.build

Wraps POST /api/v2/architect/dependencytracking/build 

Requires ALL permissions: 

* architect:dependencyTracking:rebuild

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()

try:
    # Rebuild Dependency Tracking data for an organization
    api_instance.post_architect_dependencytracking_build()
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_dependencytracking_build: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_architect_emergencygroups"></a>

## [**EmergencyGroup**](EmergencyGroup.html) post_architect_emergencygroups(body)



Creates a new emergency group



Wraps POST /api/v2/architect/emergencygroups 

Requires ANY permissions: 

* routing:emergencyGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.EmergencyGroup() # EmergencyGroup | 

try:
    # Creates a new emergency group
    api_response = api_instance.post_architect_emergencygroups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_emergencygroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmergencyGroup**](EmergencyGroup.html)|  |  |
{: class="table table-striped"}

### Return type

[**EmergencyGroup**](EmergencyGroup.html)

<a name="post_architect_ivrs"></a>

## [**IVR**](IVR.html) post_architect_ivrs(body)



Create IVR config.



Wraps POST /api/v2/architect/ivrs 

Requires ANY permissions: 

* routing:callRoute:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.IVR() # IVR | 

try:
    # Create IVR config.
    api_response = api_instance.post_architect_ivrs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_ivrs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IVR**](IVR.html)|  |  |
{: class="table table-striped"}

### Return type

[**IVR**](IVR.html)

<a name="post_architect_prompt_history"></a>

## [**Operation**](Operation.html) post_architect_prompt_history(prompt_id)



Generate prompt history

Asynchronous.  Notification topic: v2.architect.prompts.{promptId}

Wraps POST /api/v2/architect/prompts/{promptId}/history 

Requires ALL permissions: 

* architect:userPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID

try:
    # Generate prompt history
    api_response = api_instance.post_architect_prompt_history(prompt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_prompt_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="post_architect_prompt_resources"></a>

## [**PromptAsset**](PromptAsset.html) post_architect_prompt_resources(prompt_id, body)



Create a new user prompt resource



Wraps POST /api/v2/architect/prompts/{promptId}/resources 

Requires ALL permissions: 

* architect:userPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
body = PureCloudPlatformClientV2.PromptAssetCreate() # PromptAssetCreate | 

try:
    # Create a new user prompt resource
    api_response = api_instance.post_architect_prompt_resources(prompt_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_prompt_resources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **body** | [**PromptAssetCreate**](PromptAssetCreate.html)|  |  |
{: class="table table-striped"}

### Return type

[**PromptAsset**](PromptAsset.html)

<a name="post_architect_prompts"></a>

## [**Prompt**](Prompt.html) post_architect_prompts(body)



Create a new user prompt



Wraps POST /api/v2/architect/prompts 

Requires ALL permissions: 

* architect:userPrompt:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.Prompt() # Prompt | 

try:
    # Create a new user prompt
    api_response = api_instance.post_architect_prompts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_prompts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Prompt**](Prompt.html)|  |  |
{: class="table table-striped"}

### Return type

[**Prompt**](Prompt.html)

<a name="post_architect_schedulegroups"></a>

## [**ScheduleGroup**](ScheduleGroup.html) post_architect_schedulegroups(body)



Creates a new schedule group



Wraps POST /api/v2/architect/schedulegroups 

Requires ANY permissions: 

* routing:scheduleGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.ScheduleGroup() # ScheduleGroup | 

try:
    # Creates a new schedule group
    api_response = api_instance.post_architect_schedulegroups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_schedulegroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScheduleGroup**](ScheduleGroup.html)|  |  |
{: class="table table-striped"}

### Return type

[**ScheduleGroup**](ScheduleGroup.html)

<a name="post_architect_schedules"></a>

## [**Schedule**](Schedule.html) post_architect_schedules(body)



Create a new schedule.



Wraps POST /api/v2/architect/schedules 

Requires ANY permissions: 

* routing:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.Schedule() # Schedule | 

try:
    # Create a new schedule.
    api_response = api_instance.post_architect_schedules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Schedule**](Schedule.html)|  |  |
{: class="table table-striped"}

### Return type

[**Schedule**](Schedule.html)

<a name="post_architect_systemprompt_history"></a>

## [**Operation**](Operation.html) post_architect_systemprompt_history(prompt_id)



Generate system prompt history

Asynchronous.  Notification topic: v2.architect.systemprompts.{systemPromptId}

Wraps POST /api/v2/architect/systemprompts/{promptId}/history 

Requires ALL permissions: 

* architect:systemPrompt:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | promptId

try:
    # Generate system prompt history
    api_response = api_instance.post_architect_systemprompt_history(prompt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_systemprompt_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| promptId |  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="post_architect_systemprompt_resources"></a>

## [**SystemPromptAsset**](SystemPromptAsset.html) post_architect_systemprompt_resources(prompt_id, body)



Create system prompt resource override.



Wraps POST /api/v2/architect/systemprompts/{promptId}/resources 

Requires ALL permissions: 

* architect:systemPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
body = PureCloudPlatformClientV2.SystemPromptAsset() # SystemPromptAsset | 

try:
    # Create system prompt resource override.
    api_response = api_instance.post_architect_systemprompt_resources(prompt_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_systemprompt_resources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **body** | [**SystemPromptAsset**](SystemPromptAsset.html)|  |  |
{: class="table table-striped"}

### Return type

[**SystemPromptAsset**](SystemPromptAsset.html)

<a name="post_flow_versions"></a>

## [**FlowVersion**](FlowVersion.html) post_flow_versions(flow_id, body)



Create flow version



Wraps POST /api/v2/flows/{flowId}/versions 

Requires ANY permissions: 

* architect:flow:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
body = NULL # object | 

try:
    # Create flow version
    api_response = api_instance.post_flow_versions(flow_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flow_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **body** | **object**|  |  |
{: class="table table-striped"}

### Return type

[**FlowVersion**](FlowVersion.html)

<a name="post_flows"></a>

## [**Flow**](Flow.html) post_flows(body)



Create flow



Wraps POST /api/v2/flows 

Requires ANY permissions: 

* architect:flow:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.Flow() # Flow | 

try:
    # Create flow
    api_response = api_instance.post_flows(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Flow**](Flow.html)|  |  |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_checkin"></a>

## [**Operation**](Operation.html) post_flows_actions_checkin(flow)



Check-in flow

Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps POST /api/v2/flows/actions/checkin 

Requires ANY permissions: 

* architect:flow:edit
* architect:flow:unlock

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Check-in flow
    api_response = api_instance.post_flows_actions_checkin(flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_actions_checkin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID |  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="post_flows_actions_checkout"></a>

## [**Flow**](Flow.html) post_flows_actions_checkout(flow)



Check-out flow



Wraps POST /api/v2/flows/actions/checkout 

Requires ANY permissions: 

* architect:flow:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Check-out flow
    api_response = api_instance.post_flows_actions_checkout(flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_actions_checkout: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID |  |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_deactivate"></a>

## [**Flow**](Flow.html) post_flows_actions_deactivate(flow)



Deactivate flow



Wraps POST /api/v2/flows/actions/deactivate 

Requires ANY permissions: 

* architect:flow:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Deactivate flow
    api_response = api_instance.post_flows_actions_deactivate(flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_actions_deactivate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID |  |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_publish"></a>

## [**Operation**](Operation.html) post_flows_actions_publish(flow, version=version)



Publish flow

Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps POST /api/v2/flows/actions/publish 

Requires ANY permissions: 

* architect:flow:unlock
* architect:flow:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ArchitectApi->post_flows_actions_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID |  |
| **version** | **str**| version | [optional]  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

<a name="post_flows_actions_revert"></a>

## [**Flow**](Flow.html) post_flows_actions_revert(flow)



Revert flow



Wraps POST /api/v2/flows/actions/revert 

Requires ANY permissions: 

* architect:flow:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Revert flow
    api_response = api_instance.post_flows_actions_revert(flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_actions_revert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID |  |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_actions_unlock"></a>

## [**Flow**](Flow.html) post_flows_actions_unlock(flow)



Unlock flow

Allows for unlocking a flow in the case where there is no flow configuration available, and thus a check-in will not unlock the flow. The user must have Architect Admin permissions to perform this action.

Wraps POST /api/v2/flows/actions/unlock 

Requires ANY permissions: 

* architect:flow:unlock

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow = 'flow_example' # str | Flow ID

try:
    # Unlock flow
    api_response = api_instance.post_flows_actions_unlock(flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_actions_unlock: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow** | **str**| Flow ID |  |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="post_flows_datatable_export_jobs"></a>

## [**DataTableExportJob**](DataTableExportJob.html) post_flows_datatable_export_jobs(datatable_id)



Begin an export process for exporting all rows from a datatable

Create an export job for exporting rows. The caller can then poll for status of the export using the token returned in the response

Wraps POST /api/v2/flows/datatables/{datatableId}/export/jobs 

Requires ANY permissions: 

* architect:datatable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable

try:
    # Begin an export process for exporting all rows from a datatable
    api_response = api_instance.post_flows_datatable_export_jobs(datatable_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_datatable_export_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
{: class="table table-striped"}

### Return type

[**DataTableExportJob**](DataTableExportJob.html)

<a name="post_flows_datatable_import_jobs"></a>

## [**DataTableImportJob**](DataTableImportJob.html) post_flows_datatable_import_jobs(datatable_id, body)



Begin an import process for importing rows into a datatable

Create an import job for importing rows. The caller can then poll for status of the import using the token returned in the response

Wraps POST /api/v2/flows/datatables/{datatableId}/import/jobs 

Requires ANY permissions: 

* architect:datatable:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
body = PureCloudPlatformClientV2.DataTableImportJob() # DataTableImportJob | import job information

try:
    # Begin an import process for importing rows into a datatable
    api_response = api_instance.post_flows_datatable_import_jobs(datatable_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_datatable_import_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **body** | [**DataTableImportJob**](DataTableImportJob.html)| import job information |  |
{: class="table table-striped"}

### Return type

[**DataTableImportJob**](DataTableImportJob.html)

<a name="post_flows_datatable_rows"></a>

## [**dict(str, object)**](dict.html) post_flows_datatable_rows(datatable_id, data_table_row)



Create a new row entry for the datatable.

Will add the passed in row entry to the datatable with the given datatableId after verifying it against the schema.  The DataTableRow should be a json-ized' stream of key -> value pairs {      \"Field1\": \"XYZZY\",      \"Field2\": false,      \"KEY\": \"27272\"  }

Wraps POST /api/v2/flows/datatables/{datatableId}/rows 

Requires ANY permissions: 

* architect:datatable:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
data_table_row = NULL # object | 

try:
    # Create a new row entry for the datatable.
    api_response = api_instance.post_flows_datatable_rows(datatable_id, data_table_row)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_datatable_rows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **data_table_row** | **object**|  |  |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

<a name="post_flows_datatables"></a>

## [**DataTable**](DataTable.html) post_flows_datatables(body)



Create a new datatable with the specified json-schema definition

This will create a new datatable with fields that match the property definitions in the JSON schema.  The schema's title field will be overridden by the name field in the DataTable object.  See also http://json-schema.org/

Wraps POST /api/v2/flows/datatables 

Requires ANY permissions: 

* architect:datatable:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.DataTable() # DataTable | datatable json-schema

try:
    # Create a new datatable with the specified json-schema definition
    api_response = api_instance.post_flows_datatables(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_datatables: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DataTable**](DataTable.html)| datatable json-schema |  |
{: class="table table-striped"}

### Return type

[**DataTable**](DataTable.html)

<a name="post_flows_executions"></a>

## [**FlowExecutionLaunchResponse**](FlowExecutionLaunchResponse.html) post_flows_executions(flow_launch_request)



Launch an instance of a flow definition, for flow types that support it such as the 'workflow' type.

The launch is asynchronous, it returns as soon as the flow starts. You can use the returned ID to query its status if you need.

Wraps POST /api/v2/flows/executions 

Requires ANY permissions: 

* architect:flow:launch

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_launch_request = PureCloudPlatformClientV2.FlowExecutionLaunchRequest() # FlowExecutionLaunchRequest | 

try:
    # Launch an instance of a flow definition, for flow types that support it such as the 'workflow' type.
    api_response = api_instance.post_flows_executions(flow_launch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_executions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_launch_request** | [**FlowExecutionLaunchRequest**](FlowExecutionLaunchRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**FlowExecutionLaunchResponse**](FlowExecutionLaunchResponse.html)

<a name="post_flows_milestones"></a>

## [**FlowMilestone**](FlowMilestone.html) post_flows_milestones(body=body)



Create a flow milestone



Wraps POST /api/v2/flows/milestones 

Requires ALL permissions: 

* architect:flowMilestone:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.FlowMilestone() # FlowMilestone |  (optional)

try:
    # Create a flow milestone
    api_response = api_instance.post_flows_milestones(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_milestones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowMilestone**](FlowMilestone.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowMilestone**](FlowMilestone.html)

<a name="post_flows_outcomes"></a>

## [**FlowOutcome**](FlowOutcome.html) post_flows_outcomes(body=body)



Create a flow outcome

Asynchronous.  Notification topic: v2.flows.outcomes.{flowOutcomeId}

Wraps POST /api/v2/flows/outcomes 

Requires ALL permissions: 

* architect:flowOutcome:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
body = PureCloudPlatformClientV2.FlowOutcome() # FlowOutcome |  (optional)

try:
    # Create a flow outcome
    api_response = api_instance.post_flows_outcomes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_outcomes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowOutcome**](FlowOutcome.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowOutcome**](FlowOutcome.html)

<a name="put_architect_emergencygroup"></a>

## [**EmergencyGroup**](EmergencyGroup.html) put_architect_emergencygroup(emergency_group_id, body)



Updates a emergency group by ID



Wraps PUT /api/v2/architect/emergencygroups/{emergencyGroupId} 

Requires ANY permissions: 

* routing:emergencyGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
emergency_group_id = 'emergency_group_id_example' # str | Emergency group ID
body = PureCloudPlatformClientV2.EmergencyGroup() # EmergencyGroup | 

try:
    # Updates a emergency group by ID
    api_response = api_instance.put_architect_emergencygroup(emergency_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_emergencygroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **emergency_group_id** | **str**| Emergency group ID |  |
| **body** | [**EmergencyGroup**](EmergencyGroup.html)|  |  |
{: class="table table-striped"}

### Return type

[**EmergencyGroup**](EmergencyGroup.html)

<a name="put_architect_ivr"></a>

## [**IVR**](IVR.html) put_architect_ivr(ivr_id, body)



Update an IVR Config.



Wraps PUT /api/v2/architect/ivrs/{ivrId} 

Requires ANY permissions: 

* routing:callRoute:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
ivr_id = 'ivr_id_example' # str | IVR id
body = PureCloudPlatformClientV2.IVR() # IVR | 

try:
    # Update an IVR Config.
    api_response = api_instance.put_architect_ivr(ivr_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_ivr: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ivr_id** | **str**| IVR id |  |
| **body** | [**IVR**](IVR.html)|  |  |
{: class="table table-striped"}

### Return type

[**IVR**](IVR.html)

<a name="put_architect_prompt"></a>

## [**Prompt**](Prompt.html) put_architect_prompt(prompt_id, body)



Update specified user prompt



Wraps PUT /api/v2/architect/prompts/{promptId} 

Requires ALL permissions: 

* architect:userPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
body = PureCloudPlatformClientV2.Prompt() # Prompt | 

try:
    # Update specified user prompt
    api_response = api_instance.put_architect_prompt(prompt_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_prompt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **body** | [**Prompt**](Prompt.html)|  |  |
{: class="table table-striped"}

### Return type

[**Prompt**](Prompt.html)

<a name="put_architect_prompt_resource"></a>

## [**PromptAsset**](PromptAsset.html) put_architect_prompt_resource(prompt_id, language_code, body)



Update specified user prompt resource



Wraps PUT /api/v2/architect/prompts/{promptId}/resources/{languageCode} 

Requires ALL permissions: 

* architect:userPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.PromptAsset() # PromptAsset | 

try:
    # Update specified user prompt resource
    api_response = api_instance.put_architect_prompt_resource(prompt_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_prompt_resource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
| **body** | [**PromptAsset**](PromptAsset.html)|  |  |
{: class="table table-striped"}

### Return type

[**PromptAsset**](PromptAsset.html)

<a name="put_architect_schedule"></a>

## [**Schedule**](Schedule.html) put_architect_schedule(schedule_id, body)



Update schedule by ID



Wraps PUT /api/v2/architect/schedules/{scheduleId} 

Requires ANY permissions: 

* routing:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
schedule_id = 'schedule_id_example' # str | Schedule ID
body = PureCloudPlatformClientV2.Schedule() # Schedule | 

try:
    # Update schedule by ID
    api_response = api_instance.put_architect_schedule(schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
| **body** | [**Schedule**](Schedule.html)|  |  |
{: class="table table-striped"}

### Return type

[**Schedule**](Schedule.html)

<a name="put_architect_schedulegroup"></a>

## [**ScheduleGroup**](ScheduleGroup.html) put_architect_schedulegroup(schedule_group_id, body)



Updates a schedule group by ID



Wraps PUT /api/v2/architect/schedulegroups/{scheduleGroupId} 

Requires ANY permissions: 

* routing:scheduleGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
schedule_group_id = 'schedule_group_id_example' # str | Schedule group ID
body = PureCloudPlatformClientV2.ScheduleGroup() # ScheduleGroup | 

try:
    # Updates a schedule group by ID
    api_response = api_instance.put_architect_schedulegroup(schedule_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_schedulegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_group_id** | **str**| Schedule group ID |  |
| **body** | [**ScheduleGroup**](ScheduleGroup.html)|  |  |
{: class="table table-striped"}

### Return type

[**ScheduleGroup**](ScheduleGroup.html)

<a name="put_architect_systemprompt_resource"></a>

## [**SystemPromptAsset**](SystemPromptAsset.html) put_architect_systemprompt_resource(prompt_id, language_code, body)



Updates a system prompt resource override.



Wraps PUT /api/v2/architect/systemprompts/{promptId}/resources/{languageCode} 

Requires ALL permissions: 

* architect:systemPrompt:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
prompt_id = 'prompt_id_example' # str | Prompt ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.SystemPromptAsset() # SystemPromptAsset | 

try:
    # Updates a system prompt resource override.
    api_response = api_instance.put_architect_systemprompt_resource(prompt_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_systemprompt_resource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |
| **body** | [**SystemPromptAsset**](SystemPromptAsset.html)|  |  |
{: class="table table-striped"}

### Return type

[**SystemPromptAsset**](SystemPromptAsset.html)

<a name="put_flow"></a>

## [**Flow**](Flow.html) put_flow(flow_id, body)



Update flow



Wraps PUT /api/v2/flows/{flowId} 

Requires ANY permissions: 

* architect:flow:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_id = 'flow_id_example' # str | Flow ID
body = PureCloudPlatformClientV2.Flow() # Flow | 

try:
    # Update flow
    api_response = api_instance.put_flow(flow_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flow: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |
| **body** | [**Flow**](Flow.html)|  |  |
{: class="table table-striped"}

### Return type

[**Flow**](Flow.html)

<a name="put_flows_datatable"></a>

## [**DataTable**](DataTable.html) put_flows_datatable(datatable_id, expand=expand, body=body)



Updates a specific datatable by id

Updates a schema for a datatable with the given datatableId -updates allow only new fields to be added in the schema, no changes or removals of existing fields.

Wraps PUT /api/v2/flows/datatables/{datatableId} 

Requires ANY permissions: 

* architect:datatable:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
expand = 'expand_example' # str | Expand instructions for the result (optional)
body = PureCloudPlatformClientV2.DataTable() # DataTable | datatable json-schema (optional)

try:
    # Updates a specific datatable by id
    api_response = api_instance.put_flows_datatable(datatable_id, expand=expand, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flows_datatable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **expand** | **str**| Expand instructions for the result | [optional] <br />**Values**: schema |
| **body** | [**DataTable**](DataTable.html)| datatable json-schema | [optional]  |
{: class="table table-striped"}

### Return type

[**DataTable**](DataTable.html)

<a name="put_flows_datatable_row"></a>

## [**dict(str, object)**](dict.html) put_flows_datatable_row(datatable_id, row_id, body=body)



Update a row entry

Updates a row with the given rowId (the value of the key field) to the new values.  The DataTableRow should be a json-ized' stream of key -> value pairs {     \"Field1\": \"XYZZY\",     \"Field2\": false,     \"KEY\": \"27272\" }

Wraps PUT /api/v2/flows/datatables/{datatableId}/rows/{rowId} 

Requires ANY permissions: 

* architect:datatable:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
datatable_id = 'datatable_id_example' # str | id of datatable
row_id = 'row_id_example' # str | the key for the row
body = NULL # object | datatable row (optional)

try:
    # Update a row entry
    api_response = api_instance.put_flows_datatable_row(datatable_id, row_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flows_datatable_row: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **row_id** | **str**| the key for the row |  |
| **body** | **object**| datatable row | [optional]  |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

<a name="put_flows_milestone"></a>

## [**FlowMilestone**](FlowMilestone.html) put_flows_milestone(milestone_id, body=body)



Updates a flow milestone



Wraps PUT /api/v2/flows/milestones/{milestoneId} 

Requires ALL permissions: 

* architect:flowMilestone:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
milestone_id = 'milestone_id_example' # str | flow milestone ID
body = PureCloudPlatformClientV2.FlowMilestone() # FlowMilestone |  (optional)

try:
    # Updates a flow milestone
    api_response = api_instance.put_flows_milestone(milestone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flows_milestone: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **milestone_id** | **str**| flow milestone ID |  |
| **body** | [**FlowMilestone**](FlowMilestone.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowMilestone**](FlowMilestone.html)

<a name="put_flows_outcome"></a>

## [**Operation**](Operation.html) put_flows_outcome(flow_outcome_id, body=body)



Updates a flow outcome

Updates a flow outcome.  Asynchronous.  Notification topic: v2.flowoutcomes.{flowoutcomeId}

Wraps PUT /api/v2/flows/outcomes/{flowOutcomeId} 

Requires ALL permissions: 

* architect:flowOutcome:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ArchitectApi()
flow_outcome_id = 'flow_outcome_id_example' # str | flow outcome ID
body = PureCloudPlatformClientV2.FlowOutcome() # FlowOutcome |  (optional)

try:
    # Updates a flow outcome
    api_response = api_instance.put_flows_outcome(flow_outcome_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flows_outcome: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_outcome_id** | **str**| flow outcome ID |  |
| **body** | [**FlowOutcome**](FlowOutcome.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**Operation**](Operation.html)

