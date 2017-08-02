---
title: RoutingApi
---

## PureCloudPlatformClientV2.RoutingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_routing_email_domain**](RoutingApi.html#delete_routing_email_domain) | Delete a domain|
|[**delete_routing_email_domain_route**](RoutingApi.html#delete_routing_email_domain_route) | Delete a route|
|[**delete_routing_queue**](RoutingApi.html#delete_routing_queue) | Delete a queue|
|[**delete_routing_queue_user**](RoutingApi.html#delete_routing_queue_user) | Delete queue member|
|[**delete_routing_queue_wrapupcode**](RoutingApi.html#delete_routing_queue_wrapupcode) | Delete a wrap-up code from a queue|
|[**delete_routing_skill**](RoutingApi.html#delete_routing_skill) | Delete Routing Skill|
|[**delete_routing_utilization**](RoutingApi.html#delete_routing_utilization) | Delete utilization settings and revert to system defaults.|
|[**delete_routing_wrapupcode**](RoutingApi.html#delete_routing_wrapupcode) | Delete wrap-up code|
|[**delete_user_routingskill**](RoutingApi.html#delete_user_routingskill) | Remove routing skill from user|
|[**get_routing_email_domain**](RoutingApi.html#get_routing_email_domain) | Get domain|
|[**get_routing_email_domain_route**](RoutingApi.html#get_routing_email_domain_route) | Get a route|
|[**get_routing_email_domain_routes**](RoutingApi.html#get_routing_email_domain_routes) | Get routes|
|[**get_routing_email_domains**](RoutingApi.html#get_routing_email_domains) | Get domains|
|[**get_routing_email_setup**](RoutingApi.html#get_routing_email_setup) | Get email setup|
|[**get_routing_languages**](RoutingApi.html#get_routing_languages) | Get the list of supported languages.|
|[**get_routing_queue**](RoutingApi.html#get_routing_queue) | Get details about this queue.|
|[**get_routing_queue_estimatedwaittime**](RoutingApi.html#get_routing_queue_estimatedwaittime) | Get Estimated Wait Time|
|[**get_routing_queue_mediatype_estimatedwaittime**](RoutingApi.html#get_routing_queue_mediatype_estimatedwaittime) | Get Estimated Wait Time|
|[**get_routing_queue_users**](RoutingApi.html#get_routing_queue_users) | Get the members of this queue|
|[**get_routing_queue_wrapupcodes**](RoutingApi.html#get_routing_queue_wrapupcodes) | Get the wrap-up codes for a queue|
|[**get_routing_queues**](RoutingApi.html#get_routing_queues) | Get list of queues.|
|[**get_routing_skill**](RoutingApi.html#get_routing_skill) | Get Routing Skill|
|[**get_routing_skills**](RoutingApi.html#get_routing_skills) | Get the list of routing skills.|
|[**get_routing_utilization**](RoutingApi.html#get_routing_utilization) | Get the utilization settings.|
|[**get_routing_wrapupcode**](RoutingApi.html#get_routing_wrapupcode) | Get details about this wrap-up code.|
|[**get_routing_wrapupcodes**](RoutingApi.html#get_routing_wrapupcodes) | Get list of wrapup codes.|
|[**get_user_routingskills**](RoutingApi.html#get_user_routingskills) | List routing skills for user|
|[**patch_routing_queue_user**](RoutingApi.html#patch_routing_queue_user) | Update the ring number of joined status for a User in a Queue|
|[**patch_routing_queue_users**](RoutingApi.html#patch_routing_queue_users) | Join or unjoin a set of users for a queue|
|[**post_analytics_queues_observations_query**](RoutingApi.html#post_analytics_queues_observations_query) | Query for queue observations|
|[**post_routing_email_domain_routes**](RoutingApi.html#post_routing_email_domain_routes) | Create a route|
|[**post_routing_email_domains**](RoutingApi.html#post_routing_email_domains) | Create a domain|
|[**post_routing_languages**](RoutingApi.html#post_routing_languages) | Create Language|
|[**post_routing_queue_users**](RoutingApi.html#post_routing_queue_users) | Bulk add or delete up to 100 queue members|
|[**post_routing_queue_wrapupcodes**](RoutingApi.html#post_routing_queue_wrapupcodes) | Add up to 100 wrap-up codes to a queue|
|[**post_routing_queues**](RoutingApi.html#post_routing_queues) | Create queue|
|[**post_routing_skills**](RoutingApi.html#post_routing_skills) | Create Skill|
|[**post_routing_wrapupcodes**](RoutingApi.html#post_routing_wrapupcodes) | Create a wrap-up code|
|[**post_user_routingskills**](RoutingApi.html#post_user_routingskills) | Add routing skill to user|
|[**put_routing_email_domain_route**](RoutingApi.html#put_routing_email_domain_route) | Update a route|
|[**put_routing_queue**](RoutingApi.html#put_routing_queue) | Update a queue|
|[**put_routing_utilization**](RoutingApi.html#put_routing_utilization) | Update the utilization settings.|
|[**put_routing_wrapupcode**](RoutingApi.html#put_routing_wrapupcode) | Update wrap-up code|
|[**put_user_routingskill**](RoutingApi.html#put_user_routingskill) | Update routing skill proficiency or state.|
{: class="table table-striped"}

<a name="delete_routing_email_domain"></a>

##  delete_routing_email_domain(domain_id)

Delete a domain



Wraps DELETE /api/v2/routing/email/domains/{domainId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Delete a domain
    api_instance.delete_routing_email_domain(domain_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_email_domain: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_email_domain_route"></a>

##  delete_routing_email_domain_route(domain_name, route_id)

Delete a route



Wraps DELETE /api/v2/routing/email/domains/{domainName}/routes/{routeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_name = 'domain_name_example' # str | email domain
route_id = 'route_id_example' # str | route ID

try:
    # Delete a route
    api_instance.delete_routing_email_domain_route(domain_name, route_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_email_domain_route: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **route_id** | **str**| route ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_queue"></a>

##  delete_routing_queue(queue_id, force_delete=force_delete)

Delete a queue



Wraps DELETE /api/v2/routing/queues/{queueId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
force_delete = true # bool | forceDelete (optional)

try:
    # Delete a queue
    api_instance.delete_routing_queue(queue_id, force_delete=force_delete)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_queue: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **force_delete** | **bool**| forceDelete | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_queue_user"></a>

##  delete_routing_queue_user(queue_id, member_id)

Delete queue member



Wraps DELETE /api/v2/routing/queues/{queueId}/users/{memberId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
member_id = 'member_id_example' # str | Member ID

try:
    # Delete queue member
    api_instance.delete_routing_queue_user(queue_id, member_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_queue_user: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **member_id** | **str**| Member ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_queue_wrapupcode"></a>

##  delete_routing_queue_wrapupcode(queue_id, code_id)

Delete a wrap-up code from a queue



Wraps DELETE /api/v2/routing/queues/{queueId}/wrapupcodes/{codeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
code_id = 'code_id_example' # str | Code ID

try:
    # Delete a wrap-up code from a queue
    api_instance.delete_routing_queue_wrapupcode(queue_id, code_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_queue_wrapupcode: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **code_id** | **str**| Code ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_skill"></a>

##  delete_routing_skill(skill_id)

Delete Routing Skill



Wraps DELETE /api/v2/routing/skills/{skillId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
skill_id = 'skill_id_example' # str | Skill ID

try:
    # Delete Routing Skill
    api_instance.delete_routing_skill(skill_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_skill: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_id** | **str**| Skill ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_utilization"></a>

##  delete_routing_utilization()

Delete utilization settings and revert to system defaults.



Wraps DELETE /api/v2/routing/utilization 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Delete utilization settings and revert to system defaults.
    api_instance.delete_routing_utilization()
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_utilization: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_wrapupcode"></a>

##  delete_routing_wrapupcode(code_id)

Delete wrap-up code



Wraps DELETE /api/v2/routing/wrapupcodes/{codeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
code_id = 'code_id_example' # str | Wrapup Code ID

try:
    # Delete wrap-up code
    api_instance.delete_routing_wrapupcode(code_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_routing_wrapupcode: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code_id** | **str**| Wrapup Code ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_routingskill"></a>

##  delete_user_routingskill(user_id, skill_id)

Remove routing skill from user



Wraps DELETE /api/v2/users/{userId}/routingskills/{skillId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
skill_id = 'skill_id_example' # str | skillId

try:
    # Remove routing skill from user
    api_instance.delete_user_routingskill(user_id, skill_id)
except ApiException as e:
    print "Exception when calling RoutingApi->delete_user_routingskill: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_routing_email_domain"></a>

## [**InboundDomain**](InboundDomain.html) get_routing_email_domain(domain_id)

Get domain



Wraps GET /api/v2/routing/email/domains/{domainId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Get domain
    api_response = api_instance.get_routing_email_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_email_domain: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

[**InboundDomain**](InboundDomain.html)

<a name="get_routing_email_domain_route"></a>

## [**InboundRoute**](InboundRoute.html) get_routing_email_domain_route(domain_name, route_id)

Get a route



Wraps GET /api/v2/routing/email/domains/{domainName}/routes/{routeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_name = 'domain_name_example' # str | email domain
route_id = 'route_id_example' # str | route ID

try:
    # Get a route
    api_response = api_instance.get_routing_email_domain_route(domain_name, route_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_email_domain_route: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **route_id** | **str**| route ID |  |
{: class="table table-striped"}

### Return type

[**InboundRoute**](InboundRoute.html)

<a name="get_routing_email_domain_routes"></a>

## [**InboundRouteEntityListing**](InboundRouteEntityListing.html) get_routing_email_domain_routes(domain_name, page_size=page_size, page_number=page_number, pattern=pattern)

Get routes



Wraps GET /api/v2/routing/email/domains/{domainName}/routes 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_name = 'domain_name_example' # str | email domain
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
pattern = 'pattern_example' # str | Filter routes by the route's pattern property (optional)

try:
    # Get routes
    api_response = api_instance.get_routing_email_domain_routes(domain_name, page_size=page_size, page_number=page_number, pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_email_domain_routes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **pattern** | **str**| Filter routes by the route&#39;s pattern property | [optional]  |
{: class="table table-striped"}

### Return type

[**InboundRouteEntityListing**](InboundRouteEntityListing.html)

<a name="get_routing_email_domains"></a>

## [**InboundDomainEntityListing**](InboundDomainEntityListing.html) get_routing_email_domains()

Get domains



Wraps GET /api/v2/routing/email/domains 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get domains
    api_response = api_instance.get_routing_email_domains()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_email_domains: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**InboundDomainEntityListing**](InboundDomainEntityListing.html)

<a name="get_routing_email_setup"></a>

## [**EmailSetup**](EmailSetup.html) get_routing_email_setup()

Get email setup



Wraps GET /api/v2/routing/email/setup 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get email setup
    api_response = api_instance.get_routing_email_setup()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_email_setup: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**EmailSetup**](EmailSetup.html)

<a name="get_routing_languages"></a>

## [**LanguageEntityListing**](LanguageEntityListing.html) get_routing_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)

Get the list of supported languages.



Wraps GET /api/v2/routing/languages 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
name = 'name_example' # str | Name (optional)

try:
    # Get the list of supported languages.
    api_response = api_instance.get_routing_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_languages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
{: class="table table-striped"}

### Return type

[**LanguageEntityListing**](LanguageEntityListing.html)

<a name="get_routing_queue"></a>

## [**Queue**](Queue.html) get_routing_queue(queue_id)

Get details about this queue.



Wraps GET /api/v2/routing/queues/{queueId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID

try:
    # Get details about this queue.
    api_response = api_instance.get_routing_queue(queue_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_queue: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
{: class="table table-striped"}

### Return type

[**Queue**](Queue.html)

<a name="get_routing_queue_estimatedwaittime"></a>

## [**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions.html) get_routing_queue_estimatedwaittime(queue_id, conversation_id=conversation_id)

Get Estimated Wait Time



Wraps GET /api/v2/routing/queues/{queueId}/estimatedwaittime 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | queueId
conversation_id = 'conversation_id_example' # str | conversationId (optional)

try:
    # Get Estimated Wait Time
    api_response = api_instance.get_routing_queue_estimatedwaittime(queue_id, conversation_id=conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_queue_estimatedwaittime: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| queueId |  |
| **conversation_id** | **str**| conversationId | [optional]  |
{: class="table table-striped"}

### Return type

[**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions.html)

<a name="get_routing_queue_mediatype_estimatedwaittime"></a>

## [**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions.html) get_routing_queue_mediatype_estimatedwaittime(queue_id, media_type)

Get Estimated Wait Time



Wraps GET /api/v2/routing/queues/{queueId}/mediatypes/{mediaType}/estimatedwaittime 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | queueId
media_type = 'media_type_example' # str | mediaType

try:
    # Get Estimated Wait Time
    api_response = api_instance.get_routing_queue_mediatype_estimatedwaittime(queue_id, media_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_queue_mediatype_estimatedwaittime: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| queueId |  |
| **media_type** | **str**| mediaType |  |
{: class="table table-striped"}

### Return type

[**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions.html)

<a name="get_routing_queue_users"></a>

## [**QueueMemberEntityListing**](QueueMemberEntityListing.html) get_routing_queue_users(queue_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, joined=joined, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence)

Get the members of this queue



Wraps GET /api/v2/routing/queues/{queueId}/users 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'name' # str | Sort by (optional) (default to name)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
joined = true # bool | Filter by joined status (optional)
name = 'name_example' # str | Filter by queue member name (optional)
profile_skills = ['profile_skills_example'] # list[str] | Filter by profile skill (optional)
skills = ['skills_example'] # list[str] | Filter by skill (optional)
languages = ['languages_example'] # list[str] | Filter by language (optional)
routing_status = ['routing_status_example'] # list[str] | Filter by routing status (optional)
presence = ['presence_example'] # list[str] | Filter by presence (optional)

try:
    # Get the members of this queue
    api_response = api_instance.get_routing_queue_users(queue_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, joined=joined, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_queue_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups, date, geolocationsettings, organization, presencedefinitions, locationdefinitions, orgauthorization, favorites, superiors, directreports, adjacents, routingskills, routinglanguages, fieldconfigs, token, trustors |
| **joined** | **bool**| Filter by joined status | [optional]  |
| **name** | **str**| Filter by queue member name | [optional]  |
| **profile_skills** | [**list[str]**](str.html)| Filter by profile skill | [optional]  |
| **skills** | [**list[str]**](str.html)| Filter by skill | [optional]  |
| **languages** | [**list[str]**](str.html)| Filter by language | [optional]  |
| **routing_status** | [**list[str]**](str.html)| Filter by routing status | [optional]  |
| **presence** | [**list[str]**](str.html)| Filter by presence | [optional]  |
{: class="table table-striped"}

### Return type

[**QueueMemberEntityListing**](QueueMemberEntityListing.html)

<a name="get_routing_queue_wrapupcodes"></a>

## [**WrapupCodeEntityListing**](WrapupCodeEntityListing.html) get_routing_queue_wrapupcodes(queue_id)

Get the wrap-up codes for a queue



Wraps GET /api/v2/routing/queues/{queueId}/wrapupcodes 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID

try:
    # Get the wrap-up codes for a queue
    api_response = api_instance.get_routing_queue_wrapupcodes(queue_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_queue_wrapupcodes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
{: class="table table-striped"}

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing.html)

<a name="get_routing_queues"></a>

## [**QueueEntityListing**](QueueEntityListing.html) get_routing_queues(page_size=page_size, page_number=page_number, sort_by=sort_by, name=name, active=active)

Get list of queues.



Wraps GET /api/v2/routing/queues 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'name' # str | Sort by (optional) (default to name)
name = 'name_example' # str | Name (optional)
active = true # bool | Active (optional)

try:
    # Get list of queues.
    api_response = api_instance.get_routing_queues(page_size=page_size, page_number=page_number, sort_by=sort_by, name=name, active=active)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_queues: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
| **name** | **str**| Name | [optional]  |
| **active** | **bool**| Active | [optional]  |
{: class="table table-striped"}

### Return type

[**QueueEntityListing**](QueueEntityListing.html)

<a name="get_routing_skill"></a>

## [**RoutingSkill**](RoutingSkill.html) get_routing_skill(skill_id)

Get Routing Skill



Wraps GET /api/v2/routing/skills/{skillId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
skill_id = 'skill_id_example' # str | Skill ID

try:
    # Get Routing Skill
    api_response = api_instance.get_routing_skill(skill_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_skill: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_id** | **str**| Skill ID |  |
{: class="table table-striped"}

### Return type

[**RoutingSkill**](RoutingSkill.html)

<a name="get_routing_skills"></a>

## [**SkillEntityListing**](SkillEntityListing.html) get_routing_skills(page_size=page_size, page_number=page_number, name=name)

Get the list of routing skills.



Wraps GET /api/v2/routing/skills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Filter for results that start with this value (optional)

try:
    # Get the list of routing skills.
    api_response = api_instance.get_routing_skills(page_size=page_size, page_number=page_number, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_skills: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Filter for results that start with this value | [optional]  |
{: class="table table-striped"}

### Return type

[**SkillEntityListing**](SkillEntityListing.html)

<a name="get_routing_utilization"></a>

## [**Utilization**](Utilization.html) get_routing_utilization()

Get the utilization settings.



Wraps GET /api/v2/routing/utilization 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get the utilization settings.
    api_response = api_instance.get_routing_utilization()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_utilization: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Utilization**](Utilization.html)

<a name="get_routing_wrapupcode"></a>

## [**WrapupCode**](WrapupCode.html) get_routing_wrapupcode(code_id)

Get details about this wrap-up code.



Wraps GET /api/v2/routing/wrapupcodes/{codeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
code_id = 'code_id_example' # str | Wrapup Code ID

try:
    # Get details about this wrap-up code.
    api_response = api_instance.get_routing_wrapupcode(code_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_wrapupcode: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code_id** | **str**| Wrapup Code ID |  |
{: class="table table-striped"}

### Return type

[**WrapupCode**](WrapupCode.html)

<a name="get_routing_wrapupcodes"></a>

## [**WrapupCodeEntityListing**](WrapupCodeEntityListing.html) get_routing_wrapupcodes(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by)

Get list of wrapup codes.



Wraps GET /api/v2/routing/wrapupcodes 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
sort_by = 'name' # str | Sort by (optional) (default to name)

try:
    # Get list of wrapup codes.
    api_response = api_instance.get_routing_wrapupcodes(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_routing_wrapupcodes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to name] |
{: class="table table-striped"}

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing.html)

<a name="get_user_routingskills"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)

List routing skills for user



Wraps GET /api/v2/users/{userId}/routingskills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)

try:
    # List routing skills for user
    api_response = api_instance.get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->get_user_routingskills: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

<a name="patch_routing_queue_user"></a>

## [**QueueMember**](QueueMember.html) patch_routing_queue_user(queue_id, member_id, body)

Update the ring number of joined status for a User in a Queue



Wraps PATCH /api/v2/routing/queues/{queueId}/users/{memberId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
member_id = 'member_id_example' # str | Member ID
body = PureCloudPlatformClientV2.QueueMember() # QueueMember | Queue Member

try:
    # Update the ring number of joined status for a User in a Queue
    api_response = api_instance.patch_routing_queue_user(queue_id, member_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->patch_routing_queue_user: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **member_id** | **str**| Member ID |  |
| **body** | [**QueueMember**](QueueMember.html)| Queue Member |  |
{: class="table table-striped"}

### Return type

[**QueueMember**](QueueMember.html)

<a name="patch_routing_queue_users"></a>

## [**QueueMemberEntityListing**](QueueMemberEntityListing.html) patch_routing_queue_users(queue_id, body)

Join or unjoin a set of users for a queue



Wraps PATCH /api/v2/routing/queues/{queueId}/users 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.QueueMember()] # list[QueueMember] | Queue Members

try:
    # Join or unjoin a set of users for a queue
    api_response = api_instance.patch_routing_queue_users(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->patch_routing_queue_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[QueueMember]**](QueueMember.html)| Queue Members |  |
{: class="table table-striped"}

### Return type

[**QueueMemberEntityListing**](QueueMemberEntityListing.html)

<a name="post_analytics_queues_observations_query"></a>

## [**QualifierMappingObservationQueryResponse**](QualifierMappingObservationQueryResponse.html) post_analytics_queues_observations_query(body)

Query for queue observations



Wraps POST /api/v2/analytics/queues/observations/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.ObservationQuery() # ObservationQuery | query

try:
    # Query for queue observations
    api_response = api_instance.post_analytics_queues_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_analytics_queues_observations_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ObservationQuery**](ObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**QualifierMappingObservationQueryResponse**](QualifierMappingObservationQueryResponse.html)

<a name="post_routing_email_domain_routes"></a>

## [**InboundRoute**](InboundRoute.html) post_routing_email_domain_routes(domain_name, body)

Create a route



Wraps POST /api/v2/routing/email/domains/{domainName}/routes 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_name = 'domain_name_example' # str | email domain
body = PureCloudPlatformClientV2.InboundRoute() # InboundRoute | Route

try:
    # Create a route
    api_response = api_instance.post_routing_email_domain_routes(domain_name, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_email_domain_routes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **body** | [**InboundRoute**](InboundRoute.html)| Route |  |
{: class="table table-striped"}

### Return type

[**InboundRoute**](InboundRoute.html)

<a name="post_routing_email_domains"></a>

## [**InboundDomain**](InboundDomain.html) post_routing_email_domains(body)

Create a domain



Wraps POST /api/v2/routing/email/domains 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.InboundDomain() # InboundDomain | Domain

try:
    # Create a domain
    api_response = api_instance.post_routing_email_domains(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_email_domains: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**InboundDomain**](InboundDomain.html)| Domain |  |
{: class="table table-striped"}

### Return type

[**InboundDomain**](InboundDomain.html)

<a name="post_routing_languages"></a>

## [**Language**](Language.html) post_routing_languages(body)

Create Language



Wraps POST /api/v2/routing/languages 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.Language() # Language | Language

try:
    # Create Language
    api_response = api_instance.post_routing_languages(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_languages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Language**](Language.html)| Language |  |
{: class="table table-striped"}

### Return type

[**Language**](Language.html)

<a name="post_routing_queue_users"></a>

## str** post_routing_queue_users(queue_id, body, delete=delete)

Bulk add or delete up to 100 queue members



Wraps POST /api/v2/routing/queues/{queueId}/users 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.QueueMember()] # list[QueueMember] | Queue Members
delete = false # bool | True to delete queue members (optional) (default to false)

try:
    # Bulk add or delete up to 100 queue members
    api_response = api_instance.post_routing_queue_users(queue_id, body, delete=delete)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_queue_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[QueueMember]**](QueueMember.html)| Queue Members |  |
| **delete** | **bool**| True to delete queue members | [optional] [default to false] |
{: class="table table-striped"}

### Return type

**str**

<a name="post_routing_queue_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) post_routing_queue_wrapupcodes(queue_id, body)

Add up to 100 wrap-up codes to a queue



Wraps POST /api/v2/routing/queues/{queueId}/wrapupcodes 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.WrapupCode()] # list[WrapupCode] | List of wrapup codes

try:
    # Add up to 100 wrap-up codes to a queue
    api_response = api_instance.post_routing_queue_wrapupcodes(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_queue_wrapupcodes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[WrapupCode]**](WrapupCode.html)| List of wrapup codes |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="post_routing_queues"></a>

## [**Queue**](Queue.html) post_routing_queues(body)

Create queue



Wraps POST /api/v2/routing/queues 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.CreateQueueRequest() # CreateQueueRequest | Queue

try:
    # Create queue
    api_response = api_instance.post_routing_queues(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_queues: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateQueueRequest**](CreateQueueRequest.html)| Queue |  |
{: class="table table-striped"}

### Return type

[**Queue**](Queue.html)

<a name="post_routing_skills"></a>

## [**RoutingSkill**](RoutingSkill.html) post_routing_skills(body)

Create Skill



Wraps POST /api/v2/routing/skills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.RoutingSkill() # RoutingSkill | Skill

try:
    # Create Skill
    api_response = api_instance.post_routing_skills(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_skills: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoutingSkill**](RoutingSkill.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**RoutingSkill**](RoutingSkill.html)

<a name="post_routing_wrapupcodes"></a>

## [**WrapupCode**](WrapupCode.html) post_routing_wrapupcodes(body)

Create a wrap-up code



Wraps POST /api/v2/routing/wrapupcodes 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.WrapupCode() # WrapupCode | WrapupCode

try:
    # Create a wrap-up code
    api_response = api_instance.post_routing_wrapupcodes(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_routing_wrapupcodes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WrapupCode**](WrapupCode.html)| WrapupCode |  |
{: class="table table-striped"}

### Return type

[**WrapupCode**](WrapupCode.html)

<a name="post_user_routingskills"></a>

## [**UserRoutingSkill**](UserRoutingSkill.html) post_user_routingskills(user_id, body)

Add routing skill to user



Wraps POST /api/v2/users/{userId}/routingskills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UserRoutingSkillPost() # UserRoutingSkillPost | Skill

try:
    # Add routing skill to user
    api_response = api_instance.post_user_routingskills(user_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->post_user_routingskills: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingSkillPost**](UserRoutingSkillPost.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserRoutingSkill**](UserRoutingSkill.html)

<a name="put_routing_email_domain_route"></a>

## [**InboundRoute**](InboundRoute.html) put_routing_email_domain_route(domain_name, route_id, body)

Update a route



Wraps PUT /api/v2/routing/email/domains/{domainName}/routes/{routeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_name = 'domain_name_example' # str | email domain
route_id = 'route_id_example' # str | route ID
body = PureCloudPlatformClientV2.InboundRoute() # InboundRoute | Route

try:
    # Update a route
    api_response = api_instance.put_routing_email_domain_route(domain_name, route_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->put_routing_email_domain_route: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **route_id** | **str**| route ID |  |
| **body** | [**InboundRoute**](InboundRoute.html)| Route |  |
{: class="table table-striped"}

### Return type

[**InboundRoute**](InboundRoute.html)

<a name="put_routing_queue"></a>

## [**Queue**](Queue.html) put_routing_queue(queue_id, body)

Update a queue



Wraps PUT /api/v2/routing/queues/{queueId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = PureCloudPlatformClientV2.Queue() # Queue | Queue

try:
    # Update a queue
    api_response = api_instance.put_routing_queue(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->put_routing_queue: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**Queue**](Queue.html)| Queue |  |
{: class="table table-striped"}

### Return type

[**Queue**](Queue.html)

<a name="put_routing_utilization"></a>

## [**Utilization**](Utilization.html) put_routing_utilization(body)

Update the utilization settings.



Wraps PUT /api/v2/routing/utilization 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.Utilization() # Utilization | utilization

try:
    # Update the utilization settings.
    api_response = api_instance.put_routing_utilization(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->put_routing_utilization: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Utilization**](Utilization.html)| utilization |  |
{: class="table table-striped"}

### Return type

[**Utilization**](Utilization.html)

<a name="put_routing_wrapupcode"></a>

## [**WrapupCode**](WrapupCode.html) put_routing_wrapupcode(code_id, body)

Update wrap-up code



Wraps PUT /api/v2/routing/wrapupcodes/{codeId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
code_id = 'code_id_example' # str | Wrapup Code ID
body = PureCloudPlatformClientV2.WrapupCode() # WrapupCode | WrapupCode

try:
    # Update wrap-up code
    api_response = api_instance.put_routing_wrapupcode(code_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->put_routing_wrapupcode: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code_id** | **str**| Wrapup Code ID |  |
| **body** | [**WrapupCode**](WrapupCode.html)| WrapupCode |  |
{: class="table table-striped"}

### Return type

[**WrapupCode**](WrapupCode.html)

<a name="put_user_routingskill"></a>

## [**UserRoutingSkill**](UserRoutingSkill.html) put_user_routingskill(user_id, skill_id, body)

Update routing skill proficiency or state.



Wraps PUT /api/v2/users/{userId}/routingskills/{skillId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
skill_id = 'skill_id_example' # str | skillId
body = PureCloudPlatformClientV2.UserRoutingSkill() # UserRoutingSkill | Skill

try:
    # Update routing skill proficiency or state.
    api_response = api_instance.put_user_routingskill(user_id, skill_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoutingApi->put_user_routingskill: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
| **body** | [**UserRoutingSkill**](UserRoutingSkill.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserRoutingSkill**](UserRoutingSkill.html)

