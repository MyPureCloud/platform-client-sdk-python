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
|[**get_integrations_clientapps**](IntegrationsApi.html#get_integrations_clientapps) | List permitted client app integrations for the logged in user|
|[**get_integrations_credential**](IntegrationsApi.html#get_integrations_credential) | Get a single credential with sensitive fields redacted|
|[**get_integrations_credentials**](IntegrationsApi.html#get_integrations_credentials) | List multiple sets of credentials|
|[**get_integrations_credentials_types**](IntegrationsApi.html#get_integrations_credentials_types) | List all credential types|
|[**get_integrations_eventlog**](IntegrationsApi.html#get_integrations_eventlog) | List all events|
|[**get_integrations_eventlog_event_id**](IntegrationsApi.html#get_integrations_eventlog_event_id) | Get a single event|
|[**get_integrations_type**](IntegrationsApi.html#get_integrations_type) | Get integration type.|
|[**get_integrations_type_configschema**](IntegrationsApi.html#get_integrations_type_configschema) | Get properties config schema for an integration type.|
|[**get_integrations_types**](IntegrationsApi.html#get_integrations_types) | List integration types|
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
|[**put_integrations_credential**](IntegrationsApi.html#put_integrations_credential) | Update a set of credentials|
{: class="table table-striped"}

<a name="delete_integration"></a>

## [**Integration**](Integration.html) delete_integration(integration_id)



Delete integration.



Wraps DELETE /api/v2/integrations/{integrationId} 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id

try:
    # Delete integration.
    api_response = api_instance.delete_integration(integration_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->delete_integration: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Delete an Action
    api_instance.delete_integrations_action(action_id)
except ApiException as e:
    print "Exception when calling IntegrationsApi->delete_integrations_action: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Delete a Draft
    api_instance.delete_integrations_action_draft(action_id)
except ApiException as e:
    print "Exception when calling IntegrationsApi->delete_integrations_action_draft: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
credential_id = 'credential_id_example' # str | Credential ID

try:
    # Delete a set of credentials
    api_instance.delete_integrations_credential(credential_id)
except ApiException as e:
    print "Exception when calling IntegrationsApi->delete_integrations_credential: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integration: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
integration_id = 'integration_id_example' # str | Integration Id

try:
    # Get integration configuration.
    api_response = api_instance.get_integration_config_current(integration_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integration_config_current: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations: %s\n" % e
~~~

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

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
expand = 'expand_example' # str | Indicates fields of the response which should be expanded. (optional)
include_config = false # bool | Show config when available (optional) (default to false)

try:
    # Retrieves a single Action matching id.
    api_response = api_instance.get_integrations_action(action_id, expand=expand, include_config=include_config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_action: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **expand** | **str**| Indicates fields of the response which should be expanded. | [optional] <br />**Values**: contract |
| **include_config** | **bool**| Show config when available | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="get_integrations_action_draft"></a>

## [**Action**](Action.html) get_integrations_action_draft(action_id, expand=expand, include_config=include_config)



Retrieve a Draft



Wraps GET /api/v2/integrations/actions/{actionId}/draft 

Requires ANY permissions: 

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId
expand = 'expand_example' # str | Indicates fields of the response which should be expanded. (optional)
include_config = false # bool | Show config when available (optional) (default to false)

try:
    # Retrieve a Draft
    api_response = api_instance.get_integrations_action_draft(action_id, expand=expand, include_config=include_config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_action_draft: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **expand** | **str**| Indicates fields of the response which should be expanded. | [optional] <br />**Values**: contract |
| **include_config** | **bool**| Show config when available | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**Action**](Action.html)

<a name="get_integrations_action_draft_schema"></a>

## [**JsonSchemaDocument**](JsonSchemaDocument.html) get_integrations_action_draft_schema(action_id, file_name)



Retrieve schema for a Draft based on filename.



Wraps GET /api/v2/integrations/actions/{actionId}/draft/schemas/{fileName} 

Requires ANY permissions: 

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_action_draft_schema: %s\n" % e
~~~

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

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_action_draft_template: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Validate current Draft configuration.
    api_response = api_instance.get_integrations_action_draft_validation(action_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_action_draft_validation: %s\n" % e
~~~

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

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_action_schema: %s\n" % e
~~~

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

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_action_template: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **file_name** | **str**| Name of template file to be retrieved for this action. |  |
{: class="table table-striped"}

### Return type

**str**

<a name="get_integrations_actions"></a>

## [**ActionEntityListing**](ActionEntityListing.html) get_integrations_actions(category=category, secure=secure, include_auth_actions=include_auth_actions, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



Retrieves all actions associated with filters passed in via query param.



Wraps GET /api/v2/integrations/actions 

Requires ANY permissions: 

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
category = 'category_example' # str | Filter by category name (optional)
secure = 'secure_example' # str | Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. (optional)
include_auth_actions = 'include_auth_actions_example' # str | Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. (optional)
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Retrieves all actions associated with filters passed in via query param.
    api_response = api_instance.get_integrations_actions(category=category, secure=secure, include_auth_actions=include_auth_actions, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_actions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category** | **str**| Filter by category name | [optional]  |
| **secure** | **str**| Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
| **include_auth_actions** | **str**| Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. | [optional] <br />**Values**: true, false |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionEntityListing**](ActionEntityListing.html)

<a name="get_integrations_actions_categories"></a>

## [**CategoryEntityListing**](CategoryEntityListing.html) get_integrations_actions_categories(secure=secure, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



Retrieves all categories of available Actions



Wraps GET /api/v2/integrations/actions/categories 

Requires ANY permissions: 

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
secure = 'secure_example' # str | Filter to only include/exclude Action categories based on if they are considered secure. True will only include categories with Actions marked secured. False will only include categories of unsecured Actions. (optional)
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Retrieves all categories of available Actions
    api_response = api_instance.get_integrations_actions_categories(secure=secure, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_actions_categories: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **secure** | **str**| Filter to only include/exclude Action categories based on if they are considered secure. True will only include categories with Actions marked secured. False will only include categories of unsecured Actions. | [optional] <br />**Values**: true, false |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**CategoryEntityListing**](CategoryEntityListing.html)

<a name="get_integrations_actions_drafts"></a>

## [**ActionEntityListing**](ActionEntityListing.html) get_integrations_actions_drafts(category=category, secure=secure, include_auth_actions=include_auth_actions, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



Retrieves all action drafts associated with the filters passed in via query param.



Wraps GET /api/v2/integrations/actions/drafts 

Requires ANY permissions: 

* integrations:action:view* bridge:actions:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
category = 'category_example' # str | Filter by category name (optional)
secure = 'secure_example' # str | Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. (optional)
include_auth_actions = 'include_auth_actions_example' # str | Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. (optional)
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Retrieves all action drafts associated with the filters passed in via query param.
    api_response = api_instance.get_integrations_actions_drafts(category=category, secure=secure, include_auth_actions=include_auth_actions, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_actions_drafts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category** | **str**| Filter by category name | [optional]  |
| **secure** | **str**| Filter to only include secure actions. True will only include actions marked secured. False will include only unsecure actions. Do not use filter if you want all Actions. | [optional] <br />**Values**: true, false |
| **include_auth_actions** | **str**| Whether or not to include authentication actions in the response. These actions are not directly executable. Some integrations create them and will run them as needed to refresh authentication information for other actions. | [optional] <br />**Values**: true, false |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionEntityListing**](ActionEntityListing.html)

<a name="get_integrations_clientapps"></a>

## [**ClientAppEntityListing**](ClientAppEntityListing.html) get_integrations_clientapps(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



List permitted client app integrations for the logged in user



Wraps GET /api/v2/integrations/clientapps 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_clientapps: %s\n" % e
~~~

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

<a name="get_integrations_credential"></a>

## [**Credential**](Credential.html) get_integrations_credential(credential_id)



Get a single credential with sensitive fields redacted



Wraps GET /api/v2/integrations/credentials/{credentialId} 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
credential_id = 'credential_id_example' # str | Credential ID

try:
    # Get a single credential with sensitive fields redacted
    api_response = api_instance.get_integrations_credential(credential_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_credential: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_credentials: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()

try:
    # List all credential types
    api_response = api_instance.get_integrations_credentials_types()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_credentials_types: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**CredentialTypeListing**](CredentialTypeListing.html)

<a name="get_integrations_eventlog"></a>

## [**IntegrationEventEntityListing**](IntegrationEventEntityListing.html) get_integrations_eventlog(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, entity_id=entity_id)



List all events



Wraps GET /api/v2/integrations/eventlog 

Requires ANY permissions: 

* integrations:integration:view* bridge:notification:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_eventlog: %s\n" % e
~~~

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

* integrations:integration:view* bridge:notification:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
event_id = 'event_id_example' # str | Event Id

try:
    # Get a single event
    api_response = api_instance.get_integrations_eventlog_event_id(event_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_eventlog_event_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **event_id** | **str**| Event Id |  |
{: class="table table-striped"}

### Return type

[**IntegrationEvent**](IntegrationEvent.html)

<a name="get_integrations_type"></a>

## [**IntegrationType**](IntegrationType.html) get_integrations_type(type_id)



Get integration type.



Wraps GET /api/v2/integrations/types/{typeId} 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
type_id = 'type_id_example' # str | Integration Type Id

try:
    # Get integration type.
    api_response = api_instance.get_integrations_type(type_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integrations_type: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_type_configschema: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->get_integrations_types: %s\n" % e
~~~

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

<a name="patch_integration"></a>

## [**Integration**](Integration.html) patch_integration(integration_id, body=body, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



Update an integration.



Wraps PATCH /api/v2/integrations/{integrationId} 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->patch_integration: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->patch_integrations_action: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->patch_integrations_action_draft: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.CreateIntegrationRequest() # CreateIntegrationRequest | Integration (optional)

try:
    # Create an integration.
    api_response = api_instance.post_integrations(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->post_integrations: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
action_id = 'action_id_example' # str | actionId

try:
    # Create a new Draft from existing Action
    api_response = api_instance.post_integrations_action_draft(action_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->post_integrations_action_draft: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->post_integrations_action_draft_publish: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->post_integrations_action_draft_test: %s\n" % e
~~~

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

* integrations:action:execute* bridge:actions:execute

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->post_integrations_action_execute: %s\n" % e
~~~

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

* integrations:action:execute* bridge:actions:execute

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->post_integrations_action_test: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.PostActionInput() # PostActionInput | Input used to create Action.

try:
    # Create a new Action
    api_response = api_instance.post_integrations_actions(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->post_integrations_actions: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.PostActionInput() # PostActionInput | Input used to create Action Draft.

try:
    # Create a new Draft
    api_response = api_instance.post_integrations_actions_drafts(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->post_integrations_actions_drafts: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.Credential() # Credential | Credential (optional)

try:
    # Create a set of credentials
    api_response = api_instance.post_integrations_credentials(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->post_integrations_credentials: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntegrationsApi()
body = PureCloudPlatformClientV2.VendorConnectionRequest() # VendorConnectionRequest |  (optional)

try:
    # Add a vendor connection
    api_response = api_instance.post_integrations_workforcemanagement_vendorconnection(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->post_integrations_workforcemanagement_vendorconnection: %s\n" % e
~~~

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

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->put_integration_config_current: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration Id |  |
| **body** | [**IntegrationConfiguration**](IntegrationConfiguration.html)| Integration Configuration | [optional]  |
{: class="table table-striped"}

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.html)

<a name="put_integrations_credential"></a>

## [**CredentialInfo**](CredentialInfo.html) put_integrations_credential(credential_id, body=body)



Update a set of credentials



Wraps PUT /api/v2/integrations/credentials/{credentialId} 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling IntegrationsApi->put_integrations_credential: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **credential_id** | **str**| Credential ID |  |
| **body** | [**Credential**](Credential.html)| Credential | [optional]  |
{: class="table table-striped"}

### Return type

[**CredentialInfo**](CredentialInfo.html)

