---
title: IntegrationsApi
---

## PureCloudPlatformClientV2.IntegrationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_integration**](IntegrationsApi.html#delete_integration) | Delete integration.|
|[**delete_integrations_action**](IntegrationsApi.html#delete_integrations_action) | Delete an Action|
|[**delete_integrations_action_draft**](IntegrationsApi.html#delete_integrations_action_draft) | Delete a Draft|
|[**delete_integrations_credential**](IntegrationsApi.html#delete_integrations_credential) | Delete a set of credentials|
|[**get_integration**](IntegrationsApi.html#get_integration) | Get integration.|
|[**get_integration_config_current**](IntegrationsApi.html#get_integration_config_current) | Get integration configuration.|
|[**get_integrations**](IntegrationsApi.html#get_integrations) | List integrations|
|[**get_integrations_action**](IntegrationsApi.html#get_integrations_action) | Retrieves a single Action matching id.|
|[**get_integrations_action_draft**](IntegrationsApi.html#get_integrations_action_draft) | Retrieve a Draft|
|[**get_integrations_action_draft_schema**](IntegrationsApi.html#get_integrations_action_draft_schema) | Retrieve schema for a Draft based on filename.|
|[**get_integrations_action_draft_template**](IntegrationsApi.html#get_integrations_action_draft_template) | Retrieve templates for a Draft based on filename.|
|[**get_integrations_action_draft_validation**](IntegrationsApi.html#get_integrations_action_draft_validation) | Validate current Draft configuration.|
|[**get_integrations_action_schema**](IntegrationsApi.html#get_integrations_action_schema) | Retrieve schema for an action based on filename.|
|[**get_integrations_action_template**](IntegrationsApi.html#get_integrations_action_template) | Retrieve text of templates for an action based on filename.|
|[**get_integrations_actions**](IntegrationsApi.html#get_integrations_actions) | Retrieves all actions associated with filters passed in via query param.|
|[**get_integrations_actions_categories**](IntegrationsApi.html#get_integrations_actions_categories) | Retrieves all categories of available Actions|
|[**get_integrations_actions_drafts**](IntegrationsApi.html#get_integrations_actions_drafts) | Retrieves all action drafts associated with the filters passed in via query param.|
|[**get_integrations_botconnector_integration_id_bot**](IntegrationsApi.html#get_integrations_botconnector_integration_id_bot) | Get a specific botConnector bot, plus versions, for this integration|
|[**get_integrations_botconnector_integration_id_bot_versions**](IntegrationsApi.html#get_integrations_botconnector_integration_id_bot_versions) | Get a list of bot versions for a bot|
|[**get_integrations_botconnector_integration_id_bots**](IntegrationsApi.html#get_integrations_botconnector_integration_id_bots) | Get a list of botConnector bots for this integration|
|[**get_integrations_botconnector_integration_id_bots_summaries**](IntegrationsApi.html#get_integrations_botconnector_integration_id_bots_summaries) | Get a summary list of botConnector bots for this integration|
|[**get_integrations_clientapps**](IntegrationsApi.html#get_integrations_clientapps) | List permitted client app integrations for the logged in user|
|[**get_integrations_clientapps_unifiedcommunications**](IntegrationsApi.html#get_integrations_clientapps_unifiedcommunications) | UC integration client application configuration.|
|[**get_integrations_credential**](IntegrationsApi.html#get_integrations_credential) | Get a single credential with sensitive fields redacted|
|[**get_integrations_credentials**](IntegrationsApi.html#get_integrations_credentials) | List multiple sets of credentials|
|[**get_integrations_credentials_types**](IntegrationsApi.html#get_integrations_credentials_types) | List all credential types|
|[**get_integrations_eventlog**](IntegrationsApi.html#get_integrations_eventlog) | List all events|
|[**get_integrations_eventlog_event_id**](IntegrationsApi.html#get_integrations_eventlog_event_id) | Get a single event|
|[**get_integrations_speech_dialogflow_agent**](IntegrationsApi.html#get_integrations_speech_dialogflow_agent) | Get details about a Dialogflow agent|
|[**get_integrations_speech_dialogflow_agents**](IntegrationsApi.html#get_integrations_speech_dialogflow_agents) | Get a list of Dialogflow agents in the customers&#39; Google accounts|
|[**get_integrations_speech_lex_bot_alias**](IntegrationsApi.html#get_integrations_speech_lex_bot_alias) | Get details about a Lex bot alias|
|[**get_integrations_speech_lex_bot_bot_id_aliases**](IntegrationsApi.html#get_integrations_speech_lex_bot_bot_id_aliases) | Get a list of aliases for a bot in the customer&#39;s AWS accounts|
|[**get_integrations_speech_lex_bots**](IntegrationsApi.html#get_integrations_speech_lex_bots) | Get a list of Lex bots in the customers&#39; AWS accounts|
|[**get_integrations_speech_tts_engine**](IntegrationsApi.html#get_integrations_speech_tts_engine) | Get details about a TTS engine|
|[**get_integrations_speech_tts_engine_voice**](IntegrationsApi.html#get_integrations_speech_tts_engine_voice) | Get details about a specific voice for a TTS engine|
|[**get_integrations_speech_tts_engine_voices**](IntegrationsApi.html#get_integrations_speech_tts_engine_voices) | Get a list of voices for a TTS engine|
|[**get_integrations_speech_tts_engines**](IntegrationsApi.html#get_integrations_speech_tts_engines) | Get a list of TTS engines enabled for org|
|[**get_integrations_speech_tts_settings**](IntegrationsApi.html#get_integrations_speech_tts_settings) | Get TTS settings for an org|
|[**get_integrations_type**](IntegrationsApi.html#get_integrations_type) | Get integration type.|
|[**get_integrations_type_configschema**](IntegrationsApi.html#get_integrations_type_configschema) | Get properties config schema for an integration type.|
|[**get_integrations_types**](IntegrationsApi.html#get_integrations_types) | List integration types|
|[**get_integrations_userapps**](IntegrationsApi.html#get_integrations_userapps) | List permitted user app integrations for the logged in user|
|[**patch_integration**](IntegrationsApi.html#patch_integration) | Update an integration.|
|[**patch_integrations_action**](IntegrationsApi.html#patch_integrations_action) | Patch an Action|
|[**patch_integrations_action_draft**](IntegrationsApi.html#patch_integrations_action_draft) | Update an existing Draft|
|[**post_integrations**](IntegrationsApi.html#post_integrations) | Create an integration.|
|[**post_integrations_action_draft**](IntegrationsApi.html#post_integrations_action_draft) | Create a new Draft from existing Action|
|[**post_integrations_action_draft_publish**](IntegrationsApi.html#post_integrations_action_draft_publish) | Publish a Draft and make it the active Action configuration|
|[**post_integrations_action_draft_test**](IntegrationsApi.html#post_integrations_action_draft_test) | Test the execution of a draft. Responses will show execution steps broken out with intermediate results to help in debugging.|
|[**post_integrations_action_execute**](IntegrationsApi.html#post_integrations_action_execute) | Execute Action and return response from 3rd party.  Responses will follow the schemas defined on the Action for success and error.|
|[**post_integrations_action_test**](IntegrationsApi.html#post_integrations_action_test) | Test the execution of an action. Responses will show execution steps broken out with intermediate results to help in debugging.|
|[**post_integrations_actions**](IntegrationsApi.html#post_integrations_actions) | Create a new Action|
|[**post_integrations_actions_drafts**](IntegrationsApi.html#post_integrations_actions_drafts) | Create a new Draft|
|[**post_integrations_credentials**](IntegrationsApi.html#post_integrations_credentials) | Create a set of credentials|
|[**post_integrations_workforcemanagement_vendorconnection**](IntegrationsApi.html#post_integrations_workforcemanagement_vendorconnection) | Add a vendor connection|
|[**put_integration_config_current**](IntegrationsApi.html#put_integration_config_current) | Update integration configuration.|
|[**put_integrations_botconnector_integration_id_bots**](IntegrationsApi.html#put_integrations_botconnector_integration_id_bots) | Set a list of botConnector bots plus versions for this integration|
|[**put_integrations_credential**](IntegrationsApi.html#put_integrations_credential) | Update a set of credentials|
|[**put_integrations_speech_tts_settings**](IntegrationsApi.html#put_integrations_speech_tts_settings) | Update TTS settings for an org|
{: class="table table-striped"}

<a name="delete_integration"></a>

## [**Integration**](Integration.html) delete_integration(integration_id)



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
{: class="table table-striped"}

### Return type

[**Integration**](Integration.html)

<a name="delete_integrations_action"></a>

##  delete_integrations_action(action_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_integrations_action_draft"></a>

##  delete_integrations_action_draft(action_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_integrations_credential"></a>

##  delete_integrations_credential(credential_id)



Delete a set of credentials



Wraps DELETE /api/v2/integrations/credentials/{credentialId} 

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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_integration"></a>

## [**Integration**](Integration.html) get_integration(integration_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



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
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**Integration**](Integration.html)

<a name="get_integration_config_current"></a>

## [**IntegrationConfiguration**](IntegrationConfiguration.html) get_integration_config_current(integration_id)



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
{: class="table table-striped"}

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.html)

<a name="get_integrations"></a>

## [**IntegrationEntityListing**](IntegrationEntityListing.html) get_integrations(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



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
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**IntegrationEntityListing**](IntegrationEntityListing.html)

<a name="get_integrations_action"></a>

## [**Action**](Action.html) get_integrations_action(action_id, expand=expand, include_config=include_config)



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
include_config = false # bool | Return config in response. (optional) (default to false)

try:
    # Retrieves a single Action matching id.
    api_response = api_instance.get_integrations_action(action_id, expand=expand, include_config=include_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **expand** | **str**| Indicates a field in the response which should be expanded. | [optional] <br />**Values**: contract |
| **include_config** | **bool**| Return config in response. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="get_integrations_action_draft"></a>

## [**Action**](Action.html) get_integrations_action_draft(action_id, expand=expand, include_config=include_config)



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
include_config = false # bool | Return config in response. (optional) (default to false)

try:
    # Retrieve a Draft
    api_response = api_instance.get_integrations_action_draft(action_id, expand=expand, include_config=include_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **expand** | **str**| Indicates a field in the response which should be expanded. | [optional] <br />**Values**: contract |
| **include_config** | **bool**| Return config in response. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="get_integrations_action_draft_schema"></a>

## [**JsonSchemaDocument**](JsonSchemaDocument.html) get_integrations_action_draft_schema(action_id, file_name)



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

try:
    # Retrieve schema for a Draft based on filename.
    api_response = api_instance.get_integrations_action_draft_schema(action_id, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_draft_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of schema file to be retrieved for this draft. |  |
{: class="table table-striped"}

### Return type

[**JsonSchemaDocument**](JsonSchemaDocument.html)

<a name="get_integrations_action_draft_template"></a>

## str** get_integrations_action_draft_template(action_id, file_name)



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
{: class="table table-striped"}

### Return type

**str**

<a name="get_integrations_action_draft_validation"></a>

## [**DraftValidationResult**](DraftValidationResult.html) get_integrations_action_draft_validation(action_id)



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
{: class="table table-striped"}

### Return type

[**DraftValidationResult**](DraftValidationResult.html)

<a name="get_integrations_action_schema"></a>

## [**JsonSchemaDocument**](JsonSchemaDocument.html) get_integrations_action_schema(action_id, file_name)



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

try:
    # Retrieve schema for an action based on filename.
    api_response = api_instance.get_integrations_action_schema(action_id, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_action_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of schema file to be retrieved for this action. |  |
{: class="table table-striped"}

### Return type

[**JsonSchemaDocument**](JsonSchemaDocument.html)

<a name="get_integrations_action_template"></a>

## str** get_integrations_action_template(action_id, file_name)



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
{: class="table table-striped"}

### Return type

**str**

<a name="get_integrations_actions"></a>

## [**ActionEntityListing**](ActionEntityListing.html) get_integrations_actions(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, secure=secure, include_auth_actions=include_auth_actions)



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
sort_order = 'asc' # str | Direction to sort 'sortBy' field. (optional) (default to asc)
category = 'category_example' # str | Filter by category name (optional)
name = 'name_example' # str | Filter by action name. Provide full or just the first part of name. (optional)
secure = 'secure_example' # str | Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. (optional)
include_auth_actions = 'false' # str | Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. (optional) (default to false)

try:
    # Retrieves all actions associated with filters passed in via query param.
    api_response = api_instance.get_integrations_actions(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, secure=secure, include_auth_actions=include_auth_actions)
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
| **sort_order** | **str**| Direction to sort &#39;sortBy&#39; field. | [optional] [default to asc]<br />**Values**: ASC, DESC |
| **category** | **str**| Filter by category name | [optional]  |
| **name** | **str**| Filter by action name. Provide full or just the first part of name. | [optional]  |
| **secure** | **str**| Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
| **include_auth_actions** | **str**| Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. | [optional] [default to false]<br />**Values**: true, false |
{: class="table table-striped"}

### Return type

[**ActionEntityListing**](ActionEntityListing.html)

<a name="get_integrations_actions_categories"></a>

## [**CategoryEntityListing**](CategoryEntityListing.html) get_integrations_actions_categories(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, secure=secure)



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
sort_order = 'asc' # str | Direction to sort 'sortBy' field. (optional) (default to asc)
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
| **sort_order** | **str**| Direction to sort &#39;sortBy&#39; field. | [optional] [default to asc]<br />**Values**: ASC, DESC |
| **secure** | **str**| Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
{: class="table table-striped"}

### Return type

[**CategoryEntityListing**](CategoryEntityListing.html)

<a name="get_integrations_actions_drafts"></a>

## [**ActionEntityListing**](ActionEntityListing.html) get_integrations_actions_drafts(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, secure=secure, include_auth_actions=include_auth_actions)



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
sort_order = 'asc' # str | Direction to sort 'sortBy' field. (optional) (default to asc)
category = 'category_example' # str | Filter by category name (optional)
name = 'name_example' # str | Filter by action name. Provide full or just the first part of name. (optional)
secure = 'secure_example' # str | Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. (optional)
include_auth_actions = 'false' # str | Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. (optional) (default to false)

try:
    # Retrieves all action drafts associated with the filters passed in via query param.
    api_response = api_instance.get_integrations_actions_drafts(page_size=page_size, page_number=page_number, next_page=next_page, previous_page=previous_page, sort_by=sort_by, sort_order=sort_order, category=category, name=name, secure=secure, include_auth_actions=include_auth_actions)
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
| **sort_order** | **str**| Direction to sort &#39;sortBy&#39; field. | [optional] [default to asc]<br />**Values**: ASC, DESC |
| **category** | **str**| Filter by category name | [optional]  |
| **name** | **str**| Filter by action name. Provide full or just the first part of name. | [optional]  |
| **secure** | **str**| Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
| **include_auth_actions** | **str**| Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. | [optional] [default to false]<br />**Values**: true, false |
{: class="table table-striped"}

### Return type

[**ActionEntityListing**](ActionEntityListing.html)

<a name="get_integrations_botconnector_integration_id_bot"></a>

## [**BotConnectorBot**](BotConnectorBot.html) get_integrations_botconnector_integration_id_bot(integration_id, bot_id, version=version)



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
{: class="table table-striped"}

### Return type

[**BotConnectorBot**](BotConnectorBot.html)

<a name="get_integrations_botconnector_integration_id_bot_versions"></a>

## [**BotConnectorBotVersionSummaryEntityListing**](BotConnectorBotVersionSummaryEntityListing.html) get_integrations_botconnector_integration_id_bot_versions(integration_id, bot_id, page_number=page_number, page_size=page_size)



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
{: class="table table-striped"}

### Return type

[**BotConnectorBotVersionSummaryEntityListing**](BotConnectorBotVersionSummaryEntityListing.html)

<a name="get_integrations_botconnector_integration_id_bots"></a>

## [**BotList**](BotList.html) get_integrations_botconnector_integration_id_bots(integration_id)



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
{: class="table table-striped"}

### Return type

[**BotList**](BotList.html)

<a name="get_integrations_botconnector_integration_id_bots_summaries"></a>

## [**BotConnectorBotSummaryEntityListing**](BotConnectorBotSummaryEntityListing.html) get_integrations_botconnector_integration_id_bots_summaries(integration_id, page_number=page_number, page_size=page_size)



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
{: class="table table-striped"}

### Return type

[**BotConnectorBotSummaryEntityListing**](BotConnectorBotSummaryEntityListing.html)

<a name="get_integrations_clientapps"></a>

## [**ClientAppEntityListing**](ClientAppEntityListing.html) get_integrations_clientapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



List permitted client app integrations for the logged in user



Wraps GET /api/v2/integrations/clientapps 

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
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**ClientAppEntityListing**](ClientAppEntityListing.html)

<a name="get_integrations_clientapps_unifiedcommunications"></a>

## [**UCIntegrationListing**](UCIntegrationListing.html) get_integrations_clientapps_unifiedcommunications(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



UC integration client application configuration.

This endpoint returns basic UI configuration data for all Unified Communications integrations client applications enabled for the current organization.

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
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**UCIntegrationListing**](UCIntegrationListing.html)

<a name="get_integrations_credential"></a>

## [**Credential**](Credential.html) get_integrations_credential(credential_id)



Get a single credential with sensitive fields redacted



Wraps GET /api/v2/integrations/credentials/{credentialId} 

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
{: class="table table-striped"}

### Return type

[**Credential**](Credential.html)

<a name="get_integrations_credentials"></a>

## [**CredentialInfoListing**](CredentialInfoListing.html) get_integrations_credentials(page_number=page_number, page_size=page_size)



List multiple sets of credentials



Wraps GET /api/v2/integrations/credentials 

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
{: class="table table-striped"}

### Return type

[**CredentialInfoListing**](CredentialInfoListing.html)

<a name="get_integrations_credentials_types"></a>

## [**CredentialTypeListing**](CredentialTypeListing.html) get_integrations_credentials_types()



List all credential types



Wraps GET /api/v2/integrations/credentials/types 

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

[**CredentialTypeListing**](CredentialTypeListing.html)

<a name="get_integrations_eventlog"></a>

## [**IntegrationEventEntityListing**](IntegrationEventEntityListing.html) get_integrations_eventlog(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, entity_id=entity_id)



List all events



Wraps GET /api/v2/integrations/eventlog 

Requires ANY permissions: 

* integrations:integration:view
* bridge:notification:view

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
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'timestamp' # str | Sort by (optional) (default to timestamp)
sort_order = 'descending' # str | Order by (optional) (default to descending)
entity_id = 'entity_id_example' # str | Include only events with this entity ID (optional)

try:
    # List all events
    api_response = api_instance.get_integrations_eventlog(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, entity_id=entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_eventlog: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to timestamp] |
| **sort_order** | **str**| Order by | [optional] [default to descending] |
| **entity_id** | **str**| Include only events with this entity ID | [optional]  |
{: class="table table-striped"}

### Return type

[**IntegrationEventEntityListing**](IntegrationEventEntityListing.html)

<a name="get_integrations_eventlog_event_id"></a>

## [**IntegrationEvent**](IntegrationEvent.html) get_integrations_eventlog_event_id(event_id)



Get a single event



Wraps GET /api/v2/integrations/eventlog/{eventId} 

Requires ANY permissions: 

* integrations:integration:view
* bridge:notification:view

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
event_id = 'event_id_example' # str | Event Id

try:
    # Get a single event
    api_response = api_instance.get_integrations_eventlog_event_id(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations_eventlog_event_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **event_id** | **str**| Event Id |  |
{: class="table table-striped"}

### Return type

[**IntegrationEvent**](IntegrationEvent.html)

<a name="get_integrations_speech_dialogflow_agent"></a>

## [**DialogflowAgent**](DialogflowAgent.html) get_integrations_speech_dialogflow_agent(agent_id)



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
{: class="table table-striped"}

### Return type

[**DialogflowAgent**](DialogflowAgent.html)

<a name="get_integrations_speech_dialogflow_agents"></a>

## [**DialogflowAgentSummaryEntityListing**](DialogflowAgentSummaryEntityListing.html) get_integrations_speech_dialogflow_agents(page_number=page_number, page_size=page_size, name=name)



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
{: class="table table-striped"}

### Return type

[**DialogflowAgentSummaryEntityListing**](DialogflowAgentSummaryEntityListing.html)

<a name="get_integrations_speech_lex_bot_alias"></a>

## [**LexBotAlias**](LexBotAlias.html) get_integrations_speech_lex_bot_alias(alias_id)



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
{: class="table table-striped"}

### Return type

[**LexBotAlias**](LexBotAlias.html)

<a name="get_integrations_speech_lex_bot_bot_id_aliases"></a>

## [**LexBotAliasEntityListing**](LexBotAliasEntityListing.html) get_integrations_speech_lex_bot_bot_id_aliases(bot_id, page_number=page_number, page_size=page_size, status=status, name=name)



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
{: class="table table-striped"}

### Return type

[**LexBotAliasEntityListing**](LexBotAliasEntityListing.html)

<a name="get_integrations_speech_lex_bots"></a>

## [**LexBotEntityListing**](LexBotEntityListing.html) get_integrations_speech_lex_bots(page_number=page_number, page_size=page_size, name=name)



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
{: class="table table-striped"}

### Return type

[**LexBotEntityListing**](LexBotEntityListing.html)

<a name="get_integrations_speech_tts_engine"></a>

## [**TtsEngineEntity**](TtsEngineEntity.html) get_integrations_speech_tts_engine(engine_id, include_voices=include_voices)



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
include_voices = false # bool | Include voices for the engine (optional) (default to false)

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
| **include_voices** | **bool**| Include voices for the engine | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**TtsEngineEntity**](TtsEngineEntity.html)

<a name="get_integrations_speech_tts_engine_voice"></a>

## [**TtsVoiceEntity**](TtsVoiceEntity.html) get_integrations_speech_tts_engine_voice(engine_id, voice_id)



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
{: class="table table-striped"}

### Return type

[**TtsVoiceEntity**](TtsVoiceEntity.html)

<a name="get_integrations_speech_tts_engine_voices"></a>

## [**TtsVoiceEntityListing**](TtsVoiceEntityListing.html) get_integrations_speech_tts_engine_voices(engine_id, page_number=page_number, page_size=page_size)



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
{: class="table table-striped"}

### Return type

[**TtsVoiceEntityListing**](TtsVoiceEntityListing.html)

<a name="get_integrations_speech_tts_engines"></a>

## [**TtsEngineEntityListing**](TtsEngineEntityListing.html) get_integrations_speech_tts_engines(page_number=page_number, page_size=page_size, include_voices=include_voices, name=name, language=language)



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
include_voices = false # bool | Include voices for the engine (optional) (default to false)
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
| **include_voices** | **bool**| Include voices for the engine | [optional] [default to false] |
| **name** | **str**| Filter on engine name | [optional]  |
| **language** | **str**| Filter on supported language. If includeVoices=true then the voices are also filtered. | [optional]  |
{: class="table table-striped"}

### Return type

[**TtsEngineEntityListing**](TtsEngineEntityListing.html)

<a name="get_integrations_speech_tts_settings"></a>

## [**TtsSettings**](TtsSettings.html) get_integrations_speech_tts_settings()



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

[**TtsSettings**](TtsSettings.html)

<a name="get_integrations_type"></a>

## [**IntegrationType**](IntegrationType.html) get_integrations_type(type_id)



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
{: class="table table-striped"}

### Return type

[**IntegrationType**](IntegrationType.html)

<a name="get_integrations_type_configschema"></a>

## [**JsonSchemaDocument**](JsonSchemaDocument.html) get_integrations_type_configschema(type_id, config_type)



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
{: class="table table-striped"}

### Return type

[**JsonSchemaDocument**](JsonSchemaDocument.html)

<a name="get_integrations_types"></a>

## [**IntegrationTypeEntityListing**](IntegrationTypeEntityListing.html) get_integrations_types(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



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
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**IntegrationTypeEntityListing**](IntegrationTypeEntityListing.html)

<a name="get_integrations_userapps"></a>

## [**UserAppEntityListing**](UserAppEntityListing.html) get_integrations_userapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, app_host=app_host)



List permitted user app integrations for the logged in user



Wraps GET /api/v2/integrations/userapps 

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
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **app_host** | **str**| The type of UserApp to filter by | [optional]  |
{: class="table table-striped"}

### Return type

[**UserAppEntityListing**](UserAppEntityListing.html)

<a name="patch_integration"></a>

## [**Integration**](Integration.html) patch_integration(integration_id, body=body, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



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
body = PureCloudPlatformClientV2.Integration() # Integration | Integration Update (optional)
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Update an integration.
    api_response = api_instance.patch_integration(integration_id, body=body, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->patch_integration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |
| **body** | [**Integration**](Integration.html)| Integration Update | [optional]  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**Integration**](Integration.html)

<a name="patch_integrations_action"></a>

## [**Action**](Action.html) patch_integrations_action(action_id, body)



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
| **body** | [**UpdateActionInput**](UpdateActionInput.html)| Input used to patch the Action. |  |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="patch_integrations_action_draft"></a>

## [**Action**](Action.html) patch_integrations_action_draft(action_id, body)



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
| **body** | [**UpdateDraftInput**](UpdateDraftInput.html)| Input used to patch the Action Draft. |  |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="post_integrations"></a>

## [**Integration**](Integration.html) post_integrations(body=body)



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
| **body** | [**CreateIntegrationRequest**](CreateIntegrationRequest.html)| Integration | [optional]  |
{: class="table table-striped"}

### Return type

[**Integration**](Integration.html)

<a name="post_integrations_action_draft"></a>

## [**Action**](Action.html) post_integrations_action_draft(action_id)



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
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="post_integrations_action_draft_publish"></a>

## [**Action**](Action.html) post_integrations_action_draft_publish(action_id, body)



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
| **body** | [**PublishDraftInput**](PublishDraftInput.html)| Input used to patch the Action. |  |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="post_integrations_action_draft_test"></a>

## [**TestExecutionResult**](TestExecutionResult.html) post_integrations_action_draft_test(action_id, body)



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

try:
    # Test the execution of a draft. Responses will show execution steps broken out with intermediate results to help in debugging.
    api_response = api_instance.post_integrations_action_draft_test(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_draft_test: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | **object**| Map of parameters used for variable substitution. |  |
{: class="table table-striped"}

### Return type

[**TestExecutionResult**](TestExecutionResult.html)

<a name="post_integrations_action_execute"></a>

## object** post_integrations_action_execute(action_id, body)



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

try:
    # Execute Action and return response from 3rd party.  Responses will follow the schemas defined on the Action for success and error.
    api_response = api_instance.post_integrations_action_execute(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_execute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | **object**| Map of parameters used for variable substitution. |  |
{: class="table table-striped"}

### Return type

**object**

<a name="post_integrations_action_test"></a>

## [**TestExecutionResult**](TestExecutionResult.html) post_integrations_action_test(action_id, body)



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

try:
    # Test the execution of an action. Responses will show execution steps broken out with intermediate results to help in debugging.
    api_response = api_instance.post_integrations_action_test(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_action_test: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | **object**| Map of parameters used for variable substitution. |  |
{: class="table table-striped"}

### Return type

[**TestExecutionResult**](TestExecutionResult.html)

<a name="post_integrations_actions"></a>

## [**Action**](Action.html) post_integrations_actions(body)



Create a new Action



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
    # Create a new Action
    api_response = api_instance.post_integrations_actions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_actions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PostActionInput**](PostActionInput.html)| Input used to create Action. |  |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="post_integrations_actions_drafts"></a>

## [**Action**](Action.html) post_integrations_actions_drafts(body)



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
| **body** | [**PostActionInput**](PostActionInput.html)| Input used to create Action Draft. |  |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="post_integrations_credentials"></a>

## [**CredentialInfo**](CredentialInfo.html) post_integrations_credentials(body=body)



Create a set of credentials



Wraps POST /api/v2/integrations/credentials 

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
| **body** | [**Credential**](Credential.html)| Credential | [optional]  |
{: class="table table-striped"}

### Return type

[**CredentialInfo**](CredentialInfo.html)

<a name="post_integrations_workforcemanagement_vendorconnection"></a>

## [**UserActionCategoryEntityListing**](UserActionCategoryEntityListing.html) post_integrations_workforcemanagement_vendorconnection(body=body)



Add a vendor connection



Wraps POST /api/v2/integrations/workforcemanagement/vendorconnection 

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
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.VendorConnectionRequest() # VendorConnectionRequest |  (optional)

try:
    # Add a vendor connection
    api_response = api_instance.post_integrations_workforcemanagement_vendorconnection(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integrations_workforcemanagement_vendorconnection: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**VendorConnectionRequest**](VendorConnectionRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**UserActionCategoryEntityListing**](UserActionCategoryEntityListing.html)

<a name="put_integration_config_current"></a>

## [**IntegrationConfiguration**](IntegrationConfiguration.html) put_integration_config_current(integration_id, body=body)



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
| **body** | [**IntegrationConfiguration**](IntegrationConfiguration.html)| Integration Configuration | [optional]  |
{: class="table table-striped"}

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.html)

<a name="put_integrations_botconnector_integration_id_bots"></a>

##  put_integrations_botconnector_integration_id_bots(integration_id, bot_list)



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
| **bot_list** | [**BotList**](BotList.html)|  |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="put_integrations_credential"></a>

## [**CredentialInfo**](CredentialInfo.html) put_integrations_credential(credential_id, body=body)



Update a set of credentials



Wraps PUT /api/v2/integrations/credentials/{credentialId} 

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
| **body** | [**Credential**](Credential.html)| Credential | [optional]  |
{: class="table table-striped"}

### Return type

[**CredentialInfo**](CredentialInfo.html)

<a name="put_integrations_speech_tts_settings"></a>

## [**TtsSettings**](TtsSettings.html) put_integrations_speech_tts_settings(body)



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
| **body** | [**TtsSettings**](TtsSettings.html)| Updated TtsSettings |  |
{: class="table table-striped"}

### Return type

[**TtsSettings**](TtsSettings.html)

