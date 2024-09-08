---
title: SettingsApi
---

## PureCloudPlatformClientV2.SettingsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_users_agentui_agents_autoanswer_agent_id_settings**](SettingsApi.html#delete_users_agentui_agents_autoanswer_agent_id_settings) | Delete agent auto answer settings|
|[**get_emails_settings**](SettingsApi.html#get_emails_settings) | Get email Contact Center settings|
|[**get_settings_executiondata**](SettingsApi.html#get_settings_executiondata) | Get the execution history enabled setting.|
|[**get_users_agentui_agents_autoanswer_agent_id_settings**](SettingsApi.html#get_users_agentui_agents_autoanswer_agent_id_settings) | Get agent auto answer settings|
|[**patch_emails_settings**](SettingsApi.html#patch_emails_settings) | Patch email Contact Center settings|
|[**patch_settings_executiondata**](SettingsApi.html#patch_settings_executiondata) | Edit the execution history on off setting.|
|[**patch_users_agentui_agents_autoanswer_agent_id_settings**](SettingsApi.html#patch_users_agentui_agents_autoanswer_agent_id_settings) | Update agent auto answer settings|
|[**put_users_agentui_agents_autoanswer_agent_id_settings**](SettingsApi.html#put_users_agentui_agents_autoanswer_agent_id_settings) | Set agent auto answer settings|
{: class="table table-striped"}

<a name="delete_users_agentui_agents_autoanswer_agent_id_settings"></a>

##  delete_users_agentui_agents_autoanswer_agent_id_settings(agent_id)



Delete agent auto answer settings

Wraps DELETE /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to

try:
    # Delete agent auto answer settings
    api_instance.delete_users_agentui_agents_autoanswer_agent_id_settings(agent_id)
except ApiException as e:
    print("Exception when calling SettingsApi->delete_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_emails_settings"></a>

## [**EmailSettings**](EmailSettings.html) get_emails_settings()



Get email Contact Center settings

Wraps GET /api/v2/emails/settings 

Requires ANY permissions: 

* conversation:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()

try:
    # Get email Contact Center settings
    api_response = api_instance.get_emails_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_emails_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EmailSettings**](EmailSettings.html)

<a name="get_settings_executiondata"></a>

## [**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse.html) get_settings_executiondata()



Get the execution history enabled setting.

Get the execution history enabled setting.

Wraps GET /api/v2/settings/executiondata 

Requires ANY permissions: 

* settings:executiondata:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()

try:
    # Get the execution history enabled setting.
    api_response = api_instance.get_settings_executiondata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings_executiondata: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse.html)

<a name="get_users_agentui_agents_autoanswer_agent_id_settings"></a>

## [**AutoAnswerSettings**](AutoAnswerSettings.html) get_users_agentui_agents_autoanswer_agent_id_settings(agent_id)



Get agent auto answer settings

Wraps GET /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to

try:
    # Get agent auto answer settings
    api_response = api_instance.get_users_agentui_agents_autoanswer_agent_id_settings(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |
{: class="table table-striped"}

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings.html)

<a name="patch_emails_settings"></a>

## [**EmailSettings**](EmailSettings.html) patch_emails_settings(body=body)



Patch email Contact Center settings

Wraps PATCH /api/v2/emails/settings 

Requires ANY permissions: 

* conversation:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()
body = PureCloudPlatformClientV2.EmailSettings() # EmailSettings |  (optional)

try:
    # Patch email Contact Center settings
    api_response = api_instance.patch_emails_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->patch_emails_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmailSettings**](EmailSettings.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**EmailSettings**](EmailSettings.html)

<a name="patch_settings_executiondata"></a>

## [**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse.html) patch_settings_executiondata(body)



Edit the execution history on off setting.

Edit the execution history on off setting.

Wraps PATCH /api/v2/settings/executiondata 

Requires ANY permissions: 

* settings:executiondata:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()
body = PureCloudPlatformClientV2.ExecutionDataSettingsRequest() # ExecutionDataSettingsRequest | New Execution Data Setting

try:
    # Edit the execution history on off setting.
    api_response = api_instance.patch_settings_executiondata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->patch_settings_executiondata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExecutionDataSettingsRequest**](ExecutionDataSettingsRequest.html)| New Execution Data Setting |  |
{: class="table table-striped"}

### Return type

[**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse.html)

<a name="patch_users_agentui_agents_autoanswer_agent_id_settings"></a>

## [**AutoAnswerSettings**](AutoAnswerSettings.html) patch_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)



Update agent auto answer settings

Wraps PATCH /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to
body = PureCloudPlatformClientV2.AutoAnswerSettings() # AutoAnswerSettings | AutoAnswerSettings

try:
    # Update agent auto answer settings
    api_response = api_instance.patch_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->patch_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |
| **body** | [**AutoAnswerSettings**](AutoAnswerSettings.html)| AutoAnswerSettings |  |
{: class="table table-striped"}

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings.html)

<a name="put_users_agentui_agents_autoanswer_agent_id_settings"></a>

## [**AutoAnswerSettings**](AutoAnswerSettings.html) put_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)



Set agent auto answer settings

Wraps PUT /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SettingsApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to
body = PureCloudPlatformClientV2.AutoAnswerSettings() # AutoAnswerSettings | AutoAnswerSettings

try:
    # Set agent auto answer settings
    api_response = api_instance.put_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->put_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |
| **body** | [**AutoAnswerSettings**](AutoAnswerSettings.html)| AutoAnswerSettings |  |
{: class="table table-striped"}

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings.html)

