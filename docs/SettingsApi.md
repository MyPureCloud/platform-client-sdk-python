# SettingsApi

## PureCloudPlatformClientV2.SettingsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_emails_settings_threading**](#delete_emails_settings_threading) | Reset email threading settings to default|
|[**delete_externalcontacts_settings**](#delete_externalcontacts_settings) | Delete settings|
|[**delete_users_agentui_agents_autoanswer_agent_id_settings**](#delete_users_agentui_agents_autoanswer_agent_id_settings) | Delete agent auto answer settings|
|[**get_emails_settings**](#get_emails_settings) | Get email Contact Center settings|
|[**get_emails_settings_threading**](#get_emails_settings_threading) | Get email threading settings|
|[**get_externalcontacts_settings**](#get_externalcontacts_settings) | Get settings|
|[**get_settings_executiondata**](#get_settings_executiondata) | Get the execution history enabled setting.|
|[**get_users_agentui_agents_autoanswer_agent_id_settings**](#get_users_agentui_agents_autoanswer_agent_id_settings) | Get agent auto answer settings|
|[**patch_emails_settings**](#patch_emails_settings) | Patch email Contact Center settings|
|[**patch_emails_settings_threading**](#patch_emails_settings_threading) | Patch email threading settings|
|[**patch_settings_executiondata**](#patch_settings_executiondata) | Edit the execution history on off setting.|
|[**patch_users_agentui_agents_autoanswer_agent_id_settings**](#patch_users_agentui_agents_autoanswer_agent_id_settings) | Update agent auto answer settings|
|[**put_externalcontacts_settings**](#put_externalcontacts_settings) | Set settings|
|[**put_users_agentui_agents_autoanswer_agent_id_settings**](#put_users_agentui_agents_autoanswer_agent_id_settings) | Set agent auto answer settings|



## delete_emails_settings_threading

>  delete_emails_settings_threading()


Reset email threading settings to default

Wraps DELETE /api/v2/emails/settings/threading 

Requires ANY permissions: 

* conversation:emailThreadingSettings:edit

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
    # Reset email threading settings to default
    api_instance.delete_emails_settings_threading()
except ApiException as e:
    print("Exception when calling SettingsApi->delete_emails_settings_threading: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_externalcontacts_settings

> [**UpdatedSettingsResponse**](UpdatedSettingsResponse) delete_externalcontacts_settings()


Delete settings

Wraps DELETE /api/v2/externalcontacts/settings 

Requires ANY permissions: 

* externalContacts:settings:delete

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
    # Delete settings
    api_response = api_instance.delete_externalcontacts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->delete_externalcontacts_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**UpdatedSettingsResponse**](UpdatedSettingsResponse)


## delete_users_agentui_agents_autoanswer_agent_id_settings

>  delete_users_agentui_agents_autoanswer_agent_id_settings(agent_id)


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

### Return type

void (empty response body)


## get_emails_settings

> [**EmailSettings**](EmailSettings) get_emails_settings()


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

[**EmailSettings**](EmailSettings)


## get_emails_settings_threading

> [**EmailThreadingSettings**](EmailThreadingSettings) get_emails_settings_threading()


Get email threading settings

Wraps GET /api/v2/emails/settings/threading 

Requires ANY permissions: 

* conversation:emailThreadingSettings:view

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
    # Get email threading settings
    api_response = api_instance.get_emails_settings_threading()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_emails_settings_threading: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**EmailThreadingSettings**](EmailThreadingSettings)


## get_externalcontacts_settings

> [**ExternalContactsSettings**](ExternalContactsSettings) get_externalcontacts_settings()


Get settings

Wraps GET /api/v2/externalcontacts/settings 

Requires ANY permissions: 

* externalContacts:settings:view

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
    # Get settings
    api_response = api_instance.get_externalcontacts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_externalcontacts_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ExternalContactsSettings**](ExternalContactsSettings)


## get_settings_executiondata

> [**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse) get_settings_executiondata()


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

[**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse)


## get_users_agentui_agents_autoanswer_agent_id_settings

> [**AutoAnswerSettings**](AutoAnswerSettings) get_users_agentui_agents_autoanswer_agent_id_settings(agent_id)


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

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings)


## patch_emails_settings

> [**EmailSettings**](EmailSettings) patch_emails_settings(body=body)


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
| **body** | [**EmailSettings**](EmailSettings)|  | [optional]  |

### Return type

[**EmailSettings**](EmailSettings)


## patch_emails_settings_threading

> [**EmailThreadingSettings**](EmailThreadingSettings) patch_emails_settings_threading(body=body)


Patch email threading settings

Wraps PATCH /api/v2/emails/settings/threading 

Requires ANY permissions: 

* conversation:emailThreadingSettings:edit

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
body = PureCloudPlatformClientV2.EmailThreadingSettings() # EmailThreadingSettings |  (optional)

try:
    # Patch email threading settings
    api_response = api_instance.patch_emails_settings_threading(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->patch_emails_settings_threading: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmailThreadingSettings**](EmailThreadingSettings)|  | [optional]  |

### Return type

[**EmailThreadingSettings**](EmailThreadingSettings)


## patch_settings_executiondata

> [**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse) patch_settings_executiondata(body)


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
| **body** | [**ExecutionDataSettingsRequest**](ExecutionDataSettingsRequest)| New Execution Data Setting |  |

### Return type

[**ExecutionDataGlobalSettingsResponse**](ExecutionDataGlobalSettingsResponse)


## patch_users_agentui_agents_autoanswer_agent_id_settings

> [**AutoAnswerSettings**](AutoAnswerSettings) patch_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)


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
| **body** | [**AutoAnswerSettings**](AutoAnswerSettings)| AutoAnswerSettings |  |

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings)


## put_externalcontacts_settings

> [**UpdatedSettingsResponse**](UpdatedSettingsResponse) put_externalcontacts_settings(body=body)


Set settings

Wraps PUT /api/v2/externalcontacts/settings 

Requires ANY permissions: 

* externalContacts:settings:edit

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
body = PureCloudPlatformClientV2.ExternalContactsSettings() # ExternalContactsSettings |  (optional)

try:
    # Set settings
    api_response = api_instance.put_externalcontacts_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->put_externalcontacts_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalContactsSettings**](ExternalContactsSettings)|  | [optional]  |

### Return type

[**UpdatedSettingsResponse**](UpdatedSettingsResponse)


## put_users_agentui_agents_autoanswer_agent_id_settings

> [**AutoAnswerSettings**](AutoAnswerSettings) put_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)


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
| **body** | [**AutoAnswerSettings**](AutoAnswerSettings)| AutoAnswerSettings |  |

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings)


_PureCloudPlatformClientV2 248.0.0_
