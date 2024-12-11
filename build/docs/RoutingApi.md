# RoutingApi

## PureCloudPlatformClientV2.RoutingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_routing_assessment**](#delete_routing_assessment) | Delete single benefit assessment.|
|[**delete_routing_directroutingbackup_settings_me**](#delete_routing_directroutingbackup_settings_me) | Delete the user&#39;s Direct Routing Backup settings and revert to the Direct Routing Queue default.|
|[**delete_routing_email_domain**](#delete_routing_email_domain) | Delete a domain|
|[**delete_routing_email_domain_route**](#delete_routing_email_domain_route) | Delete a route|
|[**delete_routing_email_outbound_domain**](#delete_routing_email_outbound_domain) | Delete an outbound domain|
|[**delete_routing_language**](#delete_routing_language) | Delete a routing language|
|[**delete_routing_predictor**](#delete_routing_predictor) | Delete single predictor.|
|[**delete_routing_queue**](#delete_routing_queue) | Delete a queue|
|[**delete_routing_queue_member**](#delete_routing_queue_member) | Delete a queue member.|
|[**delete_routing_queue_user**](#delete_routing_queue_user) | DEPRECATED: use DELETE /routing/queues/{queueId}/members/{memberId}.  Delete queue member.|
|[**delete_routing_queue_wrapupcode**](#delete_routing_queue_wrapupcode) | Delete a wrap-up code from a queue|
|[**delete_routing_settings**](#delete_routing_settings) | Delete an organization&#39;s routing settings|
|[**delete_routing_skill**](#delete_routing_skill) | Delete Routing Skill|
|[**delete_routing_skillgroup**](#delete_routing_skillgroup) | Remove skill group definition|
|[**delete_routing_sms_address**](#delete_routing_sms_address) | Delete an Address by Id for SMS|
|[**delete_routing_sms_phonenumber**](#delete_routing_sms_phonenumber) | Delete a phone number provisioned for SMS.|
|[**delete_routing_user_directroutingbackup_settings**](#delete_routing_user_directroutingbackup_settings) | Delete the user&#39;s Direct Routing Backup settings and revert to the Direct Routing Queue default.|
|[**delete_routing_user_utilization**](#delete_routing_user_utilization) | Delete the user&#39;s max utilization settings and revert to the organization-wide default.|
|[**delete_routing_utilization**](#delete_routing_utilization) | Delete the organization-wide max utilization settings and revert to the system default.|
|[**delete_routing_utilization_label**](#delete_routing_utilization_label) | Delete a utilization label|
|[**delete_routing_utilization_tag**](#delete_routing_utilization_tag) | Delete an utilization tag|
|[**delete_routing_wrapupcode**](#delete_routing_wrapupcode) | Delete wrap-up code|
|[**delete_user_routinglanguage**](#delete_user_routinglanguage) | Remove a routing language from a user|
|[**delete_user_routingskill**](#delete_user_routingskill) | Remove a routing skill from a user|
|[**get_routing_assessment**](#get_routing_assessment) | Retrieve a single benefit assessment.|
|[**get_routing_assessments**](#get_routing_assessments) | Retrieve all benefit assessments.|
|[**get_routing_assessments_job**](#get_routing_assessments_job) | Retrieve a single benefit assessments job.|
|[**get_routing_assessments_jobs**](#get_routing_assessments_jobs) | Retrieve all benefit assessment jobs.|
|[**get_routing_availablemediatypes**](#get_routing_availablemediatypes) | Get available media types|
|[**get_routing_directroutingbackup_settings_me**](#get_routing_directroutingbackup_settings_me) | Get the user&#39;s Direct Routing Backup settings.|
|[**get_routing_email_domain**](#get_routing_email_domain) | Get domain|
|[**get_routing_email_domain_route**](#get_routing_email_domain_route) | Get a route|
|[**get_routing_email_domain_routes**](#get_routing_email_domain_routes) | Get routes|
|[**get_routing_email_domains**](#get_routing_email_domains) | Get domains|
|[**get_routing_email_outbound_domain**](#get_routing_email_outbound_domain) | Get domain|
|[**get_routing_email_outbound_domain_activation**](#get_routing_email_outbound_domain_activation) | Get activation status (cname + dkim) of an outbound domain|
|[**get_routing_email_outbound_domain_search**](#get_routing_email_outbound_domain_search) | Search a domain across organizations|
|[**get_routing_email_outbound_domains**](#get_routing_email_outbound_domains) | Get outbound domains|
|[**get_routing_email_setup**](#get_routing_email_setup) | Get email setup|
|[**get_routing_language**](#get_routing_language) | Get a routing language|
|[**get_routing_languages**](#get_routing_languages) | Get the list of supported languages.|
|[**get_routing_message_recipient**](#get_routing_message_recipient) | Get a recipient|
|[**get_routing_message_recipients**](#get_routing_message_recipients) | Get recipients|
|[**get_routing_predictor**](#get_routing_predictor) | Retrieve a single predictor.|
|[**get_routing_predictor_model_features**](#get_routing_predictor_model_features) | Retrieve Predictor Model Features.|
|[**get_routing_predictor_models**](#get_routing_predictor_models) | Retrieve Predictor Models and Top Features.|
|[**get_routing_predictors**](#get_routing_predictors) | Retrieve all predictors.|
|[**get_routing_predictors_keyperformanceindicators**](#get_routing_predictors_keyperformanceindicators) | Get a list of Key Performance Indicators|
|[**get_routing_queue**](#get_routing_queue) | Get details about this queue.|
|[**get_routing_queue_assistant**](#get_routing_queue_assistant) | Get an assistant associated with a queue.|
|[**get_routing_queue_comparisonperiod**](#get_routing_queue_comparisonperiod) | Get a Comparison Period.|
|[**get_routing_queue_comparisonperiods**](#get_routing_queue_comparisonperiods) | Get list of comparison periods|
|[**get_routing_queue_estimatedwaittime**](#get_routing_queue_estimatedwaittime) | Get Estimated Wait Time|
|[**get_routing_queue_mediatype_estimatedwaittime**](#get_routing_queue_mediatype_estimatedwaittime) | Get Estimated Wait Time|
|[**get_routing_queue_members**](#get_routing_queue_members) | Get the members of this queue.|
|[**get_routing_queue_users**](#get_routing_queue_users) | DEPRECATED: use GET /routing/queues/{queueId}/members.  Get the members of this queue.|
|[**get_routing_queue_wrapupcodes**](#get_routing_queue_wrapupcodes) | Get the wrap-up codes for a queue|
|[**get_routing_queues**](#get_routing_queues) | Get list of queues.|
|[**get_routing_queues_divisionviews**](#get_routing_queues_divisionviews) | Get a paged listing of simplified queue objects, filterable by name, queue ID(s), or division ID(s).|
|[**get_routing_queues_divisionviews_all**](#get_routing_queues_divisionviews_all) | Get a paged listing of simplified queue objects, sorted by name.  Can be used to get a digest of all queues in an organization.|
|[**get_routing_queues_me**](#get_routing_queues_me) | Get a paged listing of queues the user is a member of.|
|[**get_routing_settings**](#get_routing_settings) | Get an organization&#39;s routing settings|
|[**get_routing_settings_contactcenter**](#get_routing_settings_contactcenter) | Get Contact Center Settings|
|[**get_routing_settings_transcription**](#get_routing_settings_transcription) | Get Transcription Settings|
|[**get_routing_skill**](#get_routing_skill) | Get Routing Skill|
|[**get_routing_skillgroup**](#get_routing_skillgroup) | Get skill group|
|[**get_routing_skillgroup_members**](#get_routing_skillgroup_members) | Get skill group members|
|[**get_routing_skillgroup_members_divisions**](#get_routing_skillgroup_members_divisions) | Get list of member divisions for this skill group.|
|[**get_routing_skillgroups**](#get_routing_skillgroups) | Get skill group listing|
|[**get_routing_skills**](#get_routing_skills) | Get the list of routing skills.|
|[**get_routing_sms_address**](#get_routing_sms_address) | Get an Address by Id for SMS|
|[**get_routing_sms_addresses**](#get_routing_sms_addresses) | Get a list of Addresses for SMS|
|[**get_routing_sms_availablephonenumbers**](#get_routing_sms_availablephonenumbers) | Get a list of available phone numbers for SMS provisioning.|
|[**get_routing_sms_phonenumber**](#get_routing_sms_phonenumber) | Get a phone number provisioned for SMS.|
|[**get_routing_sms_phonenumbers**](#get_routing_sms_phonenumbers) | Get a list of provisioned phone numbers.|
|[**get_routing_user_directroutingbackup_settings**](#get_routing_user_directroutingbackup_settings) | Get the user&#39;s Direct Routing Backup settings.|
|[**get_routing_user_utilization**](#get_routing_user_utilization) | Get the user&#39;s max utilization settings.  If not configured, the organization-wide default is returned.|
|[**get_routing_utilization**](#get_routing_utilization) | Get the organization-wide max utilization settings.|
|[**get_routing_utilization_label**](#get_routing_utilization_label) | Get details about this utilization label|
|[**get_routing_utilization_label_agents**](#get_routing_utilization_label_agents) | Get list of agent ids associated with a utilization label|
|[**get_routing_utilization_labels**](#get_routing_utilization_labels) | Get list of utilization labels|
|[**get_routing_utilization_tag**](#get_routing_utilization_tag) | Get details about this utilization tag|
|[**get_routing_utilization_tag_agents**](#get_routing_utilization_tag_agents) | Get list of agent ids associated with a utilization tag|
|[**get_routing_utilization_tags**](#get_routing_utilization_tags) | Get list of utilization tags|
|[**get_routing_wrapupcode**](#get_routing_wrapupcode) | Get details about this wrap-up code.|
|[**get_routing_wrapupcodes**](#get_routing_wrapupcodes) | Get list of wrapup codes.|
|[**get_routing_wrapupcodes_divisionview**](#get_routing_wrapupcodes_divisionview) | Get a simplified wrap-up code.|
|[**get_routing_wrapupcodes_divisionviews**](#get_routing_wrapupcodes_divisionviews) | Get a paged listing of simplified wrapup code objects, filterable by name, wrapup code ID(s), or division ID(s).|
|[**get_user_queues**](#get_user_queues) | Get queues for user|
|[**get_user_routinglanguages**](#get_user_routinglanguages) | List routing languages assigned to a user|
|[**get_user_routingskills**](#get_user_routingskills) | List routing skills assigned to a user|
|[**get_user_skillgroups**](#get_user_skillgroups) | Get skill groups for a user|
|[**patch_routing_conversation**](#patch_routing_conversation) | Update attributes of an in-queue conversation|
|[**patch_routing_email_domain**](#patch_routing_email_domain) | Update domain settings|
|[**patch_routing_email_domain_validate**](#patch_routing_email_domain_validate) | Validate domain settings|
|[**patch_routing_predictor**](#patch_routing_predictor) | Update single predictor.|
|[**patch_routing_queue_member**](#patch_routing_queue_member) | Update the ring number OR joined status for a queue member.|
|[**patch_routing_queue_members**](#patch_routing_queue_members) | Join or unjoin a set of users for a queue|
|[**patch_routing_queue_user**](#patch_routing_queue_user) | DEPRECATED: use PATCH /routing/queues/{queueId}/members/{memberId}.  Update the ring number OR joined status for a User in a Queue.|
|[**patch_routing_queue_users**](#patch_routing_queue_users) | DEPRECATED: use PATCH /routing/queues/{queueId}/members.  Join or unjoin a set of users for a queue.|
|[**patch_routing_settings_contactcenter**](#patch_routing_settings_contactcenter) | Update Contact Center Settings|
|[**patch_routing_settings_transcription**](#patch_routing_settings_transcription) | Patch Transcription Settings|
|[**patch_routing_skillgroup**](#patch_routing_skillgroup) | Update skill group definition|
|[**patch_user_queue**](#patch_user_queue) | Join or unjoin a queue for a user|
|[**patch_user_queues**](#patch_user_queues) | Join or unjoin a set of queues for a user|
|[**patch_user_routinglanguage**](#patch_user_routinglanguage) | Update an assigned routing language&#39;s proficiency|
|[**patch_user_routinglanguages_bulk**](#patch_user_routinglanguages_bulk) | Assign multiple routing languages to a user. Max 50 routing languages in request body|
|[**patch_user_routingskills_bulk**](#patch_user_routingskills_bulk) | Assign multiple routing skills to a user|
|[**post_analytics_queues_observations_query**](#post_analytics_queues_observations_query) | Query for queue observations|
|[**post_analytics_routing_activity_query**](#post_analytics_routing_activity_query) | Query for user activity observations|
|[**post_routing_assessments**](#post_routing_assessments) | Create a benefit assessment.|
|[**post_routing_assessments_jobs**](#post_routing_assessments_jobs) | Create a benefit assessment job.|
|[**post_routing_email_domain_routes**](#post_routing_email_domain_routes) | Create a route|
|[**post_routing_email_domain_testconnection**](#post_routing_email_domain_testconnection) | Tests the custom SMTP server integration connection set on this domain|
|[**post_routing_email_domains**](#post_routing_email_domains) | Create a domain|
|[**post_routing_email_outbound_domains**](#post_routing_email_outbound_domains) | Create a domain|
|[**post_routing_email_outbound_domains_simulated**](#post_routing_email_outbound_domains_simulated) | Create a simulated domain|
|[**post_routing_languages**](#post_routing_languages) | Create Language|
|[**post_routing_predictors**](#post_routing_predictors) | Create a predictor.|
|[**post_routing_queue_members**](#post_routing_queue_members) | Bulk add or delete up to 100 queue members|
|[**post_routing_queue_users**](#post_routing_queue_users) | DEPRECATED: use POST /routing/queues/{queueId}/members.  Bulk add or delete up to 100 queue members.|
|[**post_routing_queue_wrapupcodes**](#post_routing_queue_wrapupcodes) | Add up to 100 wrap-up codes to a queue|
|[**post_routing_queues**](#post_routing_queues) | Create a queue|
|[**post_routing_skillgroup_members_divisions**](#post_routing_skillgroup_members_divisions) | Add or remove member divisions for this skill group.|
|[**post_routing_skillgroups**](#post_routing_skillgroups) | Create a skill group|
|[**post_routing_skills**](#post_routing_skills) | Create Skill|
|[**post_routing_sms_addresses**](#post_routing_sms_addresses) | Provision an Address for SMS|
|[**post_routing_sms_phonenumbers**](#post_routing_sms_phonenumbers) | Provision a phone number for SMS|
|[**post_routing_sms_phonenumbers_alphanumeric**](#post_routing_sms_phonenumbers_alphanumeric) | Provision an alphanumeric number for SMS|
|[**post_routing_sms_phonenumbers_import**](#post_routing_sms_phonenumbers_import) | Imports a phone number for SMS|
|[**post_routing_utilization_labels**](#post_routing_utilization_labels) | Create a utilization label|
|[**post_routing_utilization_tags**](#post_routing_utilization_tags) | Create an utilization tag|
|[**post_routing_wrapupcodes**](#post_routing_wrapupcodes) | Create a wrap-up code|
|[**post_user_routinglanguages**](#post_user_routinglanguages) | Assign a routing language to a user|
|[**post_user_routingskills**](#post_user_routingskills) | Assign a routing skill to a user|
|[**put_routing_directroutingbackup_settings_me**](#put_routing_directroutingbackup_settings_me) | Update the user&#39;s Direct Routing Backup settings.|
|[**put_routing_email_domain_route**](#put_routing_email_domain_route) | Update a route|
|[**put_routing_email_outbound_domain_activation**](#put_routing_email_outbound_domain_activation) | Request an activation status (cname + dkim) update of an outbound domain|
|[**put_routing_message_recipient**](#put_routing_message_recipient) | Update a recipient|
|[**put_routing_queue**](#put_routing_queue) | Update a queue|
|[**put_routing_settings**](#put_routing_settings) | Update an organization&#39;s routing settings|
|[**put_routing_settings_transcription**](#put_routing_settings_transcription) | Update Transcription Settings|
|[**put_routing_sms_phonenumber**](#put_routing_sms_phonenumber) | Update a phone number provisioned for SMS.|
|[**put_routing_user_directroutingbackup_settings**](#put_routing_user_directroutingbackup_settings) | Update the user&#39;s Direct Routing Backup settings.|
|[**put_routing_user_utilization**](#put_routing_user_utilization) | Update the user&#39;s max utilization settings.  Include only those media types requiring custom configuration.|
|[**put_routing_utilization**](#put_routing_utilization) | Update the organization-wide max utilization settings.  Include only those media types requiring custom configuration.|
|[**put_routing_utilization_label**](#put_routing_utilization_label) | Update a utilization label|
|[**put_routing_wrapupcode**](#put_routing_wrapupcode) | Update wrap-up code|
|[**put_user_routingskill**](#put_user_routingskill) | Update an assigned routing skill&#39;s proficiency|
|[**put_user_routingskills_bulk**](#put_user_routingskills_bulk) | Assign multiple routing skills to a user, replacing any current assignments|



## delete_routing_assessment

>  delete_routing_assessment(assessment_id)


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

### Return type

void (empty response body)


## delete_routing_directroutingbackup_settings_me

>  delete_routing_directroutingbackup_settings_me()


Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.

Wraps DELETE /api/v2/routing/directroutingbackup/settings/me 

Requires ANY permissions: 

* routing:directRoutingBackup:selfDelete

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
    # Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.
    api_instance.delete_routing_directroutingbackup_settings_me()
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_directroutingbackup_settings_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_routing_email_domain

>  delete_routing_email_domain(domain_id)


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

### Return type

void (empty response body)


## delete_routing_email_domain_route

>  delete_routing_email_domain_route(domain_name, route_id)


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

### Return type

void (empty response body)


## delete_routing_email_outbound_domain

>  delete_routing_email_outbound_domain(domain_id)


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

### Return type

void (empty response body)


## delete_routing_language

>  delete_routing_language(language_id)


Delete a routing language

Wraps DELETE /api/v2/routing/languages/{languageId} 

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
language_id = 'language_id_example' # str | Language ID

try:
    # Delete a routing language
    api_instance.delete_routing_language(language_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID |  |

### Return type

void (empty response body)


## delete_routing_predictor

>  delete_routing_predictor(predictor_id)


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

### Return type

void (empty response body)


## delete_routing_queue

>  delete_routing_queue(queue_id, force_delete=force_delete)


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

### Return type

void (empty response body)


## delete_routing_queue_member

>  delete_routing_queue_member(queue_id, member_id)


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

### Return type

void (empty response body)


## delete_routing_queue_user

>  delete_routing_queue_user(queue_id, member_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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

### Return type

void (empty response body)


## delete_routing_queue_wrapupcode

>  delete_routing_queue_wrapupcode(queue_id, code_id)


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

### Return type

void (empty response body)


## delete_routing_settings

>  delete_routing_settings()


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


## delete_routing_skill

>  delete_routing_skill(skill_id)


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

### Return type

void (empty response body)


## delete_routing_skillgroup

>  delete_routing_skillgroup(skill_group_id)


Remove skill group definition

Wraps DELETE /api/v2/routing/skillgroups/{skillGroupId} 

Requires ANY permissions: 

* routing:skillGroup:delete

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
skill_group_id = 'skill_group_id_example' # str | Skill Group ID

try:
    # Remove skill group definition
    api_instance.delete_routing_skillgroup(skill_group_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_skillgroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_group_id** | **str**| Skill Group ID |  |

### Return type

void (empty response body)


## delete_routing_sms_address

>  delete_routing_sms_address(address_id)


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

### Return type

void (empty response body)


## delete_routing_sms_phonenumber

>  delete_routing_sms_phonenumber(phone_number_id)


Delete a phone number provisioned for SMS.

Wraps DELETE /api/v2/routing/sms/phonenumbers/{phoneNumberId} 

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
phone_number_id = 'phone_number_id_example' # str | phone number

try:
    # Delete a phone number provisioned for SMS.
    api_instance.delete_routing_sms_phonenumber(phone_number_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_sms_phonenumber: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_number_id** | **str**| phone number |  |

### Return type

void (empty response body)


## delete_routing_user_directroutingbackup_settings

>  delete_routing_user_directroutingbackup_settings(user_id)


Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.

Wraps DELETE /api/v2/routing/users/{userId}/directroutingbackup/settings 

Requires ANY permissions: 

* routing:directRoutingBackup:delete

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
    # Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.
    api_instance.delete_routing_user_directroutingbackup_settings(user_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_user_directroutingbackup_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

void (empty response body)


## delete_routing_user_utilization

>  delete_routing_user_utilization(user_id)


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

### Return type

void (empty response body)


## delete_routing_utilization

>  delete_routing_utilization()


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


## delete_routing_utilization_label

>  delete_routing_utilization_label(label_id, force_delete=force_delete)


Delete a utilization label

Wraps DELETE /api/v2/routing/utilization/labels/{labelId} 

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
label_id = 'label_id_example' # str | Utilization Label ID
force_delete = False # bool | Remove all label usages (if found) without warning (optional) (default to False)

try:
    # Delete a utilization label
    api_instance.delete_routing_utilization_label(label_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_utilization_label: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **label_id** | **str**| Utilization Label ID |  |
| **force_delete** | **bool**| Remove all label usages (if found) without warning | [optional] [default to False] |

### Return type

void (empty response body)


## delete_routing_utilization_tag

>  delete_routing_utilization_tag(tag_id, force_delete=force_delete)


Delete an utilization tag

delete_routing_utilization_tag is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/routing/utilization/tags/{tagId} 

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
tag_id = 'tag_id_example' # str | Utilization Tag ID
force_delete = False # bool | Remove all tag usages (if found) without warning (optional) (default to False)

try:
    # Delete an utilization tag
    api_instance.delete_routing_utilization_tag(tag_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_routing_utilization_tag: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **tag_id** | **str**| Utilization Tag ID |  |
| **force_delete** | **bool**| Remove all tag usages (if found) without warning | [optional] [default to False] |

### Return type

void (empty response body)


## delete_routing_wrapupcode

>  delete_routing_wrapupcode(code_id)


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

### Return type

void (empty response body)


## delete_user_routinglanguage

>  delete_user_routinglanguage(user_id, language_id)


Remove a routing language from a user

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
    # Remove a routing language from a user
    api_instance.delete_user_routinglanguage(user_id, language_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_user_routinglanguage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **language_id** | **str**| languageId |  |

### Return type

void (empty response body)


## delete_user_routingskill

>  delete_user_routingskill(user_id, skill_id)


Remove a routing skill from a user

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
    # Remove a routing skill from a user
    api_instance.delete_user_routingskill(user_id, skill_id)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_user_routingskill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |

### Return type

void (empty response body)


## get_routing_assessment

> [**BenefitAssessment**](BenefitAssessment) get_routing_assessment(assessment_id)


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

### Return type

[**BenefitAssessment**](BenefitAssessment)


## get_routing_assessments

> [**AssessmentListing**](AssessmentListing) get_routing_assessments(before=before, after=after, limit=limit, page_size=page_size, queue_id=queue_id)


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
| **queue_id** | [**list[str]**](str)| Queue ID(s) to filter assessments by. | [optional]  |

### Return type

[**AssessmentListing**](AssessmentListing)


## get_routing_assessments_job

> [**BenefitAssessmentJob**](BenefitAssessmentJob) get_routing_assessments_job(job_id)


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

### Return type

[**BenefitAssessmentJob**](BenefitAssessmentJob)


## get_routing_assessments_jobs

> [**AssessmentJobListing**](AssessmentJobListing) get_routing_assessments_jobs(division_id=division_id)


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
| **division_id** | [**list[str]**](str)| Division ID(s) to filter assessment jobs by. | [optional]  |

### Return type

[**AssessmentJobListing**](AssessmentJobListing)


## get_routing_availablemediatypes

> [**AvailableMediaTypeEntityListing**](AvailableMediaTypeEntityListing) get_routing_availablemediatypes()


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

[**AvailableMediaTypeEntityListing**](AvailableMediaTypeEntityListing)


## get_routing_directroutingbackup_settings_me

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) get_routing_directroutingbackup_settings_me()


Get the user's Direct Routing Backup settings.

Wraps GET /api/v2/routing/directroutingbackup/settings/me 

Requires ANY permissions: 

* routing:directRoutingBackup:selfView

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
    # Get the user's Direct Routing Backup settings.
    api_response = api_instance.get_routing_directroutingbackup_settings_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_directroutingbackup_settings_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## get_routing_email_domain

> [**InboundDomain**](InboundDomain) get_routing_email_domain(domain_id)


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

### Return type

[**InboundDomain**](InboundDomain)


## get_routing_email_domain_route

> [**InboundRoute**](InboundRoute) get_routing_email_domain_route(domain_name, route_id)


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

### Return type

[**InboundRoute**](InboundRoute)


## get_routing_email_domain_routes

> [**InboundRouteEntityListing**](InboundRouteEntityListing) get_routing_email_domain_routes(domain_name, page_size=page_size, page_number=page_number, pattern=pattern)


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

### Return type

[**InboundRouteEntityListing**](InboundRouteEntityListing)


## get_routing_email_domains

> [**InboundDomainEntityListing**](InboundDomainEntityListing) get_routing_email_domains(page_size=page_size, page_number=page_number, exclude_status=exclude_status, filter=filter)


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
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
exclude_status = False # bool | Exclude MX record data (optional) (default to False)
filter = 'filter_example' # str | Optional search filter (optional)

try:
    # Get domains
    api_response = api_instance.get_routing_email_domains(page_size=page_size, page_number=page_number, exclude_status=exclude_status, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **exclude_status** | **bool**| Exclude MX record data | [optional] [default to False] |
| **filter** | **str**| Optional search filter | [optional]  |

### Return type

[**InboundDomainEntityListing**](InboundDomainEntityListing)


## get_routing_email_outbound_domain

> [**OutboundDomain**](OutboundDomain) get_routing_email_outbound_domain(domain_id)


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

### Return type

[**OutboundDomain**](OutboundDomain)


## get_routing_email_outbound_domain_activation

> [**EmailOutboundDomainResult**](EmailOutboundDomainResult) get_routing_email_outbound_domain_activation(domain_id)


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

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult)


## get_routing_email_outbound_domain_search

> [**OutboundDomain**](OutboundDomain) get_routing_email_outbound_domain_search(domain_id)


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

### Return type

[**OutboundDomain**](OutboundDomain)


## get_routing_email_outbound_domains

> [**OutboundDomainEntityListing**](OutboundDomainEntityListing) get_routing_email_outbound_domains(filter=filter)


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
filter = 'filter_example' # str | Optional search filter (optional)

try:
    # Get outbound domains
    api_response = api_instance.get_routing_email_outbound_domains(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_email_outbound_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Optional search filter | [optional]  |

### Return type

[**OutboundDomainEntityListing**](OutboundDomainEntityListing)


## get_routing_email_setup

> [**EmailSetup**](EmailSetup) get_routing_email_setup()


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

[**EmailSetup**](EmailSetup)


## get_routing_language

> [**Language**](Language) get_routing_language(language_id)


Get a routing language

Wraps GET /api/v2/routing/languages/{languageId} 

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
language_id = 'language_id_example' # str | Language ID

try:
    # Get a routing language
    api_response = api_instance.get_routing_language(language_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID |  |

### Return type

[**Language**](Language)


## get_routing_languages

> [**LanguageEntityListing**](LanguageEntityListing) get_routing_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, id=id)


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
| **id** | [**list[str]**](str)| id | [optional]  |

### Return type

[**LanguageEntityListing**](LanguageEntityListing)


## get_routing_message_recipient

> [**Recipient**](Recipient) get_routing_message_recipient(recipient_id)


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

### Return type

[**Recipient**](Recipient)


## get_routing_message_recipients

> [**RecipientListing**](RecipientListing) get_routing_message_recipients(messenger_type=messenger_type, name=name, page_size=page_size, page_number=page_number)


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
name = 'name_example' # str | Recipient Name (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get recipients
    api_response = api_instance.get_routing_message_recipients(messenger_type=messenger_type, name=name, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_message_recipients: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messenger_type** | **str**| Messenger Type | [optional] <br />**Values**: sms, facebook, twitter, whatsapp, open, instagram, apple |
| **name** | **str**| Recipient Name | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**RecipientListing**](RecipientListing)


## get_routing_predictor

> [**Predictor**](Predictor) get_routing_predictor(predictor_id)


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

### Return type

[**Predictor**](Predictor)


## get_routing_predictor_model_features

> [**PredictorModelFeatureListing**](PredictorModelFeatureListing) get_routing_predictor_model_features(predictor_id, model_id)


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

### Return type

[**PredictorModelFeatureListing**](PredictorModelFeatureListing)


## get_routing_predictor_models

> [**PredictorModels**](PredictorModels) get_routing_predictor_models(predictor_id)


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

### Return type

[**PredictorModels**](PredictorModels)


## get_routing_predictors

> [**PredictorListing**](PredictorListing) get_routing_predictors(before=before, after=after, limit=limit, page_size=page_size, queue_id=queue_id)


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
| **queue_id** | [**list[str]**](str)| Comma-separated list of queue Ids to filter by. | [optional]  |

### Return type

[**PredictorListing**](PredictorListing)


## get_routing_predictors_keyperformanceindicators

> [**list[KeyPerformanceIndicator]**](KeyPerformanceIndicator) get_routing_predictors_keyperformanceindicators(kpi_group=kpi_group, expand=expand)


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
expand = ['expand_example'] # list[str] | Parameter to request additional data to return in KPI payload (optional)

try:
    # Get a list of Key Performance Indicators
    api_response = api_instance.get_routing_predictors_keyperformanceindicators(kpi_group=kpi_group, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_predictors_keyperformanceindicators: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **kpi_group** | **str**| The Group of Key Performance Indicators to return | [optional] <br />**Values**: Standard, Custom |
| **expand** | [**list[str]**](str)| Parameter to request additional data to return in KPI payload | [optional] <br />**Values**: queues |

### Return type

[**list[KeyPerformanceIndicator]**](KeyPerformanceIndicator)


## get_routing_queue

> [**Queue**](Queue) get_routing_queue(queue_id)


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

### Return type

[**Queue**](Queue)


## get_routing_queue_assistant

> [**AssistantQueue**](AssistantQueue) get_routing_queue_assistant(queue_id, expand=expand)


Get an assistant associated with a queue.

Wraps GET /api/v2/routing/queues/{queueId}/assistant 

Requires ALL permissions: 

* assistants:queue:view

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
expand = 'expand_example' # str | Which fields, if any, to expand. (optional)

try:
    # Get an assistant associated with a queue.
    api_response = api_instance.get_routing_queue_assistant(queue_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_assistant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **expand** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: assistant |

### Return type

[**AssistantQueue**](AssistantQueue)


## get_routing_queue_comparisonperiod

> [**ComparisonPeriod**](ComparisonPeriod) get_routing_queue_comparisonperiod(queue_id, comparison_period_id)


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

### Return type

[**ComparisonPeriod**](ComparisonPeriod)


## get_routing_queue_comparisonperiods

> [**ComparisonPeriodListing**](ComparisonPeriodListing) get_routing_queue_comparisonperiods(queue_id)


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

### Return type

[**ComparisonPeriodListing**](ComparisonPeriodListing)


## get_routing_queue_estimatedwaittime

> [**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions) get_routing_queue_estimatedwaittime(queue_id, conversation_id=conversation_id)


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

### Return type

[**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions)


## get_routing_queue_mediatype_estimatedwaittime

> [**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions) get_routing_queue_mediatype_estimatedwaittime(queue_id, media_type, label_id=label_id)


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
label_id = 'label_id_example' # str | Unique id that represents the interaction label used with media type for EWT calculation (optional)

try:
    # Get Estimated Wait Time
    api_response = api_instance.get_routing_queue_mediatype_estimatedwaittime(queue_id, media_type, label_id=label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queue_mediatype_estimatedwaittime: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| queueId |  |
| **media_type** | **str**| mediaType | <br />**Values**: all, call, chat, callback, email, videoComm, message |
| **label_id** | **str**| Unique id that represents the interaction label used with media type for EWT calculation | [optional]  |

### Return type

[**EstimatedWaitTimePredictions**](EstimatedWaitTimePredictions)


## get_routing_queue_members

> [**QueueMemberEntityListing**](QueueMemberEntityListing) get_routing_queue_members(queue_id, page_number=page_number, page_size=page_size, sort_order=sort_order, expand=expand, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence, member_by=member_by, joined=joined)


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
name = 'name_example' # str | Filter by queue member name (contains-style search) (optional)
profile_skills = ['profile_skills_example'] # list[str] | Filter by profile skill (contains-style search) (optional)
skills = ['skills_example'] # list[str] | Filter by skill (contains-style search) (optional)
languages = ['languages_example'] # list[str] | Filter by language (contains-style search) (optional)
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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin |
| **name** | **str**| Filter by queue member name (contains-style search) | [optional]  |
| **profile_skills** | [**list[str]**](str)| Filter by profile skill (contains-style search) | [optional]  |
| **skills** | [**list[str]**](str)| Filter by skill (contains-style search) | [optional]  |
| **languages** | [**list[str]**](str)| Filter by language (contains-style search) | [optional]  |
| **routing_status** | [**list[str]**](str)| Filter by routing status | [optional]  |
| **presence** | [**list[str]**](str)| Filter by presence | [optional]  |
| **member_by** | **str**| Filter by member type | [optional] <br />**Values**: user, group |
| **joined** | **bool**| Filter by joined status | [optional] <br />**Values**: true, false |

### Return type

[**QueueMemberEntityListing**](QueueMemberEntityListing)


## get_routing_queue_users

> [**QueueMemberEntityListingV1**](QueueMemberEntityListingV1) get_routing_queue_users(queue_id, page_number=page_number, page_size=page_size, sort_order=sort_order, expand=expand, joined=joined, name=name, profile_skills=profile_skills, skills=skills, languages=languages, routing_status=routing_status, presence=presence)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin |
| **joined** | **bool**| Filter by joined status | [optional]  |
| **name** | **str**| Filter by queue member name | [optional]  |
| **profile_skills** | [**list[str]**](str)| Filter by profile skill | [optional]  |
| **skills** | [**list[str]**](str)| Filter by skill | [optional]  |
| **languages** | [**list[str]**](str)| Filter by language | [optional]  |
| **routing_status** | [**list[str]**](str)| Filter by routing status | [optional]  |
| **presence** | [**list[str]**](str)| Filter by presence | [optional]  |

### Return type

[**QueueMemberEntityListingV1**](QueueMemberEntityListingV1)


## get_routing_queue_wrapupcodes

> [**WrapupCodeEntityListing**](WrapupCodeEntityListing) get_routing_queue_wrapupcodes(queue_id, page_size=page_size, page_number=page_number)


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

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing)


## get_routing_queues

> [**QueueEntityListing**](QueueEntityListing) get_routing_queues(page_number=page_number, page_size=page_size, sort_order=sort_order, name=name, id=id, division_id=division_id, peer_id=peer_id, canned_response_library_id=canned_response_library_id, has_peer=has_peer)


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
name = 'name_example' # str | Include only queues with the given name (leading and trailing asterisks allowed) (optional)
id = ['id_example'] # list[str] | Include only queues with the specified ID(s) (optional)
division_id = ['division_id_example'] # list[str] | Include only queues in the specified division ID(s) (optional)
peer_id = ['peer_id_example'] # list[str] | Include only queues with the specified peer ID(s) (optional)
canned_response_library_id = 'canned_response_library_id_example' # str | Include only queues explicitly associated with the specified canned response library ID (optional)
has_peer = True # bool | Include only queues with a peer ID (optional)

try:
    # Get list of queues.
    api_response = api_instance.get_routing_queues(page_number=page_number, page_size=page_size, sort_order=sort_order, name=name, id=id, division_id=division_id, peer_id=peer_id, canned_response_library_id=canned_response_library_id, has_peer=has_peer)
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
| **name** | **str**| Include only queues with the given name (leading and trailing asterisks allowed) | [optional]  |
| **id** | [**list[str]**](str)| Include only queues with the specified ID(s) | [optional]  |
| **division_id** | [**list[str]**](str)| Include only queues in the specified division ID(s) | [optional]  |
| **peer_id** | [**list[str]**](str)| Include only queues with the specified peer ID(s) | [optional]  |
| **canned_response_library_id** | **str**| Include only queues explicitly associated with the specified canned response library ID | [optional]  |
| **has_peer** | **bool**| Include only queues with a peer ID | [optional]  |

### Return type

[**QueueEntityListing**](QueueEntityListing)


## get_routing_queues_divisionviews

> [**QueueEntityListing**](QueueEntityListing) get_routing_queues_divisionviews(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id, division_id=division_id)


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
| **id** | [**list[str]**](str)| Queue ID(s) | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |

### Return type

[**QueueEntityListing**](QueueEntityListing)


## get_routing_queues_divisionviews_all

> [**QueueEntityListing**](QueueEntityListing) get_routing_queues_divisionviews_all(page_size=page_size, page_number=page_number, sort_order=sort_order)


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

### Return type

[**QueueEntityListing**](QueueEntityListing)


## get_routing_queues_me

> [**UserQueueEntityListing**](UserQueueEntityListing) get_routing_queues_me(page_number=page_number, page_size=page_size, joined=joined, sort_order=sort_order)


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

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing)


## get_routing_settings

> [**RoutingSettings**](RoutingSettings) get_routing_settings()


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

[**RoutingSettings**](RoutingSettings)


## get_routing_settings_contactcenter

> [**ContactCenterSettings**](ContactCenterSettings) get_routing_settings_contactcenter()


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

[**ContactCenterSettings**](ContactCenterSettings)


## get_routing_settings_transcription

> [**TranscriptionSettings**](TranscriptionSettings) get_routing_settings_transcription()


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

[**TranscriptionSettings**](TranscriptionSettings)


## get_routing_skill

> [**RoutingSkill**](RoutingSkill) get_routing_skill(skill_id)


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

### Return type

[**RoutingSkill**](RoutingSkill)


## get_routing_skillgroup

> [**SkillGroup**](SkillGroup) get_routing_skillgroup(skill_group_id)


Get skill group

Wraps GET /api/v2/routing/skillgroups/{skillGroupId} 

Requires ANY permissions: 

* routing:skillGroup:view

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
skill_group_id = 'skill_group_id_example' # str | Skill Group ID

try:
    # Get skill group
    api_response = api_instance.get_routing_skillgroup(skill_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_skillgroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_group_id** | **str**| Skill Group ID |  |

### Return type

[**SkillGroup**](SkillGroup)


## get_routing_skillgroup_members

> [**SkillGroupMemberEntityListing**](SkillGroupMemberEntityListing) get_routing_skillgroup_members(skill_group_id, page_size=page_size, after=after, before=before, expand=expand)


Get skill group members

Wraps GET /api/v2/routing/skillgroups/{skillGroupId}/members 

Requires ANY permissions: 

* routing:skillGroup:view

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
skill_group_id = 'skill_group_id_example' # str | Skill Group ID
page_size = 25 # int | Page size (optional) (default to 25)
after = 'after_example' # str | The cursor that points to the next item (optional)
before = 'before_example' # str | The cursor that points to the previous item (optional)
expand = 'expand_example' # str | Expand the name on each user (optional)

try:
    # Get skill group members
    api_response = api_instance.get_routing_skillgroup_members(skill_group_id, page_size=page_size, after=after, before=before, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_skillgroup_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_group_id** | **str**| Skill Group ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **after** | **str**| The cursor that points to the next item | [optional]  |
| **before** | **str**| The cursor that points to the previous item | [optional]  |
| **expand** | **str**| Expand the name on each user | [optional] <br />**Values**: entities |

### Return type

[**SkillGroupMemberEntityListing**](SkillGroupMemberEntityListing)


## get_routing_skillgroup_members_divisions

> [**SkillGroupMemberDivisionList**](SkillGroupMemberDivisionList) get_routing_skillgroup_members_divisions(skill_group_id, expand=expand)


Get list of member divisions for this skill group.

Wraps GET /api/v2/routing/skillgroups/{skillGroupId}/members/divisions 

Requires ANY permissions: 

* routing:skillGroup:view

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
skill_group_id = 'skill_group_id_example' # str | Skill Group ID
expand = 'expand_example' # str | Expand the name on each user (optional)

try:
    # Get list of member divisions for this skill group.
    api_response = api_instance.get_routing_skillgroup_members_divisions(skill_group_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_skillgroup_members_divisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_group_id** | **str**| Skill Group ID |  |
| **expand** | **str**| Expand the name on each user | [optional] <br />**Values**: entities |

### Return type

[**SkillGroupMemberDivisionList**](SkillGroupMemberDivisionList)


## get_routing_skillgroups

> [**SkillGroupEntityListing**](SkillGroupEntityListing) get_routing_skillgroups(page_size=page_size, name=name, after=after, before=before)


Get skill group listing

Wraps GET /api/v2/routing/skillgroups 

Requires ANY permissions: 

* routing:skillGroup:view

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
name = 'name_example' # str | Return only skill group names whose names start with this value (case-insensitive matching) (optional)
after = 'after_example' # str | The cursor that points to the next item (optional)
before = 'before_example' # str | The cursor that points to the previous item (optional)

try:
    # Get skill group listing
    api_response = api_instance.get_routing_skillgroups(page_size=page_size, name=name, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_skillgroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Return only skill group names whose names start with this value (case-insensitive matching) | [optional]  |
| **after** | **str**| The cursor that points to the next item | [optional]  |
| **before** | **str**| The cursor that points to the previous item | [optional]  |

### Return type

[**SkillGroupEntityListing**](SkillGroupEntityListing)


## get_routing_skills

> [**SkillEntityListing**](SkillEntityListing) get_routing_skills(page_size=page_size, page_number=page_number, name=name, id=id)


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
| **id** | [**list[str]**](str)| id | [optional]  |

### Return type

[**SkillEntityListing**](SkillEntityListing)


## get_routing_sms_address

> [**SmsAddress**](SmsAddress) get_routing_sms_address(address_id)


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

### Return type

[**SmsAddress**](SmsAddress)


## get_routing_sms_addresses

> [**SmsAddressEntityListing**](SmsAddressEntityListing) get_routing_sms_addresses(page_size=page_size, page_number=page_number)


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

### Return type

[**SmsAddressEntityListing**](SmsAddressEntityListing)


## get_routing_sms_availablephonenumbers

> [**SMSAvailablePhoneNumberEntityListing**](SMSAvailablePhoneNumberEntityListing) get_routing_sms_availablephonenumbers(country_code, phone_number_type, region=region, city=city, area_code=area_code, pattern=pattern, address_requirement=address_requirement)


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

### Return type

[**SMSAvailablePhoneNumberEntityListing**](SMSAvailablePhoneNumberEntityListing)


## get_routing_sms_phonenumber

> [**SmsPhoneNumber**](SmsPhoneNumber) get_routing_sms_phonenumber(phone_number_id, expand=expand)


Get a phone number provisioned for SMS.

Wraps GET /api/v2/routing/sms/phonenumbers/{phoneNumberId} 

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
phone_number_id = 'phone_number_id_example' # str | phone number
expand = 'expand_example' # str | Expand response with additional information (optional)

try:
    # Get a phone number provisioned for SMS.
    api_response = api_instance.get_routing_sms_phonenumber(phone_number_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_phonenumber: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_number_id** | **str**| phone number |  |
| **expand** | **str**| Expand response with additional information | [optional] <br />**Values**: compliance, supportedContent |

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber)


## get_routing_sms_phonenumbers

> [**SmsPhoneNumberEntityListing**](SmsPhoneNumberEntityListing) get_routing_sms_phonenumbers(phone_number=phone_number, phone_number_type=phone_number_type, phone_number_status=phone_number_status, country_code=country_code, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, language=language, integration_id=integration_id, supported_content_id=supported_content_id)


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
integration_id = 'integration_id_example' # str | Filter on the Genesys Cloud integration id to which the phone number belongs to (optional)
supported_content_id = 'supported_content_id_example' # str | Filter based on the supported content ID (optional)

try:
    # Get a list of provisioned phone numbers.
    api_response = api_instance.get_routing_sms_phonenumbers(phone_number=phone_number, phone_number_type=phone_number_type, phone_number_status=phone_number_status, country_code=country_code, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, language=language, integration_id=integration_id, supported_content_id=supported_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_sms_phonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_number** | **str**| Filter on phone number address. Allowable characters are the digits &#39;0-9&#39; and the wild card character &#39;\\*&#39;. If just digits are present, a contains search is done on the address pattern. For example, &#39;317&#39; could be matched anywhere in the address. An &#39;\\*&#39; will match multiple digits. For example, to match a specific area code within the US a pattern like &#39;1317*&#39; could be used. | [optional]  |
| **phone_number_type** | [**list[str]**](str)| Filter on phone number type | [optional] <br />**Values**: local, mobile, tollfree, shortcode, alphanumeric |
| **phone_number_status** | [**list[str]**](str)| Filter on phone number status | [optional] <br />**Values**: active, invalid, initiated, porting, pending, pending-cancellation |
| **country_code** | [**list[str]**](str)| Filter on country code | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Optional field to sort results | [optional] <br />**Values**: phoneNumber, countryCode, country, dateCreated, dateModified, phoneNumberStatus, phoneNumberType, purchaseDate, supportsMms, supportsSms, supportsVoice |
| **sort_order** | **str**| Sort order | [optional] <br />**Values**: ascending, descending |
| **language** | **str**| A language tag (which is sometimes referred to as a \&quot;locale identifier\&quot;) to use to localize country field and sort operations | [optional] [default to &#39;en-US&#39;] |
| **integration_id** | **str**| Filter on the Genesys Cloud integration id to which the phone number belongs to | [optional]  |
| **supported_content_id** | **str**| Filter based on the supported content ID | [optional]  |

### Return type

[**SmsPhoneNumberEntityListing**](SmsPhoneNumberEntityListing)


## get_routing_user_directroutingbackup_settings

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) get_routing_user_directroutingbackup_settings(user_id)


Get the user's Direct Routing Backup settings.

Wraps GET /api/v2/routing/users/{userId}/directroutingbackup/settings 

Requires ANY permissions: 

* routing:directRoutingBackup:view

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
    # Get the user's Direct Routing Backup settings.
    api_response = api_instance.get_routing_user_directroutingbackup_settings(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_user_directroutingbackup_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## get_routing_user_utilization

> [**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse) get_routing_user_utilization(user_id)


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

### Return type

[**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse)


## get_routing_utilization

> [**UtilizationResponse**](UtilizationResponse) get_routing_utilization()


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

[**UtilizationResponse**](UtilizationResponse)


## get_routing_utilization_label

> [**UtilizationLabel**](UtilizationLabel) get_routing_utilization_label(label_id)


Get details about this utilization label

Wraps GET /api/v2/routing/utilization/labels/{labelId} 

Requires ALL permissions: 

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
label_id = 'label_id_example' # str | Utilization Label ID

try:
    # Get details about this utilization label
    api_response = api_instance.get_routing_utilization_label(label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization_label: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **label_id** | **str**| Utilization Label ID |  |

### Return type

[**UtilizationLabel**](UtilizationLabel)


## get_routing_utilization_label_agents

> list[object]** get_routing_utilization_label_agents(label_id)


Get list of agent ids associated with a utilization label

Wraps GET /api/v2/routing/utilization/labels/{labelId}/agents 

Requires ALL permissions: 

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
label_id = 'label_id_example' # str | Utilization Label ID

try:
    # Get list of agent ids associated with a utilization label
    api_response = api_instance.get_routing_utilization_label_agents(label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization_label_agents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **label_id** | **str**| Utilization Label ID |  |

### Return type

**list[object]**


## get_routing_utilization_labels

> [**UtilizationLabelEntityListing**](UtilizationLabelEntityListing) get_routing_utilization_labels(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)


Get list of utilization labels

Wraps GET /api/v2/routing/utilization/labels 

Requires ALL permissions: 

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
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ascending'' # str | Sort order by name (optional) (default to 'ascending')
name = 'name_example' # str | Utilization label's name (Wildcard is supported, e.g., 'label1*', '*label*' (optional)

try:
    # Get list of utilization labels
    api_response = api_instance.get_routing_utilization_labels(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization_labels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order by name | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Utilization label&#39;s name (Wildcard is supported, e.g., &#39;label1*&#39;, &#39;*label*&#39; | [optional]  |

### Return type

[**UtilizationLabelEntityListing**](UtilizationLabelEntityListing)


## get_routing_utilization_tag

> [**UtilizationTag**](UtilizationTag) get_routing_utilization_tag(tag_id)


Get details about this utilization tag

get_routing_utilization_tag is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/routing/utilization/tags/{tagId} 

Requires ALL permissions: 

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
tag_id = 'tag_id_example' # str | Utilization Tag ID

try:
    # Get details about this utilization tag
    api_response = api_instance.get_routing_utilization_tag(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization_tag: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **tag_id** | **str**| Utilization Tag ID |  |

### Return type

[**UtilizationTag**](UtilizationTag)


## get_routing_utilization_tag_agents

> list[object]** get_routing_utilization_tag_agents(tag_id)


Get list of agent ids associated with a utilization tag

get_routing_utilization_tag_agents is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/routing/utilization/tags/{tagId}/agents 

Requires ALL permissions: 

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
tag_id = 'tag_id_example' # str | Utilization Tag ID

try:
    # Get list of agent ids associated with a utilization tag
    api_response = api_instance.get_routing_utilization_tag_agents(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization_tag_agents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **tag_id** | **str**| Utilization Tag ID |  |

### Return type

**list[object]**


## get_routing_utilization_tags

> [**UtilizationTagEntityListing**](UtilizationTagEntityListing) get_routing_utilization_tags(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)


Get list of utilization tags

get_routing_utilization_tags is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/routing/utilization/tags 

Requires ALL permissions: 

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
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ascending'' # str | Sort order by name (optional) (default to 'ascending')
name = 'name_example' # str | Utilization tag's name (Wildcard is supported, e.g., 'tag1*') (optional)

try:
    # Get list of utilization tags
    api_response = api_instance.get_routing_utilization_tags(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_utilization_tags: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order by name | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Utilization tag&#39;s name (Wildcard is supported, e.g., &#39;tag1*&#39;) | [optional]  |

### Return type

[**UtilizationTagEntityListing**](UtilizationTagEntityListing)


## get_routing_wrapupcode

> [**WrapupCode**](WrapupCode) get_routing_wrapupcode(code_id)


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

### Return type

[**WrapupCode**](WrapupCode)


## get_routing_wrapupcodes

> [**WrapupCodeEntityListing**](WrapupCodeEntityListing) get_routing_wrapupcodes(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id, division_id=division_id)


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
id = ['id_example'] # list[str] | Filter by wrapup code ID(s) (optional)
division_id = ['division_id_example'] # list[str] | Filter by division ID(s) (optional)

try:
    # Get list of wrapup codes.
    api_response = api_instance.get_routing_wrapupcodes(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id, division_id=division_id)
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
| **id** | [**list[str]**](str)| Filter by wrapup code ID(s) | [optional]  |
| **division_id** | [**list[str]**](str)| Filter by division ID(s) | [optional]  |

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing)


## get_routing_wrapupcodes_divisionview

> [**WrapupCode**](WrapupCode) get_routing_wrapupcodes_divisionview(code_id)


Get a simplified wrap-up code.

Wraps GET /api/v2/routing/wrapupcodes/divisionviews/{codeId} 

Requires ALL permissions: 

* routing:wrapupCode:search

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
    # Get a simplified wrap-up code.
    api_response = api_instance.get_routing_wrapupcodes_divisionview(code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_wrapupcodes_divisionview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **code_id** | **str**| Wrapup Code ID |  |

### Return type

[**WrapupCode**](WrapupCode)


## get_routing_wrapupcodes_divisionviews

> [**WrapupCodeEntityListing**](WrapupCodeEntityListing) get_routing_wrapupcodes_divisionviews(page_size=page_size, page_number=page_number, name=name, id=id, division_id=division_id, include_state=include_state)


Get a paged listing of simplified wrapup code objects, filterable by name, wrapup code ID(s), or division ID(s).

Specifying both name and ID parameters is not supported.

Wraps GET /api/v2/routing/wrapupcodes/divisionviews 

Requires ALL permissions: 

* routing:wrapupCode:search

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
name = 'name_example' # str | Name (trailing asterisks allowed) (optional)
id = ['id_example'] # list[str] | Wrapup code ID(s) (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
include_state = 'include_state_example' # str | Wrapup code state(s) to include (optional)

try:
    # Get a paged listing of simplified wrapup code objects, filterable by name, wrapup code ID(s), or division ID(s).
    api_response = api_instance.get_routing_wrapupcodes_divisionviews(page_size=page_size, page_number=page_number, name=name, id=id, division_id=division_id, include_state=include_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_wrapupcodes_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name (trailing asterisks allowed) | [optional]  |
| **id** | [**list[str]**](str)| Wrapup code ID(s) | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **include_state** | **str**| Wrapup code state(s) to include | [optional] <br />**Values**: Active, Deleted, ActiveAndDeleted |

### Return type

[**WrapupCodeEntityListing**](WrapupCodeEntityListing)


## get_user_queues

> [**UserQueueEntityListing**](UserQueueEntityListing) get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined, division_id=division_id)


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
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing)


## get_user_routinglanguages

> [**UserLanguageEntityListing**](UserLanguageEntityListing) get_user_routinglanguages(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)


List routing languages assigned to a user

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
    # List routing languages assigned to a user
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

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing)


## get_user_routingskills

> [**UserSkillEntityListing**](UserSkillEntityListing) get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)


List routing skills assigned to a user

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
    # List routing skills assigned to a user
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

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing)


## get_user_skillgroups

> [**UserSkillGroupEntityListing**](UserSkillGroupEntityListing) get_user_skillgroups(user_id, page_size=page_size, after=after, before=before)


Get skill groups for a user

Wraps GET /api/v2/users/{userId}/skillgroups 

Requires ANY permissions: 

* routing:skillGroup:view

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
after = 'after_example' # str | The cursor that points to the next page (optional)
before = 'before_example' # str | The cursor that points to the previous page (optional)

try:
    # Get skill groups for a user
    api_response = api_instance.get_user_skillgroups(user_id, page_size=page_size, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_user_skillgroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **after** | **str**| The cursor that points to the next page | [optional]  |
| **before** | **str**| The cursor that points to the previous page | [optional]  |

### Return type

[**UserSkillGroupEntityListing**](UserSkillGroupEntityListing)


## patch_routing_conversation

> [**RoutingConversationAttributesResponse**](RoutingConversationAttributesResponse) patch_routing_conversation(conversation_id, body)


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
| **body** | [**RoutingConversationAttributesRequest**](RoutingConversationAttributesRequest)| Conversation Attributes |  |

### Return type

[**RoutingConversationAttributesResponse**](RoutingConversationAttributesResponse)


## patch_routing_email_domain

> [**InboundDomain**](InboundDomain) patch_routing_email_domain(domain_id, body)


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
| **body** | [**InboundDomainPatchRequest**](InboundDomainPatchRequest)| Domain settings |  |

### Return type

[**InboundDomain**](InboundDomain)


## patch_routing_email_domain_validate

> [**InboundDomain**](InboundDomain) patch_routing_email_domain_validate(domain_id, body)


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
| **body** | [**InboundDomainPatchRequest**](InboundDomainPatchRequest)| Domain settings |  |

### Return type

[**InboundDomain**](InboundDomain)


## patch_routing_predictor

> [**Predictor**](Predictor) patch_routing_predictor(predictor_id, body=body)


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
| **body** | [**PatchPredictorRequest**](PatchPredictorRequest)|  | [optional]  |

### Return type

[**Predictor**](Predictor)


## patch_routing_queue_member

>  patch_routing_queue_member(queue_id, member_id, body)


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
| **body** | [**QueueMember**](QueueMember)| Queue Member |  |

### Return type

void (empty response body)


## patch_routing_queue_members

> [**QueueMemberEntityListing**](QueueMemberEntityListing) patch_routing_queue_members(queue_id, body)


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
| **body** | [**list[QueueMember]**](QueueMember)| Queue Members |  |

### Return type

[**QueueMemberEntityListing**](QueueMemberEntityListing)


## patch_routing_queue_user

>  patch_routing_queue_user(queue_id, member_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
| **body** | [**QueueMember**](QueueMember)| Queue Member |  |

### Return type

void (empty response body)


## patch_routing_queue_users

> [**QueueMemberEntityListingV1**](QueueMemberEntityListingV1) patch_routing_queue_users(queue_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
| **body** | [**list[QueueMember]**](QueueMember)| Queue Members |  |

### Return type

[**QueueMemberEntityListingV1**](QueueMemberEntityListingV1)


## patch_routing_settings_contactcenter

>  patch_routing_settings_contactcenter(body)


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
| **body** | [**ContactCenterSettings**](ContactCenterSettings)| Contact Center Settings |  |

### Return type

void (empty response body)


## patch_routing_settings_transcription

> [**TranscriptionSettings**](TranscriptionSettings) patch_routing_settings_transcription(body)


Patch Transcription Settings

Wraps PATCH /api/v2/routing/settings/transcription 

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
    # Patch Transcription Settings
    api_response = api_instance.patch_routing_settings_transcription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_settings_transcription: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptionSettings**](TranscriptionSettings)| Organization Settings |  |

### Return type

[**TranscriptionSettings**](TranscriptionSettings)


## patch_routing_skillgroup

> [**SkillGroup**](SkillGroup) patch_routing_skillgroup(skill_group_id, body)


Update skill group definition

Wraps PATCH /api/v2/routing/skillgroups/{skillGroupId} 

Requires ANY permissions: 

* routing:skillGroup:edit

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
skill_group_id = 'skill_group_id_example' # str | Skill Group ID
body = PureCloudPlatformClientV2.SkillGroup() # SkillGroup | Update skill groups

try:
    # Update skill group definition
    api_response = api_instance.patch_routing_skillgroup(skill_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_routing_skillgroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_group_id** | **str**| Skill Group ID |  |
| **body** | [**SkillGroup**](SkillGroup)| Update skill groups |  |

### Return type

[**SkillGroup**](SkillGroup)


## patch_user_queue

> [**UserQueue**](UserQueue) patch_user_queue(queue_id, user_id, body)


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
| **body** | [**UserQueue**](UserQueue)| Queue Member |  |

### Return type

[**UserQueue**](UserQueue)


## patch_user_queues

> [**UserQueueEntityListing**](UserQueueEntityListing) patch_user_queues(user_id, body, division_id=division_id)


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
| **body** | [**list[UserQueue]**](UserQueue)| User Queues |  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing)


## patch_user_routinglanguage

> [**UserRoutingLanguage**](UserRoutingLanguage) patch_user_routinglanguage(user_id, language_id, body)


Update an assigned routing language's proficiency

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
    # Update an assigned routing language's proficiency
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
| **body** | [**UserRoutingLanguage**](UserRoutingLanguage)| Language |  |

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage)


## patch_user_routinglanguages_bulk

> [**UserLanguageEntityListing**](UserLanguageEntityListing) patch_user_routinglanguages_bulk(user_id, body)


Assign multiple routing languages to a user. Max 50 routing languages in request body

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
    # Assign multiple routing languages to a user. Max 50 routing languages in request body
    api_response = api_instance.patch_user_routinglanguages_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_routinglanguages_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingLanguagePost]**](UserRoutingLanguagePost)| Language |  |

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing)


## patch_user_routingskills_bulk

> [**UserSkillEntityListing**](UserSkillEntityListing) patch_user_routingskills_bulk(user_id, body)


Assign multiple routing skills to a user

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
    # Assign multiple routing skills to a user
    api_response = api_instance.patch_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->patch_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost)| Skill |  |

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing)


## post_analytics_queues_observations_query

> [**QueueObservationQueryResponse**](QueueObservationQueryResponse) post_analytics_queues_observations_query(body)


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
| **body** | [**QueueObservationQuery**](QueueObservationQuery)| query |  |

### Return type

[**QueueObservationQueryResponse**](QueueObservationQueryResponse)


## post_analytics_routing_activity_query

> [**RoutingActivityResponse**](RoutingActivityResponse) post_analytics_routing_activity_query(body, page_size=page_size, page_number=page_number)


Query for user activity observations

Wraps POST /api/v2/analytics/routing/activity/query 

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
body = PureCloudPlatformClientV2.RoutingActivityQuery() # RoutingActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for user activity observations
    api_response = api_instance.post_analytics_routing_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_analytics_routing_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoutingActivityQuery**](RoutingActivityQuery)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |

### Return type

[**RoutingActivityResponse**](RoutingActivityResponse)


## post_routing_assessments

> [**BenefitAssessment**](BenefitAssessment) post_routing_assessments(body=body)


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
| **body** | [**CreateBenefitAssessmentRequest**](CreateBenefitAssessmentRequest)|  | [optional]  |

### Return type

[**BenefitAssessment**](BenefitAssessment)


## post_routing_assessments_jobs

> [**BenefitAssessmentJob**](BenefitAssessmentJob) post_routing_assessments_jobs(body=body)


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
| **body** | [**CreateBenefitAssessmentJobRequest**](CreateBenefitAssessmentJobRequest)|  | [optional]  |

### Return type

[**BenefitAssessmentJob**](BenefitAssessmentJob)


## post_routing_email_domain_routes

> [**InboundRoute**](InboundRoute) post_routing_email_domain_routes(domain_name, body)


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
| **body** | [**InboundRoute**](InboundRoute)| Route |  |

### Return type

[**InboundRoute**](InboundRoute)


## post_routing_email_domain_testconnection

> [**TestMessage**](TestMessage) post_routing_email_domain_testconnection(domain_id, body=body)


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
| **body** | [**TestMessage**](TestMessage)| TestMessage | [optional]  |

### Return type

[**TestMessage**](TestMessage)


## post_routing_email_domains

> [**InboundDomain**](InboundDomain) post_routing_email_domains(body)


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
| **body** | [**InboundDomain**](InboundDomain)| Domain |  |

### Return type

[**InboundDomain**](InboundDomain)


## post_routing_email_outbound_domains

> [**EmailOutboundDomainResult**](EmailOutboundDomainResult) post_routing_email_outbound_domains(body)


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
| **body** | [**OutboundDomain**](OutboundDomain)| Domain |  |

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult)


## post_routing_email_outbound_domains_simulated

> [**EmailOutboundDomainResult**](EmailOutboundDomainResult) post_routing_email_outbound_domains_simulated(body)


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
| **body** | [**OutboundDomain**](OutboundDomain)| Domain |  |

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult)


## post_routing_languages

> [**Language**](Language) post_routing_languages(body)


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
| **body** | [**Language**](Language)| Language |  |

### Return type

[**Language**](Language)


## post_routing_predictors

> [**Predictor**](Predictor) post_routing_predictors(body=body)


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
| **body** | [**CreatePredictorRequest**](CreatePredictorRequest)|  | [optional]  |

### Return type

[**Predictor**](Predictor)


## post_routing_queue_members

>  post_routing_queue_members(queue_id, body, delete=delete)


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
| **body** | [**list[WritableEntity]**](WritableEntity)| Queue Members |  |
| **delete** | **bool**| True to delete queue members | [optional] [default to False] |

### Return type

void (empty response body)


## post_routing_queue_users

>  post_routing_queue_users(queue_id, body, delete=delete)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
| **body** | [**list[WritableEntity]**](WritableEntity)| Queue Members |  |
| **delete** | **bool**| True to delete queue members | [optional] [default to False] |

### Return type

void (empty response body)


## post_routing_queue_wrapupcodes

> [**list[WrapupCode]**](WrapupCode) post_routing_queue_wrapupcodes(queue_id, body)


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
| **body** | [**list[WrapUpCodeReference]**](WrapUpCodeReference)| List of wrapup codes |  |

### Return type

[**list[WrapupCode]**](WrapupCode)


## post_routing_queues

> [**Queue**](Queue) post_routing_queues(body)


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
| **body** | [**CreateQueueRequest**](CreateQueueRequest)| Queue |  |

### Return type

[**Queue**](Queue)


## post_routing_skillgroup_members_divisions

>  post_routing_skillgroup_members_divisions(skill_group_id, body=body)


Add or remove member divisions for this skill group.

Wraps POST /api/v2/routing/skillgroups/{skillGroupId}/members/divisions 

Requires ALL permissions: 

* routing:skillGroup:add

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
skill_group_id = 'skill_group_id_example' # str | Skill Group ID
body = PureCloudPlatformClientV2.SkillGroupMemberDivisions() # SkillGroupMemberDivisions |  (optional)

try:
    # Add or remove member divisions for this skill group.
    api_instance.post_routing_skillgroup_members_divisions(skill_group_id, body=body)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_skillgroup_members_divisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **skill_group_id** | **str**| Skill Group ID |  |
| **body** | [**SkillGroupMemberDivisions**](SkillGroupMemberDivisions)|  | [optional]  |

### Return type

void (empty response body)


## post_routing_skillgroups

> [**SkillGroupWithMemberDivisions**](SkillGroupWithMemberDivisions) post_routing_skillgroups(body)


Create a skill group

Wraps POST /api/v2/routing/skillgroups 

Requires ALL permissions: 

* routing:skillGroup:add

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
body = PureCloudPlatformClientV2.SkillGroupWithMemberDivisions() # SkillGroupWithMemberDivisions | Create skill group

try:
    # Create a skill group
    api_response = api_instance.post_routing_skillgroups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_skillgroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SkillGroupWithMemberDivisions**](SkillGroupWithMemberDivisions)| Create skill group |  |

### Return type

[**SkillGroupWithMemberDivisions**](SkillGroupWithMemberDivisions)


## post_routing_skills

> [**RoutingSkill**](RoutingSkill) post_routing_skills(body)


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
| **body** | [**RoutingSkill**](RoutingSkill)| Skill |  |

### Return type

[**RoutingSkill**](RoutingSkill)


## post_routing_sms_addresses

> [**SmsAddress**](SmsAddress) post_routing_sms_addresses(body)


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
| **body** | [**SmsAddressProvision**](SmsAddressProvision)| SmsAddress |  |

### Return type

[**SmsAddress**](SmsAddress)


## post_routing_sms_phonenumbers

> [**SmsPhoneNumber**](SmsPhoneNumber) post_routing_sms_phonenumbers(body)


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
| **body** | [**SmsPhoneNumberProvision**](SmsPhoneNumberProvision)| SmsPhoneNumber |  |

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber)


## post_routing_sms_phonenumbers_alphanumeric

> [**SmsPhoneNumber**](SmsPhoneNumber) post_routing_sms_phonenumbers_alphanumeric(body)


Provision an alphanumeric number for SMS

post_routing_sms_phonenumbers_alphanumeric is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/routing/sms/phonenumbers/alphanumeric 

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
body = PureCloudPlatformClientV2.SmsAlphanumericProvision() # SmsAlphanumericProvision | SmsPhoneNumber

try:
    # Provision an alphanumeric number for SMS
    api_response = api_instance.post_routing_sms_phonenumbers_alphanumeric(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_sms_phonenumbers_alphanumeric: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SmsAlphanumericProvision**](SmsAlphanumericProvision)| SmsPhoneNumber |  |

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber)


## post_routing_sms_phonenumbers_import

> [**SmsPhoneNumber**](SmsPhoneNumber) post_routing_sms_phonenumbers_import(body)


Imports a phone number for SMS

Wraps POST /api/v2/routing/sms/phonenumbers/import 

Requires ALL permissions: 

* sms:phoneNumber:byoImport

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
body = PureCloudPlatformClientV2.SmsPhoneNumberImport() # SmsPhoneNumberImport | SmsPhoneNumber

try:
    # Imports a phone number for SMS
    api_response = api_instance.post_routing_sms_phonenumbers_import(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_sms_phonenumbers_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SmsPhoneNumberImport**](SmsPhoneNumberImport)| SmsPhoneNumber |  |

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber)


## post_routing_utilization_labels

> [**UtilizationLabel**](UtilizationLabel) post_routing_utilization_labels(body)


Create a utilization label

Wraps POST /api/v2/routing/utilization/labels 

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
body = PureCloudPlatformClientV2.CreateUtilizationLabelRequest() # CreateUtilizationLabelRequest | UtilizationLabel

try:
    # Create a utilization label
    api_response = api_instance.post_routing_utilization_labels(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_utilization_labels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateUtilizationLabelRequest**](CreateUtilizationLabelRequest)| UtilizationLabel |  |

### Return type

[**UtilizationLabel**](UtilizationLabel)


## post_routing_utilization_tags

> [**UtilizationTag**](UtilizationTag) post_routing_utilization_tags(body)


Create an utilization tag

post_routing_utilization_tags is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/routing/utilization/tags 

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
body = PureCloudPlatformClientV2.CreateUtilizationTagRequest() # CreateUtilizationTagRequest | UtilizationTag

try:
    # Create an utilization tag
    api_response = api_instance.post_routing_utilization_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_routing_utilization_tags: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateUtilizationTagRequest**](CreateUtilizationTagRequest)| UtilizationTag |  |

### Return type

[**UtilizationTag**](UtilizationTag)


## post_routing_wrapupcodes

> [**WrapupCode**](WrapupCode) post_routing_wrapupcodes(body)


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
body = PureCloudPlatformClientV2.WrapupCodeRequest() # WrapupCodeRequest | WrapupCode

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
| **body** | [**WrapupCodeRequest**](WrapupCodeRequest)| WrapupCode |  |

### Return type

[**WrapupCode**](WrapupCode)


## post_user_routinglanguages

> [**UserRoutingLanguage**](UserRoutingLanguage) post_user_routinglanguages(user_id, body)


Assign a routing language to a user

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
    # Assign a routing language to a user
    api_response = api_instance.post_user_routinglanguages(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_user_routinglanguages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingLanguagePost**](UserRoutingLanguagePost)| Language |  |

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage)


## post_user_routingskills

> [**UserRoutingSkill**](UserRoutingSkill) post_user_routingskills(user_id, body)


Assign a routing skill to a user

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
    # Assign a routing skill to a user
    api_response = api_instance.post_user_routingskills(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_user_routingskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingSkillPost**](UserRoutingSkillPost)| Skill |  |

### Return type

[**UserRoutingSkill**](UserRoutingSkill)


## put_routing_directroutingbackup_settings_me

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) put_routing_directroutingbackup_settings_me(body)


Update the user's Direct Routing Backup settings.

Wraps PUT /api/v2/routing/directroutingbackup/settings/me 

Requires ANY permissions: 

* routing:directRoutingBackup:selfEdit

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
body = PureCloudPlatformClientV2.AgentDirectRoutingBackupSettings() # AgentDirectRoutingBackupSettings | directRoutingBackup

try:
    # Update the user's Direct Routing Backup settings.
    api_response = api_instance.put_routing_directroutingbackup_settings_me(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_directroutingbackup_settings_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)| directRoutingBackup |  |

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## put_routing_email_domain_route

> [**InboundRoute**](InboundRoute) put_routing_email_domain_route(domain_name, route_id, body)


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
| **body** | [**InboundRoute**](InboundRoute)| Route |  |

### Return type

[**InboundRoute**](InboundRoute)


## put_routing_email_outbound_domain_activation

> [**EmailOutboundDomainResult**](EmailOutboundDomainResult) put_routing_email_outbound_domain_activation(domain_id)


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

### Return type

[**EmailOutboundDomainResult**](EmailOutboundDomainResult)


## put_routing_message_recipient

> [**Recipient**](Recipient) put_routing_message_recipient(recipient_id, body)


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
body = PureCloudPlatformClientV2.RecipientRequest() # RecipientRequest | Recipient

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
| **body** | [**RecipientRequest**](RecipientRequest)| Recipient |  |

### Return type

[**Recipient**](Recipient)


## put_routing_queue

> [**Queue**](Queue) put_routing_queue(queue_id, body)


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
| **body** | [**QueueRequest**](QueueRequest)| Queue |  |

### Return type

[**Queue**](Queue)


## put_routing_settings

> [**RoutingSettings**](RoutingSettings) put_routing_settings(body)


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
| **body** | [**RoutingSettings**](RoutingSettings)| Organization Settings |  |

### Return type

[**RoutingSettings**](RoutingSettings)


## put_routing_settings_transcription

> [**TranscriptionSettings**](TranscriptionSettings) put_routing_settings_transcription(body)


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
| **body** | [**TranscriptionSettings**](TranscriptionSettings)| Organization Settings |  |

### Return type

[**TranscriptionSettings**](TranscriptionSettings)


## put_routing_sms_phonenumber

> [**SmsPhoneNumber**](SmsPhoneNumber) put_routing_sms_phonenumber(phone_number_id, body)


Update a phone number provisioned for SMS.

Wraps PUT /api/v2/routing/sms/phonenumbers/{phoneNumberId} 

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
phone_number_id = 'phone_number_id_example' # str | phone number
body = PureCloudPlatformClientV2.SmsPhoneNumber() # SmsPhoneNumber | SmsPhoneNumber

try:
    # Update a phone number provisioned for SMS.
    api_response = api_instance.put_routing_sms_phonenumber(phone_number_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_sms_phonenumber: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_number_id** | **str**| phone number |  |
| **body** | [**SmsPhoneNumber**](SmsPhoneNumber)| SmsPhoneNumber |  |

### Return type

[**SmsPhoneNumber**](SmsPhoneNumber)


## put_routing_user_directroutingbackup_settings

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) put_routing_user_directroutingbackup_settings(user_id, body)


Update the user's Direct Routing Backup settings.

Wraps PUT /api/v2/routing/users/{userId}/directroutingbackup/settings 

Requires ANY permissions: 

* routing:directRoutingBackup:edit

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
body = PureCloudPlatformClientV2.AgentDirectRoutingBackupSettings() # AgentDirectRoutingBackupSettings | directRoutingBackup

try:
    # Update the user's Direct Routing Backup settings.
    api_response = api_instance.put_routing_user_directroutingbackup_settings(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_user_directroutingbackup_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)| directRoutingBackup |  |

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## put_routing_user_utilization

> [**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse) put_routing_user_utilization(user_id, body)


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
body = PureCloudPlatformClientV2.UtilizationRequest() # UtilizationRequest | utilization

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
| **body** | [**UtilizationRequest**](UtilizationRequest)| utilization |  |

### Return type

[**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse)


## put_routing_utilization

> [**UtilizationResponse**](UtilizationResponse) put_routing_utilization(body)


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
body = PureCloudPlatformClientV2.UtilizationRequest() # UtilizationRequest | utilization

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
| **body** | [**UtilizationRequest**](UtilizationRequest)| utilization |  |

### Return type

[**UtilizationResponse**](UtilizationResponse)


## put_routing_utilization_label

> [**UtilizationLabel**](UtilizationLabel) put_routing_utilization_label(label_id, body)


Update a utilization label

Wraps PUT /api/v2/routing/utilization/labels/{labelId} 

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
label_id = 'label_id_example' # str | Utilization Label ID
body = PureCloudPlatformClientV2.UpdateUtilizationLabelRequest() # UpdateUtilizationLabelRequest | UtilizationLabel

try:
    # Update a utilization label
    api_response = api_instance.put_routing_utilization_label(label_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_routing_utilization_label: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **label_id** | **str**| Utilization Label ID |  |
| **body** | [**UpdateUtilizationLabelRequest**](UpdateUtilizationLabelRequest)| UtilizationLabel |  |

### Return type

[**UtilizationLabel**](UtilizationLabel)


## put_routing_wrapupcode

> [**WrapupCode**](WrapupCode) put_routing_wrapupcode(code_id, body)


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
body = PureCloudPlatformClientV2.WrapupCodeRequest() # WrapupCodeRequest | WrapupCode

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
| **body** | [**WrapupCodeRequest**](WrapupCodeRequest)| WrapupCode |  |

### Return type

[**WrapupCode**](WrapupCode)


## put_user_routingskill

> [**UserRoutingSkill**](UserRoutingSkill) put_user_routingskill(user_id, skill_id, body)


Update an assigned routing skill's proficiency

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
    # Update an assigned routing skill's proficiency
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
| **body** | [**UserRoutingSkill**](UserRoutingSkill)| Skill |  |

### Return type

[**UserRoutingSkill**](UserRoutingSkill)


## put_user_routingskills_bulk

> [**UserSkillEntityListing**](UserSkillEntityListing) put_user_routingskills_bulk(user_id, body)


Assign multiple routing skills to a user, replacing any current assignments

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
    # Assign multiple routing skills to a user, replacing any current assignments
    api_response = api_instance.put_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->put_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost)| Skill |  |

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing)


_PureCloudPlatformClientV2 218.0.0_
