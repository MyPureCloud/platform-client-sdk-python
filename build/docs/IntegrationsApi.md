# IntegrationsApi

## PureCloudPlatformClientV2.IntegrationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_integration**](#delete_integration) | Delete integration.|
|[**delete_integrations_action**](#delete_integrations_action) | Delete an Action|
|[**delete_integrations_action_draft**](#delete_integrations_action_draft) | Delete a Draft|
|[**delete_integrations_credential**](#delete_integrations_credential) | Delete a set of credentials|
|[**get_integration**](#get_integration) | Get integration.|
|[**get_integration_config_current**](#get_integration_config_current) | Get integration configuration.|
|[**get_integrations**](#get_integrations) | List integrations|
|[**get_integrations_action**](#get_integrations_action) | Retrieves a single Action matching id.|
|[**get_integrations_action_draft**](#get_integrations_action_draft) | Retrieve a Draft|
|[**get_integrations_action_draft_function**](#get_integrations_action_draft_function) | Get draft function settings for Action|
|[**get_integrations_action_draft_schema**](#get_integrations_action_draft_schema) | Retrieve schema for a Draft based on filename.|
|[**get_integrations_action_draft_template**](#get_integrations_action_draft_template) | Retrieve templates for a Draft based on filename.|
|[**get_integrations_action_draft_validation**](#get_integrations_action_draft_validation) | Validate current Draft configuration.|
|[**get_integrations_action_function**](#get_integrations_action_function) | Get published function settings for Action|
|[**get_integrations_action_schema**](#get_integrations_action_schema) | Retrieve schema for an action based on filename.|
|[**get_integrations_action_template**](#get_integrations_action_template) | Retrieve text of templates for an action based on filename.|
|[**get_integrations_actions**](#get_integrations_actions) | Retrieves all actions associated with filters passed in via query param.|
|[**get_integrations_actions_categories**](#get_integrations_actions_categories) | Retrieves all categories of available Actions|
|[**get_integrations_actions_certificates**](#get_integrations_actions_certificates) | Retrieves the available mTLS client certificates in use. This endpoint will return inconsistent results while a certificate rotation is in progress.|
|[**get_integrations_actions_certificates_truststore**](#get_integrations_actions_certificates_truststore) | Retrieves basic info about trusted root CA certificates|
|[**get_integrations_actions_drafts**](#get_integrations_actions_drafts) | Retrieves all action drafts associated with the filters passed in via query param.|
|[**get_integrations_actions_functions_runtimes**](#get_integrations_actions_functions_runtimes) | Get action function settings for Action|
|[**get_integrations_botconnector_bot**](#get_integrations_botconnector_bot) | Get a specific Bot details|
|[**get_integrations_botconnector_bots**](#get_integrations_botconnector_bots) | Get the list of bots for this integration.|
|[**get_integrations_botconnector_bots_summaries**](#get_integrations_botconnector_bots_summaries) | Get the summary list of bots for this integration.|
|[**get_integrations_botconnector_integration_id_bot**](#get_integrations_botconnector_integration_id_bot) | Get a specific botConnector bot, plus versions, for this integration|
|[**get_integrations_botconnector_integration_id_bot_versions**](#get_integrations_botconnector_integration_id_bot_versions) | Get a list of bot versions for a bot|
|[**get_integrations_botconnector_integration_id_bots**](#get_integrations_botconnector_integration_id_bots) | Get a list of botConnector bots for this integration|
|[**get_integrations_botconnector_integration_id_bots_summaries**](#get_integrations_botconnector_integration_id_bots_summaries) | Get a summary list of botConnector bots for this integration|
|[**get_integrations_clientapps**](#get_integrations_clientapps) | List permitted client app integrations for the logged in user|
|[**get_integrations_clientapps_unifiedcommunications**](#get_integrations_clientapps_unifiedcommunications) | UC integration client application configuration.|
|[**get_integrations_credential**](#get_integrations_credential) | Get a single credential with sensitive fields redacted|
|[**get_integrations_credentials**](#get_integrations_credentials) | List multiple sets of credentials|
|[**get_integrations_credentials_listing**](#get_integrations_credentials_listing) | List multiple sets of credentials using cursor-based paging|
|[**get_integrations_credentials_types**](#get_integrations_credentials_types) | List all credential types|
|[**get_integrations_speech_audioconnector**](#get_integrations_speech_audioconnector) | Get a list of Audio Connector integrations|
|[**get_integrations_speech_audioconnector_integration_id**](#get_integrations_speech_audioconnector_integration_id) | Get an Audio Connector integration|
|[**get_integrations_speech_dialogflow_agent**](#get_integrations_speech_dialogflow_agent) | Get details about a Dialogflow agent|
|[**get_integrations_speech_dialogflow_agents**](#get_integrations_speech_dialogflow_agents) | Get a list of Dialogflow agents in the customers&#39; Google accounts|
|[**get_integrations_speech_dialogflowcx_agent**](#get_integrations_speech_dialogflowcx_agent) | Get details about a Dialogflow CX agent|
|[**get_integrations_speech_dialogflowcx_agents**](#get_integrations_speech_dialogflowcx_agents) | Get a list of Dialogflow CX agents in the customers&#39; Google accounts|
|[**get_integrations_speech_lex_bot_alias**](#get_integrations_speech_lex_bot_alias) | Get details about a Lex bot alias|
|[**get_integrations_speech_lex_bot_bot_id_aliases**](#get_integrations_speech_lex_bot_bot_id_aliases) | Get a list of aliases for a bot in the customer&#39;s AWS accounts|
|[**get_integrations_speech_lex_bots**](#get_integrations_speech_lex_bots) | Get a list of Lex bots in the customers&#39; AWS accounts|
|[**get_integrations_speech_lexv2_bot_alias**](#get_integrations_speech_lexv2_bot_alias) | Get details about a Lex V2 bot alias|
|[**get_integrations_speech_lexv2_bot_bot_id_aliases**](#get_integrations_speech_lexv2_bot_bot_id_aliases) | Get a list of aliases for a Lex V2 bot|
|[**get_integrations_speech_lexv2_bots**](#get_integrations_speech_lexv2_bots) | Get a list of Lex V2 bots|
|[**get_integrations_speech_nuance_nuance_integration_id_bot**](#get_integrations_speech_nuance_nuance_integration_id_bot) | Get a Nuance bot in the specified Integration|
|[**get_integrations_speech_nuance_nuance_integration_id_bot_job**](#get_integrations_speech_nuance_nuance_integration_id_bot_job) | Get the status of an asynchronous Nuance bot GET job|
|[**get_integrations_speech_nuance_nuance_integration_id_bot_job_results**](#get_integrations_speech_nuance_nuance_integration_id_bot_job_results) | Get the result of an asynchronous Nuance bot GET job|
|[**get_integrations_speech_nuance_nuance_integration_id_bots**](#get_integrations_speech_nuance_nuance_integration_id_bots) | Get a list of Nuance bots available in the specified Integration|
|[**get_integrations_speech_nuance_nuance_integration_id_bots_job**](#get_integrations_speech_nuance_nuance_integration_id_bots_job) | Get the status of an asynchronous Nuance bots GET job|
|[**get_integrations_speech_nuance_nuance_integration_id_bots_job_results**](#get_integrations_speech_nuance_nuance_integration_id_bots_job_results) | Get the result of an asynchronous Nuance bots GET job|
|[**get_integrations_speech_stt_engine**](#get_integrations_speech_stt_engine) | Get details about a STT engine|
|[**get_integrations_speech_stt_engines**](#get_integrations_speech_stt_engines) | Get a list of STT engines enabled for org|
|[**get_integrations_speech_tts_engine**](#get_integrations_speech_tts_engine) | Get details about a TTS engine|
|[**get_integrations_speech_tts_engine_voice**](#get_integrations_speech_tts_engine_voice) | Get details about a specific voice for a TTS engine|
|[**get_integrations_speech_tts_engine_voices**](#get_integrations_speech_tts_engine_voices) | Get a list of voices for a TTS engine|
|[**get_integrations_speech_tts_engines**](#get_integrations_speech_tts_engines) | Get a list of TTS engines enabled for org|
|[**get_integrations_speech_tts_settings**](#get_integrations_speech_tts_settings) | Get TTS settings for an org|
|[**get_integrations_type**](#get_integrations_type) | Get integration type.|
|[**get_integrations_type_configschema**](#get_integrations_type_configschema) | Get properties config schema for an integration type.|
|[**get_integrations_types**](#get_integrations_types) | List integration types|
|[**get_integrations_unifiedcommunications_clientapp**](#get_integrations_unifiedcommunications_clientapp) | UC integration client application configuration.|
|[**get_integrations_unifiedcommunications_clientapps**](#get_integrations_unifiedcommunications_clientapps) | List UC integration client application configurations.|
|[**get_integrations_userapps**](#get_integrations_userapps) | List permitted user app integrations for the logged in user|
|[**patch_integration**](#patch_integration) | Update an integration.|
|[**patch_integrations_action**](#patch_integrations_action) | Patch an Action|
|[**patch_integrations_action_draft**](#patch_integrations_action_draft) | Update an existing Draft|
|[**post_integrations**](#post_integrations) | Create an integration.|
|[**post_integrations_action_draft**](#post_integrations_action_draft) | Create a new Draft from existing Action|
|[**post_integrations_action_draft_function_upload**](#post_integrations_action_draft_function_upload) | Create upload presigned URL for draft function package file.|
|[**post_integrations_action_draft_publish**](#post_integrations_action_draft_publish) | Publish a Draft and make it the active Action configuration|
|[**post_integrations_action_draft_test**](#post_integrations_action_draft_test) | Test the execution of a draft. Responses will show execution steps broken out with intermediate results to help in debugging.|
|[**post_integrations_action_execute**](#post_integrations_action_execute) | Execute Action and return response from 3rd party.  Responses will follow the schemas defined on the Action for success and error.|
|[**post_integrations_action_test**](#post_integrations_action_test) | Test the execution of an action. Responses will show execution steps broken out with intermediate results to help in debugging.|
|[**post_integrations_actions**](#post_integrations_actions) | Create a new Action. Not supported for &#39;Function Integration&#39; actions. Function integrations must be created as drafts to allow managing of uploading required ZIP function package before they may be used as a published action.|
|[**post_integrations_actions_drafts**](#post_integrations_actions_drafts) | Create a new Draft|
|[**post_integrations_botconnectors_incoming_messages**](#post_integrations_botconnectors_incoming_messages) | Send an incoming message to the bot.|
|[**post_integrations_botconnectors_outgoing_messages**](#post_integrations_botconnectors_outgoing_messages) | Send an outgoing message to the end user.|
|[**post_integrations_credentials**](#post_integrations_credentials) | Create a set of credentials|
|[**post_integrations_speech_nuance_nuance_integration_id_bot_jobs**](#post_integrations_speech_nuance_nuance_integration_id_bot_jobs) | Get a Nuance bot in the specified Integration asynchronously|
|[**post_integrations_speech_nuance_nuance_integration_id_bots_jobs**](#post_integrations_speech_nuance_nuance_integration_id_bots_jobs) | Get a list of Nuance bots in the specified Integration asynchronously|
|[**post_integrations_speech_nuance_nuance_integration_id_bots_launch_validate**](#post_integrations_speech_nuance_nuance_integration_id_bots_launch_validate) | Try out a single credential for a Nuance bot to know if the secret is correct|
|[**post_integrations_webhook_events**](#post_integrations_webhook_events) | Invoke Webhook|
|[**put_integration_config_current**](#put_integration_config_current) | Update integration configuration.|
|[**put_integrations_action_draft_function**](#put_integrations_action_draft_function) | Update draft function settings.|
|[**put_integrations_botconnector_integration_id_bots**](#put_integrations_botconnector_integration_id_bots) | Set a list of botConnector bots plus versions for this integration|
|[**put_integrations_credential**](#put_integrations_credential) | Update a set of credentials|
|[**put_integrations_speech_nuance_nuance_integration_id_bots_launch_settings**](#put_integrations_speech_nuance_nuance_integration_id_bots_launch_settings) | Update the Nuance bot list for the specific bots made available to Genesys Cloud in the specified Integration|
|[**put_integrations_speech_tts_settings**](#put_integrations_speech_tts_settings) | Update TTS settings for an org|
|[**put_integrations_unifiedcommunication_thirdpartypresences**](#put_integrations_unifiedcommunication_thirdpartypresences) | Bulk integration presence ingestion|



## delete_integration

> [**Integration**](Integration) delete_integration(integration_id)


Delete integration.

Wraps DELETE /api/v2/integrations/{integrationId} 

Requires ANY permissions: 

* integrations:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id

try:
    # Delete integration.
    api_response = api_instance.delete_integration(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |

### Return type

[**Integration**](Integration)


## delete_integrations_action

>  delete_integrations_action(action_id)


Delete an Action

Wraps DELETE /api/v2/integrations/actions/{actionId} 

Requires ANY permissions: 

* integrations:action:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Delete an Action
    api_instance.delete_integrations_action(action_id)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integrations_action: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |

### Return type

void (empty response body)


## delete_integrations_action_draft

>  delete_integrations_action_draft(action_id)


Delete a Draft

Wraps DELETE /api/v2/integrations/actions/{actionId}/draft 

Requires ANY permissions: 

* integrations:action:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Delete a Draft
    api_instance.delete_integrations_action_draft(action_id)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integrations_action_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |

### Return type

void (empty response body)


## delete_integrations_credential

>  delete_integrations_credential(credential_id)


Delete a set of credentials

Wraps DELETE /api/v2/integrations/credentials/{credentialId} 

Requires ANY permissions: 

* integrations:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
credential_id = 'credential_id_example' # str | Credential ID

try:
    # Delete a set of credentials
    api_instance.delete_integrations_credential(credential_id)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integrations_credential: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **credential_id** | **str**| Credential ID |  |

### Return type

void (empty response body)


## get_integration

> [**Integration**](Integration) get_integration(integration_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)


Get integration.

Wraps GET /api/v2/integrations/{integrationId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Get integration.
    api_response = api_instance.get_integration(integration_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**Integration**](Integration)


## get_integration_config_current

> [**IntegrationConfiguration**](IntegrationConfiguration) get_integration_config_current(integration_id)


Get integration configuration.

Wraps GET /api/v2/integrations/{integrationId}/config/current 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id

try:
    # Get integration configuration.
    api_response = api_instance.get_integration_config_current(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration_config_current: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration)


## get_integrations

> [**IntegrationEntityListing**](IntegrationEntityListing) get_integrations(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)


List integrations

Wraps GET /api/v2/integrations 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # List integrations
    api_response = api_instance.get_integrations(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**IntegrationEntityListing**](IntegrationEntityListing)


## get_integrations_action

> [**Action**](Action) get_integrations_action(action_id, expand=expand, flatten=flatten, include_config=include_config)


Retrieves a single Action matching id.

Wraps GET /api/v2/integrations/actions/{actionId} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
expand = 'expand_example' # str | Indicates a field in the response which should be expanded. (optional)
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)
include_config = False # bool | Return config in response. (optional) (default to False)

try:
    # Retrieves a single Action matching id.
    api_response = api_instance.get_integrations_action(action_id, expand=expand, flatten=flatten, include_config=include_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **expand** | **str**| Indicates a field in the response which should be expanded. | [optional] <br />**Values**: contract |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False]<br />**Values**: true, false |
| **include_config** | **bool**| Return config in response. | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**Action**](Action)


## get_integrations_action_draft

> [**Action**](Action) get_integrations_action_draft(action_id, expand=expand, flatten=flatten, include_config=include_config)


Retrieve a Draft

Wraps GET /api/v2/integrations/actions/{actionId}/draft 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
expand = 'expand_example' # str | Indicates a field in the response which should be expanded. (optional)
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)
include_config = False # bool | Return config in response. (optional) (default to False)

try:
    # Retrieve a Draft
    api_response = api_instance.get_integrations_action_draft(action_id, expand=expand, flatten=flatten, include_config=include_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **expand** | **str**| Indicates a field in the response which should be expanded. | [optional] <br />**Values**: contract |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False]<br />**Values**: true, false |
| **include_config** | **bool**| Return config in response. | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**Action**](Action)


## get_integrations_action_draft_function

> [**FunctionConfig**](FunctionConfig) get_integrations_action_draft_function(action_id)


Get draft function settings for Action

Wraps GET /api/v2/integrations/actions/{actionId}/draft/function 

Requires ANY permissions: 

* integrations:actionFunction:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Get draft function settings for Action
    api_response = api_instance.get_integrations_action_draft_function(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft_function: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |

### Return type

[**FunctionConfig**](FunctionConfig)


## get_integrations_action_draft_schema

> [**JsonSchemaDocument**](JsonSchemaDocument) get_integrations_action_draft_schema(action_id, file_name, flatten=flatten)


Retrieve schema for a Draft based on filename.

Wraps GET /api/v2/integrations/actions/{actionId}/draft/schemas/{fileName} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
file_name = 'file_name_example' # str | Name of schema file to be retrieved for this draft.
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)

try:
    # Retrieve schema for a Draft based on filename.
    api_response = api_instance.get_integrations_action_draft_schema(action_id, file_name, flatten=flatten)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of schema file to be retrieved for this draft. |  |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False] |

### Return type

[**JsonSchemaDocument**](JsonSchemaDocument)


## get_integrations_action_draft_template

> str** get_integrations_action_draft_template(action_id, file_name)


Retrieve templates for a Draft based on filename.

Wraps GET /api/v2/integrations/actions/{actionId}/draft/templates/{fileName} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
file_name = 'file_name_example' # str | Name of template file to be retrieved for this action draft.

try:
    # Retrieve templates for a Draft based on filename.
    api_response = api_instance.get_integrations_action_draft_template(action_id, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of template file to be retrieved for this action draft. |  |

### Return type

**str**


## get_integrations_action_draft_validation

> [**DraftValidationResult**](DraftValidationResult) get_integrations_action_draft_validation(action_id)


Validate current Draft configuration.

Wraps GET /api/v2/integrations/actions/{actionId}/draft/validation 

Requires ANY permissions: 

* integrations:action:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Validate current Draft configuration.
    api_response = api_instance.get_integrations_action_draft_validation(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft_validation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |

### Return type

[**DraftValidationResult**](DraftValidationResult)


## get_integrations_action_function

> [**FunctionConfig**](FunctionConfig) get_integrations_action_function(action_id)


Get published function settings for Action

Wraps GET /api/v2/integrations/actions/{actionId}/function 

Requires ANY permissions: 

* integrations:actionFunction:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Get published function settings for Action
    api_response = api_instance.get_integrations_action_function(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_function: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |

### Return type

[**FunctionConfig**](FunctionConfig)


## get_integrations_action_schema

> [**JsonSchemaDocument**](JsonSchemaDocument) get_integrations_action_schema(action_id, file_name, flatten=flatten)


Retrieve schema for an action based on filename.

Wraps GET /api/v2/integrations/actions/{actionId}/schemas/{fileName} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
file_name = 'file_name_example' # str | Name of schema file to be retrieved for this action.
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)

try:
    # Retrieve schema for an action based on filename.
    api_response = api_instance.get_integrations_action_schema(action_id, file_name, flatten=flatten)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of schema file to be retrieved for this action. |  |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False] |

### Return type

[**JsonSchemaDocument**](JsonSchemaDocument)


## get_integrations_action_template

> str** get_integrations_action_template(action_id, file_name)


Retrieve text of templates for an action based on filename.

Wraps GET /api/v2/integrations/actions/{actionId}/templates/{fileName} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
file_name = 'file_name_example' # str | Name of template file to be retrieved for this action.

try:
    # Retrieve text of templates for an action based on filename.
    api_response = api_instance.get_integrations_action_template(action_id, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of template file to be retrieved for this action. |  |

### Return type

**str**


## get_integrations_actions

> [**ActionEntityListing**](ActionEntityListing) get_integrations_actions(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, ids=ids, secure=secure, include_auth_actions=include_auth_actions)


Retrieves all actions associated with filters passed in via query param.

Wraps GET /api/v2/integrations/actions 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
sort_by = 'sort_by_example' # str | Root level field name to sort on. (optional)
sort_order = ''asc'' # str | Direction to sort 'sortBy' field. (optional) (default to 'asc')
category = 'category_example' # str | Filter by category name. (optional)
name = 'name_example' # str | Filter by partial or complete action name. (optional)
ids = 'ids_example' # str | Filter by action Id. Can be a comma separated list to request multiple actions.  Limit of 50 Ids. (optional)
secure = 'secure_example' # str | Filter based on 'secure' configuration option. True will only return actions marked as secure. False will return only non-secure actions. Do not use filter if you want all Actions. (optional)
include_auth_actions = ''false'' # str | Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. (optional) (default to 'false')

try:
    # Retrieves all actions associated with filters passed in via query param.
    api_response = api_instance.get_integrations_actions(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, ids=ids, secure=secure, include_auth_actions=include_auth_actions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_actions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **sort_by** | **str**| Root level field name to sort on. | [optional]  |
| **sort_order** | **str**| Direction to sort &#39;sortBy&#39; field. | [optional] [default to &#39;asc&#39;]<br />**Values**: ASC, DESC |
| **category** | **str**| Filter by category name. | [optional]  |
| **name** | **str**| Filter by partial or complete action name. | [optional]  |
| **ids** | **str**| Filter by action Id. Can be a comma separated list to request multiple actions.  Limit of 50 Ids. | [optional]  |
| **secure** | **str**| Filter based on &#39;secure&#39; configuration option. True will only return actions marked as secure. False will return only non-secure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
| **include_auth_actions** | **str**| Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. | [optional] [default to &#39;false&#39;]<br />**Values**: true, false |

### Return type

[**ActionEntityListing**](ActionEntityListing)


## get_integrations_actions_categories

> [**CategoryEntityListing**](CategoryEntityListing) get_integrations_actions_categories(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, secure=secure)


Retrieves all categories of available Actions

Wraps GET /api/v2/integrations/actions/categories 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
sort_by = 'sort_by_example' # str | Root level field name to sort on.  Only 'name' is supported on this endpoint. (optional)
sort_order = ''asc'' # str | Direction to sort 'sortBy' field. (optional) (default to 'asc')
secure = 'secure_example' # str | Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. (optional)

try:
    # Retrieves all categories of available Actions
    api_response = api_instance.get_integrations_actions_categories(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, secure=secure)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_actions_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **sort_by** | **str**| Root level field name to sort on.  Only &#39;name&#39; is supported on this endpoint. | [optional]  |
| **sort_order** | **str**| Direction to sort &#39;sortBy&#39; field. | [optional] [default to &#39;asc&#39;]<br />**Values**: ASC, DESC |
| **secure** | **str**| Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |

### Return type

[**CategoryEntityListing**](CategoryEntityListing)


## get_integrations_actions_certificates

> [**ActionCertificateListing**](ActionCertificateListing) get_integrations_actions_certificates(status=status, type=type)


Retrieves the available mTLS client certificates in use. This endpoint will return inconsistent results while a certificate rotation is in progress.

Wraps GET /api/v2/integrations/actions/certificates 

Requires ANY permissions: 

* integrations:actionCertificate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
status = 'status_example' # str | Indicates the validity of the certificate in question. (optional)
type = 'type_example' # str | Indicates the type of the certificate. (optional)

try:
    # Retrieves the available mTLS client certificates in use. This endpoint will return inconsistent results while a certificate rotation is in progress.
    api_response = api_instance.get_integrations_actions_certificates(status=status, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_actions_certificates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **status** | **str**| Indicates the validity of the certificate in question. | [optional] <br />**Values**: Current, Upcoming |
| **type** | **str**| Indicates the type of the certificate. | [optional] <br />**Values**: Client |

### Return type

[**ActionCertificateListing**](ActionCertificateListing)


## get_integrations_actions_certificates_truststore

> [**TrustedCertificates**](TrustedCertificates) get_integrations_actions_certificates_truststore()


Retrieves basic info about trusted root CA certificates

Wraps GET /api/v2/integrations/actions/certificates/truststore 

Requires ANY permissions: 

* integrations:actionCertificate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()

try:
    # Retrieves basic info about trusted root CA certificates
    api_response = api_instance.get_integrations_actions_certificates_truststore()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_actions_certificates_truststore: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**TrustedCertificates**](TrustedCertificates)


## get_integrations_actions_drafts

> [**ActionEntityListing**](ActionEntityListing) get_integrations_actions_drafts(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, ids=ids, secure=secure, include_auth_actions=include_auth_actions)


Retrieves all action drafts associated with the filters passed in via query param.

Wraps GET /api/v2/integrations/actions/drafts 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
sort_by = 'sort_by_example' # str | Root level field name to sort on. (optional)
sort_order = ''asc'' # str | Direction to sort 'sortBy' field. (optional) (default to 'asc')
category = 'category_example' # str | Filter by category name. (optional)
name = 'name_example' # str | Filter by partial or complete action name. (optional)
ids = 'ids_example' # str | Filter by action Id. Can be a comma separated list to request multiple actions.  Limit of 50 Ids. (optional)
secure = 'secure_example' # str | Filter based on 'secure' configuration option. True will only return actions marked as secure. False will return only non-secure actions. Do not use filter if you want all Actions. (optional)
include_auth_actions = ''false'' # str | Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. (optional) (default to 'false')

try:
    # Retrieves all action drafts associated with the filters passed in via query param.
    api_response = api_instance.get_integrations_actions_drafts(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, ids=ids, secure=secure, include_auth_actions=include_auth_actions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_actions_drafts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **sort_by** | **str**| Root level field name to sort on. | [optional]  |
| **sort_order** | **str**| Direction to sort &#39;sortBy&#39; field. | [optional] [default to &#39;asc&#39;]<br />**Values**: ASC, DESC |
| **category** | **str**| Filter by category name. | [optional]  |
| **name** | **str**| Filter by partial or complete action name. | [optional]  |
| **ids** | **str**| Filter by action Id. Can be a comma separated list to request multiple actions.  Limit of 50 Ids. | [optional]  |
| **secure** | **str**| Filter based on &#39;secure&#39; configuration option. True will only return actions marked as secure. False will return only non-secure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
| **include_auth_actions** | **str**| Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. | [optional] [default to &#39;false&#39;]<br />**Values**: true, false |

### Return type

[**ActionEntityListing**](ActionEntityListing)


## get_integrations_actions_functions_runtimes

> [**list[FunctionRuntime]**](FunctionRuntime) get_integrations_actions_functions_runtimes()


Get action function settings for Action

Wraps GET /api/v2/integrations/actions/functions/runtimes 

Requires ANY permissions: 

* integrations:actionFunction:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()

try:
    # Get action function settings for Action
    api_response = api_instance.get_integrations_actions_functions_runtimes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_actions_functions_runtimes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**list[FunctionRuntime]**](FunctionRuntime)


## get_integrations_botconnector_bot

> [**Bot**](Bot) get_integrations_botconnector_bot(integration_id, bot_id, version=version)


Get a specific Bot details

get_integrations_botconnector_bot is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/integrations/botconnectors/{integrationId}/bots/{botId} 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots
bot_id = 'bot_id_example' # str | The bot ID for this bot
version = 'version_example' # str | Specific Version (optional)

try:
    # Get a specific Bot details
    api_response = api_instance.get_integrations_botconnector_bot(integration_id, bot_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_bot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_id** | **str**| The bot ID for this bot |  |
| **version** | **str**| Specific Version | [optional]  |

### Return type

[**Bot**](Bot)


## get_integrations_botconnector_bots

> [**BotListing**](BotListing) get_integrations_botconnector_bots(integration_id, page_number=page_number, page_size=page_size)


Get the list of bots for this integration.

get_integrations_botconnector_bots is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/integrations/botconnectors/{integrationId}/bots 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots.
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get the list of bots for this integration.
    api_response = api_instance.get_integrations_botconnector_bots(integration_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_bots: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots. |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**BotListing**](BotListing)


## get_integrations_botconnector_bots_summaries

> [**BotSummaryEntityListing**](BotSummaryEntityListing) get_integrations_botconnector_bots_summaries(integration_id, page_number=page_number, page_size=page_size)


Get the summary list of bots for this integration.

get_integrations_botconnector_bots_summaries is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/integrations/botconnectors/{integrationId}/bots/summaries 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots.
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get the summary list of bots for this integration.
    api_response = api_instance.get_integrations_botconnector_bots_summaries(integration_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_bots_summaries: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots. |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**BotSummaryEntityListing**](BotSummaryEntityListing)


## get_integrations_botconnector_integration_id_bot

> [**BotConnectorBot**](BotConnectorBot) get_integrations_botconnector_integration_id_bot(integration_id, bot_id, version=version)


Get a specific botConnector bot, plus versions, for this integration

Wraps GET /api/v2/integrations/botconnector/{integrationId}/bots/{botId} 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots
bot_id = 'bot_id_example' # str | The botID for this bot
version = 'version_example' # str | Specific Version (optional)

try:
    # Get a specific botConnector bot, plus versions, for this integration
    api_response = api_instance.get_integrations_botconnector_integration_id_bot(integration_id, bot_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_integration_id_bot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_id** | **str**| The botID for this bot |  |
| **version** | **str**| Specific Version | [optional]  |

### Return type

[**BotConnectorBot**](BotConnectorBot)


## get_integrations_botconnector_integration_id_bot_versions

> [**BotConnectorBotVersionSummaryEntityListing**](BotConnectorBotVersionSummaryEntityListing) get_integrations_botconnector_integration_id_bot_versions(integration_id, bot_id, page_number=page_number, page_size=page_size)


Get a list of bot versions for a bot

Wraps GET /api/v2/integrations/botconnector/{integrationId}/bots/{botId}/versions 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this bot group
bot_id = 'bot_id_example' # str | The botID for this bot
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of bot versions for a bot
    api_response = api_instance.get_integrations_botconnector_integration_id_bot_versions(integration_id, bot_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_integration_id_bot_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this bot group |  |
| **bot_id** | **str**| The botID for this bot |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**BotConnectorBotVersionSummaryEntityListing**](BotConnectorBotVersionSummaryEntityListing)


## get_integrations_botconnector_integration_id_bots

> [**BotList**](BotList) get_integrations_botconnector_integration_id_bots(integration_id)


Get a list of botConnector bots for this integration

Wraps GET /api/v2/integrations/botconnector/{integrationId}/bots 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots

try:
    # Get a list of botConnector bots for this integration
    api_response = api_instance.get_integrations_botconnector_integration_id_bots(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_integration_id_bots: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots |  |

### Return type

[**BotList**](BotList)


## get_integrations_botconnector_integration_id_bots_summaries

> [**BotConnectorBotSummaryEntityListing**](BotConnectorBotSummaryEntityListing) get_integrations_botconnector_integration_id_bots_summaries(integration_id, page_number=page_number, page_size=page_size)


Get a summary list of botConnector bots for this integration

Wraps GET /api/v2/integrations/botconnector/{integrationId}/bots/summaries 

Requires ANY permissions: 

* integration:botconnector:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a summary list of botConnector bots for this integration
    api_response = api_instance.get_integrations_botconnector_integration_id_bots_summaries(integration_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_botconnector_integration_id_bots_summaries: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**BotConnectorBotSummaryEntityListing**](BotConnectorBotSummaryEntityListing)


## get_integrations_clientapps

> [**ClientAppEntityListing**](ClientAppEntityListing) get_integrations_clientapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)


List permitted client app integrations for the logged in user

Wraps GET /api/v2/integrations/clientapps 

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
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # List permitted client app integrations for the logged in user
    api_response = api_instance.get_integrations_clientapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_clientapps: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**ClientAppEntityListing**](ClientAppEntityListing)


## get_integrations_clientapps_unifiedcommunications

> [**UCIntegrationListing**](UCIntegrationListing) get_integrations_clientapps_unifiedcommunications(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

UC integration client application configuration.

Deprecated: Please use GET /integrations/unifiedcommunications/clientapps instead. This endpoint returns basic UI configuration data for all Unified Communications integrations client applications enabled for the current organization.

Wraps GET /api/v2/integrations/clientapps/unifiedcommunications 

Requires ANY permissions: 

* integration:unifiedCommunications:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # UC integration client application configuration.
    api_response = api_instance.get_integrations_clientapps_unifiedcommunications(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_clientapps_unifiedcommunications: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**UCIntegrationListing**](UCIntegrationListing)


## get_integrations_credential

> [**Credential**](Credential) get_integrations_credential(credential_id)


Get a single credential with sensitive fields redacted

Wraps GET /api/v2/integrations/credentials/{credentialId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
credential_id = 'credential_id_example' # str | Credential ID

try:
    # Get a single credential with sensitive fields redacted
    api_response = api_instance.get_integrations_credential(credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_credential: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **credential_id** | **str**| Credential ID |  |

### Return type

[**Credential**](Credential)


## get_integrations_credentials

> [**CredentialInfoListing**](CredentialInfoListing) get_integrations_credentials(page_number=page_number, page_size=page_size)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

List multiple sets of credentials

This endpoint is deprecated. Please see the Listing API (GET /api/v2/integrations/credentials/listing)

Wraps GET /api/v2/integrations/credentials 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # List multiple sets of credentials
    api_response = api_instance.get_integrations_credentials(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_credentials: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**CredentialInfoListing**](CredentialInfoListing)


## get_integrations_credentials_listing

> [**CredentialInfoCursorListing**](CredentialInfoCursorListing) get_integrations_credentials_listing(before=before, after=after, page_size=page_size)


List multiple sets of credentials using cursor-based paging

Wraps GET /api/v2/integrations/credentials/listing 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # List multiple sets of credentials using cursor-based paging
    api_response = api_instance.get_integrations_credentials_listing(before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_credentials_listing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**CredentialInfoCursorListing**](CredentialInfoCursorListing)


## get_integrations_credentials_types

> [**CredentialTypeListing**](CredentialTypeListing) get_integrations_credentials_types()


List all credential types

Wraps GET /api/v2/integrations/credentials/types 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()

try:
    # List all credential types
    api_response = api_instance.get_integrations_credentials_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_credentials_types: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CredentialTypeListing**](CredentialTypeListing)


## get_integrations_speech_audioconnector

> [**AudioConnectorIntegrationEntityListing**](AudioConnectorIntegrationEntityListing) get_integrations_speech_audioconnector(page_number=page_number, page_size=page_size)


Get a list of Audio Connector integrations

Wraps GET /api/v2/integrations/speech/audioconnector 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of Audio Connector integrations
    api_response = api_instance.get_integrations_speech_audioconnector(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_audioconnector: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**AudioConnectorIntegrationEntityListing**](AudioConnectorIntegrationEntityListing)


## get_integrations_speech_audioconnector_integration_id

> [**AudioConnectorIntegration**](AudioConnectorIntegration) get_integrations_speech_audioconnector_integration_id(integration_id)


Get an Audio Connector integration

Wraps GET /api/v2/integrations/speech/audioconnector/{integrationId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID

try:
    # Get an Audio Connector integration
    api_response = api_instance.get_integrations_speech_audioconnector_integration_id(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_audioconnector_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID |  |

### Return type

[**AudioConnectorIntegration**](AudioConnectorIntegration)


## get_integrations_speech_dialogflow_agent

> [**DialogflowAgent**](DialogflowAgent) get_integrations_speech_dialogflow_agent(agent_id)


Get details about a Dialogflow agent

Wraps GET /api/v2/integrations/speech/dialogflow/agents/{agentId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
agent_id = 'agent_id_example' # str | The agent ID

try:
    # Get details about a Dialogflow agent
    api_response = api_instance.get_integrations_speech_dialogflow_agent(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_dialogflow_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent ID |  |

### Return type

[**DialogflowAgent**](DialogflowAgent)


## get_integrations_speech_dialogflow_agents

> [**DialogflowAgentSummaryEntityListing**](DialogflowAgentSummaryEntityListing) get_integrations_speech_dialogflow_agents(page_number=page_number, page_size=page_size, name=name)


Get a list of Dialogflow agents in the customers' Google accounts

Wraps GET /api/v2/integrations/speech/dialogflow/agents 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Filter on agent name (optional)

try:
    # Get a list of Dialogflow agents in the customers' Google accounts
    api_response = api_instance.get_integrations_speech_dialogflow_agents(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_dialogflow_agents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Filter on agent name | [optional]  |

### Return type

[**DialogflowAgentSummaryEntityListing**](DialogflowAgentSummaryEntityListing)


## get_integrations_speech_dialogflowcx_agent

> [**DialogflowCXAgent**](DialogflowCXAgent) get_integrations_speech_dialogflowcx_agent(agent_id)


Get details about a Dialogflow CX agent

Wraps GET /api/v2/integrations/speech/dialogflowcx/agents/{agentId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
agent_id = 'agent_id_example' # str | The agent ID

try:
    # Get details about a Dialogflow CX agent
    api_response = api_instance.get_integrations_speech_dialogflowcx_agent(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_dialogflowcx_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent ID |  |

### Return type

[**DialogflowCXAgent**](DialogflowCXAgent)


## get_integrations_speech_dialogflowcx_agents

> [**DialogflowCXAgentSummaryEntityListing**](DialogflowCXAgentSummaryEntityListing) get_integrations_speech_dialogflowcx_agents(page_number=page_number, page_size=page_size, name=name)


Get a list of Dialogflow CX agents in the customers' Google accounts

Wraps GET /api/v2/integrations/speech/dialogflowcx/agents 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Filter on agent name (optional)

try:
    # Get a list of Dialogflow CX agents in the customers' Google accounts
    api_response = api_instance.get_integrations_speech_dialogflowcx_agents(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_dialogflowcx_agents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Filter on agent name | [optional]  |

### Return type

[**DialogflowCXAgentSummaryEntityListing**](DialogflowCXAgentSummaryEntityListing)


## get_integrations_speech_lex_bot_alias

> [**LexBotAlias**](LexBotAlias) get_integrations_speech_lex_bot_alias(alias_id)


Get details about a Lex bot alias

Wraps GET /api/v2/integrations/speech/lex/bot/alias/{aliasId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
alias_id = 'alias_id_example' # str | The alias ID

try:
    # Get details about a Lex bot alias
    api_response = api_instance.get_integrations_speech_lex_bot_alias(alias_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_lex_bot_alias: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alias_id** | **str**| The alias ID |  |

### Return type

[**LexBotAlias**](LexBotAlias)


## get_integrations_speech_lex_bot_bot_id_aliases

> [**LexBotAliasEntityListing**](LexBotAliasEntityListing) get_integrations_speech_lex_bot_bot_id_aliases(bot_id, page_number=page_number, page_size=page_size, status=status, name=name)


Get a list of aliases for a bot in the customer's AWS accounts

Wraps GET /api/v2/integrations/speech/lex/bot/{botId}/aliases 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
bot_id = 'bot_id_example' # str | The bot ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
status = 'status_example' # str | Filter on alias status (optional)
name = 'name_example' # str | Filter on alias name (optional)

try:
    # Get a list of aliases for a bot in the customer's AWS accounts
    api_response = api_instance.get_integrations_speech_lex_bot_bot_id_aliases(bot_id, page_number=page_number, page_size=page_size, status=status, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_lex_bot_bot_id_aliases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bot_id** | **str**| The bot ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **status** | **str**| Filter on alias status | [optional] <br />**Values**: READY, FAILED, BUILDING, NOT_BUILT |
| **name** | **str**| Filter on alias name | [optional]  |

### Return type

[**LexBotAliasEntityListing**](LexBotAliasEntityListing)


## get_integrations_speech_lex_bots

> [**LexBotEntityListing**](LexBotEntityListing) get_integrations_speech_lex_bots(page_number=page_number, page_size=page_size, name=name)


Get a list of Lex bots in the customers' AWS accounts

Wraps GET /api/v2/integrations/speech/lex/bots 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Filter on bot name (optional)

try:
    # Get a list of Lex bots in the customers' AWS accounts
    api_response = api_instance.get_integrations_speech_lex_bots(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_lex_bots: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Filter on bot name | [optional]  |

### Return type

[**LexBotEntityListing**](LexBotEntityListing)


## get_integrations_speech_lexv2_bot_alias

> [**LexV2BotAlias**](LexV2BotAlias) get_integrations_speech_lexv2_bot_alias(alias_id)


Get details about a Lex V2 bot alias

Wraps GET /api/v2/integrations/speech/lexv2/bot/alias/{aliasId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
alias_id = 'alias_id_example' # str | The Alias ID

try:
    # Get details about a Lex V2 bot alias
    api_response = api_instance.get_integrations_speech_lexv2_bot_alias(alias_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_lexv2_bot_alias: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alias_id** | **str**| The Alias ID |  |

### Return type

[**LexV2BotAlias**](LexV2BotAlias)


## get_integrations_speech_lexv2_bot_bot_id_aliases

> [**LexV2BotAliasEntityListing**](LexV2BotAliasEntityListing) get_integrations_speech_lexv2_bot_bot_id_aliases(bot_id, page_number=page_number, page_size=page_size, status=status, name=name)


Get a list of aliases for a Lex V2 bot

Wraps GET /api/v2/integrations/speech/lexv2/bot/{botId}/aliases 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
bot_id = 'bot_id_example' # str | The Bot ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
status = 'status_example' # str | Filter on alias status (optional)
name = 'name_example' # str | Filter on alias name (optional)

try:
    # Get a list of aliases for a Lex V2 bot
    api_response = api_instance.get_integrations_speech_lexv2_bot_bot_id_aliases(bot_id, page_number=page_number, page_size=page_size, status=status, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_lexv2_bot_bot_id_aliases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bot_id** | **str**| The Bot ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **status** | **str**| Filter on alias status | [optional] <br />**Values**: Creating, Available, Deleting, Failed |
| **name** | **str**| Filter on alias name | [optional]  |

### Return type

[**LexV2BotAliasEntityListing**](LexV2BotAliasEntityListing)


## get_integrations_speech_lexv2_bots

> [**LexV2BotEntityListing**](LexV2BotEntityListing) get_integrations_speech_lexv2_bots(page_number=page_number, page_size=page_size, name=name)


Get a list of Lex V2 bots

Wraps GET /api/v2/integrations/speech/lexv2/bots 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Filter on bot name (optional)

try:
    # Get a list of Lex V2 bots
    api_response = api_instance.get_integrations_speech_lexv2_bots(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_lexv2_bots: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Filter on bot name | [optional]  |

### Return type

[**LexV2BotEntityListing**](LexV2BotEntityListing)


## get_integrations_speech_nuance_nuance_integration_id_bot

> [**NuanceBot**](NuanceBot) get_integrations_speech_nuance_nuance_integration_id_bot(nuance_integration_id, bot_id, expand=expand, target_channel=target_channel)


Get a Nuance bot in the specified Integration

Wraps GET /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/{botId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
bot_id = 'bot_id_example' # str | The Nuance bot ID to get
expand = ['expand_example'] # list[str] | expand (optional)
target_channel = 'target_channel_example' # str | targetChannel (optional)

try:
    # Get a Nuance bot in the specified Integration
    api_response = api_instance.get_integrations_speech_nuance_nuance_integration_id_bot(nuance_integration_id, bot_id, expand=expand, target_channel=target_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_nuance_nuance_integration_id_bot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_id** | **str**| The Nuance bot ID to get |  |
| **expand** | [**list[str]**](str)| expand | [optional] <br />**Values**: variables, transferNodes, channels, locales |
| **target_channel** | **str**| targetChannel | [optional] <br />**Values**: digital, voice |

### Return type

[**NuanceBot**](NuanceBot)


## get_integrations_speech_nuance_nuance_integration_id_bot_job

> [**AsyncJob**](AsyncJob) get_integrations_speech_nuance_nuance_integration_id_bot_job(nuance_integration_id, bot_id, job_id)


Get the status of an asynchronous Nuance bot GET job

Wraps GET /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/{botId}/jobs/{jobId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
bot_id = 'bot_id_example' # str | The Nuance bot ID
job_id = 'job_id_example' # str | The asynchronous job ID

try:
    # Get the status of an asynchronous Nuance bot GET job
    api_response = api_instance.get_integrations_speech_nuance_nuance_integration_id_bot_job(nuance_integration_id, bot_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_nuance_nuance_integration_id_bot_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_id** | **str**| The Nuance bot ID |  |
| **job_id** | **str**| The asynchronous job ID |  |

### Return type

[**AsyncJob**](AsyncJob)


## get_integrations_speech_nuance_nuance_integration_id_bot_job_results

> [**NuanceBot**](NuanceBot) get_integrations_speech_nuance_nuance_integration_id_bot_job_results(nuance_integration_id, bot_id, job_id)


Get the result of an asynchronous Nuance bot GET job

Wraps GET /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/{botId}/jobs/{jobId}/results 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
bot_id = 'bot_id_example' # str | The Nuance bot ID
job_id = 'job_id_example' # str | The asynchronous job ID

try:
    # Get the result of an asynchronous Nuance bot GET job
    api_response = api_instance.get_integrations_speech_nuance_nuance_integration_id_bot_job_results(nuance_integration_id, bot_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_nuance_nuance_integration_id_bot_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_id** | **str**| The Nuance bot ID |  |
| **job_id** | **str**| The asynchronous job ID |  |

### Return type

[**NuanceBot**](NuanceBot)


## get_integrations_speech_nuance_nuance_integration_id_bots

> [**NuanceBotEntityListing**](NuanceBotEntityListing) get_integrations_speech_nuance_nuance_integration_id_bots(nuance_integration_id, page_number=page_number, page_size=page_size, only_registered_bots=only_registered_bots)


Get a list of Nuance bots available in the specified Integration

If the 'onlyRegisteredBots' param is set, the returned data will only include the Nuance bots which have configured client secrets within the Integration,  otherwise all of the Nuance bots available to the Integration's configured discovery credentials are returned.

Wraps GET /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
only_registered_bots = True # bool | Limit bots to the ones configured for Genesys Cloud usage (optional) (default to True)

try:
    # Get a list of Nuance bots available in the specified Integration
    api_response = api_instance.get_integrations_speech_nuance_nuance_integration_id_bots(nuance_integration_id, page_number=page_number, page_size=page_size, only_registered_bots=only_registered_bots)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_nuance_nuance_integration_id_bots: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **only_registered_bots** | **bool**| Limit bots to the ones configured for Genesys Cloud usage | [optional] [default to True] |

### Return type

[**NuanceBotEntityListing**](NuanceBotEntityListing)


## get_integrations_speech_nuance_nuance_integration_id_bots_job

> [**AsyncJob**](AsyncJob) get_integrations_speech_nuance_nuance_integration_id_bots_job(nuance_integration_id, job_id)


Get the status of an asynchronous Nuance bots GET job

Wraps GET /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/jobs/{jobId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
job_id = 'job_id_example' # str | The asynchronous job ID

try:
    # Get the status of an asynchronous Nuance bots GET job
    api_response = api_instance.get_integrations_speech_nuance_nuance_integration_id_bots_job(nuance_integration_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_nuance_nuance_integration_id_bots_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **job_id** | **str**| The asynchronous job ID |  |

### Return type

[**AsyncJob**](AsyncJob)


## get_integrations_speech_nuance_nuance_integration_id_bots_job_results

> [**NuanceBotEntityListing**](NuanceBotEntityListing) get_integrations_speech_nuance_nuance_integration_id_bots_job_results(nuance_integration_id, job_id)


Get the result of an asynchronous Nuance bots GET job

Wraps GET /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/jobs/{jobId}/results 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
job_id = 'job_id_example' # str | The asynchronous job ID

try:
    # Get the result of an asynchronous Nuance bots GET job
    api_response = api_instance.get_integrations_speech_nuance_nuance_integration_id_bots_job_results(nuance_integration_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_nuance_nuance_integration_id_bots_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **job_id** | **str**| The asynchronous job ID |  |

### Return type

[**NuanceBotEntityListing**](NuanceBotEntityListing)


## get_integrations_speech_stt_engine

> [**SttEngineEntity**](SttEngineEntity) get_integrations_speech_stt_engine(engine_id)


Get details about a STT engine

Wraps GET /api/v2/integrations/speech/stt/engines/{engineId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
engine_id = 'engine_id_example' # str | The engine ID

try:
    # Get details about a STT engine
    api_response = api_instance.get_integrations_speech_stt_engine(engine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_stt_engine: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **engine_id** | **str**| The engine ID |  |

### Return type

[**SttEngineEntity**](SttEngineEntity)


## get_integrations_speech_stt_engines

> [**SttEngineEntityListing**](SttEngineEntityListing) get_integrations_speech_stt_engines(page_number=page_number, page_size=page_size, name=name)


Get a list of STT engines enabled for org

Wraps GET /api/v2/integrations/speech/stt/engines 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Filter on engine name (optional)

try:
    # Get a list of STT engines enabled for org
    api_response = api_instance.get_integrations_speech_stt_engines(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_stt_engines: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Filter on engine name | [optional]  |

### Return type

[**SttEngineEntityListing**](SttEngineEntityListing)


## get_integrations_speech_tts_engine

> [**TtsEngineEntity**](TtsEngineEntity) get_integrations_speech_tts_engine(engine_id, include_voices=include_voices)


Get details about a TTS engine

Wraps GET /api/v2/integrations/speech/tts/engines/{engineId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
engine_id = 'engine_id_example' # str | The engine ID
include_voices = False # bool | Include voices for the engine (optional) (default to False)

try:
    # Get details about a TTS engine
    api_response = api_instance.get_integrations_speech_tts_engine(engine_id, include_voices=include_voices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_tts_engine: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **engine_id** | **str**| The engine ID |  |
| **include_voices** | **bool**| Include voices for the engine | [optional] [default to False] |

### Return type

[**TtsEngineEntity**](TtsEngineEntity)


## get_integrations_speech_tts_engine_voice

> [**TtsVoiceEntity**](TtsVoiceEntity) get_integrations_speech_tts_engine_voice(engine_id, voice_id)


Get details about a specific voice for a TTS engine

Wraps GET /api/v2/integrations/speech/tts/engines/{engineId}/voices/{voiceId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
engine_id = 'engine_id_example' # str | The engine ID
voice_id = 'voice_id_example' # str | The voice ID

try:
    # Get details about a specific voice for a TTS engine
    api_response = api_instance.get_integrations_speech_tts_engine_voice(engine_id, voice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_tts_engine_voice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **engine_id** | **str**| The engine ID |  |
| **voice_id** | **str**| The voice ID |  |

### Return type

[**TtsVoiceEntity**](TtsVoiceEntity)


## get_integrations_speech_tts_engine_voices

> [**TtsVoiceEntityListing**](TtsVoiceEntityListing) get_integrations_speech_tts_engine_voices(engine_id, page_number=page_number, page_size=page_size)


Get a list of voices for a TTS engine

Wraps GET /api/v2/integrations/speech/tts/engines/{engineId}/voices 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
engine_id = 'engine_id_example' # str | The engine ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of voices for a TTS engine
    api_response = api_instance.get_integrations_speech_tts_engine_voices(engine_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_tts_engine_voices: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **engine_id** | **str**| The engine ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**TtsVoiceEntityListing**](TtsVoiceEntityListing)


## get_integrations_speech_tts_engines

> [**TtsEngineEntityListing**](TtsEngineEntityListing) get_integrations_speech_tts_engines(page_number=page_number, page_size=page_size, include_voices=include_voices, name=name, language=language)


Get a list of TTS engines enabled for org

Wraps GET /api/v2/integrations/speech/tts/engines 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
include_voices = False # bool | Include voices for the engine (optional) (default to False)
name = 'name_example' # str | Filter on engine name (optional)
language = 'language_example' # str | Filter on supported language. If includeVoices=true then the voices are also filtered. (optional)

try:
    # Get a list of TTS engines enabled for org
    api_response = api_instance.get_integrations_speech_tts_engines(page_number=page_number, page_size=page_size, include_voices=include_voices, name=name, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_tts_engines: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **include_voices** | **bool**| Include voices for the engine | [optional] [default to False] |
| **name** | **str**| Filter on engine name | [optional]  |
| **language** | **str**| Filter on supported language. If includeVoices&#x3D;true then the voices are also filtered. | [optional]  |

### Return type

[**TtsEngineEntityListing**](TtsEngineEntityListing)


## get_integrations_speech_tts_settings

> [**TtsSettings**](TtsSettings) get_integrations_speech_tts_settings()


Get TTS settings for an org

Wraps GET /api/v2/integrations/speech/tts/settings 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()

try:
    # Get TTS settings for an org
    api_response = api_instance.get_integrations_speech_tts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_speech_tts_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**TtsSettings**](TtsSettings)


## get_integrations_type

> [**IntegrationType**](IntegrationType) get_integrations_type(type_id)


Get integration type.

Wraps GET /api/v2/integrations/types/{typeId} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
type_id = 'type_id_example' # str | Integration Type Id

try:
    # Get integration type.
    api_response = api_instance.get_integrations_type(type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_type: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type_id** | **str**| Integration Type Id |  |

### Return type

[**IntegrationType**](IntegrationType)


## get_integrations_type_configschema

> [**JsonSchemaDocument**](JsonSchemaDocument) get_integrations_type_configschema(type_id, config_type)


Get properties config schema for an integration type.

Wraps GET /api/v2/integrations/types/{typeId}/configschemas/{configType} 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
type_id = 'type_id_example' # str | Integration Type Id
config_type = 'config_type_example' # str | Config schema type

try:
    # Get properties config schema for an integration type.
    api_response = api_instance.get_integrations_type_configschema(type_id, config_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_type_configschema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type_id** | **str**| Integration Type Id |  |
| **config_type** | **str**| Config schema type | <br />**Values**: properties, advanced |

### Return type

[**JsonSchemaDocument**](JsonSchemaDocument)


## get_integrations_types

> [**IntegrationTypeEntityListing**](IntegrationTypeEntityListing) get_integrations_types(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)


List integration types

Wraps GET /api/v2/integrations/types 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # List integration types
    api_response = api_instance.get_integrations_types(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_types: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**IntegrationTypeEntityListing**](IntegrationTypeEntityListing)


## get_integrations_unifiedcommunications_clientapp

> [**UnifiedCommunicationsIntegration**](UnifiedCommunicationsIntegration) get_integrations_unifiedcommunications_clientapp(uc_integration_id)


UC integration client application configuration.

This endpoint returns basic UI configuration data for the specified Unified Communications integration client application.

Wraps GET /api/v2/integrations/unifiedcommunications/clientapps/{ucIntegrationId} 

Requires ANY permissions: 

* integration:unifiedCommunications:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
uc_integration_id = 'uc_integration_id_example' # str | 3rd Party Service Type

try:
    # UC integration client application configuration.
    api_response = api_instance.get_integrations_unifiedcommunications_clientapp(uc_integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_unifiedcommunications_clientapp: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uc_integration_id** | **str**| 3rd Party Service Type |  |

### Return type

[**UnifiedCommunicationsIntegration**](UnifiedCommunicationsIntegration)


## get_integrations_unifiedcommunications_clientapps

> [**UnifiedCommunicationsIntegrationListing**](UnifiedCommunicationsIntegrationListing) get_integrations_unifiedcommunications_clientapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)


List UC integration client application configurations.

This endpoint returns basic UI configuration data for all Unified Communications integrations client applications enabled.

Wraps GET /api/v2/integrations/unifiedcommunications/clientapps 

Requires ANY permissions: 

* integration:unifiedCommunications:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # List UC integration client application configurations.
    api_response = api_instance.get_integrations_unifiedcommunications_clientapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_unifiedcommunications_clientapps: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**UnifiedCommunicationsIntegrationListing**](UnifiedCommunicationsIntegrationListing)


## get_integrations_userapps

> [**UserAppEntityListing**](UserAppEntityListing) get_integrations_userapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, app_host=app_host)


List permitted user app integrations for the logged in user

Wraps GET /api/v2/integrations/userapps 

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
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
app_host = 'app_host_example' # str | The type of UserApp to filter by (optional)

try:
    # List permitted user app integrations for the logged in user
    api_response = api_instance.get_integrations_userapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, app_host=app_host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_userapps: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **app_host** | **str**| The type of UserApp to filter by | [optional]  |

### Return type

[**UserAppEntityListing**](UserAppEntityListing)


## patch_integration

> [**Integration**](Integration) patch_integration(integration_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, body=body)


Update an integration.

Wraps PATCH /api/v2/integrations/{integrationId} 

Requires ANY permissions: 

* integrations:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
body = PureCloudPlatformClientV2.Integration() # Integration | Integration Update (optional)

try:
    # Update an integration.
    api_response = api_instance.patch_integration(integration_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->patch_integration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **body** | [**Integration**](Integration)| Integration Update | [optional]  |

### Return type

[**Integration**](Integration)


## patch_integrations_action

> [**Action**](Action) patch_integrations_action(action_id, body)


Patch an Action

Wraps PATCH /api/v2/integrations/actions/{actionId} 

Requires ANY permissions: 

* integrations:action:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = PureCloudPlatformClientV2.UpdateActionInput() # UpdateActionInput | Input used to patch the Action.

try:
    # Patch an Action
    api_response = api_instance.patch_integrations_action(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->patch_integrations_action: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**UpdateActionInput**](UpdateActionInput)| Input used to patch the Action. |  |

### Return type

[**Action**](Action)


## patch_integrations_action_draft

> [**Action**](Action) patch_integrations_action_draft(action_id, body)


Update an existing Draft

Wraps PATCH /api/v2/integrations/actions/{actionId}/draft 

Requires ANY permissions: 

* integrations:action:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = PureCloudPlatformClientV2.UpdateDraftInput() # UpdateDraftInput | Input used to patch the Action Draft.

try:
    # Update an existing Draft
    api_response = api_instance.patch_integrations_action_draft(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->patch_integrations_action_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**UpdateDraftInput**](UpdateDraftInput)| Input used to patch the Action Draft. |  |

### Return type

[**Action**](Action)


## post_integrations

> [**Integration**](Integration) post_integrations(body=body)


Create an integration.

Wraps POST /api/v2/integrations 

Requires ANY permissions: 

* integrations:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.CreateIntegrationRequest() # CreateIntegrationRequest | Integration (optional)

try:
    # Create an integration.
    api_response = api_instance.post_integrations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateIntegrationRequest**](CreateIntegrationRequest)| Integration | [optional]  |

### Return type

[**Integration**](Integration)


## post_integrations_action_draft

> [**Action**](Action) post_integrations_action_draft(action_id)


Create a new Draft from existing Action

Wraps POST /api/v2/integrations/actions/{actionId}/draft 

Requires ANY permissions: 

* integrations:action:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Create a new Draft from existing Action
    api_response = api_instance.post_integrations_action_draft(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |

### Return type

[**Action**](Action)


## post_integrations_action_draft_function_upload

> [**FunctionUploadResponse**](FunctionUploadResponse) post_integrations_action_draft_function_upload(action_id, body)


Create upload presigned URL for draft function package file.

Wraps POST /api/v2/integrations/actions/{actionId}/draft/function/upload 

Requires ANY permissions: 

* integrations:actionFunction:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = PureCloudPlatformClientV2.FunctionUploadRequest() # FunctionUploadRequest | Input used to request URL upload.

try:
    # Create upload presigned URL for draft function package file.
    api_response = api_instance.post_integrations_action_draft_function_upload(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_draft_function_upload: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**FunctionUploadRequest**](FunctionUploadRequest)| Input used to request URL upload. |  |

### Return type

[**FunctionUploadResponse**](FunctionUploadResponse)


## post_integrations_action_draft_publish

> [**Action**](Action) post_integrations_action_draft_publish(action_id, body)


Publish a Draft and make it the active Action configuration

Wraps POST /api/v2/integrations/actions/{actionId}/draft/publish 

Requires ANY permissions: 

* integrations:action:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = PureCloudPlatformClientV2.PublishDraftInput() # PublishDraftInput | Input used to patch the Action.

try:
    # Publish a Draft and make it the active Action configuration
    api_response = api_instance.post_integrations_action_draft_publish(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_draft_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**PublishDraftInput**](PublishDraftInput)| Input used to patch the Action. |  |

### Return type

[**Action**](Action)


## post_integrations_action_draft_test

> [**TestExecutionResult**](TestExecutionResult) post_integrations_action_draft_test(action_id, body, flatten=flatten)


Test the execution of a draft. Responses will show execution steps broken out with intermediate results to help in debugging.

Wraps POST /api/v2/integrations/actions/{actionId}/draft/test 

Requires ANY permissions: 

* integrations:action:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = NULL # object | Map of parameters used for variable substitution.
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)

try:
    # Test the execution of a draft. Responses will show execution steps broken out with intermediate results to help in debugging.
    api_response = api_instance.post_integrations_action_draft_test(action_id, body, flatten=flatten)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_draft_test: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**object**](object)| Map of parameters used for variable substitution. |  |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False] |

### Return type

[**TestExecutionResult**](TestExecutionResult)


## post_integrations_action_execute

> object** post_integrations_action_execute(action_id, body, flatten=flatten)


Execute Action and return response from 3rd party.  Responses will follow the schemas defined on the Action for success and error.

Wraps POST /api/v2/integrations/actions/{actionId}/execute 

Requires ANY permissions: 

* integrations:action:execute
* bridge:actions:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = NULL # object | Map of parameters used for variable substitution.
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)

try:
    # Execute Action and return response from 3rd party.  Responses will follow the schemas defined on the Action for success and error.
    api_response = api_instance.post_integrations_action_execute(action_id, body, flatten=flatten)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_execute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**object**](object)| Map of parameters used for variable substitution. |  |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False] |

### Return type

**object**


## post_integrations_action_test

> [**TestExecutionResult**](TestExecutionResult) post_integrations_action_test(action_id, body, flatten=flatten)


Test the execution of an action. Responses will show execution steps broken out with intermediate results to help in debugging.

Wraps POST /api/v2/integrations/actions/{actionId}/test 

Requires ANY permissions: 

* integrations:action:execute
* bridge:actions:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = NULL # object | Map of parameters used for variable substitution.
flatten = False # bool | Indicates the response should be reformatted, based on Architect's flattening format. (optional) (default to False)

try:
    # Test the execution of an action. Responses will show execution steps broken out with intermediate results to help in debugging.
    api_response = api_instance.post_integrations_action_test(action_id, body, flatten=flatten)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_test: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**object**](object)| Map of parameters used for variable substitution. |  |
| **flatten** | **bool**| Indicates the response should be reformatted, based on Architect&#39;s flattening format. | [optional] [default to False] |

### Return type

[**TestExecutionResult**](TestExecutionResult)


## post_integrations_actions

> [**Action**](Action) post_integrations_actions(body)


Create a new Action. Not supported for 'Function Integration' actions. Function integrations must be created as drafts to allow managing of uploading required ZIP function package before they may be used as a published action.

Wraps POST /api/v2/integrations/actions 

Requires ANY permissions: 

* integrations:action:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.PostActionInput() # PostActionInput | Input used to create Action.

try:
    # Create a new Action. Not supported for 'Function Integration' actions. Function integrations must be created as drafts to allow managing of uploading required ZIP function package before they may be used as a published action.
    api_response = api_instance.post_integrations_actions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_actions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PostActionInput**](PostActionInput)| Input used to create Action. |  |

### Return type

[**Action**](Action)


## post_integrations_actions_drafts

> [**Action**](Action) post_integrations_actions_drafts(body)


Create a new Draft

Wraps POST /api/v2/integrations/actions/drafts 

Requires ANY permissions: 

* integrations:action:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.PostActionInput() # PostActionInput | Input used to create Action Draft.

try:
    # Create a new Draft
    api_response = api_instance.post_integrations_actions_drafts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_actions_drafts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PostActionInput**](PostActionInput)| Input used to create Action Draft. |  |

### Return type

[**Action**](Action)


## post_integrations_botconnectors_incoming_messages

> [**IncomingMessageResponse**](IncomingMessageResponse) post_integrations_botconnectors_incoming_messages(body)


Send an incoming message to the bot.

post_integrations_botconnectors_incoming_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/integrations/botconnectors/incoming/messages 

Requires ANY permissions: 

* integration:botconnector:send

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.IncomingMessageRequest() # IncomingMessageRequest | Incoming Message Request

try:
    # Send an incoming message to the bot.
    api_response = api_instance.post_integrations_botconnectors_incoming_messages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_botconnectors_incoming_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IncomingMessageRequest**](IncomingMessageRequest)| Incoming Message Request |  |

### Return type

[**IncomingMessageResponse**](IncomingMessageResponse)


## post_integrations_botconnectors_outgoing_messages

> [**OutgoingMessageResponse**](OutgoingMessageResponse) post_integrations_botconnectors_outgoing_messages(body)


Send an outgoing message to the end user.

post_integrations_botconnectors_outgoing_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/integrations/botconnectors/outgoing/messages 

Requires ANY permissions: 

* integration:botconnector:send

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.OutgoingMessageRequest() # OutgoingMessageRequest | Outgoing Message Request

try:
    # Send an outgoing message to the end user.
    api_response = api_instance.post_integrations_botconnectors_outgoing_messages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_botconnectors_outgoing_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutgoingMessageRequest**](OutgoingMessageRequest)| Outgoing Message Request |  |

### Return type

[**OutgoingMessageResponse**](OutgoingMessageResponse)


## post_integrations_credentials

> [**CredentialInfo**](CredentialInfo) post_integrations_credentials(body=body)


Create a set of credentials

Wraps POST /api/v2/integrations/credentials 

Requires ANY permissions: 

* integrations:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.Credential() # Credential | Credential (optional)

try:
    # Create a set of credentials
    api_response = api_instance.post_integrations_credentials(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_credentials: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Credential**](Credential)| Credential | [optional]  |

### Return type

[**CredentialInfo**](CredentialInfo)


## post_integrations_speech_nuance_nuance_integration_id_bot_jobs

> [**AsyncJob**](AsyncJob) post_integrations_speech_nuance_nuance_integration_id_bot_jobs(nuance_integration_id, bot_id, expand=expand, body=body)


Get a Nuance bot in the specified Integration asynchronously

Wraps POST /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/{botId}/jobs 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
bot_id = 'bot_id_example' # str | The Nuance bot ID
expand = ['expand_example'] # list[str] | expand (optional)
body = 'body_example' # str | targetChannel (optional)

try:
    # Get a Nuance bot in the specified Integration asynchronously
    api_response = api_instance.post_integrations_speech_nuance_nuance_integration_id_bot_jobs(nuance_integration_id, bot_id, expand=expand, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_speech_nuance_nuance_integration_id_bot_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_id** | **str**| The Nuance bot ID |  |
| **expand** | [**list[str]**](str)| expand | [optional] <br />**Values**: variables, transferNodes, channels, locales |
| **body** | **str**| targetChannel | [optional]  |

### Return type

[**AsyncJob**](AsyncJob)


## post_integrations_speech_nuance_nuance_integration_id_bots_jobs

> [**AsyncJob**](AsyncJob) post_integrations_speech_nuance_nuance_integration_id_bots_jobs(nuance_integration_id, page_number=page_number, page_size=page_size, only_registered_bots=only_registered_bots)


Get a list of Nuance bots in the specified Integration asynchronously

Wraps POST /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/jobs 

Requires ANY permissions: 

* integrations:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
only_registered_bots = True # bool | Limit bots to the ones configured for Genesys Cloud usage (optional) (default to True)

try:
    # Get a list of Nuance bots in the specified Integration asynchronously
    api_response = api_instance.post_integrations_speech_nuance_nuance_integration_id_bots_jobs(nuance_integration_id, page_number=page_number, page_size=page_size, only_registered_bots=only_registered_bots)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_speech_nuance_nuance_integration_id_bots_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **only_registered_bots** | **bool**| Limit bots to the ones configured for Genesys Cloud usage | [optional] [default to True] |

### Return type

[**AsyncJob**](AsyncJob)


## post_integrations_speech_nuance_nuance_integration_id_bots_launch_validate

>  post_integrations_speech_nuance_nuance_integration_id_bots_launch_validate(nuance_integration_id, settings)


Try out a single credential for a Nuance bot to know if the secret is correct

Wraps POST /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/launch/validate 

Requires ANY permissions: 

* integrations:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
settings = PureCloudPlatformClientV2.BotExecutionConfiguration() # BotExecutionConfiguration | 

try:
    # Try out a single credential for a Nuance bot to know if the secret is correct
    api_instance.post_integrations_speech_nuance_nuance_integration_id_bots_launch_validate(nuance_integration_id, settings)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_speech_nuance_nuance_integration_id_bots_launch_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **settings** | [**BotExecutionConfiguration**](BotExecutionConfiguration)|  |  |

### Return type

void (empty response body)


## post_integrations_webhook_events

> [**WebhookInvocationResponse**](WebhookInvocationResponse) post_integrations_webhook_events(token_id, body)


Invoke Webhook

Wraps POST /api/v2/integrations/webhooks/{tokenId}/events 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
token_id = 'token_id_example' # str | The token of the webhook to be invoked
body = NULL # object | Webhook Invocation Payload

try:
    # Invoke Webhook
    api_response = api_instance.post_integrations_webhook_events(token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_webhook_events: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **token_id** | **str**| The token of the webhook to be invoked |  |
| **body** | [**object**](object)| Webhook Invocation Payload |  |

### Return type

[**WebhookInvocationResponse**](WebhookInvocationResponse)


## put_integration_config_current

> [**IntegrationConfiguration**](IntegrationConfiguration) put_integration_config_current(integration_id, body=body)


Update integration configuration.

Wraps PUT /api/v2/integrations/{integrationId}/config/current 

Requires ANY permissions: 

* integrations:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id
body = PureCloudPlatformClientV2.IntegrationConfiguration() # IntegrationConfiguration | Integration Configuration (optional)

try:
    # Update integration configuration.
    api_response = api_instance.put_integration_config_current(integration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integration_config_current: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |
| **body** | [**IntegrationConfiguration**](IntegrationConfiguration)| Integration Configuration | [optional]  |

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration)


## put_integrations_action_draft_function

> [**FunctionConfig**](FunctionConfig) put_integrations_action_draft_function(action_id, body)


Update draft function settings.

Wraps PUT /api/v2/integrations/actions/{actionId}/draft/function 

Requires ANY permissions: 

* integrations:actionFunction:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
body = PureCloudPlatformClientV2.Function() # Function | Input used to update function settings.

try:
    # Update draft function settings.
    api_response = api_instance.put_integrations_action_draft_function(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integrations_action_draft_function: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**Function**](Function)| Input used to update function settings. |  |

### Return type

[**FunctionConfig**](FunctionConfig)


## put_integrations_botconnector_integration_id_bots

>  put_integrations_botconnector_integration_id_bots(integration_id, bot_list)


Set a list of botConnector bots plus versions for this integration

Wraps PUT /api/v2/integrations/botconnector/{integrationId}/bots 

Requires ANY permissions: 

* integration:botconnector:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration ID for this group of bots
bot_list = PureCloudPlatformClientV2.BotList() # BotList | 

try:
    # Set a list of botConnector bots plus versions for this integration
    api_instance.put_integrations_botconnector_integration_id_bots(integration_id, bot_list)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integrations_botconnector_integration_id_bots: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| The integration ID for this group of bots |  |
| **bot_list** | [**BotList**](BotList)|  |  |

### Return type

void (empty response body)


## put_integrations_credential

> [**CredentialInfo**](CredentialInfo) put_integrations_credential(credential_id, body=body)


Update a set of credentials

Wraps PUT /api/v2/integrations/credentials/{credentialId} 

Requires ANY permissions: 

* integrations:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
credential_id = 'credential_id_example' # str | Credential ID
body = PureCloudPlatformClientV2.Credential() # Credential | Credential (optional)

try:
    # Update a set of credentials
    api_response = api_instance.put_integrations_credential(credential_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integrations_credential: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **credential_id** | **str**| Credential ID |  |
| **body** | [**Credential**](Credential)| Credential | [optional]  |

### Return type

[**CredentialInfo**](CredentialInfo)


## put_integrations_speech_nuance_nuance_integration_id_bots_launch_settings

>  put_integrations_speech_nuance_nuance_integration_id_bots_launch_settings(nuance_integration_id, settings)


Update the Nuance bot list for the specific bots made available to Genesys Cloud in the specified Integration

Wraps PUT /api/v2/integrations/speech/nuance/{nuanceIntegrationId}/bots/launch/settings 

Requires ANY permissions: 

* integrations:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
nuance_integration_id = 'nuance_integration_id_example' # str | The integration ID for this group of bots
settings = PureCloudPlatformClientV2.NuanceBotLaunchSettings() # NuanceBotLaunchSettings | 

try:
    # Update the Nuance bot list for the specific bots made available to Genesys Cloud in the specified Integration
    api_instance.put_integrations_speech_nuance_nuance_integration_id_bots_launch_settings(nuance_integration_id, settings)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integrations_speech_nuance_nuance_integration_id_bots_launch_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nuance_integration_id** | **str**| The integration ID for this group of bots |  |
| **settings** | [**NuanceBotLaunchSettings**](NuanceBotLaunchSettings)|  |  |

### Return type

void (empty response body)


## put_integrations_speech_tts_settings

> [**TtsSettings**](TtsSettings) put_integrations_speech_tts_settings(body)


Update TTS settings for an org

Wraps PUT /api/v2/integrations/speech/tts/settings 

Requires ANY permissions: 

* integrations:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.TtsSettings() # TtsSettings | Updated TtsSettings

try:
    # Update TTS settings for an org
    api_response = api_instance.put_integrations_speech_tts_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integrations_speech_tts_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TtsSettings**](TtsSettings)| Updated TtsSettings |  |

### Return type

[**TtsSettings**](TtsSettings)


## put_integrations_unifiedcommunication_thirdpartypresences

> str** put_integrations_unifiedcommunication_thirdpartypresences(uc_integration_id, body)


Bulk integration presence ingestion

This endpoint accepts bulk presence updates from a 3rd-party presence integration and maps the 3rd-party user to a Genesys Cloud user via the matching email address. The 3rd-party presence value will be mapped to a Genesys Cloud organization presence definition value.

Wraps PUT /api/v2/integrations/unifiedcommunications/{ucIntegrationId}/thirdpartypresences 

Requires ANY permissions: 

* integration:presence:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
uc_integration_id = 'uc_integration_id_example' # str | UC Integration ID
body = [PureCloudPlatformClientV2.UCThirdPartyPresence()] # list[UCThirdPartyPresence] | List of User presences

try:
    # Bulk integration presence ingestion
    api_response = api_instance.put_integrations_unifiedcommunication_thirdpartypresences(uc_integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->put_integrations_unifiedcommunication_thirdpartypresences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uc_integration_id** | **str**| UC Integration ID |  |
| **body** | [**list[UCThirdPartyPresence]**](UCThirdPartyPresence)| List of User presences |  |

### Return type

**str**


_PureCloudPlatformClientV2 237.0.0_
