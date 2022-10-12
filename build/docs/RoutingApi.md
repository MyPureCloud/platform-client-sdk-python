---
title: RoutingApi
---

## PureCloudPlatformClientV2.RoutingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_routing_assessment**](RoutingApi.html#delete_routing_assessment) | Delete single benefit assessment.|
|[**delete_routing_email_domain**](RoutingApi.html#delete_routing_email_domain) | Delete a domain|
|[**delete_routing_email_domain_route**](RoutingApi.html#delete_routing_email_domain_route) | Delete a route|
|[**delete_routing_email_outbound_domain**](RoutingApi.html#delete_routing_email_outbound_domain) | Delete an outbound domain|
|[**delete_routing_predictor**](RoutingApi.html#delete_routing_predictor) | Delete single predictor.|
|[**delete_routing_queue**](RoutingApi.html#delete_routing_queue) | Delete a queue|
|[**delete_routing_queue_member**](RoutingApi.html#delete_routing_queue_member) | Delete a queue member.|
|[**delete_routing_queue_user**](RoutingApi.html#delete_routing_queue_user) | DEPRECATED: use DELETE /routing/queues/{queueId}/members/{memberId}.  Delete queue member.|
|[**delete_routing_queue_wrapupcode**](RoutingApi.html#delete_routing_queue_wrapupcode) | Delete a wrap-up code from a queue|
|[**delete_routing_settings**](RoutingApi.html#delete_routing_settings) | Delete an organization&#39;s routing settings|
|[**delete_routing_skill**](RoutingApi.html#delete_routing_skill) | Delete Routing Skill|
|[**delete_routing_sms_address**](RoutingApi.html#delete_routing_sms_address) | Delete an Address by Id for SMS|
|[**delete_routing_sms_phonenumber**](RoutingApi.html#delete_routing_sms_phonenumber) | Delete a phone number provisioned for SMS.|
|[**delete_routing_user_utilization**](RoutingApi.html#delete_routing_user_utilization) | Delete the user&#39;s max utilization settings and revert to the organization-wide default.|
|[**delete_routing_utilization**](RoutingApi.html#delete_routing_utilization) | Delete the organization-wide max utilization settings and revert to the system default.|
|[**delete_routing_wrapupcode**](RoutingApi.html#delete_routing_wrapupcode) | Delete wrap-up code|
|[**delete_user_routinglanguage**](RoutingApi.html#delete_user_routinglanguage) | Remove routing language from user|
|[**delete_user_routingskill**](RoutingApi.html#delete_user_routingskill) | Remove routing skill from user|
|[**get_routing_assessment**](RoutingApi.html#get_routing_assessment) | Retrieve a single benefit assessment.|
|[**get_routing_assessments**](RoutingApi.html#get_routing_assessments) | Retrieve all benefit assessments.|
|[**get_routing_assessments_job**](RoutingApi.html#get_routing_assessments_job) | Retrieve a single benefit assessments job.|
|[**get_routing_assessments_jobs**](RoutingApi.html#get_routing_assessments_jobs) | Retrieve all benefit assessment jobs.|
|[**get_routing_availablemediatypes**](RoutingApi.html#get_routing_availablemediatypes) | Get available media types|
|[**get_routing_email_domain**](RoutingApi.html#get_routing_email_domain) | Get domain|
|[**get_routing_email_domain_route**](RoutingApi.html#get_routing_email_domain_route) | Get a route|
|[**get_routing_email_domain_routes**](RoutingApi.html#get_routing_email_domain_routes) | Get routes|
|[**get_routing_email_domains**](RoutingApi.html#get_routing_email_domains) | Get domains|
|[**get_routing_email_outbound_domain**](RoutingApi.html#get_routing_email_outbound_domain) | Get domain|
|[**get_routing_email_outbound_domain_activation**](RoutingApi.html#get_routing_email_outbound_domain_activation) | Get activation status (cname + dkim) of an outbound domain|
|[**get_routing_email_outbound_domain_search**](RoutingApi.html#get_routing_email_outbound_domain_search) | Search a domain across organizations|
|[**get_routing_email_outbound_domains**](RoutingApi.html#get_routing_email_outbound_domains) | Get outbound domains|
|[**get_routing_email_setup**](RoutingApi.html#get_routing_email_setup) | Get email setup|
|[**get_routing_languages**](RoutingApi.html#get_routing_languages) | Get the list of supported languages.|
|[**get_routing_message_recipient**](RoutingApi.html#get_routing_message_recipient) | Get a recipient|
|[**get_routing_message_recipients**](RoutingApi.html#get_routing_message_recipients) | Get recipients|
|[**get_routing_predictor**](RoutingApi.html#get_routing_predictor) | Retrieve a single predictor.|
|[**get_routing_predictor_model_features**](RoutingApi.html#get_routing_predictor_model_features) | Retrieve Predictor Model Features.|
|[**get_routing_predictor_models**](RoutingApi.html#get_routing_predictor_models) | Retrieve Predictor Models and Top Features.|
|[**get_routing_predictors**](RoutingApi.html#get_routing_predictors) | Retrieve all predictors.|
|[**get_routing_predictors_keyperformanceindicators**](RoutingApi.html#get_routing_predictors_keyperformanceindicators) | Get a list of Key Performance Indicators|
|[**get_routing_queue**](RoutingApi.html#get_routing_queue) | Get details about this queue.|
|[**get_routing_queue_comparisonperiod**](RoutingApi.html#get_routing_queue_comparisonperiod) | Get a Comparison Period.|
|[**get_routing_queue_comparisonperiods**](RoutingApi.html#get_routing_queue_comparisonperiods) | Get list of comparison periods|
|[**get_routing_queue_estimatedwaittime**](RoutingApi.html#get_routing_queue_estimatedwaittime) | Get Estimated Wait Time|
|[**get_routing_queue_mediatype_estimatedwaittime**](RoutingApi.html#get_routing_queue_mediatype_estimatedwaittime) | Get Estimated Wait Time|
|[**get_routing_queue_members**](RoutingApi.html#get_routing_queue_members) | Get the members of this queue.|
|[**get_routing_queue_users**](RoutingApi.html#get_routing_queue_users) | DEPRECATED: use GET /routing/queues/{queueId}/members.  Get the members of this queue.|
|[**get_routing_queue_wrapupcodes**](RoutingApi.html#get_routing_queue_wrapupcodes) | Get the wrap-up codes for a queue|
|[**get_routing_queues**](RoutingApi.html#get_routing_queues) | Get list of queues.|
|[**get_routing_queues_divisionviews**](RoutingApi.html#get_routing_queues_divisionviews) | Get a paged listing of simplified queue objects, filterable by name, queue ID(s), or division ID(s).|
|[**get_routing_queues_divisionviews_all**](RoutingApi.html#get_routing_queues_divisionviews_all) | Get a paged listing of simplified queue objects, sorted by name.  Can be used to get a digest of all queues in an organization.|
|[**get_routing_queues_me**](RoutingApi.html#get_routing_queues_me) | Get a paged listing of queues the user is a member of.|
|[**get_routing_settings**](RoutingApi.html#get_routing_settings) | Get an organization&#39;s routing settings|
|[**get_routing_settings_contactcenter**](RoutingApi.html#get_routing_settings_contactcenter) | Get Contact Center Settings|
|[**get_routing_settings_transcription**](RoutingApi.html#get_routing_settings_transcription) | Get Transcription Settings|
|[**get_routing_skill**](RoutingApi.html#get_routing_skill) | Get Routing Skill|
|[**get_routing_skills**](RoutingApi.html#get_routing_skills) | Get the list of routing skills.|
|[**get_routing_sms_address**](RoutingApi.html#get_routing_sms_address) | Get an Address by Id for SMS|
|[**get_routing_sms_addresses**](RoutingApi.html#get_routing_sms_addresses) | Get a list of Addresses for SMS|
|[**get_routing_sms_availablephonenumbers**](RoutingApi.html#get_routing_sms_availablephonenumbers) | Get a list of available phone numbers for SMS provisioning.|
|[**get_routing_sms_phonenumber**](RoutingApi.html#get_routing_sms_phonenumber) | Get a phone number provisioned for SMS.|
|[**get_routing_sms_phonenumbers**](RoutingApi.html#get_routing_sms_phonenumbers) | Get a list of provisioned phone numbers.|
|[**get_routing_user_utilization**](RoutingApi.html#get_routing_user_utilization) | Get the user&#39;s max utilization settings.  If not configured, the organization-wide default is returned.|
|[**get_routing_utilization**](RoutingApi.html#get_routing_utilization) | Get the organization-wide max utilization settings.|
|[**get_routing_wrapupcode**](RoutingApi.html#get_routing_wrapupcode) | Get details about this wrap-up code.|
|[**get_routing_wrapupcodes**](RoutingApi.html#get_routing_wrapupcodes) | Get list of wrapup codes.|
|[**get_user_queues**](RoutingApi.html#get_user_queues) | Get queues for user|
|[**get_user_routinglanguages**](RoutingApi.html#get_user_routinglanguages) | List routing language for user|
|[**get_user_routingskills**](RoutingApi.html#get_user_routingskills) | List routing skills for user|
|[**patch_routing_conversation**](RoutingApi.html#patch_routing_conversation) | Update attributes of an in-queue conversation|
|[**patch_routing_email_domain**](RoutingApi.html#patch_routing_email_domain) | Update domain settings|
|[**patch_routing_email_domain_validate**](RoutingApi.html#patch_routing_email_domain_validate) | Validate domain settings|
|[**patch_routing_predictor**](RoutingApi.html#patch_routing_predictor) | Update single predictor.|
|[**patch_routing_queue_member**](RoutingApi.html#patch_routing_queue_member) | Update the ring number OR joined status for a queue member.|
|[**patch_routing_queue_members**](RoutingApi.html#patch_routing_queue_members) | Join or unjoin a set of users for a queue|
|[**patch_routing_queue_user**](RoutingApi.html#patch_routing_queue_user) | DEPRECATED: use PATCH /routing/queues/{queueId}/members/{memberId}.  Update the ring number OR joined status for a User in a Queue.|
|[**patch_routing_queue_users**](RoutingApi.html#patch_routing_queue_users) | DEPRECATED: use PATCH /routing/queues/{queueId}/members.  Join or unjoin a set of users for a queue.|
|[**patch_routing_settings_contactcenter**](RoutingApi.html#patch_routing_settings_contactcenter) | Update Contact Center Settings|
|[**patch_user_queue**](RoutingApi.html#patch_user_queue) | Join or unjoin a queue for a user|
|[**patch_user_queues**](RoutingApi.html#patch_user_queues) | Join or unjoin a set of queues for a user|
|[**patch_user_routinglanguage**](RoutingApi.html#patch_user_routinglanguage) | Update routing language proficiency or state.|
|[**patch_user_routinglanguages_bulk**](RoutingApi.html#patch_user_routinglanguages_bulk) | Add bulk routing language to user. Max limit 50 languages|
|[**patch_user_routingskills_bulk**](RoutingApi.html#patch_user_routingskills_bulk) | Bulk add routing skills to user|
|[**post_analytics_queues_observations_query**](RoutingApi.html#post_analytics_queues_observations_query) | Query for queue observations|
|[**post_routing_assessments**](RoutingApi.html#post_routing_assessments) | Create a benefit assessment.|
|[**post_routing_assessments_jobs**](RoutingApi.html#post_routing_assessments_jobs) | Create a benefit assessment job.|
|[**post_routing_email_domain_routes**](RoutingApi.html#post_routing_email_domain_routes) | Create a route|
|[**post_routing_email_domain_testconnection**](RoutingApi.html#post_routing_email_domain_testconnection) | Tests the custom SMTP server integration connection set on this domain|
|[**post_routing_email_domains**](RoutingApi.html#post_routing_email_domains) | Create a domain|
|[**post_routing_email_outbound_domains**](RoutingApi.html#post_routing_email_outbound_domains) | Create a domain|
|[**post_routing_email_outbound_domains_simulated**](RoutingApi.html#post_routing_email_outbound_domains_simulated) | Create a simulated domain|
|[**post_routing_languages**](RoutingApi.html#post_routing_languages) | Create Language|
|[**post_routing_predictors**](RoutingApi.html#post_routing_predictors) | Create a predictor.|
|[**post_routing_queue_members**](RoutingApi.html#post_routing_queue_members) | Bulk add or delete up to 100 queue members|
|[**post_routing_queue_users**](RoutingApi.html#post_routing_queue_users) | DEPRECATED: use POST /routing/queues/{queueId}/members.  Bulk add or delete up to 100 queue members.|
|[**post_routing_queue_wrapupcodes**](RoutingApi.html#post_routing_queue_wrapupcodes) | Add up to 100 wrap-up codes to a queue|
|[**post_routing_queues**](RoutingApi.html#post_routing_queues) | Create a queue|
|[**post_routing_skills**](RoutingApi.html#post_routing_skills) | Create Skill|
|[**post_routing_sms_addresses**](RoutingApi.html#post_routing_sms_addresses) | Provision an Address for SMS|
|[**post_routing_sms_phonenumbers**](RoutingApi.html#post_routing_sms_phonenumbers) | Provision a phone number for SMS|
|[**post_routing_wrapupcodes**](RoutingApi.html#post_routing_wrapupcodes) | Create a wrap-up code|
|[**post_user_routinglanguages**](RoutingApi.html#post_user_routinglanguages) | Add routing language to user|
|[**post_user_routingskills**](RoutingApi.html#post_user_routingskills) | Add routing skill to user|
|[**put_routing_email_domain_route**](RoutingApi.html#put_routing_email_domain_route) | Update a route|
|[**put_routing_email_outbound_domain_activation**](RoutingApi.html#put_routing_email_outbound_domain_activation) | Request an activation status (cname + dkim) update of an outbound domain|
|[**put_routing_message_recipient**](RoutingApi.html#put_routing_message_recipient) | Update a recipient|
|[**put_routing_queue**](RoutingApi.html#put_routing_queue) | Update a queue|
|[**put_routing_settings**](RoutingApi.html#put_routing_settings) | Update an organization&#39;s routing settings|
|[**put_routing_settings_transcription**](RoutingApi.html#put_routing_settings_transcription) | Update Transcription Settings|
|[**put_routing_sms_phonenumber**](RoutingApi.html#put_routing_sms_phonenumber) | Update a phone number provisioned for SMS.|
|[**put_routing_user_utilization**](RoutingApi.html#put_routing_user_utilization) | Update the user&#39;s max utilization settings.  Include only those media types requiring custom configuration.|
|[**put_routing_utilization**](RoutingApi.html#put_routing_utilization) | Update the organization-wide max utilization settings.  Include only those media types requiring custom configuration.|
|[**put_routing_wrapupcode**](RoutingApi.html#put_routing_wrapupcode) | Update wrap-up code|
|[**put_user_routingskill**](RoutingApi.html#put_user_routingskill) | Update routing skill proficiency or state.|
|[**put_user_routingskills_bulk**](RoutingApi.html#put_user_routingskills_bulk) | Replace all routing skills assigned to a user|
{: class="table table-striped"}

<a name="delete_routing_assessment"></a>

##  delete_routing_assessment(assessment_id)



Delete single benefit assessment.



Wraps DELETE /api/v2/routing/assessments/{assessmentId} 

Requires ANY permissions: 

* routing:assessment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
assessment_id = 'assessment_id_example' # str | Benefit Assessment ID

try:
    # Delete single benefit assessment.
    api_instance.delete_routing_assessment(assessment_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_assessment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assessment_id** | **str**| Benefit Assessment ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_email_domain"></a>

##  delete_routing_email_domain(domain_id)



Delete a domain



Wraps DELETE /api/v2/routing/email/domains/{domainId} 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Delete a domain
    api_instance.delete_routing_email_domain(domain_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_email_domain: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_name = 'domain_name_example' # str | email domain
route_id = 'route_id_example' # str | route ID

try:
    # Delete a route
    api_instance.delete_routing_email_domain_route(domain_name, route_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_email_domain_route: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **route_id** | **str**| route ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_email_outbound_domain"></a>

##  delete_routing_email_outbound_domain(domain_id)



Delete an outbound domain



Wraps DELETE /api/v2/routing/email/outbound/domains/{domainId} 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Delete an outbound domain
    api_instance.delete_routing_email_outbound_domain(domain_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_email_outbound_domain: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_predictor"></a>

##  delete_routing_predictor(predictor_id)



Delete single predictor.



Wraps DELETE /api/v2/routing/predictors/{predictorId} 

Requires ALL permissions: 

* routing:predictor:delete
* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
predictor_id = 'predictor_id_example' # str | Predictor ID

try:
    # Delete single predictor.
    api_instance.delete_routing_predictor(predictor_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_predictor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| Predictor ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_queue"></a>

##  delete_routing_queue(queue_id, force_delete=force_delete)



Delete a queue



Wraps DELETE /api/v2/routing/queues/{queueId} 

Requires ALL permissions: 

* routing:queue:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
force_delete = True # bool | forceDelete (optional)

try:
    # Delete a queue
    api_instance.delete_routing_queue(queue_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **force_delete** | **bool**| forceDelete | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_queue_member"></a>

##  delete_routing_queue_member(queue_id, member_id)



Delete a queue member.



Wraps DELETE /api/v2/routing/queues/{queueId}/members/{memberId} 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
member_id = 'member_id_example' # str | Member ID

try:
    # Delete a queue member.
    api_instance.delete_routing_queue_member(queue_id, member_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_queue_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **member_id** | **str**| Member ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_queue_user"></a>

##  delete_routing_queue_user(queue_id, member_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

DEPRECATED: use DELETE /routing/queues/{queueId}/members/{memberId}.  Delete queue member.



Wraps DELETE /api/v2/routing/queues/{queueId}/users/{memberId} 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
member_id = 'member_id_example' # str | Member ID

try:
    # DEPRECATED: use DELETE /routing/queues/{queueId}/members/{memberId}.  Delete queue member.
    api_instance.delete_routing_queue_user(queue_id, member_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_queue_user: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
code_id = 'code_id_example' # str | Code ID

try:
    # Delete a wrap-up code from a queue
    api_instance.delete_routing_queue_wrapupcode(queue_id, code_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_queue_wrapupcode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **code_id** | **str**| Code ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_settings"></a>

##  delete_routing_settings()



Delete an organization's routing settings



Wraps DELETE /api/v2/routing/settings 

Requires ANY permissions: 

* routing:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Delete an organization's routing settings
    api_instance.delete_routing_settings()
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

void (empty response body)

<a name="delete_routing_skill"></a>

##  delete_routing_skill(skill_id)



Delete Routing Skill



Wraps DELETE /api/v2/routing/skills/{skillId} 

Requires ALL permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
skill_id = 'skill_id_example' # str | Skill ID

try:
    # Delete Routing Skill
    api_instance.delete_routing_skill(skill_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_skill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_id** | **str**| Skill ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_sms_address"></a>

##  delete_routing_sms_address(address_id)



Delete an Address by Id for SMS



Wraps DELETE /api/v2/routing/sms/addresses/{addressId} 

Requires ALL permissions: 

* sms:phoneNumber:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
address_id = 'address_id_example' # str | Address ID

try:
    # Delete an Address by Id for SMS
    api_instance.delete_routing_sms_address(address_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_sms_address: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **address_id** | **str**| Address ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_sms_phonenumber"></a>

##  delete_routing_sms_phonenumber(address_id)



Delete a phone number provisioned for SMS.



Wraps DELETE /api/v2/routing/sms/phonenumbers/{addressId} 

Requires ALL permissions: 

* sms:phoneNumber:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
address_id = 'address_id_example' # str | Address ID

try:
    # Delete a phone number provisioned for SMS.
    api_instance.delete_routing_sms_phonenumber(address_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_sms_phonenumber: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **address_id** | **str**| Address ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_user_utilization"></a>

##  delete_routing_user_utilization(user_id)



Delete the user's max utilization settings and revert to the organization-wide default.



Wraps DELETE /api/v2/routing/users/{userId}/utilization 

Requires ANY permissions: 

* routing:utilization:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID

try:
    # Delete the user's max utilization settings and revert to the organization-wide default.
    api_instance.delete_routing_user_utilization(user_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_user_utilization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_utilization"></a>

##  delete_routing_utilization()



Delete the organization-wide max utilization settings and revert to the system default.



Wraps DELETE /api/v2/routing/utilization 

Requires ALL permissions: 

* routing:utilization:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Delete the organization-wide max utilization settings and revert to the system default.
    api_instance.delete_routing_utilization()
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_utilization: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

void (empty response body)

<a name="delete_routing_wrapupcode"></a>

##  delete_routing_wrapupcode(code_id)



Delete wrap-up code



Wraps DELETE /api/v2/routing/wrapupcodes/{codeId} 

Requires ALL permissions: 

* routing:wrapupCode:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
code_id = 'code_id_example' # str | Wrapup Code ID

try:
    # Delete wrap-up code
    api_instance.delete_routing_wrapupcode(code_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_wrapupcode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code_id** | **str**| Wrapup Code ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_routinglanguage"></a>

##  delete_user_routinglanguage(user_id, language_id)



Remove routing language from user



Wraps DELETE /api/v2/users/{userId}/routinglanguages/{languageId} 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
language_id = 'language_id_example' # str | languageId

try:
    # Remove routing language from user
    api_instance.delete_user_routinglanguage(user_id, language_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_user_routinglanguage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **language_id** | **str**| languageId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_routingskill"></a>

##  delete_user_routingskill(user_id, skill_id)



Remove routing skill from user



Wraps DELETE /api/v2/users/{userId}/routingskills/{skillId} 

Requires ALL permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
skill_id = 'skill_id_example' # str | skillId

try:
    # Remove routing skill from user
    api_instance.delete_user_routingskill(user_id, skill_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_user_routingskill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_routing_assessment"></a>

## [**BenefitAssessment**](BenefitAssessment.html) get_routing_assessment(assessment_id)



Retrieve a single benefit assessment.



Wraps GET /api/v2/routing/assessments/{assessmentId} 

Requires ANY permissions: 

* routing:assessment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
assessment_id = 'assessment_id_example' # str | Benefit Assessment ID

try:
    # Retrieve a single benefit assessment.
    api_response = api_instance.get_routing_assessment(assessment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_assessment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assessment_id** | **str**| Benefit Assessment ID |  |
{: class="table table-striped"}

### Return type

[**BenefitAssessment**](BenefitAssessment.html)

<a name="get_routing_assessments"></a>

## [**AssessmentListing**](AssessmentListing.html) get_routing_assessments(before=before, after=after, limit=limit, page_size=page_size, queue_id=queue_id)



Retrieve all benefit assessments.



Wraps GET /api/v2/routing/assessments 

Requires ANY permissions: 

* routing:queue:view
* routing:assessment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
queue_id = ['queue_id_example'] # list[str] | Queue ID(s) to filter assessments by. (optional)

try:
    # Retrieve all benefit assessments.
    api_response = api_instance.get_routing_assessments(before=before, after=after, limit=limit, page_size=page_size, queue_id=queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_assessments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **queue_id** | [**list[str]**](str.html)| Queue ID(s) to filter assessments by. | [optional]  |
{: class="table table-striped"}

### Return type

[**AssessmentListing**](AssessmentListing.html)

<a name="get_routing_assessments_job"></a>

## [**BenefitAssessmentJob**](BenefitAssessmentJob.html) get_routing_assessments_job(job_id)



Retrieve a single benefit assessments job.



Wraps GET /api/v2/routing/assessments/jobs/{jobId} 

Requires ANY permissions: 

* routing:assessment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
job_id = 'job_id_example' # str | Benefit Assessment Job ID

try:
    # Retrieve a single benefit assessments job.
    api_response = api_instance.get_routing_assessments_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_assessments_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Benefit Assessment Job ID |  |
{: class="table table-striped"}

### Return type

[**BenefitAssessmentJob**](BenefitAssessmentJob.html)

<a name="get_routing_assessments_jobs"></a>

## [**AssessmentJobListing**](AssessmentJobListing.html) get_routing_assessments_jobs(division_id=division_id)



Retrieve all benefit assessment jobs.



Wraps GET /api/v2/routing/assessments/jobs 

Requires ANY permissions: 

* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
division_id = ['division_id_example'] # list[str] | Division ID(s) to filter assessment jobs by. (optional)

try:
    # Retrieve all benefit assessment jobs.
    api_response = api_instance.get_routing_assessments_jobs(division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_assessments_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | [**list[str]**](str.html)| Division ID(s) to filter assessment jobs by. | [optional]  |
{: class="table table-striped"}

### Return type

[**AssessmentJobListing**](AssessmentJobListing.html)

<a name="get_routing_availablemediatypes"></a>

## [**AvailableMediaTypeEntityListing**](AvailableMediaTypeEntityListing.html) get_routing_availablemediatypes()



Get available media types



Wraps GET /api/v2/routing/availablemediatypes 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get available media types
    api_response = api_instance.get_routing_availablemediatypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_availablemediatypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**AvailableMediaTypeEntityListing**](AvailableMediaTypeEntityListing.html)

<a name="get_routing_email_domain"></a>

## [**InboundDomain**](InboundDomain.html) get_routing_email_domain(domain_id)



Get domain



Wraps GET /api/v2/routing/email/domains/{domainId} 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Get domain
    api_response = api_instance.get_routing_email_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_domain: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->get_routing_email_domain_route: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->get_routing_email_domain_routes: %s\n" % e)
```

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

## [**InboundDomainEntityListing**](InboundDomainEntityListing.html) get_routing_email_domains(exclude_status=exclude_status)



Get domains



Wraps GET /api/v2/routing/email/domains 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
exclude_status = False # bool | Exclude MX record data (optional) (default to False)

try:
    # Get domains
    api_response = api_instance.get_routing_email_domains(exclude_status=exclude_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **exclude_status** | **bool**| Exclude MX record data | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**InboundDomainEntityListing**](InboundDomainEntityListing.html)

<a name="get_routing_email_outbound_domain"></a>

## [**OutboundDomain**](OutboundDomain.html) get_routing_email_outbound_domain(domain_id)



Get domain



Wraps GET /api/v2/routing/email/outbound/domains/{domainId} 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Get domain
    api_response = api_instance.get_routing_email_outbound_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_outbound_domain: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

[**OutboundDomain**](OutboundDomain.html)

<a name="get_routing_email_outbound_domain_activation"></a>

## [**EmailOutboundDomainResult**](EmailOutboundDomainResult.html) get_routing_email_outbound_domain_activation(domain_id)



Get activation status (cname + dkim) of an outbound domain



Wraps GET /api/v2/routing/email/outbound/domains/{domainId}/activation 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Get activation status (cname + dkim) of an outbound domain
    api_response = api_instance.get_routing_email_outbound_domain_activation(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_outbound_domain_activation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult.html)

<a name="get_routing_email_outbound_domain_search"></a>

## [**OutboundDomain**](OutboundDomain.html) get_routing_email_outbound_domain_search(domain_id)



Search a domain across organizations



Wraps GET /api/v2/routing/email/outbound/domains/{domainId}/search 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Search a domain across organizations
    api_response = api_instance.get_routing_email_outbound_domain_search(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_outbound_domain_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

[**OutboundDomain**](OutboundDomain.html)

<a name="get_routing_email_outbound_domains"></a>

## [**OutboundDomainEntityListing**](OutboundDomainEntityListing.html) get_routing_email_outbound_domains()



Get outbound domains



Wraps GET /api/v2/routing/email/outbound/domains 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get outbound domains
    api_response = api_instance.get_routing_email_outbound_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_outbound_domains: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**OutboundDomainEntityListing**](OutboundDomainEntityListing.html)

<a name="get_routing_email_setup"></a>

## [**EmailSetup**](EmailSetup.html) get_routing_email_setup()



Get email setup



Wraps GET /api/v2/routing/email/setup 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get email setup
    api_response = api_instance.get_routing_email_setup()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_setup: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EmailSetup**](EmailSetup.html)

<a name="get_routing_languages"></a>

## [**LanguageEntityListing**](LanguageEntityListing.html) get_routing_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, id=id)



Get the list of supported languages.



Wraps GET /api/v2/routing/languages 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)

try:
    # Get the list of supported languages.
    api_response = api_instance.get_routing_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_languages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str.html)| id | [optional]  |
{: class="table table-striped"}

### Return type

[**LanguageEntityListing**](LanguageEntityListing.html)

<a name="get_routing_message_recipient"></a>

## [**Recipient**](Recipient.html) get_routing_message_recipient(recipient_id)



Get a recipient



Wraps GET /api/v2/routing/message/recipients/{recipientId} 

Requires ALL permissions: 

* routing:message:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
recipient_id = 'recipient_id_example' # str | Recipient ID

try:
    # Get a recipient
    api_response = api_instance.get_routing_message_recipient(recipient_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_message_recipient: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recipient_id** | **str**| Recipient ID |  |
{: class="table table-striped"}

### Return type

[**Recipient**](Recipient.html)

<a name="get_routing_message_recipients"></a>

## [**RecipientListing**](RecipientListing.html) get_routing_message_recipients(messenger_type=messenger_type, page_size=page_size, page_number=page_number)



Get recipients



Wraps GET /api/v2/routing/message/recipients 

Requires ALL permissions: 

* routing:message:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
messenger_type = 'messenger_type_example' # str | Messenger Type (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get recipients
    api_response = api_instance.get_routing_message_recipients(messenger_type=messenger_type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_message_recipients: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messenger_type** | **str**| Messenger Type | [optional] <br />**Values**: sms, facebook, twitter, line, whatsapp, open, instagram |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**RecipientListing**](RecipientListing.html)

<a name="get_routing_predictor"></a>

## [**Predictor**](Predictor.html) get_routing_predictor(predictor_id)



Retrieve a single predictor.



Wraps GET /api/v2/routing/predictors/{predictorId} 

Requires ANY permissions: 

* routing:predictor:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
predictor_id = 'predictor_id_example' # str | Predictor ID

try:
    # Retrieve a single predictor.
    api_response = api_instance.get_routing_predictor(predictor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_predictor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| Predictor ID |  |
{: class="table table-striped"}

### Return type

[**Predictor**](Predictor.html)

<a name="get_routing_predictor_model_features"></a>

## [**PredictorModelFeatureListing**](PredictorModelFeatureListing.html) get_routing_predictor_model_features(predictor_id, model_id)



Retrieve Predictor Model Features.



Wraps GET /api/v2/routing/predictors/{predictorId}/models/{modelId}/features 

Requires ALL permissions: 

* routing:predictorModelFeature:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
predictor_id = 'predictor_id_example' # str | Predictor ID
model_id = 'model_id_example' # str | Model ID

try:
    # Retrieve Predictor Model Features.
    api_response = api_instance.get_routing_predictor_model_features(predictor_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_predictor_model_features: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| Predictor ID |  |
| **model_id** | **str**| Model ID |  |
{: class="table table-striped"}

### Return type

[**PredictorModelFeatureListing**](PredictorModelFeatureListing.html)

<a name="get_routing_predictor_models"></a>

## [**PredictorModels**](PredictorModels.html) get_routing_predictor_models(predictor_id)



Retrieve Predictor Models and Top Features.



Wraps GET /api/v2/routing/predictors/{predictorId}/models 

Requires ALL permissions: 

* routing:predictorModel:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
predictor_id = 'predictor_id_example' # str | Predictor ID

try:
    # Retrieve Predictor Models and Top Features.
    api_response = api_instance.get_routing_predictor_models(predictor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_predictor_models: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| Predictor ID |  |
{: class="table table-striped"}

### Return type

[**PredictorModels**](PredictorModels.html)

<a name="get_routing_predictors"></a>

## [**PredictorListing**](PredictorListing.html) get_routing_predictors(before=before, after=after, limit=limit, page_size=page_size, queue_id=queue_id)



Retrieve all predictors.



Wraps GET /api/v2/routing/predictors 

Requires ANY permissions: 

* routing:predictor:view
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
queue_id = ['queue_id_example'] # list[str] | Comma-separated list of queue Ids to filter by. (optional)

try:
    # Retrieve all predictors.
    api_response = api_instance.get_routing_predictors(before=before, after=after, limit=limit, page_size=page_size, queue_id=queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_predictors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **queue_id** | [**list[str]**](str.html)| Comma-separated list of queue Ids to filter by. | [optional]  |
{: class="table table-striped"}

### Return type

[**PredictorListing**](PredictorListing.html)

<a name="get_routing_predictors_keyperformanceindicators"></a>

## [**list[KeyPerformanceIndicator]**](KeyPerformanceIndicator.html) get_routing_predictors_keyperformanceindicators(kpi_group=kpi_group)



Get a list of Key Performance Indicators



Wraps GET /api/v2/routing/predictors/keyperformanceindicators 

Requires ANY permissions: 

* routing:keyPerformanceIndicator:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
kpi_group = 'kpi_group_example' # str | The Group of Key Performance Indicators to return (optional)

try:
    # Get a list of Key Performance Indicators
    api_response = api_instance.get_routing_predictors_keyperformanceindicators(kpi_group=kpi_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_predictors_keyperformanceindicators: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **kpi_group** | **str**| The Group of Key Performance Indicators to return | [optional] <br />**Values**: Standard, Custom |
{: class="table table-striped"}

### Return type

[**list[KeyPerformanceIndicator]**](KeyPerformanceIndicator.html)

<a name="get_routing_queue"></a>

## [**Queue**](Queue.html) get_routing_queue(queue_id)



Get details about this queue.



Wraps GET /api/v2/routing/queues/{queueId} 

Requires ALL permissions: 

* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID

try:
    # Get details about this queue.
    api_response = api_instance.get_routing_queue(queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
{: class="table table-striped"}

### Return type

[**Queue**](Queue.html)

<a name="get_routing_queue_comparisonperiod"></a>

## [**ComparisonPeriod**](ComparisonPeriod.html) get_routing_queue_comparisonperiod(queue_id, comparison_period_id)



Get a Comparison Period.



Wraps GET /api/v2/routing/queues/{queueId}/comparisonperiods/{comparisonPeriodId} 

Requires ALL permissions: 

* routing:comparisonPeriod:view
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue id
comparison_period_id = 'comparison_period_id_example' # str | ComparisonPeriod id

try:
    # Get a Comparison Period.
    api_response = api_instance.get_routing_queue_comparisonperiod(queue_id, comparison_period_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_comparisonperiod: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue id |  |
| **comparison_period_id** | **str**| ComparisonPeriod id |  |
{: class="table table-striped"}

### Return type

[**ComparisonPeriod**](ComparisonPeriod.html)

<a name="get_routing_queue_comparisonperiods"></a>

## [**ComparisonPeriodListing**](ComparisonPeriodListing.html) get_routing_queue_comparisonperiods(queue_id)



Get list of comparison periods



Wraps GET /api/v2/routing/queues/{queueId}/comparisonperiods 

Requires ALL permissions: 

* routing:comparisonPeriod:view
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue id

try:
    # Get list of comparison periods
    api_response = api_instance.get_routing_queue_comparisonperiods(queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_comparisonperiods: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue id |  |
{: class="table table-striped"}

### Return type

[**ComparisonPeriodListing**](ComparisonPeriodListing.html)

<a name="get_routing_queue_estimatedwaittime"></a>

## [**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions.html) get_routing_queue_estimatedwaittime(queue_id, conversation_id=conversation_id)



Get Estimated Wait Time



Wraps GET /api/v2/routing/queues/{queueId}/estimatedwaittime 

Requires ALL permissions: 

* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->get_routing_queue_estimatedwaittime: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->get_routing_queue_mediatype_estimatedwaittime: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| queueId |  |
| **media_type** | **str**| mediaType |  |
{: class="table table-striped"}

### Return type

[**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions.html)

<a name="get_routing_queue_members"></a>

## [**QueueMemberEntityListing**](QueueMemberEntityListing.html) get_routing_queue_members(queue_id, page_number=page_number, page_size=page_size, sort_order=sort_order, expand=expand, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence, member_by=member_by, joined=joined)



Get the members of this queue.



Wraps GET /api/v2/routing/queues/{queueId}/members 

Requires ANY permissions: 

* routing:queue:view
* routing:queue:edit
* routing:queue:readonly
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int | Max value is 100 (optional) (default to 25)
sort_order = ''asc'' # str | Note: results are sorted by name. (optional) (default to 'asc')
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
name = 'name_example' # str | Filter by queue member name (optional)
profile_skills = ['profile_skills_example'] # list[str] | Filter by profile skill (optional)
skills = ['skills_example'] # list[str] | Filter by skill (optional)
languages = ['languages_example'] # list[str] | Filter by language (optional)
routing_status = ['routing_status_example'] # list[str] | Filter by routing status (optional)
presence = ['presence_example'] # list[str] | Filter by presence (optional)
member_by = 'member_by_example' # str | Filter by member type (optional)
joined = True # bool | Filter by joined status (optional)

try:
    # Get the members of this queue.
    api_response = api_instance.get_routing_queue_members(queue_id, page_number=page_number, page_size=page_size, sort_order=sort_order, expand=expand, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence, member_by=member_by, joined=joined)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**| Max value is 100 | [optional] [default to 25] |
| **sort_order** | **str**| Note: results are sorted by name. | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, dateLastLogin, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
| **name** | **str**| Filter by queue member name | [optional]  |
| **profile_skills** | [**list[str]**](str.html)| Filter by profile skill | [optional]  |
| **skills** | [**list[str]**](str.html)| Filter by skill | [optional]  |
| **languages** | [**list[str]**](str.html)| Filter by language | [optional]  |
| **routing_status** | [**list[str]**](str.html)| Filter by routing status | [optional]  |
| **presence** | [**list[str]**](str.html)| Filter by presence | [optional]  |
| **member_by** | **str**| Filter by member type | [optional] <br />**Values**: user, group |
| **joined** | **bool**| Filter by joined status | [optional] <br />**Values**: true, false |
{: class="table table-striped"}

### Return type

[**QueueMemberEntityListing**](QueueMemberEntityListing.html)

<a name="get_routing_queue_users"></a>

## [**QueueMemberEntityListingV1**](QueueMemberEntityListingV1.html) get_routing_queue_users(queue_id, page_number=page_number, page_size=page_size, sort_order=sort_order, expand=expand, joined=joined, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

DEPRECATED: use GET /routing/queues/{queueId}/members.  Get the members of this queue.



Wraps GET /api/v2/routing/queues/{queueId}/users 

Requires ANY permissions: 

* routing:queue:view
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int | Max value is 100 (optional) (default to 25)
sort_order = ''asc'' # str | Note: results are sorted by name. (optional) (default to 'asc')
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
joined = True # bool | Filter by joined status (optional)
name = 'name_example' # str | Filter by queue member name (optional)
profile_skills = ['profile_skills_example'] # list[str] | Filter by profile skill (optional)
skills = ['skills_example'] # list[str] | Filter by skill (optional)
languages = ['languages_example'] # list[str] | Filter by language (optional)
routing_status = ['routing_status_example'] # list[str] | Filter by routing status (optional)
presence = ['presence_example'] # list[str] | Filter by presence (optional)

try:
    # DEPRECATED: use GET /routing/queues/{queueId}/members.  Get the members of this queue.
    api_response = api_instance.get_routing_queue_users(queue_id, page_number=page_number, page_size=page_size, sort_order=sort_order, expand=expand, joined=joined, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**| Max value is 100 | [optional] [default to 25] |
| **sort_order** | **str**| Note: results are sorted by name. | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, dateLastLogin, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
| **joined** | **bool**| Filter by joined status | [optional]  |
| **name** | **str**| Filter by queue member name | [optional]  |
| **profile_skills** | [**list[str]**](str.html)| Filter by profile skill | [optional]  |
| **skills** | [**list[str]**](str.html)| Filter by skill | [optional]  |
| **languages** | [**list[str]**](str.html)| Filter by language | [optional]  |
| **routing_status** | [**list[str]**](str.html)| Filter by routing status | [optional]  |
| **presence** | [**list[str]**](str.html)| Filter by presence | [optional]  |
{: class="table table-striped"}

### Return type

[**QueueMemberEntityListingV1**](QueueMemberEntityListingV1.html)

<a name="get_routing_queue_wrapupcodes"></a>

## [**WrapupCodeEntityListing**](WrapupCodeEntityListing.html) get_routing_queue_wrapupcodes(queue_id, page_size=page_size, page_number=page_number)



Get the wrap-up codes for a queue



Wraps GET /api/v2/routing/queues/{queueId}/wrapupcodes 

Requires ALL permissions: 

* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get the wrap-up codes for a queue
    api_response = api_instance.get_routing_queue_wrapupcodes(queue_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing.html)

<a name="get_routing_queues"></a>

## [**QueueEntityListing**](QueueEntityListing.html) get_routing_queues(page_number=page_number, page_size=page_size, sort_order=sort_order, name=name, id=id, division_id=division_id, peer_id=peer_id, has_peer=has_peer)



Get list of queues.



Wraps GET /api/v2/routing/queues 

Requires ANY permissions: 

* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_order = ''asc'' # str | Note: results are sorted by name. (optional) (default to 'asc')
name = 'name_example' # str | Filter by queue name (optional)
id = ['id_example'] # list[str] | Filter by queue ID(s) (optional)
division_id = ['division_id_example'] # list[str] | Filter by queue division ID(s) (optional)
peer_id = ['peer_id_example'] # list[str] | Filter by queue peer ID(s) (optional)
has_peer = True # bool | Filter by queues associated with peer (optional)

try:
    # Get list of queues.
    api_response = api_instance.get_routing_queues(page_number=page_number, page_size=page_size, sort_order=sort_order, name=name, id=id, division_id=division_id, peer_id=peer_id, has_peer=has_peer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_order** | **str**| Note: results are sorted by name. | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **name** | **str**| Filter by queue name | [optional]  |
| **id** | [**list[str]**](str.html)| Filter by queue ID(s) | [optional]  |
| **division_id** | [**list[str]**](str.html)| Filter by queue division ID(s) | [optional]  |
| **peer_id** | [**list[str]**](str.html)| Filter by queue peer ID(s) | [optional]  |
| **has_peer** | **bool**| Filter by queues associated with peer | [optional]  |
{: class="table table-striped"}

### Return type

[**QueueEntityListing**](QueueEntityListing.html)

<a name="get_routing_queues_divisionviews"></a>

## [**QueueEntityListing**](QueueEntityListing.html) get_routing_queues_divisionviews(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id, division_id=division_id)



Get a paged listing of simplified queue objects, filterable by name, queue ID(s), or division ID(s).



Wraps GET /api/v2/routing/queues/divisionviews 

Requires ALL permissions: 

* routing:queue:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size [max value is 100] (optional) (default to 25)
page_number = 1 # int | Page number [max value is 5] (optional) (default to 1)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | Queue ID(s) (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)

try:
    # Get a paged listing of simplified queue objects, filterable by name, queue ID(s), or division ID(s).
    api_response = api_instance.get_routing_queues_divisionviews(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queues_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size [max value is 100] | [optional] [default to 25] |
| **page_number** | **int**| Page number [max value is 5] | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;]<br />**Values**: name, id, divisionId |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str.html)| Queue ID(s) | [optional]  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
{: class="table table-striped"}

### Return type

[**QueueEntityListing**](QueueEntityListing.html)

<a name="get_routing_queues_divisionviews_all"></a>

## [**QueueEntityListing**](QueueEntityListing.html) get_routing_queues_divisionviews_all(page_size=page_size, page_number=page_number, sort_order=sort_order)



Get a paged listing of simplified queue objects, sorted by name.  Can be used to get a digest of all queues in an organization.



Wraps GET /api/v2/routing/queues/divisionviews/all 

Requires ALL permissions: 

* routing:queue:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size [max value is 500] (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')

try:
    # Get a paged listing of simplified queue objects, sorted by name.  Can be used to get a digest of all queues in an organization.
    api_response = api_instance.get_routing_queues_divisionviews_all(page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queues_divisionviews_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size [max value is 500] | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
{: class="table table-striped"}

### Return type

[**QueueEntityListing**](QueueEntityListing.html)

<a name="get_routing_queues_me"></a>

## [**UserQueueEntityListing**](UserQueueEntityListing.html) get_routing_queues_me(page_number=page_number, page_size=page_size, joined=joined, sort_order=sort_order)



Get a paged listing of queues the user is a member of.



Wraps GET /api/v2/routing/queues/me 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
joined = True # bool | Filter by joined status. (optional)
sort_order = ''asc'' # str | Note: results are sorted by name. (optional) (default to 'asc')

try:
    # Get a paged listing of queues the user is a member of.
    api_response = api_instance.get_routing_queues_me(page_number=page_number, page_size=page_size, joined=joined, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queues_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **joined** | **bool**| Filter by joined status. | [optional] <br />**Values**: true, false |
| **sort_order** | **str**| Note: results are sorted by name. | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="get_routing_settings"></a>

## [**RoutingSettings**](RoutingSettings.html) get_routing_settings()



Get an organization's routing settings



Wraps GET /api/v2/routing/settings 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get an organization's routing settings
    api_response = api_instance.get_routing_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**RoutingSettings**](RoutingSettings.html)

<a name="get_routing_settings_contactcenter"></a>

## [**ContactCenterSettings**](ContactCenterSettings.html) get_routing_settings_contactcenter()



Get Contact Center Settings



Wraps GET /api/v2/routing/settings/contactcenter 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get Contact Center Settings
    api_response = api_instance.get_routing_settings_contactcenter()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_settings_contactcenter: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ContactCenterSettings**](ContactCenterSettings.html)

<a name="get_routing_settings_transcription"></a>

## [**TranscriptionSettings**](TranscriptionSettings.html) get_routing_settings_transcription()



Get Transcription Settings



Wraps GET /api/v2/routing/settings/transcription 

Requires ANY permissions: 

* routing:transcriptionSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get Transcription Settings
    api_response = api_instance.get_routing_settings_transcription()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_settings_transcription: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**TranscriptionSettings**](TranscriptionSettings.html)

<a name="get_routing_skill"></a>

## [**RoutingSkill**](RoutingSkill.html) get_routing_skill(skill_id)



Get Routing Skill



Wraps GET /api/v2/routing/skills/{skillId} 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()
skill_id = 'skill_id_example' # str | Skill ID

try:
    # Get Routing Skill
    api_response = api_instance.get_routing_skill(skill_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_skill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_id** | **str**| Skill ID |  |
{: class="table table-striped"}

### Return type

[**RoutingSkill**](RoutingSkill.html)

<a name="get_routing_skills"></a>

## [**SkillEntityListing**](SkillEntityListing.html) get_routing_skills(page_size=page_size, page_number=page_number, name=name, id=id)



Get the list of routing skills.



Wraps GET /api/v2/routing/skills 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Filter for results that start with this value (optional)
id = ['id_example'] # list[str] | id (optional)

try:
    # Get the list of routing skills.
    api_response = api_instance.get_routing_skills(page_size=page_size, page_number=page_number, name=name, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_skills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Filter for results that start with this value | [optional]  |
| **id** | [**list[str]**](str.html)| id | [optional]  |
{: class="table table-striped"}

### Return type

[**SkillEntityListing**](SkillEntityListing.html)

<a name="get_routing_sms_address"></a>

## [**SmsAddress**](SmsAddress.html) get_routing_sms_address(address_id)



Get an Address by Id for SMS



Wraps GET /api/v2/routing/sms/addresses/{addressId} 

Requires ALL permissions: 

* sms:phoneNumber:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
address_id = 'address_id_example' # str | Address ID

try:
    # Get an Address by Id for SMS
    api_response = api_instance.get_routing_sms_address(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_address: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **address_id** | **str**| Address ID |  |
{: class="table table-striped"}

### Return type

[**SmsAddress**](SmsAddress.html)

<a name="get_routing_sms_addresses"></a>

## [**SmsAddressEntityListing**](SmsAddressEntityListing.html) get_routing_sms_addresses(page_size=page_size, page_number=page_number)



Get a list of Addresses for SMS



Wraps GET /api/v2/routing/sms/addresses 

Requires ALL permissions: 

* sms:phoneNumber:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Addresses for SMS
    api_response = api_instance.get_routing_sms_addresses(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_addresses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**SmsAddressEntityListing**](SmsAddressEntityListing.html)

<a name="get_routing_sms_availablephonenumbers"></a>

## [**SMSAvailablePhoneNumberEntityListing**](SMSAvailablePhoneNumberEntityListing.html) get_routing_sms_availablephonenumbers(country_code, phone_number_type, region=region, city=city, area_code=area_code, pattern=pattern, address_requirement=address_requirement)



Get a list of available phone numbers for SMS provisioning.

This request will return up to 30 random phone numbers matching the criteria specified.  To get additional phone numbers repeat the request.



Wraps GET /api/v2/routing/sms/availablephonenumbers 

Requires ALL permissions: 

* sms:phoneNumber:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
country_code = 'country_code_example' # str | The ISO 3166-1 alpha-2 country code of the county for which available phone numbers should be returned
phone_number_type = 'phone_number_type_example' # str | Type of available phone numbers searched
region = 'region_example' # str | Region/province/state that can be used to restrict the numbers returned (optional)
city = 'city_example' # str | City that can be used to restrict the numbers returned (optional)
area_code = 'area_code_example' # str | Area code that can be used to restrict the numbers returned (optional)
pattern = 'pattern_example' # str | A pattern to match phone numbers. Valid characters are '*' and [0-9a-zA-Z]. The '*' character will match any single digit. (optional)
address_requirement = 'address_requirement_example' # str | This indicates whether the phone number requires to have an Address registered. (optional)

try:
    # Get a list of available phone numbers for SMS provisioning.
    api_response = api_instance.get_routing_sms_availablephonenumbers(country_code, phone_number_type, region=region, city=city, area_code=area_code, pattern=pattern, address_requirement=address_requirement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_availablephonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **country_code** | **str**| The ISO 3166-1 alpha-2 country code of the county for which available phone numbers should be returned |  |
| **phone_number_type** | **str**| Type of available phone numbers searched | <br />**Values**: local, mobile, tollfree |
| **region** | **str**| Region/province/state that can be used to restrict the numbers returned | [optional]  |
| **city** | **str**| City that can be used to restrict the numbers returned | [optional]  |
| **area_code** | **str**| Area code that can be used to restrict the numbers returned | [optional]  |
| **pattern** | **str**| A pattern to match phone numbers. Valid characters are &#39;*&#39; and [0-9a-zA-Z]. The &#39;*&#39; character will match any single digit. | [optional]  |
| **address_requirement** | **str**| This indicates whether the phone number requires to have an Address registered. | [optional] <br />**Values**: none, any, local, foreign |
{: class="table table-striped"}

### Return type

[**SMSAvailablePhoneNumberEntityListing**](SMSAvailablePhoneNumberEntityListing.html)

<a name="get_routing_sms_phonenumber"></a>

## [**SmsPhoneNumber**](SmsPhoneNumber.html) get_routing_sms_phonenumber(address_id)



Get a phone number provisioned for SMS.



Wraps GET /api/v2/routing/sms/phonenumbers/{addressId} 

Requires ALL permissions: 

* sms:phoneNumber:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
address_id = 'address_id_example' # str | Address ID

try:
    # Get a phone number provisioned for SMS.
    api_response = api_instance.get_routing_sms_phonenumber(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_phonenumber: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **address_id** | **str**| Address ID |  |
{: class="table table-striped"}

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber.html)

<a name="get_routing_sms_phonenumbers"></a>

## [**SmsPhoneNumberEntityListing**](SmsPhoneNumberEntityListing.html) get_routing_sms_phonenumbers(phone_number=phone_number, phone_number_type=phone_number_type, phone_number_status=phone_number_status, country_code=country_code, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, language=language)



Get a list of provisioned phone numbers.



Wraps GET /api/v2/routing/sms/phonenumbers 

Requires ALL permissions: 

* sms:phoneNumber:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
phone_number = 'phone_number_example' # str | Filter on phone number address. Allowable characters are the digits '0-9' and the wild card character '\\*'. If just digits are present, a contains search is done on the address pattern. For example, '317' could be matched anywhere in the address. An '\\*' will match multiple digits. For example, to match a specific area code within the US a pattern like '1317*' could be used. (optional)
phone_number_type = ['phone_number_type_example'] # list[str] | Filter on phone number type (optional)
phone_number_status = ['phone_number_status_example'] # list[str] | Filter on phone number status (optional)
country_code = ['country_code_example'] # list[str] | Filter on country code (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'sort_by_example' # str | Optional field to sort results (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)
language = ''en-US'' # str | A language tag (which is sometimes referred to as a \"locale identifier\") to use to localize country field and sort operations (optional) (default to 'en-US')

try:
    # Get a list of provisioned phone numbers.
    api_response = api_instance.get_routing_sms_phonenumbers(phone_number=phone_number, phone_number_type=phone_number_type, phone_number_status=phone_number_status, country_code=country_code, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_phonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_number** | **str**| Filter on phone number address. Allowable characters are the digits &#39;0-9&#39; and the wild card character &#39;\\*&#39;. If just digits are present, a contains search is done on the address pattern. For example, &#39;317&#39; could be matched anywhere in the address. An &#39;\\*&#39; will match multiple digits. For example, to match a specific area code within the US a pattern like &#39;1317*&#39; could be used. | [optional]  |
| **phone_number_type** | [**list[str]**](str.html)| Filter on phone number type | [optional] <br />**Values**: local, mobile, tollfree, shortcode |
| **phone_number_status** | [**list[str]**](str.html)| Filter on phone number status | [optional] <br />**Values**: active, invalid, initiated, porting, pending, pending-cancellation |
| **country_code** | [**list[str]**](str.html)| Filter on country code | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Optional field to sort results | [optional] <br />**Values**: phoneNumber, countryCode, country, dateCreated, dateModified, phoneNumberStatus, phoneNumberType, purchaseDate, supportsMms, supportsSms, supportsVoice |
| **sort_order** | **str**| Sort order | [optional] <br />**Values**: ascending, descending |
| **language** | **str**| A language tag (which is sometimes referred to as a \&quot;locale identifier\&quot;) to use to localize country field and sort operations | [optional] [default to &#39;en-US&#39;] |
{: class="table table-striped"}

### Return type

[**SmsPhoneNumberEntityListing**](SmsPhoneNumberEntityListing.html)

<a name="get_routing_user_utilization"></a>

## [**AgentMaxUtilization**](AgentMaxUtilization.html) get_routing_user_utilization(user_id)



Get the user's max utilization settings.  If not configured, the organization-wide default is returned.



Wraps GET /api/v2/routing/users/{userId}/utilization 

Requires ANY permissions: 

* routing:utilization:manage
* routing:utilization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get the user's max utilization settings.  If not configured, the organization-wide default is returned.
    api_response = api_instance.get_routing_user_utilization(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_user_utilization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**AgentMaxUtilization**](AgentMaxUtilization.html)

<a name="get_routing_utilization"></a>

## [**Utilization**](Utilization.html) get_routing_utilization()



Get the organization-wide max utilization settings.



Wraps GET /api/v2/routing/utilization 

Requires ANY permissions: 

* routing:utilization:manage
* routing:utilization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()

try:
    # Get the organization-wide max utilization settings.
    api_response = api_instance.get_routing_utilization()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**Utilization**](Utilization.html)

<a name="get_routing_wrapupcode"></a>

## [**WrapupCode**](WrapupCode.html) get_routing_wrapupcode(code_id)



Get details about this wrap-up code.



Wraps GET /api/v2/routing/wrapupcodes/{codeId} 

Requires ALL permissions: 

* routing:wrapupCode:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
code_id = 'code_id_example' # str | Wrapup Code ID

try:
    # Get details about this wrap-up code.
    api_response = api_instance.get_routing_wrapupcode(code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_wrapupcode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code_id** | **str**| Wrapup Code ID |  |
{: class="table table-striped"}

### Return type

[**WrapupCode**](WrapupCode.html)

<a name="get_routing_wrapupcodes"></a>

## [**WrapupCodeEntityListing**](WrapupCodeEntityListing.html) get_routing_wrapupcodes(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name)



Get list of wrapup codes.



Wraps GET /api/v2/routing/wrapupcodes 

Requires ALL permissions: 

* routing:wrapupCode:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')
name = 'name_example' # str | Wrapup code's name ('Sort by' param is ignored unless this field is provided) (optional)

try:
    # Get list of wrapup codes.
    api_response = api_instance.get_routing_wrapupcodes(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;]<br />**Values**: name, id |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Wrapup code&#39;s name (&#39;Sort by&#39; param is ignored unless this field is provided) | [optional]  |
{: class="table table-striped"}

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing.html)

<a name="get_user_queues"></a>

## [**UserQueueEntityListing**](UserQueueEntityListing.html) get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined, division_id=division_id)



Get queues for user



Wraps GET /api/v2/users/{userId}/queues 

Requires ANY permissions: 

* routing:queue:view
* routing:queue:join
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
joined = True # bool | Is joined to the queue (optional) (default to True)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)

try:
    # Get queues for user
    api_response = api_instance.get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_user_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **joined** | **bool**| Is joined to the queue | [optional] [default to True] |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="get_user_routinglanguages"></a>

## [**UserLanguageEntityListing**](UserLanguageEntityListing.html) get_user_routinglanguages(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)



List routing language for user



Wraps GET /api/v2/users/{userId}/routinglanguages 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')

try:
    # List routing language for user
    api_response = api_instance.get_user_routinglanguages(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_user_routinglanguages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing.html)

<a name="get_user_routingskills"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)



List routing skills for user



Wraps GET /api/v2/users/{userId}/routingskills 

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
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')

try:
    # List routing skills for user
    api_response = api_instance.get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_user_routingskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

<a name="patch_routing_conversation"></a>

## [**RoutingConversationAttributesResponse**](RoutingConversationAttributesResponse.html) patch_routing_conversation(conversation_id, body)



Update attributes of an in-queue conversation

Returns an object indicating the updated values of all settable attributes. Supported attributes: skillIds, languageId, and priority.



Wraps PATCH /api/v2/routing/conversations/{conversationId} 

Requires ANY permissions: 

* routing:conversation:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
body = PureCloudPlatformClientV2.RoutingConversationAttributesRequest() # RoutingConversationAttributesRequest | Conversation Attributes

try:
    # Update attributes of an in-queue conversation
    api_response = api_instance.patch_routing_conversation(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **body** | [**RoutingConversationAttributesRequest**](RoutingConversationAttributesRequest.html)| Conversation Attributes |  |
{: class="table table-striped"}

### Return type

[**RoutingConversationAttributesResponse**](RoutingConversationAttributesResponse.html)

<a name="patch_routing_email_domain"></a>

## [**InboundDomain**](InboundDomain.html) patch_routing_email_domain(domain_id, body)



Update domain settings



Wraps PATCH /api/v2/routing/email/domains/{domainId} 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID
body = PureCloudPlatformClientV2.InboundDomainPatchRequest() # InboundDomainPatchRequest | Domain settings

try:
    # Update domain settings
    api_response = api_instance.patch_routing_email_domain(domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_email_domain: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
| **body** | [**InboundDomainPatchRequest**](InboundDomainPatchRequest.html)| Domain settings |  |
{: class="table table-striped"}

### Return type

[**InboundDomain**](InboundDomain.html)

<a name="patch_routing_email_domain_validate"></a>

## [**InboundDomain**](InboundDomain.html) patch_routing_email_domain_validate(domain_id, body)



Validate domain settings



Wraps PATCH /api/v2/routing/email/domains/{domainId}/validate 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID
body = PureCloudPlatformClientV2.InboundDomainPatchRequest() # InboundDomainPatchRequest | Domain settings

try:
    # Validate domain settings
    api_response = api_instance.patch_routing_email_domain_validate(domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_email_domain_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
| **body** | [**InboundDomainPatchRequest**](InboundDomainPatchRequest.html)| Domain settings |  |
{: class="table table-striped"}

### Return type

[**InboundDomain**](InboundDomain.html)

<a name="patch_routing_predictor"></a>

## [**Predictor**](Predictor.html) patch_routing_predictor(predictor_id, body=body)



Update single predictor.



Wraps PATCH /api/v2/routing/predictors/{predictorId} 

Requires ALL permissions: 

* routing:predictor:edit
* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
predictor_id = 'predictor_id_example' # str | Predictor ID
body = PureCloudPlatformClientV2.PatchPredictorRequest() # PatchPredictorRequest |  (optional)

try:
    # Update single predictor.
    api_response = api_instance.patch_routing_predictor(predictor_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_predictor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| Predictor ID |  |
| **body** | [**PatchPredictorRequest**](PatchPredictorRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**Predictor**](Predictor.html)

<a name="patch_routing_queue_member"></a>

##  patch_routing_queue_member(queue_id, member_id, body)



Update the ring number OR joined status for a queue member.



Wraps PATCH /api/v2/routing/queues/{queueId}/members/{memberId} 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
member_id = 'member_id_example' # str | Member ID
body = PureCloudPlatformClientV2.QueueMember() # QueueMember | Queue Member

try:
    # Update the ring number OR joined status for a queue member.
    api_instance.patch_routing_queue_member(queue_id, member_id, body)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_queue_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **member_id** | **str**| Member ID |  |
| **body** | [**QueueMember**](QueueMember.html)| Queue Member |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_routing_queue_members"></a>

## [**QueueMemberEntityListing**](QueueMemberEntityListing.html) patch_routing_queue_members(queue_id, body)



Join or unjoin a set of users for a queue



Wraps PATCH /api/v2/routing/queues/{queueId}/members 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.QueueMember()] # list[QueueMember] | Queue Members

try:
    # Join or unjoin a set of users for a queue
    api_response = api_instance.patch_routing_queue_members(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_queue_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[QueueMember]**](QueueMember.html)| Queue Members |  |
{: class="table table-striped"}

### Return type

[**QueueMemberEntityListing**](QueueMemberEntityListing.html)

<a name="patch_routing_queue_user"></a>

##  patch_routing_queue_user(queue_id, member_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

DEPRECATED: use PATCH /routing/queues/{queueId}/members/{memberId}.  Update the ring number OR joined status for a User in a Queue.



Wraps PATCH /api/v2/routing/queues/{queueId}/users/{memberId} 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
member_id = 'member_id_example' # str | Member ID
body = PureCloudPlatformClientV2.QueueMember() # QueueMember | Queue Member

try:
    # DEPRECATED: use PATCH /routing/queues/{queueId}/members/{memberId}.  Update the ring number OR joined status for a User in a Queue.
    api_instance.patch_routing_queue_user(queue_id, member_id, body)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_queue_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **member_id** | **str**| Member ID |  |
| **body** | [**QueueMember**](QueueMember.html)| Queue Member |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_routing_queue_users"></a>

## [**QueueMemberEntityListingV1**](QueueMemberEntityListingV1.html) patch_routing_queue_users(queue_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

DEPRECATED: use PATCH /routing/queues/{queueId}/members.  Join or unjoin a set of users for a queue.



Wraps PATCH /api/v2/routing/queues/{queueId}/users 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.QueueMember()] # list[QueueMember] | Queue Members

try:
    # DEPRECATED: use PATCH /routing/queues/{queueId}/members.  Join or unjoin a set of users for a queue.
    api_response = api_instance.patch_routing_queue_users(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_queue_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[QueueMember]**](QueueMember.html)| Queue Members |  |
{: class="table table-striped"}

### Return type

[**QueueMemberEntityListingV1**](QueueMemberEntityListingV1.html)

<a name="patch_routing_settings_contactcenter"></a>

##  patch_routing_settings_contactcenter(body)



Update Contact Center Settings



Wraps PATCH /api/v2/routing/settings/contactcenter 

Requires ANY permissions: 

* routing:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.ContactCenterSettings() # ContactCenterSettings | Contact Center Settings

try:
    # Update Contact Center Settings
    api_instance.patch_routing_settings_contactcenter(body)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_settings_contactcenter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactCenterSettings**](ContactCenterSettings.html)| Contact Center Settings |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_user_queue"></a>

## [**UserQueue**](UserQueue.html) patch_user_queue(queue_id, user_id, body)



Join or unjoin a queue for a user



Wraps PATCH /api/v2/users/{userId}/queues/{queueId} 

Requires ANY permissions: 

* routing:queue:join
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UserQueue() # UserQueue | Queue Member

try:
    # Join or unjoin a queue for a user
    api_response = api_instance.patch_user_queue(queue_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **user_id** | **str**| User ID |  |
| **body** | [**UserQueue**](UserQueue.html)| Queue Member |  |
{: class="table table-striped"}

### Return type

[**UserQueue**](UserQueue.html)

<a name="patch_user_queues"></a>

## [**UserQueueEntityListing**](UserQueueEntityListing.html) patch_user_queues(user_id, body, division_id=division_id)



Join or unjoin a set of queues for a user



Wraps PATCH /api/v2/users/{userId}/queues 

Requires ANY permissions: 

* routing:queue:join
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserQueue()] # list[UserQueue] | User Queues
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)

try:
    # Join or unjoin a set of queues for a user
    api_response = api_instance.patch_user_queues(user_id, body, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserQueue]**](UserQueue.html)| User Queues |  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="patch_user_routinglanguage"></a>

## [**UserRoutingLanguage**](UserRoutingLanguage.html) patch_user_routinglanguage(user_id, language_id, body)



Update routing language proficiency or state.



Wraps PATCH /api/v2/users/{userId}/routinglanguages/{languageId} 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
language_id = 'language_id_example' # str | languageId
body = PureCloudPlatformClientV2.UserRoutingLanguage() # UserRoutingLanguage | Language

try:
    # Update routing language proficiency or state.
    api_response = api_instance.patch_user_routinglanguage(user_id, language_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_routinglanguage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **language_id** | **str**| languageId |  |
| **body** | [**UserRoutingLanguage**](UserRoutingLanguage.html)| Language |  |
{: class="table table-striped"}

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage.html)

<a name="patch_user_routinglanguages_bulk"></a>

## [**UserLanguageEntityListing**](UserLanguageEntityListing.html) patch_user_routinglanguages_bulk(user_id, body)



Add bulk routing language to user. Max limit 50 languages



Wraps PATCH /api/v2/users/{userId}/routinglanguages/bulk 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserRoutingLanguagePost()] # list[UserRoutingLanguagePost] | Language

try:
    # Add bulk routing language to user. Max limit 50 languages
    api_response = api_instance.patch_user_routinglanguages_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_routinglanguages_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingLanguagePost]**](UserRoutingLanguagePost.html)| Language |  |
{: class="table table-striped"}

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing.html)

<a name="patch_user_routingskills_bulk"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) patch_user_routingskills_bulk(user_id, body)



Bulk add routing skills to user



Wraps PATCH /api/v2/users/{userId}/routingskills/bulk 

Requires ANY permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserRoutingSkillPost()] # list[UserRoutingSkillPost] | Skill

try:
    # Bulk add routing skills to user
    api_response = api_instance.patch_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

<a name="post_analytics_queues_observations_query"></a>

## [**QueueObservationQueryResponse**](QueueObservationQueryResponse.html) post_analytics_queues_observations_query(body)



Query for queue observations



Wraps POST /api/v2/analytics/queues/observations/query 

Requires ANY permissions: 

* analytics:queueObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.QueueObservationQuery() # QueueObservationQuery | query

try:
    # Query for queue observations
    api_response = api_instance.post_analytics_queues_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_analytics_queues_observations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**QueueObservationQuery**](QueueObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**QueueObservationQueryResponse**](QueueObservationQueryResponse.html)

<a name="post_routing_assessments"></a>

## [**BenefitAssessment**](BenefitAssessment.html) post_routing_assessments(body=body)



Create a benefit assessment.



Wraps POST /api/v2/routing/assessments 

Requires ALL permissions: 

* routing:assessment:add
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.CreateBenefitAssessmentRequest() # CreateBenefitAssessmentRequest |  (optional)

try:
    # Create a benefit assessment.
    api_response = api_instance.post_routing_assessments(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_assessments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBenefitAssessmentRequest**](CreateBenefitAssessmentRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**BenefitAssessment**](BenefitAssessment.html)

<a name="post_routing_assessments_jobs"></a>

## [**BenefitAssessmentJob**](BenefitAssessmentJob.html) post_routing_assessments_jobs(body=body)



Create a benefit assessment job.



Wraps POST /api/v2/routing/assessments/jobs 

Requires ANY permissions: 

* routing:assessment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.CreateBenefitAssessmentJobRequest() # CreateBenefitAssessmentJobRequest |  (optional)

try:
    # Create a benefit assessment job.
    api_response = api_instance.post_routing_assessments_jobs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_assessments_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBenefitAssessmentJobRequest**](CreateBenefitAssessmentJobRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**BenefitAssessmentJob**](BenefitAssessmentJob.html)

<a name="post_routing_email_domain_routes"></a>

## [**InboundRoute**](InboundRoute.html) post_routing_email_domain_routes(domain_name, body)



Create a route



Wraps POST /api/v2/routing/email/domains/{domainName}/routes 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->post_routing_email_domain_routes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **body** | [**InboundRoute**](InboundRoute.html)| Route |  |
{: class="table table-striped"}

### Return type

[**InboundRoute**](InboundRoute.html)

<a name="post_routing_email_domain_testconnection"></a>

## [**TestMessage**](TestMessage.html) post_routing_email_domain_testconnection(domain_id, body=body)



Tests the custom SMTP server integration connection set on this domain

The request body is optional. If omitted, this endpoint will just test the connection of the Custom SMTP Server. If the body is specified, there will be an attempt to send an email message to the server.



Wraps POST /api/v2/routing/email/domains/{domainId}/testconnection 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID
body = PureCloudPlatformClientV2.TestMessage() # TestMessage | TestMessage (optional)

try:
    # Tests the custom SMTP server integration connection set on this domain
    api_response = api_instance.post_routing_email_domain_testconnection(domain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_email_domain_testconnection: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
| **body** | [**TestMessage**](TestMessage.html)| TestMessage | [optional]  |
{: class="table table-striped"}

### Return type

[**TestMessage**](TestMessage.html)

<a name="post_routing_email_domains"></a>

## [**InboundDomain**](InboundDomain.html) post_routing_email_domains(body)



Create a domain



Wraps POST /api/v2/routing/email/domains 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.InboundDomain() # InboundDomain | Domain

try:
    # Create a domain
    api_response = api_instance.post_routing_email_domains(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_email_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**InboundDomain**](InboundDomain.html)| Domain |  |
{: class="table table-striped"}

### Return type

[**InboundDomain**](InboundDomain.html)

<a name="post_routing_email_outbound_domains"></a>

## [**EmailOutboundDomainResult**](EmailOutboundDomainResult.html) post_routing_email_outbound_domains(body)



Create a domain



Wraps POST /api/v2/routing/email/outbound/domains 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.OutboundDomain() # OutboundDomain | Domain

try:
    # Create a domain
    api_response = api_instance.post_routing_email_outbound_domains(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_email_outbound_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutboundDomain**](OutboundDomain.html)| Domain |  |
{: class="table table-striped"}

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult.html)

<a name="post_routing_email_outbound_domains_simulated"></a>

## [**EmailOutboundDomainResult**](EmailOutboundDomainResult.html) post_routing_email_outbound_domains_simulated(body)



Create a simulated domain



Wraps POST /api/v2/routing/email/outbound/domains/simulated 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.OutboundDomain() # OutboundDomain | Domain

try:
    # Create a simulated domain
    api_response = api_instance.post_routing_email_outbound_domains_simulated(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_email_outbound_domains_simulated: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutboundDomain**](OutboundDomain.html)| Domain |  |
{: class="table table-striped"}

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult.html)

<a name="post_routing_languages"></a>

## [**Language**](Language.html) post_routing_languages(body)



Create Language



Wraps POST /api/v2/routing/languages 

Requires ANY permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.Language() # Language | Language

try:
    # Create Language
    api_response = api_instance.post_routing_languages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_languages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Language**](Language.html)| Language |  |
{: class="table table-striped"}

### Return type

[**Language**](Language.html)

<a name="post_routing_predictors"></a>

## [**Predictor**](Predictor.html) post_routing_predictors(body=body)



Create a predictor.



Wraps POST /api/v2/routing/predictors 

Requires ALL permissions: 

* routing:predictor:add
* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.CreatePredictorRequest() # CreatePredictorRequest |  (optional)

try:
    # Create a predictor.
    api_response = api_instance.post_routing_predictors(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_predictors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreatePredictorRequest**](CreatePredictorRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**Predictor**](Predictor.html)

<a name="post_routing_queue_members"></a>

##  post_routing_queue_members(queue_id, body, delete=delete)



Bulk add or delete up to 100 queue members



Wraps POST /api/v2/routing/queues/{queueId}/members 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.WritableEntity()] # list[WritableEntity] | Queue Members
delete = False # bool | True to delete queue members (optional) (default to False)

try:
    # Bulk add or delete up to 100 queue members
    api_instance.post_routing_queue_members(queue_id, body, delete=delete)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_queue_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[WritableEntity]**](WritableEntity.html)| Queue Members |  |
| **delete** | **bool**| True to delete queue members | [optional] [default to False] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_routing_queue_users"></a>

##  post_routing_queue_users(queue_id, body, delete=delete)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

DEPRECATED: use POST /routing/queues/{queueId}/members.  Bulk add or delete up to 100 queue members.



Wraps POST /api/v2/routing/queues/{queueId}/users 

Requires ANY permissions: 

* routing:queue:edit
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.WritableEntity()] # list[WritableEntity] | Queue Members
delete = False # bool | True to delete queue members (optional) (default to False)

try:
    # DEPRECATED: use POST /routing/queues/{queueId}/members.  Bulk add or delete up to 100 queue members.
    api_instance.post_routing_queue_users(queue_id, body, delete=delete)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_queue_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[WritableEntity]**](WritableEntity.html)| Queue Members |  |
| **delete** | **bool**| True to delete queue members | [optional] [default to False] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_routing_queue_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) post_routing_queue_wrapupcodes(queue_id, body)



Add up to 100 wrap-up codes to a queue



Wraps POST /api/v2/routing/queues/{queueId}/wrapupcodes 

Requires ALL permissions: 

* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = [PureCloudPlatformClientV2.WrapUpCodeReference()] # list[WrapUpCodeReference] | List of wrapup codes

try:
    # Add up to 100 wrap-up codes to a queue
    api_response = api_instance.post_routing_queue_wrapupcodes(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_queue_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**list[WrapUpCodeReference]**](WrapUpCodeReference.html)| List of wrapup codes |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="post_routing_queues"></a>

## [**Queue**](Queue.html) post_routing_queues(body)



Create a queue



Wraps POST /api/v2/routing/queues 

Requires ANY permissions: 

* routing:queue:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.CreateQueueRequest() # CreateQueueRequest | Queue

try:
    # Create a queue
    api_response = api_instance.post_routing_queues(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_queues: %s\n" % e)
```

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

Requires ANY permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.RoutingSkill() # RoutingSkill | Skill

try:
    # Create Skill
    api_response = api_instance.post_routing_skills(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_skills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoutingSkill**](RoutingSkill.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**RoutingSkill**](RoutingSkill.html)

<a name="post_routing_sms_addresses"></a>

## [**SmsAddress**](SmsAddress.html) post_routing_sms_addresses(body)



Provision an Address for SMS



Wraps POST /api/v2/routing/sms/addresses 

Requires ALL permissions: 

* sms:phoneNumber:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.SmsAddressProvision() # SmsAddressProvision | SmsAddress

try:
    # Provision an Address for SMS
    api_response = api_instance.post_routing_sms_addresses(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_sms_addresses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SmsAddressProvision**](SmsAddressProvision.html)| SmsAddress |  |
{: class="table table-striped"}

### Return type

[**SmsAddress**](SmsAddress.html)

<a name="post_routing_sms_phonenumbers"></a>

## [**SmsPhoneNumber**](SmsPhoneNumber.html) post_routing_sms_phonenumbers(body)



Provision a phone number for SMS



Wraps POST /api/v2/routing/sms/phonenumbers 

Requires ALL permissions: 

* sms:phoneNumber:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.SmsPhoneNumberProvision() # SmsPhoneNumberProvision | SmsPhoneNumber

try:
    # Provision a phone number for SMS
    api_response = api_instance.post_routing_sms_phonenumbers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_sms_phonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SmsPhoneNumberProvision**](SmsPhoneNumberProvision.html)| SmsPhoneNumber |  |
{: class="table table-striped"}

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber.html)

<a name="post_routing_wrapupcodes"></a>

## [**WrapupCode**](WrapupCode.html) post_routing_wrapupcodes(body)



Create a wrap-up code



Wraps POST /api/v2/routing/wrapupcodes 

Requires ALL permissions: 

* routing:wrapupCode:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.WrapupCode() # WrapupCode | WrapupCode

try:
    # Create a wrap-up code
    api_response = api_instance.post_routing_wrapupcodes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WrapupCode**](WrapupCode.html)| WrapupCode |  |
{: class="table table-striped"}

### Return type

[**WrapupCode**](WrapupCode.html)

<a name="post_user_routinglanguages"></a>

## [**UserRoutingLanguage**](UserRoutingLanguage.html) post_user_routinglanguages(user_id, body)



Add routing language to user



Wraps POST /api/v2/users/{userId}/routinglanguages 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UserRoutingLanguagePost() # UserRoutingLanguagePost | Language

try:
    # Add routing language to user
    api_response = api_instance.post_user_routinglanguages(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_user_routinglanguages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingLanguagePost**](UserRoutingLanguagePost.html)| Language |  |
{: class="table table-striped"}

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage.html)

<a name="post_user_routingskills"></a>

## [**UserRoutingSkill**](UserRoutingSkill.html) post_user_routingskills(user_id, body)



Add routing skill to user



Wraps POST /api/v2/users/{userId}/routingskills 

Requires ALL permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->post_user_routingskills: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->put_routing_email_domain_route: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_name** | **str**| email domain |  |
| **route_id** | **str**| route ID |  |
| **body** | [**InboundRoute**](InboundRoute.html)| Route |  |
{: class="table table-striped"}

### Return type

[**InboundRoute**](InboundRoute.html)

<a name="put_routing_email_outbound_domain_activation"></a>

## [**EmailOutboundDomainResult**](EmailOutboundDomainResult.html) put_routing_email_outbound_domain_activation(domain_id)



Request an activation status (cname + dkim) update of an outbound domain



Wraps PUT /api/v2/routing/email/outbound/domains/{domainId}/activation 

Requires ALL permissions: 

* routing:email:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
domain_id = 'domain_id_example' # str | domain ID

try:
    # Request an activation status (cname + dkim) update of an outbound domain
    api_response = api_instance.put_routing_email_outbound_domain_activation(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_email_outbound_domain_activation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| domain ID |  |
{: class="table table-striped"}

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult.html)

<a name="put_routing_message_recipient"></a>

## [**Recipient**](Recipient.html) put_routing_message_recipient(recipient_id, body)



Update a recipient



Wraps PUT /api/v2/routing/message/recipients/{recipientId} 

Requires ALL permissions: 

* routing:message:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
recipient_id = 'recipient_id_example' # str | Recipient ID
body = PureCloudPlatformClientV2.Recipient() # Recipient | Recipient

try:
    # Update a recipient
    api_response = api_instance.put_routing_message_recipient(recipient_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_message_recipient: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recipient_id** | **str**| Recipient ID |  |
| **body** | [**Recipient**](Recipient.html)| Recipient |  |
{: class="table table-striped"}

### Return type

[**Recipient**](Recipient.html)

<a name="put_routing_queue"></a>

## [**Queue**](Queue.html) put_routing_queue(queue_id, body)



Update a queue



Wraps PUT /api/v2/routing/queues/{queueId} 

Requires ANY permissions: 

* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
queue_id = 'queue_id_example' # str | Queue ID
body = PureCloudPlatformClientV2.QueueRequest() # QueueRequest | Queue

try:
    # Update a queue
    api_response = api_instance.put_routing_queue(queue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **body** | [**QueueRequest**](QueueRequest.html)| Queue |  |
{: class="table table-striped"}

### Return type

[**Queue**](Queue.html)

<a name="put_routing_settings"></a>

## [**RoutingSettings**](RoutingSettings.html) put_routing_settings(body)



Update an organization's routing settings



Wraps PUT /api/v2/routing/settings 

Requires ANY permissions: 

* routing:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.RoutingSettings() # RoutingSettings | Organization Settings

try:
    # Update an organization's routing settings
    api_response = api_instance.put_routing_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoutingSettings**](RoutingSettings.html)| Organization Settings |  |
{: class="table table-striped"}

### Return type

[**RoutingSettings**](RoutingSettings.html)

<a name="put_routing_settings_transcription"></a>

## [**TranscriptionSettings**](TranscriptionSettings.html) put_routing_settings_transcription(body)



Update Transcription Settings



Wraps PUT /api/v2/routing/settings/transcription 

Requires ANY permissions: 

* routing:transcriptionSettings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.TranscriptionSettings() # TranscriptionSettings | Organization Settings

try:
    # Update Transcription Settings
    api_response = api_instance.put_routing_settings_transcription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_settings_transcription: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptionSettings**](TranscriptionSettings.html)| Organization Settings |  |
{: class="table table-striped"}

### Return type

[**TranscriptionSettings**](TranscriptionSettings.html)

<a name="put_routing_sms_phonenumber"></a>

## [**SmsPhoneNumber**](SmsPhoneNumber.html) put_routing_sms_phonenumber(address_id, body)



Update a phone number provisioned for SMS.



Wraps PUT /api/v2/routing/sms/phonenumbers/{addressId} 

Requires ALL permissions: 

* sms:phoneNumber:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
address_id = 'address_id_example' # str | Address ID
body = PureCloudPlatformClientV2.SmsPhoneNumber() # SmsPhoneNumber | SmsPhoneNumber

try:
    # Update a phone number provisioned for SMS.
    api_response = api_instance.put_routing_sms_phonenumber(address_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_sms_phonenumber: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **address_id** | **str**| Address ID |  |
| **body** | [**SmsPhoneNumber**](SmsPhoneNumber.html)| SmsPhoneNumber |  |
{: class="table table-striped"}

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber.html)

<a name="put_routing_user_utilization"></a>

## [**AgentMaxUtilization**](AgentMaxUtilization.html) put_routing_user_utilization(user_id, body)



Update the user's max utilization settings.  Include only those media types requiring custom configuration.



Wraps PUT /api/v2/routing/users/{userId}/utilization 

Requires ANY permissions: 

* routing:utilization:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.Utilization() # Utilization | utilization

try:
    # Update the user's max utilization settings.  Include only those media types requiring custom configuration.
    api_response = api_instance.put_routing_user_utilization(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_user_utilization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**Utilization**](Utilization.html)| utilization |  |
{: class="table table-striped"}

### Return type

[**AgentMaxUtilization**](AgentMaxUtilization.html)

<a name="put_routing_utilization"></a>

## [**Utilization**](Utilization.html) put_routing_utilization(body)



Update the organization-wide max utilization settings.  Include only those media types requiring custom configuration.



Wraps PUT /api/v2/routing/utilization 

Requires ALL permissions: 

* routing:utilization:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
body = PureCloudPlatformClientV2.Utilization() # Utilization | utilization

try:
    # Update the organization-wide max utilization settings.  Include only those media types requiring custom configuration.
    api_response = api_instance.put_routing_utilization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_utilization: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:wrapupCode:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->put_routing_wrapupcode: %s\n" % e)
```

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

Requires ALL permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RoutingApi->put_user_routingskill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
| **body** | [**UserRoutingSkill**](UserRoutingSkill.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserRoutingSkill**](UserRoutingSkill.html)

<a name="put_user_routingskills_bulk"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) put_user_routingskills_bulk(user_id, body)



Replace all routing skills assigned to a user



Wraps PUT /api/v2/users/{userId}/routingskills/bulk 

Requires ANY permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RoutingApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserRoutingSkillPost()] # list[UserRoutingSkillPost] | Skill

try:
    # Replace all routing skills assigned to a user
    api_response = api_instance.put_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

