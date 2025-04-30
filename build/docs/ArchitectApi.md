# ArchitectApi

## PureCloudPlatformClientV2.ArchitectApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_architect_emergencygroup**](#delete_architect_emergencygroup) | Deletes a emergency group by ID|
|[**delete_architect_grammar**](#delete_architect_grammar) | Delete a grammar.|
|[**delete_architect_grammar_language**](#delete_architect_grammar_language) | Delete specified grammar language|
|[**delete_architect_grammar_language_files_dtmf**](#delete_architect_grammar_language_files_dtmf) | Clear the DTMF mode file for the grammar language if there is one|
|[**delete_architect_grammar_language_files_voice**](#delete_architect_grammar_language_files_voice) | Clear the voice mode file for the grammar language if there is one|
|[**delete_architect_ivr**](#delete_architect_ivr) | Delete an IVR Config.|
|[**delete_architect_prompt**](#delete_architect_prompt) | Delete specified user prompt|
|[**delete_architect_prompt_resource**](#delete_architect_prompt_resource) | Delete specified user prompt resource|
|[**delete_architect_prompt_resource_audio**](#delete_architect_prompt_resource_audio) | Delete specified user prompt resource audio|
|[**delete_architect_prompts**](#delete_architect_prompts) | Batch-delete a list of prompts|
|[**delete_architect_schedule**](#delete_architect_schedule) | Delete a schedule by id|
|[**delete_architect_schedulegroup**](#delete_architect_schedulegroup) | Deletes a schedule group by ID|
|[**delete_architect_systemprompt_resource**](#delete_architect_systemprompt_resource) | Delete a system prompt resource override.|
|[**delete_flow**](#delete_flow) | Delete flow|
|[**delete_flow_instances_settings_loglevels**](#delete_flow_instances_settings_loglevels) | Deletes a log level for a flow by flow id.|
|[**delete_flows**](#delete_flows) | Batch-delete a list of flows|
|[**delete_flows_datatable**](#delete_flows_datatable) | deletes a specific datatable by id|
|[**delete_flows_datatable_row**](#delete_flows_datatable_row) | Delete a row entry|
|[**delete_flows_instances_settings_loglevels_default**](#delete_flows_instances_settings_loglevels_default) | Resets the org log level to default, base|
|[**delete_flows_milestone**](#delete_flows_milestone) | Delete a flow milestone.|
|[**get_architect_dependencytracking**](#get_architect_dependencytracking) | Get Dependency Tracking objects that have a given display name|
|[**get_architect_dependencytracking_build**](#get_architect_dependencytracking_build) | Get Dependency Tracking build status for an organization|
|[**get_architect_dependencytracking_consumedresources**](#get_architect_dependencytracking_consumedresources) | Get resources that are consumed by a given Dependency Tracking object|
|[**get_architect_dependencytracking_consumingresources**](#get_architect_dependencytracking_consumingresources) | Get resources that consume a given Dependency Tracking object|
|[**get_architect_dependencytracking_deletedresourceconsumers**](#get_architect_dependencytracking_deletedresourceconsumers) | Get Dependency Tracking objects that consume deleted resources|
|[**get_architect_dependencytracking_object**](#get_architect_dependencytracking_object) | Get a Dependency Tracking object|
|[**get_architect_dependencytracking_type**](#get_architect_dependencytracking_type) | Get a Dependency Tracking type.|
|[**get_architect_dependencytracking_types**](#get_architect_dependencytracking_types) | Get Dependency Tracking types.|
|[**get_architect_dependencytracking_updatedresourceconsumers**](#get_architect_dependencytracking_updatedresourceconsumers) | Get Dependency Tracking objects that depend on updated resources|
|[**get_architect_emergencygroup**](#get_architect_emergencygroup) | Gets a emergency group by ID|
|[**get_architect_emergencygroups**](#get_architect_emergencygroups) | Get a list of emergency groups.|
|[**get_architect_emergencygroups_divisionviews**](#get_architect_emergencygroups_divisionviews) | Get a pageable list of basic emergency group objects filterable by query parameters.|
|[**get_architect_grammar**](#get_architect_grammar) | Get a grammar|
|[**get_architect_grammar_language**](#get_architect_grammar_language) | Get a grammar language.|
|[**get_architect_grammars**](#get_architect_grammars) | Get a pageable list of grammars, filtered by query parameters|
|[**get_architect_ivr**](#get_architect_ivr) | Get an IVR config.|
|[**get_architect_ivr_identityresolution**](#get_architect_ivr_identityresolution) | Get an IVR IdentityResolutionConfig.|
|[**get_architect_ivrs**](#get_architect_ivrs) | Get IVR configs.|
|[**get_architect_ivrs_divisionviews**](#get_architect_ivrs_divisionviews) | Get a pageable list of basic ivr configuration information objects filterable by query parameters.|
|[**get_architect_prompt**](#get_architect_prompt) | Get specified user prompt|
|[**get_architect_prompt_history_history_id**](#get_architect_prompt_history_history_id) | Get generated prompt history|
|[**get_architect_prompt_resource**](#get_architect_prompt_resource) | Get specified user prompt resource|
|[**get_architect_prompt_resources**](#get_architect_prompt_resources) | Get a pageable list of user prompt resources|
|[**get_architect_prompts**](#get_architect_prompts) | Get a pageable list of user prompts|
|[**get_architect_schedule**](#get_architect_schedule) | Get a schedule by ID|
|[**get_architect_schedulegroup**](#get_architect_schedulegroup) | Gets a schedule group by ID|
|[**get_architect_schedulegroups**](#get_architect_schedulegroups) | Get a list of schedule groups.|
|[**get_architect_schedulegroups_divisionviews**](#get_architect_schedulegroups_divisionviews) | Get a pageable list of basic schedule group configuration information objects filterable by query parameters.|
|[**get_architect_schedules**](#get_architect_schedules) | Get a list of schedules.|
|[**get_architect_schedules_divisionviews**](#get_architect_schedules_divisionviews) | Get a pageable list of basic schedule configuration information objects filterable by query parameters.|
|[**get_architect_systemprompt**](#get_architect_systemprompt) | Get a system prompt|
|[**get_architect_systemprompt_history_history_id**](#get_architect_systemprompt_history_history_id) | Get generated prompt history|
|[**get_architect_systemprompt_resource**](#get_architect_systemprompt_resource) | Get a system prompt resource.|
|[**get_architect_systemprompt_resources**](#get_architect_systemprompt_resources) | Get system prompt resources.|
|[**get_architect_systemprompts**](#get_architect_systemprompts) | Get System Prompts|
|[**get_flow**](#get_flow) | Get flow|
|[**get_flow_history_history_id**](#get_flow_history_history_id) | Get generated flow history|
|[**get_flow_instances_settings_loglevels**](#get_flow_instances_settings_loglevels) | Retrieves the log level for a flow by flow id.|
|[**get_flow_latestconfiguration**](#get_flow_latestconfiguration) | Get the latest configuration for flow|
|[**get_flow_version**](#get_flow_version) | Get flow version|
|[**get_flow_version_configuration**](#get_flow_version_configuration) | Get flow version configuration|
|[**get_flow_version_health**](#get_flow_version_health) | Get overall health scores for all intents present in the NLU domain version associated with the bot flow version.|
|[**get_flow_version_intent_health**](#get_flow_version_intent_health) | Get health scores and other health metrics for a specific intent. This includes the health metrics for each utterance in an intent.|
|[**get_flow_version_intent_utterance_health**](#get_flow_version_intent_utterance_health) | Get health metrics associated with a specific utterance of an intent.|
|[**get_flow_versions**](#get_flow_versions) | Get flow version list|
|[**get_flows**](#get_flows) | Get a pageable list of flows, filtered by query parameters|
|[**get_flows_datatable**](#get_flows_datatable) | Returns a specific datatable by id|
|[**get_flows_datatable_export_job**](#get_flows_datatable_export_job) | Returns the state information about an export job|
|[**get_flows_datatable_import_job**](#get_flows_datatable_import_job) | Returns the state information about an import job|
|[**get_flows_datatable_import_jobs**](#get_flows_datatable_import_jobs) | Get all recent import jobs|
|[**get_flows_datatable_row**](#get_flows_datatable_row) | Returns a specific row for the datatable|
|[**get_flows_datatable_rows**](#get_flows_datatable_rows) | Returns the rows for the datatable with the given id|
|[**get_flows_datatables**](#get_flows_datatables) | Retrieve a list of datatables for the org|
|[**get_flows_datatables_divisionview**](#get_flows_datatables_divisionview) | Returns a specific datatable by id|
|[**get_flows_datatables_divisionviews**](#get_flows_datatables_divisionviews) | Retrieve a list of datatables for the org|
|[**get_flows_divisionviews**](#get_flows_divisionviews) | Get a pageable list of basic flow information objects filterable by query parameters.|
|[**get_flows_execution**](#get_flows_execution) | Get a flow execution&#39;s details. Flow execution details are available for several days after the flow is started.|
|[**get_flows_export_job**](#get_flows_export_job) | Fetch Architect Export Job Status|
|[**get_flows_instance**](#get_flows_instance) | Start a process (job) to prepare a download of a singular flow execution data instance by Id|
|[**get_flows_instances_job**](#get_flows_instances_job) | Get the status and/or results of an asynchronous flow execution data retrieval job|
|[**get_flows_instances_querycapabilities**](#get_flows_instances_querycapabilities) | Retrieve a list of capabilities that the org can use to query for execution data|
|[**get_flows_instances_settings_executiondata**](#get_flows_instances_settings_executiondata) | Get the execution history enabled setting.|
|[**get_flows_instances_settings_loglevels**](#get_flows_instances_settings_loglevels) | Retrieve a list of LogLevels for the organization.|
|[**get_flows_instances_settings_loglevels_characteristics**](#get_flows_instances_settings_loglevels_characteristics) | Gets the available flow log level characteristics for this organization.|
|[**get_flows_instances_settings_loglevels_default**](#get_flows_instances_settings_loglevels_default) | Returns the flow default log level.|
|[**get_flows_job**](#get_flows_job) | Fetch Architect Job Status|
|[**get_flows_milestone**](#get_flows_milestone) | Get a flow milestone|
|[**get_flows_milestones**](#get_flows_milestones) | Get a pageable list of flow milestones, filtered by query parameters|
|[**get_flows_milestones_divisionviews**](#get_flows_milestones_divisionviews) | Get a pageable list of basic flow milestone information objects filterable by query parameters.|
|[**get_flows_outcome**](#get_flows_outcome) | Get a flow outcome|
|[**get_flows_outcomes**](#get_flows_outcomes) | Get a pageable list of flow outcomes, filtered by query parameters|
|[**get_flows_outcomes_divisionviews**](#get_flows_outcomes_divisionviews) | Get a pageable list of basic flow outcome information objects filterable by query parameters.|
|[**patch_architect_grammar**](#patch_architect_grammar) | Updates a grammar|
|[**patch_architect_grammar_language**](#patch_architect_grammar_language) | Updates a grammar language|
|[**patch_flows_instances_settings_executiondata**](#patch_flows_instances_settings_executiondata) | Edit the execution history enabled setting.|
|[**post_architect_dependencytracking_build**](#post_architect_dependencytracking_build) | Rebuild Dependency Tracking data for an organization|
|[**post_architect_emergencygroups**](#post_architect_emergencygroups) | Creates a new emergency group|
|[**post_architect_grammar_language_files_dtmf**](#post_architect_grammar_language_files_dtmf) | Creates a presigned URL for uploading a grammar DTMF mode file|
|[**post_architect_grammar_language_files_voice**](#post_architect_grammar_language_files_voice) | Creates a presigned URL for uploading a grammar voice mode file|
|[**post_architect_grammar_languages**](#post_architect_grammar_languages) | Create a new language for a given grammar|
|[**post_architect_grammars**](#post_architect_grammars) | Create a new grammar|
|[**post_architect_ivrs**](#post_architect_ivrs) | Create IVR config.|
|[**post_architect_prompt_history**](#post_architect_prompt_history) | Generate prompt history|
|[**post_architect_prompt_resource_uploads**](#post_architect_prompt_resource_uploads) | Creates a presigned URL for uploading a user prompt file|
|[**post_architect_prompt_resources**](#post_architect_prompt_resources) | Create a new user prompt resource|
|[**post_architect_prompts**](#post_architect_prompts) | Create a new user prompt|
|[**post_architect_schedulegroups**](#post_architect_schedulegroups) | Creates a new schedule group|
|[**post_architect_schedules**](#post_architect_schedules) | Create a new schedule.|
|[**post_architect_systemprompt_history**](#post_architect_systemprompt_history) | Generate system prompt history|
|[**post_architect_systemprompt_resource_uploads**](#post_architect_systemprompt_resource_uploads) | Creates a presigned URL for uploading a system prompt file|
|[**post_architect_systemprompt_resources**](#post_architect_systemprompt_resources) | Create system prompt resource override.|
|[**post_flow_history**](#post_flow_history) | Generate flow history|
|[**post_flow_instances_settings_loglevels**](#post_flow_instances_settings_loglevels) | Set the logLevel for a particular flow id|
|[**post_flow_versions**](#post_flow_versions) | Create flow version|
|[**post_flows**](#post_flows) | Create flow|
|[**post_flows_actions_checkin**](#post_flows_actions_checkin) | Check-in flow|
|[**post_flows_actions_checkout**](#post_flows_actions_checkout) | Check-out flow|
|[**post_flows_actions_deactivate**](#post_flows_actions_deactivate) | Deactivate flow|
|[**post_flows_actions_publish**](#post_flows_actions_publish) | Publish flow|
|[**post_flows_actions_revert**](#post_flows_actions_revert) | Revert flow|
|[**post_flows_actions_unlock**](#post_flows_actions_unlock) | Unlock flow|
|[**post_flows_datatable_export_jobs**](#post_flows_datatable_export_jobs) | Begin an export process for exporting all rows from a datatable|
|[**post_flows_datatable_import_jobs**](#post_flows_datatable_import_jobs) | Begin an import process for importing rows into a datatable|
|[**post_flows_datatable_rows**](#post_flows_datatable_rows) | Create a new row entry for the datatable.|
|[**post_flows_datatables**](#post_flows_datatables) | Create a new datatable with the specified json-schema definition|
|[**post_flows_executions**](#post_flows_executions) | Launch an instance of a flow definition, for flow types that support it such as the &#39;workflow&#39; type.|
|[**post_flows_export_jobs**](#post_flows_export_jobs) | Register Architect Export Job|
|[**post_flows_instances_jobs**](#post_flows_instances_jobs) | Start a process (job) that will prepare a list of execution data IDs for download.|
|[**post_flows_instances_query**](#post_flows_instances_query) | Query the database of existing flow histories to look for particular flow criteria|
|[**post_flows_jobs**](#post_flows_jobs) | Register Architect Job. Returns a URL where a file, such as an Architect flow YAML file, can be PUT which will then initiate the job.|
|[**post_flows_milestones**](#post_flows_milestones) | Create a flow milestone|
|[**post_flows_outcomes**](#post_flows_outcomes) | Create a flow outcome|
|[**put_architect_emergencygroup**](#put_architect_emergencygroup) | Updates a emergency group by ID|
|[**put_architect_ivr**](#put_architect_ivr) | Update an IVR Config.|
|[**put_architect_ivr_identityresolution**](#put_architect_ivr_identityresolution) | Update an IVR IdentityResolutionConfig.|
|[**put_architect_prompt**](#put_architect_prompt) | Update specified user prompt|
|[**put_architect_prompt_resource**](#put_architect_prompt_resource) | Update specified user prompt resource|
|[**put_architect_schedule**](#put_architect_schedule) | Update schedule by ID|
|[**put_architect_schedulegroup**](#put_architect_schedulegroup) | Updates a schedule group by ID|
|[**put_architect_systemprompt_resource**](#put_architect_systemprompt_resource) | Updates a system prompt resource override.|
|[**put_flow**](#put_flow) | Update flow|
|[**put_flow_instances_settings_loglevels**](#put_flow_instances_settings_loglevels) | Edit the logLevel for a particular flow id|
|[**put_flows_datatable**](#put_flows_datatable) | Updates a specific datatable by id|
|[**put_flows_datatable_row**](#put_flows_datatable_row) | Update a row entry|
|[**put_flows_instances_settings_loglevels_default**](#put_flows_instances_settings_loglevels_default) | Edit the flow default log level.|
|[**put_flows_milestone**](#put_flows_milestone) | Updates a flow milestone|
|[**put_flows_outcome**](#put_flows_outcome) | Updates a flow outcome|



## delete_architect_emergencygroup

>  delete_architect_emergencygroup(emergency_group_id)


Deletes a emergency group by ID

Wraps DELETE /api/v2/architect/emergencygroups/{emergencyGroupId} 

Requires ALL permissions: 

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

### Return type

void (empty response body)


## delete_architect_grammar

> object** delete_architect_grammar(grammar_id)


Delete a grammar.

Wraps DELETE /api/v2/architect/grammars/{grammarId} 

Requires ALL permissions: 

* architect:grammar:delete

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
grammar_id = 'grammar_id_example' # str | grammar ID

try:
    # Delete a grammar.
    api_response = api_instance.delete_architect_grammar(grammar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_grammar: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| grammar ID |  |

### Return type

**object**


## delete_architect_grammar_language

>  delete_architect_grammar_language(grammar_id, language_code)


Delete specified grammar language

Wraps DELETE /api/v2/architect/grammars/{grammarId}/languages/{languageCode} 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language

try:
    # Delete specified grammar language
    api_instance.delete_architect_grammar_language(grammar_id, language_code)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_grammar_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |

### Return type

void (empty response body)


## delete_architect_grammar_language_files_dtmf

>  delete_architect_grammar_language_files_dtmf(grammar_id, language_code)


Clear the DTMF mode file for the grammar language if there is one

Wraps DELETE /api/v2/architect/grammars/{grammarId}/languages/{languageCode}/files/dtmf 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language

try:
    # Clear the DTMF mode file for the grammar language if there is one
    api_instance.delete_architect_grammar_language_files_dtmf(grammar_id, language_code)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_grammar_language_files_dtmf: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |

### Return type

void (empty response body)


## delete_architect_grammar_language_files_voice

>  delete_architect_grammar_language_files_voice(grammar_id, language_code)


Clear the voice mode file for the grammar language if there is one

Wraps DELETE /api/v2/architect/grammars/{grammarId}/languages/{languageCode}/files/voice 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language

try:
    # Clear the voice mode file for the grammar language if there is one
    api_instance.delete_architect_grammar_language_files_voice(grammar_id, language_code)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_architect_grammar_language_files_voice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |

### Return type

void (empty response body)


## delete_architect_ivr

>  delete_architect_ivr(ivr_id)


Delete an IVR Config.

Wraps DELETE /api/v2/architect/ivrs/{ivrId} 

Requires ALL permissions: 

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

### Return type

void (empty response body)


## delete_architect_prompt

>  delete_architect_prompt(prompt_id, all_resources=all_resources)


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
all_resources = True # bool | Whether or not to delete all the prompt resources (optional)

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

### Return type

void (empty response body)


## delete_architect_prompt_resource

>  delete_architect_prompt_resource(prompt_id, language_code)


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

### Return type

void (empty response body)


## delete_architect_prompt_resource_audio

>  delete_architect_prompt_resource_audio(prompt_id, language_code)


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

### Return type

void (empty response body)


## delete_architect_prompts

> [**Operation**](Operation) delete_architect_prompts(id)


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
| **id** | [**list[str]**](str)| List of Prompt IDs |  |

### Return type

[**Operation**](Operation)


## delete_architect_schedule

>  delete_architect_schedule(schedule_id)


Delete a schedule by id

Wraps DELETE /api/v2/architect/schedules/{scheduleId} 

Requires ALL permissions: 

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

### Return type

void (empty response body)


## delete_architect_schedulegroup

>  delete_architect_schedulegroup(schedule_group_id)


Deletes a schedule group by ID

Wraps DELETE /api/v2/architect/schedulegroups/{scheduleGroupId} 

Requires ALL permissions: 

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

### Return type

void (empty response body)


## delete_architect_systemprompt_resource

>  delete_architect_systemprompt_resource(prompt_id, language_code)


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

### Return type

void (empty response body)


## delete_flow

>  delete_flow(flow_id)


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

### Return type

void (empty response body)


## delete_flow_instances_settings_loglevels

>  delete_flow_instances_settings_loglevels(flow_id)


Deletes a log level for a flow by flow id.

Deletes the associated log level for a flow by flow id

Wraps DELETE /api/v2/flows/{flowId}/instances/settings/loglevels 

Requires ALL permissions: 

* architect:flowLogLevel:delete

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
flow_id = 'flow_id_example' # str | The flow id to delete the loglevel for

try:
    # Deletes a log level for a flow by flow id.
    api_instance.delete_flow_instances_settings_loglevels(flow_id)
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flow_instances_settings_loglevels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| The flow id to delete the loglevel for |  |

### Return type

void (empty response body)


## delete_flows

> [**Operation**](Operation) delete_flows(id)


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
| **id** | [**list[str]**](str)| List of Flow IDs |  |

### Return type

[**Operation**](Operation)


## delete_flows_datatable

>  delete_flows_datatable(datatable_id, force=force)


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
force = False # bool | force delete, even if in use (optional) (default to False)

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
| **force** | **bool**| force delete, even if in use | [optional] [default to False] |

### Return type

void (empty response body)


## delete_flows_datatable_row

>  delete_flows_datatable_row(datatable_id, row_id)


Delete a row entry

Deletes a row with a given rowId (the value of the key field).

Wraps DELETE /api/v2/flows/datatables/{datatableId}/rows/{rowId} 

Requires ANY permissions: 

* architect:datatable:delete
* architect:datatableRow:delete

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

### Return type

void (empty response body)


## delete_flows_instances_settings_loglevels_default

>  delete_flows_instances_settings_loglevels_default()


Resets the org log level to default, base

Resets the org log level to default, base

Wraps DELETE /api/v2/flows/instances/settings/loglevels/default 

Requires ANY permissions: 

* architect:flowLogLevelDefault:delete

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
    # Resets the org log level to default, base
    api_instance.delete_flows_instances_settings_loglevels_default()
except ApiException as e:
    print("Exception when calling ArchitectApi->delete_flows_instances_settings_loglevels_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_flows_milestone

> object** delete_flows_milestone(milestone_id)


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

### Return type

**object**


## get_architect_dependencytracking

> [**DependencyObjectEntityListing**](DependencyObjectEntityListing) get_architect_dependencytracking(name, page_number=page_number, page_size=page_size, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type)


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
consumed_resources = True # bool | Include resources each result item consumes (optional)
consuming_resources = True # bool | Include resources that consume each result item (optional)
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
| **object_type** | [**list[str]**](str)| Object type(s) to search for | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **consumed_resources** | **bool**| Include resources each result item consumes | [optional]  |
| **consuming_resources** | **bool**| Include resources that consume each result item | [optional]  |
| **consumed_resource_type** | [**list[str]**](str)| Types of consumed resources to return, if consumed resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **consuming_resource_type** | [**list[str]**](str)| Types of consuming resources to return, if consuming resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing)


## get_architect_dependencytracking_build

> [**DependencyStatus**](DependencyStatus) get_architect_dependencytracking_build()


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

This endpoint does not need any parameters.

### Return type

[**DependencyStatus**](DependencyStatus)


## get_architect_dependencytracking_consumedresources

> [**ConsumedResourcesEntityListing**](ConsumedResourcesEntityListing) get_architect_dependencytracking_consumedresources(id, version, object_type, resource_type=resource_type, page_number=page_number, page_size=page_size)


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
| **object_type** | **str**| Consuming object type.  Only versioned types are allowed here. | <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **resource_type** | [**list[str]**](str)| Types of consumed resources to show | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**ConsumedResourcesEntityListing**](ConsumedResourcesEntityListing)


## get_architect_dependencytracking_consumingresources

> [**ConsumingResourcesEntityListing**](ConsumingResourcesEntityListing) get_architect_dependencytracking_consumingresources(id, object_type, resource_type=resource_type, version=version, page_number=page_number, page_size=page_size, flow_filter=flow_filter)


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
| **object_type** | **str**| Consumed object type | <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **resource_type** | [**list[str]**](str)| Types of consuming resources to show.  Only versioned types are allowed here. | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **version** | **str**| Object version | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **flow_filter** | **str**| Show only checkedIn or published flows | [optional] <br />**Values**: checkedIn, published |

### Return type

[**ConsumingResourcesEntityListing**](ConsumingResourcesEntityListing)


## get_architect_dependencytracking_deletedresourceconsumers

> [**DependencyObjectEntityListing**](DependencyObjectEntityListing) get_architect_dependencytracking_deletedresourceconsumers(name=name, object_type=object_type, flow_filter=flow_filter, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)


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
consumed_resources = False # bool | Return consumed resources? (optional) (default to False)
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
| **object_type** | [**list[str]**](str)| Object type(s) to search for | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **flow_filter** | **str**| Show only checkedIn or published flows | [optional] <br />**Values**: checkedIn, published |
| **consumed_resources** | **bool**| Return consumed resources? | [optional] [default to False] |
| **consumed_resource_type** | [**list[str]**](str)| Resource type(s) to return | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing)


## get_architect_dependencytracking_object

> [**DependencyObject**](DependencyObject) get_architect_dependencytracking_object(id, version=version, object_type=object_type, consumed_resources=consumed_resources, consuming_resources=consuming_resources, consumed_resource_type=consumed_resource_type, consuming_resource_type=consuming_resource_type, consumed_resource_request=consumed_resource_request)


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
consumed_resources = True # bool | Include resources this item consumes (optional)
consuming_resources = True # bool | Include resources that consume this item (optional)
consumed_resource_type = ['consumed_resource_type_example'] # list[str] | Types of consumed resources to return, if consumed resources are requested (optional)
consuming_resource_type = ['consuming_resource_type_example'] # list[str] | Types of consuming resources to return, if consuming resources are requested (optional)
consumed_resource_request = True # bool | Indicate that this is going to look up a consumed resource object (optional)

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
| **object_type** | **str**| Object type | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **consumed_resources** | **bool**| Include resources this item consumes | [optional]  |
| **consuming_resources** | **bool**| Include resources that consume this item | [optional]  |
| **consumed_resource_type** | [**list[str]**](str)| Types of consumed resources to return, if consumed resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **consuming_resource_type** | [**list[str]**](str)| Types of consuming resources to return, if consuming resources are requested | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **consumed_resource_request** | **bool**| Indicate that this is going to look up a consumed resource object | [optional]  |

### Return type

[**DependencyObject**](DependencyObject)


## get_architect_dependencytracking_type

> [**DependencyType**](DependencyType) get_architect_dependencytracking_type(type_id)


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

### Return type

[**DependencyType**](DependencyType)


## get_architect_dependencytracking_types

> [**DependencyTypeEntityListing**](DependencyTypeEntityListing) get_architect_dependencytracking_types(page_number=page_number, page_size=page_size)


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

### Return type

[**DependencyTypeEntityListing**](DependencyTypeEntityListing)


## get_architect_dependencytracking_updatedresourceconsumers

> [**DependencyObjectEntityListing**](DependencyObjectEntityListing) get_architect_dependencytracking_updatedresourceconsumers(name=name, object_type=object_type, consumed_resources=consumed_resources, consumed_resource_type=consumed_resource_type, page_number=page_number, page_size=page_size)


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
consumed_resources = False # bool | Return consumed resources? (optional) (default to False)
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
| **object_type** | [**list[str]**](str)| Object type(s) to search for | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **consumed_resources** | **bool**| Return consumed resources? | [optional] [default to False] |
| **consumed_resource_type** | [**list[str]**](str)| Resource type(s) to return | [optional] <br />**Values**: ACDLANGUAGE, ACDSKILL, ACDWRAPUPCODE, AUDIOCONNECTORBOT, BOTCONNECTORBOT, BOTCONNECTORINTEGRATION, BOTFLOW, BRIDGEACTION, COMMONMODULEFLOW, COMPOSERSCRIPT, CONTACTLIST, DATAACTION, DATATABLE, DECISIONTABLE, DIALOGENGINEBOT, DIALOGENGINEBOTVERSION, DIALOGFLOWAGENT, DIALOGFLOWCXAGENT, DIGITALBOTCONNECTOR, DIGITALBOTFLOW, EMAILROUTE, EMERGENCYGROUP, FLOWACTION, FLOWDATATYPE, FLOWMILESTONE, FLOWOUTCOME, GRAMMAR, GROUP, IMAGE, INBOUNDCALLFLOW, INBOUNDCHATFLOW, INBOUNDEMAILFLOW, INBOUNDSHORTMESSAGEFLOW, INQUEUECALLFLOW, INQUEUEEMAILFLOW, INQUEUESHORTMESSAGEFLOW, IVRCONFIGURATION, KNOWLEDGEBASE, KNOWLEDGEBASEDOCUMENT, LANGUAGE, LEXBOT, LEXBOTALIAS, LEXV2BOT, LEXV2BOTALIAS, NLUDOMAIN, NUANCEMIXBOT, NUANCEMIXINTEGRATION, OAUTHCLIENT, OUTBOUNDCALLFLOW, QUEUE, RECORDINGPOLICY, RESPONSE, SCHEDULE, SCHEDULEGROUP, SECUREACTION, SECURECALLFLOW, SMSPHONENUMBER, STTENGINE, SURVEYFORM, SURVEYINVITEFLOW, SYSTEMPROMPT, TTSENGINE, TTSVOICE, USER, USERPROMPT, UTILIZATIONLABEL, VOICEFLOW, VOICEMAILFLOW, VOICESURVEYFLOW, WIDGET, WORKFLOW, WORKITEMFLOW, WORKTYPE |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**DependencyObjectEntityListing**](DependencyObjectEntityListing)


## get_architect_emergencygroup

> [**EmergencyGroup**](EmergencyGroup) get_architect_emergencygroup(emergency_group_id)


Gets a emergency group by ID

Wraps GET /api/v2/architect/emergencygroups/{emergencyGroupId} 

Requires ALL permissions: 

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

### Return type

[**EmergencyGroup**](EmergencyGroup)


## get_architect_emergencygroups

> [**EmergencyGroupListing**](EmergencyGroupListing) get_architect_emergencygroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name)


Get a list of emergency groups.

Wraps GET /api/v2/architect/emergencygroups 

Requires ALL permissions: 

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
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
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **name** | **str**| Name of the Emergency Group to filter by. | [optional]  |

### Return type

[**EmergencyGroupListing**](EmergencyGroupListing)


## get_architect_emergencygroups_divisionviews

> [**EmergencyGroupDivisionViewEntityListing**](EmergencyGroupDivisionViewEntityListing) get_architect_emergencygroups_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


Get a pageable list of basic emergency group objects filterable by query parameters.

This returns emergency groups consisting of name and division. If one or more IDs are specified, the search will fetch flow outcomes that match the given ID(s) and not use any additional supplied query parameters in the search.

Wraps GET /api/v2/architect/emergencygroups/divisionviews 

Requires ALL permissions: 

* routing:emergencyGroup:search

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
id = ['id_example'] # list[str] | ID of the Emergency Groups to filter by. (optional)
name = 'name_example' # str | Name of the Emergency Group to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a pageable list of basic emergency group objects filterable by query parameters.
    api_response = api_instance.get_architect_emergencygroups_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_emergencygroups_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **id** | [**list[str]**](str)| ID of the Emergency Groups to filter by. | [optional]  |
| **name** | **str**| Name of the Emergency Group to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**EmergencyGroupDivisionViewEntityListing**](EmergencyGroupDivisionViewEntityListing)


## get_architect_grammar

> [**Grammar**](Grammar) get_architect_grammar(grammar_id, include_file_urls=include_file_urls)


Get a grammar

Returns a specified grammar

Wraps GET /api/v2/architect/grammars/{grammarId} 

Requires ALL permissions: 

* architect:grammar:view

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
grammar_id = 'grammar_id_example' # str | grammar ID
include_file_urls = True # bool | Include grammar language file URLs (optional)

try:
    # Get a grammar
    api_response = api_instance.get_architect_grammar(grammar_id, include_file_urls=include_file_urls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_grammar: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| grammar ID |  |
| **include_file_urls** | **bool**| Include grammar language file URLs | [optional]  |

### Return type

[**Grammar**](Grammar)


## get_architect_grammar_language

> [**GrammarLanguage**](GrammarLanguage) get_architect_grammar_language(grammar_id, language_code)


Get a grammar language.

Wraps GET /api/v2/architect/grammars/{grammarId}/languages/{languageCode} 

Requires ALL permissions: 

* architect:grammar:view

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language

try:
    # Get a grammar language.
    api_response = api_instance.get_architect_grammar_language(grammar_id, language_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_grammar_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |

### Return type

[**GrammarLanguage**](GrammarLanguage)


## get_architect_grammars

> [**GrammarListing**](GrammarListing) get_architect_grammars(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, include_file_urls=include_file_urls)


Get a pageable list of grammars, filtered by query parameters

Multiple IDs can be specified, in which case all matching grammars will be returned, and no other parameters will be evaluated.

Wraps GET /api/v2/architect/grammars 

Requires ALL permissions: 

* architect:grammar:view

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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
include_file_urls = True # bool | Include grammar language file URLs (optional)

try:
    # Get a pageable list of grammars, filtered by query parameters
    api_response = api_instance.get_architect_grammars(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, include_file_urls=include_file_urls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_grammars: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;]<br />**Values**: description, id, name |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **include_file_urls** | **bool**| Include grammar language file URLs | [optional]  |

### Return type

[**GrammarListing**](GrammarListing)


## get_architect_ivr

> [**IVR**](IVR) get_architect_ivr(ivr_id)


Get an IVR config.

Wraps GET /api/v2/architect/ivrs/{ivrId} 

Requires ALL permissions: 

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

### Return type

[**IVR**](IVR)


## get_architect_ivr_identityresolution

> [**IdentityResolutionConfig**](IdentityResolutionConfig) get_architect_ivr_identityresolution(ivr_id)


Get an IVR IdentityResolutionConfig.

get_architect_ivr_identityresolution is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/architect/ivrs/{ivrId}/identityresolution 

Requires ALL permissions: 

* routing:callRoute:view
* routing:identityResolution:view

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
    # Get an IVR IdentityResolutionConfig.
    api_response = api_instance.get_architect_ivr_identityresolution(ivr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_ivr_identityresolution: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ivr_id** | **str**| IVR id |  |

### Return type

[**IdentityResolutionConfig**](IdentityResolutionConfig)


## get_architect_ivrs

> [**IVREntityListing**](IVREntityListing) get_architect_ivrs(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, dnis=dnis, schedule_group=schedule_group)


Get IVR configs.

Wraps GET /api/v2/architect/ivrs 

Requires ALL permissions: 

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
name = 'name_example' # str | Name of the IVR to filter by. (optional)
dnis = 'dnis_example' # str | The phone number of the IVR to filter by. (optional)
schedule_group = 'schedule_group_example' # str | The Schedule Group of the IVR to filter by. (optional)

try:
    # Get IVR configs.
    api_response = api_instance.get_architect_ivrs(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, dnis=dnis, schedule_group=schedule_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_ivrs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **name** | **str**| Name of the IVR to filter by. | [optional]  |
| **dnis** | **str**| The phone number of the IVR to filter by. | [optional]  |
| **schedule_group** | **str**| The Schedule Group of the IVR to filter by. | [optional]  |

### Return type

[**IVREntityListing**](IVREntityListing)


## get_architect_ivrs_divisionviews

> [**IVRDivisionViewEntityListing**](IVRDivisionViewEntityListing) get_architect_ivrs_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


Get a pageable list of basic ivr configuration information objects filterable by query parameters.

Wraps GET /api/v2/architect/ivrs/divisionviews 

Requires ALL permissions: 

* routing:callRoute:search

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
id = ['id_example'] # list[str] | ID of the IVR to filter by. (optional)
name = 'name_example' # str | Name of the IVR to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a pageable list of basic ivr configuration information objects filterable by query parameters.
    api_response = api_instance.get_architect_ivrs_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_ivrs_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **id** | [**list[str]**](str)| ID of the IVR to filter by. | [optional]  |
| **name** | **str**| Name of the IVR to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**IVRDivisionViewEntityListing**](IVRDivisionViewEntityListing)


## get_architect_prompt

> [**Prompt**](Prompt) get_architect_prompt(prompt_id, include_media_uris=include_media_uris, include_resources=include_resources, language=language)


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
include_media_uris = True # bool | Include the media URIs for each resource (optional) (default to True)
include_resources = True # bool | Include the resources for each system prompt (optional) (default to True)
language = ['language_example'] # list[str] | Filter the resources down to the provided languages (optional)

try:
    # Get specified user prompt
    api_response = api_instance.get_architect_prompt(prompt_id, include_media_uris=include_media_uris, include_resources=include_resources, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_prompt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **include_media_uris** | **bool**| Include the media URIs for each resource | [optional] [default to True] |
| **include_resources** | **bool**| Include the resources for each system prompt | [optional] [default to True] |
| **language** | [**list[str]**](str)| Filter the resources down to the provided languages | [optional]  |

### Return type

[**Prompt**](Prompt)


## get_architect_prompt_history_history_id

> [**HistoryListing**](HistoryListing) get_architect_prompt_history_history_id(prompt_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)


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
sort_order = ''desc'' # str | Sort order (optional) (default to 'desc')
sort_by = ''timestamp'' # str | Sort by (optional) (default to 'timestamp')
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
| **sort_order** | **str**| Sort order | [optional] [default to &#39;desc&#39;] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;timestamp&#39;]<br />**Values**: action, timestamp, user |
| **action** | [**list[str]**](str)| Flow actions to include (omit to include all) | [optional] <br />**Values**: checkin, checkout, create, deactivate, debug, delete, publish, revert, save |

### Return type

[**HistoryListing**](HistoryListing)


## get_architect_prompt_resource

> [**PromptAsset**](PromptAsset) get_architect_prompt_resource(prompt_id, language_code)


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

### Return type

[**PromptAsset**](PromptAsset)


## get_architect_prompt_resources

> [**PromptAssetEntityListing**](PromptAssetEntityListing) get_architect_prompt_resources(prompt_id, page_number=page_number, page_size=page_size)


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

### Return type

[**PromptAssetEntityListing**](PromptAssetEntityListing)


## get_architect_prompts

> [**PromptEntityListing**](PromptEntityListing) get_architect_prompts(page_number=page_number, page_size=page_size, name=name, description=description, name_or_description=name_or_description, sort_by=sort_by, sort_order=sort_order, include_media_uris=include_media_uris, include_resources=include_resources, language=language)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
include_media_uris = True # bool | Include the media URIs for each resource (optional) (default to True)
include_resources = True # bool | Include the resources for each system prompt (optional) (default to True)
language = ['language_example'] # list[str] | Filter the resources down to the provided languages (optional)

try:
    # Get a pageable list of user prompts
    api_response = api_instance.get_architect_prompts(page_number=page_number, page_size=page_size, name=name, description=description, name_or_description=name_or_description, sort_by=sort_by, sort_order=sort_order, include_media_uris=include_media_uris, include_resources=include_resources, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_prompts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | [**list[str]**](str)| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **include_media_uris** | **bool**| Include the media URIs for each resource | [optional] [default to True] |
| **include_resources** | **bool**| Include the resources for each system prompt | [optional] [default to True] |
| **language** | [**list[str]**](str)| Filter the resources down to the provided languages | [optional]  |

### Return type

[**PromptEntityListing**](PromptEntityListing)


## get_architect_schedule

> [**Schedule**](Schedule) get_architect_schedule(schedule_id)


Get a schedule by ID

Wraps GET /api/v2/architect/schedules/{scheduleId} 

Requires ALL permissions: 

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

### Return type

[**Schedule**](Schedule)


## get_architect_schedulegroup

> [**ScheduleGroup**](ScheduleGroup) get_architect_schedulegroup(schedule_group_id)


Gets a schedule group by ID

Wraps GET /api/v2/architect/schedulegroups/{scheduleGroupId} 

Requires ALL permissions: 

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

### Return type

[**ScheduleGroup**](ScheduleGroup)


## get_architect_schedulegroups

> [**ScheduleGroupEntityListing**](ScheduleGroupEntityListing) get_architect_schedulegroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, schedule_ids=schedule_ids, division_id=division_id)


Get a list of schedule groups.

Wraps GET /api/v2/architect/schedulegroups 

Requires ALL permissions: 

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
name = 'name_example' # str | Name of the Schedule Group to filter by. (optional)
schedule_ids = 'schedule_ids_example' # str | A comma-delimited list of Schedule IDs to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a list of schedule groups.
    api_response = api_instance.get_architect_schedulegroups(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, schedule_ids=schedule_ids, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedulegroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **name** | **str**| Name of the Schedule Group to filter by. | [optional]  |
| **schedule_ids** | **str**| A comma-delimited list of Schedule IDs to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**ScheduleGroupEntityListing**](ScheduleGroupEntityListing)


## get_architect_schedulegroups_divisionviews

> [**ScheduleGroupDivisionViewEntityListing**](ScheduleGroupDivisionViewEntityListing) get_architect_schedulegroups_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


Get a pageable list of basic schedule group configuration information objects filterable by query parameters.

Wraps GET /api/v2/architect/schedulegroups/divisionviews 

Requires ALL permissions: 

* routing:scheduleGroup:search

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
id = ['id_example'] # list[str] | ID of the schedule group to filter by. (optional)
name = 'name_example' # str | Name of the schedule group to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a pageable list of basic schedule group configuration information objects filterable by query parameters.
    api_response = api_instance.get_architect_schedulegroups_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedulegroups_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **id** | [**list[str]**](str)| ID of the schedule group to filter by. | [optional]  |
| **name** | **str**| Name of the schedule group to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**ScheduleGroupDivisionViewEntityListing**](ScheduleGroupDivisionViewEntityListing)


## get_architect_schedules

> [**ScheduleEntityListing**](ScheduleEntityListing) get_architect_schedules(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, division_id=division_id)


Get a list of schedules.

Wraps GET /api/v2/architect/schedules 

Requires ALL permissions: 

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
name = 'name_example' # str | Name of the Schedule to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a list of schedules.
    api_response = api_instance.get_architect_schedules(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **name** | **str**| Name of the Schedule to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**ScheduleEntityListing**](ScheduleEntityListing)


## get_architect_schedules_divisionviews

> [**ScheduleDivisionViewEntityListing**](ScheduleDivisionViewEntityListing) get_architect_schedules_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


Get a pageable list of basic schedule configuration information objects filterable by query parameters.

Wraps GET /api/v2/architect/schedules/divisionviews 

Requires ALL permissions: 

* routing:schedule:search

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
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
id = ['id_example'] # list[str] | ID of the schedule group to filter by. (optional)
name = 'name_example' # str | Name of the schedule group to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a pageable list of basic schedule configuration information objects filterable by query parameters.
    api_response = api_instance.get_architect_schedules_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_schedules_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **id** | [**list[str]**](str)| ID of the schedule group to filter by. | [optional]  |
| **name** | **str**| Name of the schedule group to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**ScheduleDivisionViewEntityListing**](ScheduleDivisionViewEntityListing)


## get_architect_systemprompt

> [**SystemPrompt**](SystemPrompt) get_architect_systemprompt(prompt_id, include_media_uris=include_media_uris, include_resources=include_resources, language=language)


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
include_media_uris = True # bool | Include the media URIs for each resource (optional) (default to True)
include_resources = True # bool | Include the resources for each system prompt (optional) (default to True)
language = ['language_example'] # list[str] | Filter the resources down to the provided languages (optional)

try:
    # Get a system prompt
    api_response = api_instance.get_architect_systemprompt(prompt_id, include_media_uris=include_media_uris, include_resources=include_resources, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_systemprompt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| promptId |  |
| **include_media_uris** | **bool**| Include the media URIs for each resource | [optional] [default to True] |
| **include_resources** | **bool**| Include the resources for each system prompt | [optional] [default to True] |
| **language** | [**list[str]**](str)| Filter the resources down to the provided languages | [optional]  |

### Return type

[**SystemPrompt**](SystemPrompt)


## get_architect_systemprompt_history_history_id

> [**HistoryListing**](HistoryListing) get_architect_systemprompt_history_history_id(prompt_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)


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
sort_order = ''desc'' # str | Sort order (optional) (default to 'desc')
sort_by = ''timestamp'' # str | Sort by (optional) (default to 'timestamp')
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
| **sort_order** | **str**| Sort order | [optional] [default to &#39;desc&#39;] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;timestamp&#39;]<br />**Values**: action, timestamp, user |
| **action** | [**list[str]**](str)| Flow actions to include (omit to include all) | [optional] <br />**Values**: checkin, checkout, create, deactivate, debug, delete, publish, revert, save |

### Return type

[**HistoryListing**](HistoryListing)


## get_architect_systemprompt_resource

> [**SystemPromptAsset**](SystemPromptAsset) get_architect_systemprompt_resource(prompt_id, language_code)


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

### Return type

[**SystemPromptAsset**](SystemPromptAsset)


## get_architect_systemprompt_resources

> [**SystemPromptAssetEntityListing**](SystemPromptAssetEntityListing) get_architect_systemprompt_resources(prompt_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')

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
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |

### Return type

[**SystemPromptAssetEntityListing**](SystemPromptAssetEntityListing)


## get_architect_systemprompts

> [**SystemPromptEntityListing**](SystemPromptEntityListing) get_architect_systemprompts(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, description=description, name_or_description=name_or_description, include_media_uris=include_media_uris, include_resources=include_resources, language=language)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
include_media_uris = True # bool | Include the media URIs for each resource (optional) (default to True)
include_resources = True # bool | Include the resources for each system prompt (optional) (default to True)
language = ['language_example'] # list[str] | Filter the resources down to the provided languages (optional)

try:
    # Get System Prompts
    api_response = api_instance.get_architect_systemprompts(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, name=name, description=description, name_or_description=name_or_description, include_media_uris=include_media_uris, include_resources=include_resources, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_architect_systemprompts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **include_media_uris** | **bool**| Include the media URIs for each resource | [optional] [default to True] |
| **include_resources** | **bool**| Include the resources for each system prompt | [optional] [default to True] |
| **language** | [**list[str]**](str)| Filter the resources down to the provided languages | [optional]  |

### Return type

[**SystemPromptEntityListing**](SystemPromptEntityListing)


## get_flow

> [**Flow**](Flow) get_flow(flow_id, deleted=deleted)


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
deleted = False # bool | Deleted flows (optional) (default to False)

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
| **deleted** | **bool**| Deleted flows | [optional] [default to False] |

### Return type

[**Flow**](Flow)


## get_flow_history_history_id

> [**HistoryListing**](HistoryListing) get_flow_history_history_id(flow_id, history_id, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, action=action)


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
sort_order = ''desc'' # str | Sort order (optional) (default to 'desc')
sort_by = ''timestamp'' # str | Sort by (optional) (default to 'timestamp')
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
| **sort_order** | **str**| Sort order | [optional] [default to &#39;desc&#39;] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;timestamp&#39;]<br />**Values**: action, timestamp, user |
| **action** | [**list[str]**](str)| Flow actions to include (omit to include all) | [optional] <br />**Values**: checkin, checkout, create, deactivate, debug, delete, publish, revert, save |

### Return type

[**HistoryListing**](HistoryListing)


## get_flow_instances_settings_loglevels

> [**FlowSettingsResponse**](FlowSettingsResponse) get_flow_instances_settings_loglevels(flow_id, expand=expand)


Retrieves the log level for a flow by flow id.

Retrieves the log level for a flow by flow id.

Wraps GET /api/v2/flows/{flowId}/instances/settings/loglevels 

Requires ALL permissions: 

* architect:flowLogLevel:view

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
flow_id = 'flow_id_example' # str | The flow id to get the loglevel for
expand = ['expand_example'] # list[str] | Expand instructions for the result (optional)

try:
    # Retrieves the log level for a flow by flow id.
    api_response = api_instance.get_flow_instances_settings_loglevels(flow_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_instances_settings_loglevels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| The flow id to get the loglevel for |  |
| **expand** | [**list[str]**](str)| Expand instructions for the result | [optional] <br />**Values**: name, type, logLevelCharacteristics.characteristics |

### Return type

[**FlowSettingsResponse**](FlowSettingsResponse)


## get_flow_latestconfiguration

> object** get_flow_latestconfiguration(flow_id, deleted=deleted)


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
deleted = False # bool | Deleted flows (optional) (default to False)

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
| **deleted** | **bool**| Deleted flows | [optional] [default to False] |

### Return type

**object**


## get_flow_version

> [**FlowVersion**](FlowVersion) get_flow_version(flow_id, version_id, deleted=deleted)


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

### Return type

[**FlowVersion**](FlowVersion)


## get_flow_version_configuration

> object** get_flow_version_configuration(flow_id, version_id, deleted=deleted)


Get flow version configuration

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
    # Get flow version configuration
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

### Return type

**object**


## get_flow_version_health

> [**FlowHealth**](FlowHealth) get_flow_version_health(flow_id, version_id, language=language)


Get overall health scores for all intents present in the NLU domain version associated with the bot flow version.

Wraps GET /api/v2/flows/{flowId}/versions/{versionId}/health 

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
flow_id = 'flow_id_example' # str | Flow ID.
version_id = 'version_id_example' # str | Version ID.
language = 'language_example' # str | Language to filter for (optional)

try:
    # Get overall health scores for all intents present in the NLU domain version associated with the bot flow version.
    api_response = api_instance.get_flow_version_health(flow_id, version_id, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_version_health: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID. |  |
| **version_id** | **str**| Version ID. |  |
| **language** | **str**| Language to filter for | [optional] <br />**Values**: en-us, en-gb, en-au, en-za, en-nz, en-ie, fr-ca, fr-fr, es-us, es-es, es-mx, de-de, it-it, pt-br, pt-pt, nl-nl |

### Return type

[**FlowHealth**](FlowHealth)


## get_flow_version_intent_health

> [**FlowHealthIntent**](FlowHealthIntent) get_flow_version_intent_health(flow_id, version_id, intent_id, language)


Get health scores and other health metrics for a specific intent. This includes the health metrics for each utterance in an intent.

Wraps GET /api/v2/flows/{flowId}/versions/{versionId}/intents/{intentId}/health 

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
flow_id = 'flow_id_example' # str | Flow ID.
version_id = 'version_id_example' # str | Version ID.
intent_id = 'intent_id_example' # str | Intent ID.
language = 'language_example' # str | Language to filter for

try:
    # Get health scores and other health metrics for a specific intent. This includes the health metrics for each utterance in an intent.
    api_response = api_instance.get_flow_version_intent_health(flow_id, version_id, intent_id, language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_version_intent_health: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID. |  |
| **version_id** | **str**| Version ID. |  |
| **intent_id** | **str**| Intent ID. |  |
| **language** | **str**| Language to filter for | <br />**Values**: en-us, en-gb, en-au, en-za, en-nz, en-ie, fr-ca, fr-fr, es-us, es-es, es-mx, de-de, it-it, pt-br, pt-pt, nl-nl |

### Return type

[**FlowHealthIntent**](FlowHealthIntent)


## get_flow_version_intent_utterance_health

> [**FlowHealthUtterance**](FlowHealthUtterance) get_flow_version_intent_utterance_health(flow_id, version_id, intent_id, utterance_id, language)


Get health metrics associated with a specific utterance of an intent.

Wraps GET /api/v2/flows/{flowId}/versions/{versionId}/intents/{intentId}/utterances/{utteranceId}/health 

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
flow_id = 'flow_id_example' # str | Flow ID.
version_id = 'version_id_example' # str | Version ID.
intent_id = 'intent_id_example' # str | Intent ID.
utterance_id = 'utterance_id_example' # str | Utterance ID.
language = 'language_example' # str | Language to filter for

try:
    # Get health metrics associated with a specific utterance of an intent.
    api_response = api_instance.get_flow_version_intent_utterance_health(flow_id, version_id, intent_id, utterance_id, language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flow_version_intent_utterance_health: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID. |  |
| **version_id** | **str**| Version ID. |  |
| **intent_id** | **str**| Intent ID. |  |
| **utterance_id** | **str**| Utterance ID. |  |
| **language** | **str**| Language to filter for | <br />**Values**: en-us, en-gb, en-au, en-za, en-nz, en-ie, fr-ca, fr-fr, es-us, es-es, es-mx, de-de, it-it, pt-br, pt-pt, nl-nl |

### Return type

[**FlowHealthUtterance**](FlowHealthUtterance)


## get_flow_versions

> [**FlowVersionEntityListing**](FlowVersionEntityListing) get_flow_versions(flow_id, page_number=page_number, page_size=page_size, deleted=deleted)


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
deleted = True # bool | Include Deleted flows (optional)

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

### Return type

[**FlowVersionEntityListing**](FlowVersionEntityListing)


## get_flows

> [**FlowEntityListing**](FlowEntityListing) get_flows(type=type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, publish_version_id=publish_version_id, editable_by=editable_by, locked_by=locked_by, locked_by_client_id=locked_by_client_id, secure=secure, deleted=deleted, include_schemas=include_schemas, published_after=published_after, published_before=published_before, division_id=division_id)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
publish_version_id = 'publish_version_id_example' # str | Publish version ID (optional)
editable_by = 'editable_by_example' # str | Editable by (optional)
locked_by = 'locked_by_example' # str | Locked by (optional)
locked_by_client_id = 'locked_by_client_id_example' # str | Locked by client ID (optional)
secure = 'secure_example' # str | Secure (optional)
deleted = False # bool | Include deleted (optional) (default to False)
include_schemas = False # bool | Include variable schemas (optional) (default to False)
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
| **type** | [**list[str]**](str)| Type | [optional] <br />**Values**: bot, commonmodule, digitalbot, inboundcall, inboundchat, inboundemail, inboundshortmessage, outboundcall, inqueuecall, inqueueemail, inqueueshortmessage, speech, securecall, surveyinvite, voice, voicemail, voicesurvey, workflow, workitem |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **publish_version_id** | **str**| Publish version ID | [optional]  |
| **editable_by** | **str**| Editable by | [optional]  |
| **locked_by** | **str**| Locked by | [optional]  |
| **locked_by_client_id** | **str**| Locked by client ID | [optional]  |
| **secure** | **str**| Secure | [optional] <br />**Values**: any, checkedin, published |
| **deleted** | **bool**| Include deleted | [optional] [default to False] |
| **include_schemas** | **bool**| Include variable schemas | [optional] [default to False] |
| **published_after** | **str**| Published after | [optional]  |
| **published_before** | **str**| Published before | [optional]  |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |

### Return type

[**FlowEntityListing**](FlowEntityListing)


## get_flows_datatable

> [**DataTable**](DataTable) get_flows_datatable(datatable_id, expand=expand)


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

### Return type

[**DataTable**](DataTable)


## get_flows_datatable_export_job

> [**DataTableExportJob**](DataTableExportJob) get_flows_datatable_export_job(datatable_id, export_job_id)


Returns the state information about an export job

Returns the state information about an export job.

Wraps GET /api/v2/flows/datatables/{datatableId}/export/jobs/{exportJobId} 

Requires ANY permissions: 

* architect:datatable:view
* architect:datatableRow:view

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

### Return type

[**DataTableExportJob**](DataTableExportJob)


## get_flows_datatable_import_job

> [**DataTableImportJob**](DataTableImportJob) get_flows_datatable_import_job(datatable_id, import_job_id)


Returns the state information about an import job

Returns the state information about an import job.

Wraps GET /api/v2/flows/datatables/{datatableId}/import/jobs/{importJobId} 

Requires ANY permissions: 

* architect:datatable:view
* architect:datatableRow:view

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

### Return type

[**DataTableImportJob**](DataTableImportJob)


## get_flows_datatable_import_jobs

> [**DataTableImportEntityListing**](DataTableImportEntityListing) get_flows_datatable_import_jobs(datatable_id, page_number=page_number, page_size=page_size)


Get all recent import jobs

Get all recent import jobs

Wraps GET /api/v2/flows/datatables/{datatableId}/import/jobs 

Requires ANY permissions: 

* architect:datatable:edit
* architect:datatableRow:view

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

### Return type

[**DataTableImportEntityListing**](DataTableImportEntityListing)


## get_flows_datatable_row

> dict(str, object)** get_flows_datatable_row(datatable_id, row_id, showbrief=showbrief)


Returns a specific row for the datatable

Given a datatableId and a rowId (the value of the key field) this will return the full row contents for that rowId.

Wraps GET /api/v2/flows/datatables/{datatableId}/rows/{rowId} 

Requires ANY permissions: 

* architect:datatable:view
* architect:datatableRow:view

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
showbrief = True # bool | if true returns just the key field for the row (optional) (default to True)

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
| **showbrief** | **bool**| if true returns just the key field for the row | [optional] [default to True] |

### Return type

**dict(str, object)**


## get_flows_datatable_rows

> [**DataTableRowEntityListing**](DataTableRowEntityListing) get_flows_datatable_rows(datatable_id, page_number=page_number, page_size=page_size, showbrief=showbrief, sort_order=sort_order)


Returns the rows for the datatable with the given id

Returns all of the rows for the datatable with the given datatableId.  By default this will just be a truncated list returning the key for each row. Set showBrief to false to return all of the row contents.

Wraps GET /api/v2/flows/datatables/{datatableId}/rows 

Requires ANY permissions: 

* architect:datatable:view
* architect:datatableRow:view

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
showbrief = True # bool | If true returns just the key value of the row (optional) (default to True)
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')

try:
    # Returns the rows for the datatable with the given id
    api_response = api_instance.get_flows_datatable_rows(datatable_id, page_number=page_number, page_size=page_size, showbrief=showbrief, sort_order=sort_order)
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
| **showbrief** | **bool**| If true returns just the key value of the row | [optional] [default to True] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |

### Return type

[**DataTableRowEntityListing**](DataTableRowEntityListing)


## get_flows_datatables

> [**DataTablesDomainEntityListing**](DataTablesDomainEntityListing) get_flows_datatables(expand=expand, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, division_id=division_id, name=name)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)
name = 'exactMatch, beginsWith*, *endsWith, *contains*' # str | Filter by Name. The wildcard character * is supported within the filter. Matches are case-insensitive. (optional)

try:
    # Retrieve a list of datatables for the org
    api_response = api_instance.get_flows_datatables(expand=expand, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, division_id=division_id, name=name)
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
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;]<br />**Values**: id, name |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;] |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |
| **name** | **str**| Filter by Name. The wildcard character * is supported within the filter. Matches are case-insensitive. | [optional]  |

### Return type

[**DataTablesDomainEntityListing**](DataTablesDomainEntityListing)


## get_flows_datatables_divisionview

> [**DataTable**](DataTable) get_flows_datatables_divisionview(datatable_id, expand=expand)


Returns a specific datatable by id

Given a datatableId returns the datatable object and schema associated with it.

Wraps GET /api/v2/flows/datatables/divisionviews/{datatableId} 

Requires ALL permissions: 

* architect:datatable:search

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
    api_response = api_instance.get_flows_datatables_divisionview(datatable_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatables_divisionview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **expand** | **str**| Expand instructions for the result | [optional] <br />**Values**: schema |

### Return type

[**DataTable**](DataTable)


## get_flows_datatables_divisionviews

> [**DataTablesDomainEntityListing**](DataTablesDomainEntityListing) get_flows_datatables_divisionviews(expand=expand, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, division_id=division_id, name=name)


Retrieve a list of datatables for the org

Returns a metadata list of the datatables associated with this org, including datatableId, name and description.

Wraps GET /api/v2/flows/datatables/divisionviews 

Requires ALL permissions: 

* architect:datatable:search

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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)
name = 'exactMatch, beginsWith*, *endsWith, *contains*' # str | Filter by Name. The wildcard character * is supported within the filter. Matches are case-insensitive. (optional)

try:
    # Retrieve a list of datatables for the org
    api_response = api_instance.get_flows_datatables_divisionviews(expand=expand, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, division_id=division_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_datatables_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | **str**| Expand instructions for the result | [optional] <br />**Values**: schema |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;]<br />**Values**: id, name |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;] |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |
| **name** | **str**| Filter by Name. The wildcard character * is supported within the filter. Matches are case-insensitive. | [optional]  |

### Return type

[**DataTablesDomainEntityListing**](DataTablesDomainEntityListing)


## get_flows_divisionviews

> [**FlowDivisionViewEntityListing**](FlowDivisionViewEntityListing) get_flows_divisionviews(type=type, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, publish_version_id=publish_version_id, published_after=published_after, published_before=published_before, division_id=division_id, include_schemas=include_schemas)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
publish_version_id = 'publish_version_id_example' # str | Publish version ID (optional)
published_after = '2015-01-01T12:00:00-0600, 2015-01-01T18:00:00Z, 2015-01-01T12:00:00.000-0600, 2015-01-01T18:00:00.000Z, 2015-01-01' # str | Published after (optional)
published_before = '2015-01-01T12:00:00-0600, 2015-01-01T18:00:00Z, 2015-01-01T12:00:00.000-0600, 2015-01-01T18:00:00.000Z, 2015-01-01' # str | Published before (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)
include_schemas = False # bool | Include variable schemas (optional) (default to False)

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
| **type** | [**list[str]**](str)| Type | [optional] <br />**Values**: bot, commonmodule, digitalbot, inboundcall, inboundchat, inboundemail, inboundshortmessage, outboundcall, inqueuecall, inqueueemail, inqueueshortmessage, speech, securecall, surveyinvite, voice, voicemail, voicesurvey, workflow, workitem |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **publish_version_id** | **str**| Publish version ID | [optional]  |
| **published_after** | **str**| Published after | [optional]  |
| **published_before** | **str**| Published before | [optional]  |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |
| **include_schemas** | **bool**| Include variable schemas | [optional] [default to False] |

### Return type

[**FlowDivisionViewEntityListing**](FlowDivisionViewEntityListing)


## get_flows_execution

> [**FlowRuntimeExecution**](FlowRuntimeExecution) get_flows_execution(flow_execution_id)


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

### Return type

[**FlowRuntimeExecution**](FlowRuntimeExecution)


## get_flows_export_job

> [**ArchitectExportJobStateResponse**](ArchitectExportJobStateResponse) get_flows_export_job(job_id, expand=expand)


Fetch Architect Export Job Status

Wraps GET /api/v2/flows/export/jobs/{jobId} 

Requires ALL permissions: 

* architect:jobExport:view

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
job_id = 'job_id_example' # str | Job ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Fetch Architect Export Job Status
    api_response = api_instance.get_flows_export_job(job_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_export_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Job ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: messages |

### Return type

[**ArchitectExportJobStateResponse**](ArchitectExportJobStateResponse)


## get_flows_instance

> [**GetFlowExecutionDataJobResult**](GetFlowExecutionDataJobResult) get_flows_instance(instance_id, expand=expand)


Start a process (job) to prepare a download of a singular flow execution data instance by Id

Returns a JobResult object that contains an ID that can be used to check status and/or download links when the process (job) is complete.

Wraps GET /api/v2/flows/instances/{instanceId} 

Requires ANY permissions: 

* architect:flowInstance:view

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
instance_id = 'instance_id_example' # str | Instance ID
expand = 'expand_example' # str | Expand various details. (optional)

try:
    # Start a process (job) to prepare a download of a singular flow execution data instance by Id
    api_response = api_instance.get_flows_instance(instance_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instance: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **instance_id** | **str**| Instance ID |  |
| **expand** | **str**| Expand various details. | [optional] <br />**Values**: bots, dataActions |

### Return type

[**GetFlowExecutionDataJobResult**](GetFlowExecutionDataJobResult)


## get_flows_instances_job

> [**GetFlowExecutionDataJobResult**](GetFlowExecutionDataJobResult) get_flows_instances_job(job_id)


Get the status and/or results of an asynchronous flow execution data retrieval job

Wraps GET /api/v2/flows/instances/jobs/{jobId} 

Requires ANY permissions: 

* architect:flowInstance:view

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
job_id = 'job_id_example' # str | The asynchronous job ID

try:
    # Get the status and/or results of an asynchronous flow execution data retrieval job
    api_response = api_instance.get_flows_instances_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instances_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The asynchronous job ID |  |

### Return type

[**GetFlowExecutionDataJobResult**](GetFlowExecutionDataJobResult)


## get_flows_instances_querycapabilities

> [**FlowsQueryCriteriaResponse**](FlowsQueryCriteriaResponse) get_flows_instances_querycapabilities(expand=expand)


Retrieve a list of capabilities that the org can use to query for execution data

Returns the queryable parameters that can be used to build a query for execution data.

Wraps GET /api/v2/flows/instances/querycapabilities 

Requires ANY permissions: 

* architect:flowInstance:search

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
expand = 'expand_example' # str | Expand various query types. (optional)

try:
    # Retrieve a list of capabilities that the org can use to query for execution data
    api_response = api_instance.get_flows_instances_querycapabilities(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instances_querycapabilities: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | **str**| Expand various query types. | [optional] <br />**Values**: flow, action |

### Return type

[**FlowsQueryCriteriaResponse**](FlowsQueryCriteriaResponse)


## get_flows_instances_settings_executiondata

> [**ExecutionDataFlowSettingsResponse**](ExecutionDataFlowSettingsResponse) get_flows_instances_settings_executiondata()


Get the execution history enabled setting.

Get the execution history enabled setting.

Wraps GET /api/v2/flows/instances/settings/executiondata 

Requires ANY permissions: 

* architect:flowinstanceexecutiondata:view

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
    # Get the execution history enabled setting.
    api_response = api_instance.get_flows_instances_settings_executiondata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instances_settings_executiondata: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ExecutionDataFlowSettingsResponse**](ExecutionDataFlowSettingsResponse)


## get_flows_instances_settings_loglevels

> [**FlowSettingsResponseEntityListing**](FlowSettingsResponseEntityListing) get_flows_instances_settings_loglevels(expand=expand, page_number=page_number, page_size=page_size)


Retrieve a list of LogLevels for the organization.

Returns a paged set of LogLevels per flow id

Wraps GET /api/v2/flows/instances/settings/loglevels 

Requires ALL permissions: 

* architect:flowLogLevel:view
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
expand = ['expand_example'] # list[str] | Expand instructions for the result (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Number of entities to return. Maximum of 200. (optional) (default to 25)

try:
    # Retrieve a list of LogLevels for the organization.
    api_response = api_instance.get_flows_instances_settings_loglevels(expand=expand, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instances_settings_loglevels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str)| Expand instructions for the result | [optional] <br />**Values**: name, type, logLevelCharacteristics.characteristics |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Number of entities to return. Maximum of 200. | [optional] [default to 25] |

### Return type

[**FlowSettingsResponseEntityListing**](FlowSettingsResponseEntityListing)


## get_flows_instances_settings_loglevels_characteristics

> [**FlowLogLevelCharacteristicsDefinitions**](FlowLogLevelCharacteristicsDefinitions) get_flows_instances_settings_loglevels_characteristics()


Gets the available flow log level characteristics for this organization.

Log levels can be customized and this returns the set of available characteristics that can be enabled/disabled.

Wraps GET /api/v2/flows/instances/settings/loglevels/characteristics 

Requires ANY permissions: 

* architect:flowLogLevel:view
* architect:flowLogLevelDefault:view

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
    # Gets the available flow log level characteristics for this organization.
    api_response = api_instance.get_flows_instances_settings_loglevels_characteristics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instances_settings_loglevels_characteristics: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**FlowLogLevelCharacteristicsDefinitions**](FlowLogLevelCharacteristicsDefinitions)


## get_flows_instances_settings_loglevels_default

> [**FlowSettingsResponse**](FlowSettingsResponse) get_flows_instances_settings_loglevels_default(expand=expand)


Returns the flow default log level.

Returns the flow default log level which will be used if no specific flow id log level is found.

Wraps GET /api/v2/flows/instances/settings/loglevels/default 

Requires ANY permissions: 

* architect:flowLogLevelDefault:view

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
expand = ['expand_example'] # list[str] | Expand instructions for the result (optional)

try:
    # Returns the flow default log level.
    api_response = api_instance.get_flows_instances_settings_loglevels_default(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_instances_settings_loglevels_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str)| Expand instructions for the result | [optional] <br />**Values**: logLevelCharacteristics.characteristics |

### Return type

[**FlowSettingsResponse**](FlowSettingsResponse)


## get_flows_job

> [**ArchitectJobStateResponse**](ArchitectJobStateResponse) get_flows_job(job_id, expand=expand)


Fetch Architect Job Status

Wraps GET /api/v2/flows/jobs/{jobId} 

Requires ALL permissions: 

* architect:job:view

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
job_id = 'job_id_example' # str | Job ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Fetch Architect Job Status
    api_response = api_instance.get_flows_job(job_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Job ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: messages |

### Return type

[**ArchitectJobStateResponse**](ArchitectJobStateResponse)


## get_flows_milestone

> [**FlowMilestone**](FlowMilestone) get_flows_milestone(milestone_id)


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

### Return type

[**FlowMilestone**](FlowMilestone)


## get_flows_milestones

> [**FlowMilestoneListing**](FlowMilestoneListing) get_flows_milestones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, division_id=division_id)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)

try:
    # Get a pageable list of flow milestones, filtered by query parameters
    api_response = api_instance.get_flows_milestones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_milestones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |

### Return type

[**FlowMilestoneListing**](FlowMilestoneListing)


## get_flows_milestones_divisionviews

> [**FlowMilestoneDivisionViewEntityListing**](FlowMilestoneDivisionViewEntityListing) get_flows_milestones_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


Get a pageable list of basic flow milestone information objects filterable by query parameters.

This returns flow milestones consisting of name and division. If one or more IDs are specified, the search will fetch flow milestones that match the given ID(s) and not use any additional supplied query parameters in the search.

Wraps GET /api/v2/flows/milestones/divisionviews 

Requires ALL permissions: 

* architect:flowMilestone:search

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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)

try:
    # Get a pageable list of basic flow milestone information objects filterable by query parameters.
    api_response = api_instance.get_flows_milestones_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_milestones_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |

### Return type

[**FlowMilestoneDivisionViewEntityListing**](FlowMilestoneDivisionViewEntityListing)


## get_flows_outcome

> [**FlowOutcome**](FlowOutcome) get_flows_outcome(flow_outcome_id)


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

### Return type

[**FlowOutcome**](FlowOutcome)


## get_flows_outcomes

> [**FlowOutcomeListing**](FlowOutcomeListing) get_flows_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, division_id=division_id)


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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
description = 'description_example' # str | Description (optional)
name_or_description = 'name_or_description_example' # str | Name or description (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)

try:
    # Get a pageable list of flow outcomes, filtered by query parameters
    api_response = api_instance.get_flows_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, description=description, name_or_description=name_or_description, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_outcomes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **description** | **str**| Description | [optional]  |
| **name_or_description** | **str**| Name or description | [optional]  |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |

### Return type

[**FlowOutcomeListing**](FlowOutcomeListing)


## get_flows_outcomes_divisionviews

> [**FlowOutcomeDivisionViewEntityListing**](FlowOutcomeDivisionViewEntityListing) get_flows_outcomes_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


Get a pageable list of basic flow outcome information objects filterable by query parameters.

This returns flow outcomes consisting of name and division. If one or more IDs are specified, the search will fetch flow outcomes that match the given ID(s) and not use any additional supplied query parameters in the search.

Wraps GET /api/v2/flows/outcomes/divisionviews 

Requires ALL permissions: 

* architect:flowOutcome:search

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
sort_by = ''id'' # str | Sort by (optional) (default to 'id')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
id = ['id_example'] # list[str] | ID (optional)
name = 'name_example' # str | Name (optional)
division_id = ['division_id_example'] # list[str] | division ID(s) (optional)

try:
    # Get a pageable list of basic flow outcome information objects filterable by query parameters.
    api_response = api_instance.get_flows_outcomes_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->get_flows_outcomes_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;id&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
| **id** | [**list[str]**](str)| ID | [optional]  |
| **name** | **str**| Name | [optional]  |
| **division_id** | [**list[str]**](str)| division ID(s) | [optional]  |

### Return type

[**FlowOutcomeDivisionViewEntityListing**](FlowOutcomeDivisionViewEntityListing)


## patch_architect_grammar

> [**Grammar**](Grammar) patch_architect_grammar(grammar_id, body=body)


Updates a grammar

Wraps PATCH /api/v2/architect/grammars/{grammarId} 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | grammar ID
body = PureCloudPlatformClientV2.Grammar() # Grammar |  (optional)

try:
    # Updates a grammar
    api_response = api_instance.patch_architect_grammar(grammar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->patch_architect_grammar: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| grammar ID |  |
| **body** | [**Grammar**](Grammar)|  | [optional]  |

### Return type

[**Grammar**](Grammar)


## patch_architect_grammar_language

> [**GrammarLanguage**](GrammarLanguage) patch_architect_grammar_language(grammar_id, language_code, body=body)


Updates a grammar language

Wraps PATCH /api/v2/architect/grammars/{grammarId}/languages/{languageCode} 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.GrammarLanguageUpdate() # GrammarLanguageUpdate |  (optional)

try:
    # Updates a grammar language
    api_response = api_instance.patch_architect_grammar_language(grammar_id, language_code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->patch_architect_grammar_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |
| **body** | [**GrammarLanguageUpdate**](GrammarLanguageUpdate)|  | [optional]  |

### Return type

[**GrammarLanguage**](GrammarLanguage)


## patch_flows_instances_settings_executiondata

> [**ExecutionDataFlowSettingsResponse**](ExecutionDataFlowSettingsResponse) patch_flows_instances_settings_executiondata(body)


Edit the execution history enabled setting.

Edit the execution history enabled setting.

Wraps PATCH /api/v2/flows/instances/settings/executiondata 

Requires ANY permissions: 

* architect:flowinstanceexecutiondata:edit

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
body = PureCloudPlatformClientV2.ExecutionDataSettingsRequest() # ExecutionDataSettingsRequest | New Execution Data Setting

try:
    # Edit the execution history enabled setting.
    api_response = api_instance.patch_flows_instances_settings_executiondata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->patch_flows_instances_settings_executiondata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExecutionDataSettingsRequest**](ExecutionDataSettingsRequest)| New Execution Data Setting |  |

### Return type

[**ExecutionDataFlowSettingsResponse**](ExecutionDataFlowSettingsResponse)


## post_architect_dependencytracking_build

>  post_architect_dependencytracking_build()


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

This endpoint does not need any parameters.

### Return type

void (empty response body)


## post_architect_emergencygroups

> [**EmergencyGroup**](EmergencyGroup) post_architect_emergencygroups(body)


Creates a new emergency group

Wraps POST /api/v2/architect/emergencygroups 

Requires ALL permissions: 

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
| **body** | [**EmergencyGroup**](EmergencyGroup)|  |  |

### Return type

[**EmergencyGroup**](EmergencyGroup)


## post_architect_grammar_language_files_dtmf

> [**UploadUrlResponse**](UploadUrlResponse) post_architect_grammar_language_files_dtmf(grammar_id, language_code, body)


Creates a presigned URL for uploading a grammar DTMF mode file

Wraps POST /api/v2/architect/grammars/{grammarId}/languages/{languageCode}/files/dtmf 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.GrammarFileUploadRequest() # GrammarFileUploadRequest | query

try:
    # Creates a presigned URL for uploading a grammar DTMF mode file
    api_response = api_instance.post_architect_grammar_language_files_dtmf(grammar_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_grammar_language_files_dtmf: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |
| **body** | [**GrammarFileUploadRequest**](GrammarFileUploadRequest)| query |  |

### Return type

[**UploadUrlResponse**](UploadUrlResponse)


## post_architect_grammar_language_files_voice

> [**UploadUrlResponse**](UploadUrlResponse) post_architect_grammar_language_files_voice(grammar_id, language_code, body)


Creates a presigned URL for uploading a grammar voice mode file

Wraps POST /api/v2/architect/grammars/{grammarId}/languages/{languageCode}/files/voice 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
language_code = 'language_code_example' # str | Language
body = PureCloudPlatformClientV2.GrammarFileUploadRequest() # GrammarFileUploadRequest | query

try:
    # Creates a presigned URL for uploading a grammar voice mode file
    api_response = api_instance.post_architect_grammar_language_files_voice(grammar_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_grammar_language_files_voice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **language_code** | **str**| Language |  |
| **body** | [**GrammarFileUploadRequest**](GrammarFileUploadRequest)| query |  |

### Return type

[**UploadUrlResponse**](UploadUrlResponse)


## post_architect_grammar_languages

> [**GrammarLanguage**](GrammarLanguage) post_architect_grammar_languages(grammar_id, body)


Create a new language for a given grammar

Wraps POST /api/v2/architect/grammars/{grammarId}/languages 

Requires ALL permissions: 

* architect:grammar:edit

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
grammar_id = 'grammar_id_example' # str | Grammar ID
body = PureCloudPlatformClientV2.GrammarLanguage() # GrammarLanguage | 

try:
    # Create a new language for a given grammar
    api_response = api_instance.post_architect_grammar_languages(grammar_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_grammar_languages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **grammar_id** | **str**| Grammar ID |  |
| **body** | [**GrammarLanguage**](GrammarLanguage)|  |  |

### Return type

[**GrammarLanguage**](GrammarLanguage)


## post_architect_grammars

> [**Grammar**](Grammar) post_architect_grammars(body)


Create a new grammar

Wraps POST /api/v2/architect/grammars 

Requires ALL permissions: 

* architect:grammar:add

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
body = PureCloudPlatformClientV2.Grammar() # Grammar | 

try:
    # Create a new grammar
    api_response = api_instance.post_architect_grammars(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_grammars: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Grammar**](Grammar)|  |  |

### Return type

[**Grammar**](Grammar)


## post_architect_ivrs

> [**IVR**](IVR) post_architect_ivrs(body)


Create IVR config.

Wraps POST /api/v2/architect/ivrs 

Requires ALL permissions: 

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
| **body** | [**IVR**](IVR)|  |  |

### Return type

[**IVR**](IVR)


## post_architect_prompt_history

> [**Operation**](Operation) post_architect_prompt_history(prompt_id)


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

### Return type

[**Operation**](Operation)


## post_architect_prompt_resource_uploads

> [**PromptAssetUpload**](PromptAssetUpload) post_architect_prompt_resource_uploads(prompt_id, language_code)


Creates a presigned URL for uploading a user prompt file

Wraps POST /api/v2/architect/prompts/{promptId}/resources/{languageCode}/uploads 

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
    # Creates a presigned URL for uploading a user prompt file
    api_response = api_instance.post_architect_prompt_resource_uploads(prompt_id, language_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_prompt_resource_uploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |

### Return type

[**PromptAssetUpload**](PromptAssetUpload)


## post_architect_prompt_resources

> [**PromptAsset**](PromptAsset) post_architect_prompt_resources(prompt_id, body)


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
| **body** | [**PromptAssetCreate**](PromptAssetCreate)|  |  |

### Return type

[**PromptAsset**](PromptAsset)


## post_architect_prompts

> [**Prompt**](Prompt) post_architect_prompts(body)


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
| **body** | [**Prompt**](Prompt)|  |  |

### Return type

[**Prompt**](Prompt)


## post_architect_schedulegroups

> [**ScheduleGroup**](ScheduleGroup) post_architect_schedulegroups(body)


Creates a new schedule group

Wraps POST /api/v2/architect/schedulegroups 

Requires ALL permissions: 

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
| **body** | [**ScheduleGroup**](ScheduleGroup)|  |  |

### Return type

[**ScheduleGroup**](ScheduleGroup)


## post_architect_schedules

> [**Schedule**](Schedule) post_architect_schedules(body)


Create a new schedule.

Wraps POST /api/v2/architect/schedules 

Requires ALL permissions: 

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
| **body** | [**Schedule**](Schedule)|  |  |

### Return type

[**Schedule**](Schedule)


## post_architect_systemprompt_history

> [**Operation**](Operation) post_architect_systemprompt_history(prompt_id)


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

### Return type

[**Operation**](Operation)


## post_architect_systemprompt_resource_uploads

> [**PromptAssetUpload**](PromptAssetUpload) post_architect_systemprompt_resource_uploads(prompt_id, language_code)


Creates a presigned URL for uploading a system prompt file

Wraps POST /api/v2/architect/systemprompts/{promptId}/resources/{languageCode}/uploads 

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
    # Creates a presigned URL for uploading a system prompt file
    api_response = api_instance.post_architect_systemprompt_resource_uploads(prompt_id, language_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_architect_systemprompt_resource_uploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt_id** | **str**| Prompt ID |  |
| **language_code** | **str**| Language |  |

### Return type

[**PromptAssetUpload**](PromptAssetUpload)


## post_architect_systemprompt_resources

> [**SystemPromptAsset**](SystemPromptAsset) post_architect_systemprompt_resources(prompt_id, body)


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
| **body** | [**SystemPromptAsset**](SystemPromptAsset)|  |  |

### Return type

[**SystemPromptAsset**](SystemPromptAsset)


## post_flow_history

> [**Operation**](Operation) post_flow_history(flow_id)


Generate flow history

Asynchronous.  Notification topic: v2.flows.{flowId}

Wraps POST /api/v2/flows/{flowId}/history 

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

try:
    # Generate flow history
    api_response = api_instance.post_flow_history(flow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flow_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| Flow ID |  |

### Return type

[**Operation**](Operation)


## post_flow_instances_settings_loglevels

> [**FlowSettingsResponse**](FlowSettingsResponse) post_flow_instances_settings_loglevels(flow_id, body, expand=expand)


Set the logLevel for a particular flow id

Assigns a new loglevel to a flow id

Wraps POST /api/v2/flows/{flowId}/instances/settings/loglevels 

Requires ALL permissions: 

* architect:flowLogLevel:add

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
flow_id = 'flow_id_example' # str | The flow id to set the loglevel for
body = PureCloudPlatformClientV2.FlowLogLevelRequest() # FlowLogLevelRequest | New LogLevel settings
expand = ['expand_example'] # list[str] | Expand instructions for the result (optional)

try:
    # Set the logLevel for a particular flow id
    api_response = api_instance.post_flow_instances_settings_loglevels(flow_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flow_instances_settings_loglevels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| The flow id to set the loglevel for |  |
| **body** | [**FlowLogLevelRequest**](FlowLogLevelRequest)| New LogLevel settings |  |
| **expand** | [**list[str]**](str)| Expand instructions for the result | [optional] <br />**Values**: name, type, logLevelCharacteristics.characteristics |

### Return type

[**FlowSettingsResponse**](FlowSettingsResponse)


## post_flow_versions

> [**FlowVersion**](FlowVersion) post_flow_versions(flow_id, body)


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
| **body** | [**object**](object)|  |  |

### Return type

[**FlowVersion**](FlowVersion)


## post_flows

> [**Flow**](Flow) post_flows(body, language=language)


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
language = 'language_example' # str | Language (optional)

try:
    # Create flow
    api_response = api_instance.post_flows(body, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Flow**](Flow)|  |  |
| **language** | **str**| Language | [optional]  |

### Return type

[**Flow**](Flow)


## post_flows_actions_checkin

> [**Operation**](Operation) post_flows_actions_checkin(flow)


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

### Return type

[**Operation**](Operation)


## post_flows_actions_checkout

> [**Flow**](Flow) post_flows_actions_checkout(flow)


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

### Return type

[**Flow**](Flow)


## post_flows_actions_deactivate

> [**Flow**](Flow) post_flows_actions_deactivate(flow)


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

### Return type

[**Flow**](Flow)


## post_flows_actions_publish

> [**Operation**](Operation) post_flows_actions_publish(flow, version=version)


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

### Return type

[**Operation**](Operation)


## post_flows_actions_revert

> [**Flow**](Flow) post_flows_actions_revert(flow)


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

### Return type

[**Flow**](Flow)


## post_flows_actions_unlock

> [**Flow**](Flow) post_flows_actions_unlock(flow)


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

### Return type

[**Flow**](Flow)


## post_flows_datatable_export_jobs

> [**DataTableExportJob**](DataTableExportJob) post_flows_datatable_export_jobs(datatable_id)


Begin an export process for exporting all rows from a datatable

Create an export job for exporting rows. The caller can then poll for status of the export using the token returned in the response

Wraps POST /api/v2/flows/datatables/{datatableId}/export/jobs 

Requires ANY permissions: 

* architect:datatable:view
* architect:datatableRow:view

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

### Return type

[**DataTableExportJob**](DataTableExportJob)


## post_flows_datatable_import_jobs

> [**DataTableImportJob**](DataTableImportJob) post_flows_datatable_import_jobs(datatable_id, body)


Begin an import process for importing rows into a datatable

Create an import job for importing rows. The caller can then poll for status of the import using the token returned in the response

Wraps POST /api/v2/flows/datatables/{datatableId}/import/jobs 

Requires ANY permissions: 

* architect:datatable:edit
* architect:datatableRow:add

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
| **body** | [**DataTableImportJob**](DataTableImportJob)| import job information |  |

### Return type

[**DataTableImportJob**](DataTableImportJob)


## post_flows_datatable_rows

> dict(str, object)** post_flows_datatable_rows(datatable_id, data_table_row)


Create a new row entry for the datatable.

Will add the passed in row entry to the datatable with the given datatableId after verifying it against the schema.  When building the request body within API Explorer, Pro mode should be used. The DataTableRow should be a json-ized' stream of key -> value pairs {      \"Field1\": \"XYZZY\",      \"Field2\": false,      \"KEY\": \"27272\"  }

Wraps POST /api/v2/flows/datatables/{datatableId}/rows 

Requires ANY permissions: 

* architect:datatable:add
* architect:datatableRow:add

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
| **data_table_row** | [**object**](object)|  |  |

### Return type

**dict(str, object)**


## post_flows_datatables

> [**DataTable**](DataTable) post_flows_datatables(body)


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
| **body** | [**DataTable**](DataTable)| datatable json-schema |  |

### Return type

[**DataTable**](DataTable)


## post_flows_executions

> [**FlowExecutionLaunchResponse**](FlowExecutionLaunchResponse) post_flows_executions(flow_launch_request)


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
| **flow_launch_request** | [**FlowExecutionLaunchRequest**](FlowExecutionLaunchRequest)|  |  |

### Return type

[**FlowExecutionLaunchResponse**](FlowExecutionLaunchResponse)


## post_flows_export_jobs

> [**RegisterArchitectExportJobResponse**](RegisterArchitectExportJobResponse) post_flows_export_jobs(body)


Register Architect Export Job

Wraps POST /api/v2/flows/export/jobs 

Requires ALL permissions: 

* architect:jobExport:create

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
body = PureCloudPlatformClientV2.RegisterArchitectExportJob() # RegisterArchitectExportJob | 

try:
    # Register Architect Export Job
    api_response = api_instance.post_flows_export_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_export_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RegisterArchitectExportJob**](RegisterArchitectExportJob)|  |  |

### Return type

[**RegisterArchitectExportJobResponse**](RegisterArchitectExportJobResponse)


## post_flows_instances_jobs

> [**GetFlowExecutionDataJobResult**](GetFlowExecutionDataJobResult) post_flows_instances_jobs(body, expand=expand)


Start a process (job) that will prepare a list of execution data IDs for download.

Returns a JobResult object that contains an ID that can be used to check status and/or download links when the process (job) is complete.

Wraps POST /api/v2/flows/instances/jobs 

Requires ANY permissions: 

* architect:flowInstance:view

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
body = PureCloudPlatformClientV2.ExecutionDataRequest() # ExecutionDataRequest | Requested Flow Ids
expand = 'expand_example' # str | Expand various query types. (optional)

try:
    # Start a process (job) that will prepare a list of execution data IDs for download.
    api_response = api_instance.post_flows_instances_jobs(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_instances_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExecutionDataRequest**](ExecutionDataRequest)| Requested Flow Ids |  |
| **expand** | **str**| Expand various query types. | [optional] <br />**Values**: bots, dataActions |

### Return type

[**GetFlowExecutionDataJobResult**](GetFlowExecutionDataJobResult)


## post_flows_instances_query

> [**FlowResultEntityListing**](FlowResultEntityListing) post_flows_instances_query(body, index_only=index_only, page_size=page_size)


Query the database of existing flow histories to look for particular flow criteria

Returns a list of matching flow histories up to 200 max.

Wraps POST /api/v2/flows/instances/query 

Requires ANY permissions: 

* architect:flowInstance:search

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
body = PureCloudPlatformClientV2.CriteriaQuery() # CriteriaQuery | query
index_only = True # bool | indexes only (optional)
page_size = 50 # int | number of results to return (optional) (default to 50)

try:
    # Query the database of existing flow histories to look for particular flow criteria
    api_response = api_instance.post_flows_instances_query(body, index_only=index_only, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_instances_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CriteriaQuery**](CriteriaQuery)| query |  |
| **index_only** | **bool**| indexes only | [optional]  |
| **page_size** | **int**| number of results to return | [optional] [default to 50] |

### Return type

[**FlowResultEntityListing**](FlowResultEntityListing)


## post_flows_jobs

> [**RegisterArchitectJobResponse**](RegisterArchitectJobResponse) post_flows_jobs()


Register Architect Job. Returns a URL where a file, such as an Architect flow YAML file, can be PUT which will then initiate the job.

Wraps POST /api/v2/flows/jobs 

Requires ALL permissions: 

* architect:job:create

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
    # Register Architect Job. Returns a URL where a file, such as an Architect flow YAML file, can be PUT which will then initiate the job.
    api_response = api_instance.post_flows_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->post_flows_jobs: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**RegisterArchitectJobResponse**](RegisterArchitectJobResponse)


## post_flows_milestones

> [**FlowMilestone**](FlowMilestone) post_flows_milestones(body=body)


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
| **body** | [**FlowMilestone**](FlowMilestone)|  | [optional]  |

### Return type

[**FlowMilestone**](FlowMilestone)


## post_flows_outcomes

> [**FlowOutcome**](FlowOutcome) post_flows_outcomes(body=body)


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
| **body** | [**FlowOutcome**](FlowOutcome)|  | [optional]  |

### Return type

[**FlowOutcome**](FlowOutcome)


## put_architect_emergencygroup

> [**EmergencyGroup**](EmergencyGroup) put_architect_emergencygroup(emergency_group_id, body)


Updates a emergency group by ID

Wraps PUT /api/v2/architect/emergencygroups/{emergencyGroupId} 

Requires ALL permissions: 

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
| **body** | [**EmergencyGroup**](EmergencyGroup)|  |  |

### Return type

[**EmergencyGroup**](EmergencyGroup)


## put_architect_ivr

> [**IVR**](IVR) put_architect_ivr(ivr_id, body)


Update an IVR Config.

Wraps PUT /api/v2/architect/ivrs/{ivrId} 

Requires ALL permissions: 

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
| **body** | [**IVR**](IVR)|  |  |

### Return type

[**IVR**](IVR)


## put_architect_ivr_identityresolution

> [**IdentityResolutionConfig**](IdentityResolutionConfig) put_architect_ivr_identityresolution(ivr_id, body)


Update an IVR IdentityResolutionConfig.

put_architect_ivr_identityresolution is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/architect/ivrs/{ivrId}/identityresolution 

Requires ALL permissions: 

* routing:callRoute:edit
* routing:identityResolution:edit

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
body = PureCloudPlatformClientV2.IdentityResolutionConfig() # IdentityResolutionConfig | 

try:
    # Update an IVR IdentityResolutionConfig.
    api_response = api_instance.put_architect_ivr_identityresolution(ivr_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_architect_ivr_identityresolution: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ivr_id** | **str**| IVR id |  |
| **body** | [**IdentityResolutionConfig**](IdentityResolutionConfig)|  |  |

### Return type

[**IdentityResolutionConfig**](IdentityResolutionConfig)


## put_architect_prompt

> [**Prompt**](Prompt) put_architect_prompt(prompt_id, body)


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
| **body** | [**Prompt**](Prompt)|  |  |

### Return type

[**Prompt**](Prompt)


## put_architect_prompt_resource

> [**PromptAsset**](PromptAsset) put_architect_prompt_resource(prompt_id, language_code, body)


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
| **body** | [**PromptAsset**](PromptAsset)|  |  |

### Return type

[**PromptAsset**](PromptAsset)


## put_architect_schedule

> [**Schedule**](Schedule) put_architect_schedule(schedule_id, body)


Update schedule by ID

Wraps PUT /api/v2/architect/schedules/{scheduleId} 

Requires ALL permissions: 

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
| **body** | [**Schedule**](Schedule)|  |  |

### Return type

[**Schedule**](Schedule)


## put_architect_schedulegroup

> [**ScheduleGroup**](ScheduleGroup) put_architect_schedulegroup(schedule_group_id, body)


Updates a schedule group by ID

Wraps PUT /api/v2/architect/schedulegroups/{scheduleGroupId} 

Requires ALL permissions: 

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
| **body** | [**ScheduleGroup**](ScheduleGroup)|  |  |

### Return type

[**ScheduleGroup**](ScheduleGroup)


## put_architect_systemprompt_resource

> [**SystemPromptAsset**](SystemPromptAsset) put_architect_systemprompt_resource(prompt_id, language_code, body)


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
| **body** | [**SystemPromptAsset**](SystemPromptAsset)|  |  |

### Return type

[**SystemPromptAsset**](SystemPromptAsset)


## put_flow

> [**Flow**](Flow) put_flow(flow_id, body)


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
| **body** | [**Flow**](Flow)|  |  |

### Return type

[**Flow**](Flow)


## put_flow_instances_settings_loglevels

> [**FlowSettingsResponse**](FlowSettingsResponse) put_flow_instances_settings_loglevels(flow_id, body, expand=expand)


Edit the logLevel for a particular flow id

Updates the loglevel for a flow id

Wraps PUT /api/v2/flows/{flowId}/instances/settings/loglevels 

Requires ALL permissions: 

* architect:flowLogLevel:edit

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
flow_id = 'flow_id_example' # str | The flow id to edit the loglevel for
body = PureCloudPlatformClientV2.FlowLogLevelRequest() # FlowLogLevelRequest | New LogLevel settings
expand = ['expand_example'] # list[str] | Expand instructions for the result (optional)

try:
    # Edit the logLevel for a particular flow id
    api_response = api_instance.put_flow_instances_settings_loglevels(flow_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flow_instances_settings_loglevels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **flow_id** | **str**| The flow id to edit the loglevel for |  |
| **body** | [**FlowLogLevelRequest**](FlowLogLevelRequest)| New LogLevel settings |  |
| **expand** | [**list[str]**](str)| Expand instructions for the result | [optional] <br />**Values**: name, type, logLevelCharacteristics.characteristics |

### Return type

[**FlowSettingsResponse**](FlowSettingsResponse)


## put_flows_datatable

> [**DataTable**](DataTable) put_flows_datatable(datatable_id, body, expand=expand)


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
body = PureCloudPlatformClientV2.DataTable() # DataTable | datatable json-schema
expand = 'expand_example' # str | Expand instructions for the result (optional)

try:
    # Updates a specific datatable by id
    api_response = api_instance.put_flows_datatable(datatable_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flows_datatable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **datatable_id** | **str**| id of datatable |  |
| **body** | [**DataTable**](DataTable)| datatable json-schema |  |
| **expand** | **str**| Expand instructions for the result | [optional] <br />**Values**: schema |

### Return type

[**DataTable**](DataTable)


## put_flows_datatable_row

> dict(str, object)** put_flows_datatable_row(datatable_id, row_id, body=body)


Update a row entry

Updates a row with the given rowId (the value of the key field) to the new values.  When building the request body within API Explorer, Pro mode should be used. The DataTableRow should be a json-ized' stream of key -> value pairs {     \"Field1\": \"XYZZY\",     \"Field2\": false,     \"KEY\": \"27272\" }

Wraps PUT /api/v2/flows/datatables/{datatableId}/rows/{rowId} 

Requires ANY permissions: 

* architect:datatable:edit
* architect:datatableRow:edit

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
| **body** | [**object**](object)| datatable row | [optional]  |

### Return type

**dict(str, object)**


## put_flows_instances_settings_loglevels_default

> [**FlowSettingsResponse**](FlowSettingsResponse) put_flows_instances_settings_loglevels_default(body, expand=expand)


Edit the flow default log level.

Edit the flow default log level.

Wraps PUT /api/v2/flows/instances/settings/loglevels/default 

Requires ANY permissions: 

* architect:flowLogLevelDefault:edit

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
body = PureCloudPlatformClientV2.FlowLogLevelRequest() # FlowLogLevelRequest | New LogLevel settings
expand = ['expand_example'] # list[str] | Expand instructions for the result (optional)

try:
    # Edit the flow default log level.
    api_response = api_instance.put_flows_instances_settings_loglevels_default(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchitectApi->put_flows_instances_settings_loglevels_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowLogLevelRequest**](FlowLogLevelRequest)| New LogLevel settings |  |
| **expand** | [**list[str]**](str)| Expand instructions for the result | [optional] <br />**Values**: logLevelCharacteristics.characteristics |

### Return type

[**FlowSettingsResponse**](FlowSettingsResponse)


## put_flows_milestone

> [**FlowMilestone**](FlowMilestone) put_flows_milestone(milestone_id, body=body)


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
| **body** | [**FlowMilestone**](FlowMilestone)|  | [optional]  |

### Return type

[**FlowMilestone**](FlowMilestone)


## put_flows_outcome

> [**Operation**](Operation) put_flows_outcome(flow_outcome_id, body=body)


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
| **body** | [**FlowOutcome**](FlowOutcome)|  | [optional]  |

### Return type

[**Operation**](Operation)


_PureCloudPlatformClientV2 227.0.0_
