---
title: OutboundApi
---

## PureCloudPlatformClientV2.OutboundApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_outbound_attemptlimit**](OutboundApi.html#delete_outbound_attemptlimit) | Delete attempt limits|
|[**delete_outbound_callabletimeset**](OutboundApi.html#delete_outbound_callabletimeset) | Delete callable time set|
|[**delete_outbound_callanalysisresponseset**](OutboundApi.html#delete_outbound_callanalysisresponseset) | Delete a dialer call analysis response set.|
|[**delete_outbound_campaign**](OutboundApi.html#delete_outbound_campaign) | Delete a campaign.|
|[**delete_outbound_campaign_progress**](OutboundApi.html#delete_outbound_campaign_progress) | Reset campaign progress and recycle the campaign|
|[**delete_outbound_campaignrule**](OutboundApi.html#delete_outbound_campaignrule) | Delete Campaign Rule|
|[**delete_outbound_contactlist**](OutboundApi.html#delete_outbound_contactlist) | Delete a contact list.|
|[**delete_outbound_contactlist_contact**](OutboundApi.html#delete_outbound_contactlist_contact) | Delete a contact.|
|[**delete_outbound_contactlist_contacts**](OutboundApi.html#delete_outbound_contactlist_contacts) | Delete contacts from a contact list.|
|[**delete_outbound_contactlistfilter**](OutboundApi.html#delete_outbound_contactlistfilter) | Delete Contact List Filter|
|[**delete_outbound_contactlists**](OutboundApi.html#delete_outbound_contactlists) | Delete multiple contact lists.|
|[**delete_outbound_dnclist**](OutboundApi.html#delete_outbound_dnclist) | Delete dialer DNC list|
|[**delete_outbound_messagingcampaign**](OutboundApi.html#delete_outbound_messagingcampaign) | Delete an Outbound Messaging Campaign|
|[**delete_outbound_ruleset**](OutboundApi.html#delete_outbound_ruleset) | Delete a Rule Set.|
|[**delete_outbound_schedules_campaign**](OutboundApi.html#delete_outbound_schedules_campaign) | Delete a dialer campaign schedule.|
|[**delete_outbound_schedules_sequence**](OutboundApi.html#delete_outbound_schedules_sequence) | Delete a dialer sequence schedule.|
|[**delete_outbound_sequence**](OutboundApi.html#delete_outbound_sequence) | Delete a dialer campaign sequence.|
|[**get_outbound_attemptlimit**](OutboundApi.html#get_outbound_attemptlimit) | Get attempt limits|
|[**get_outbound_attemptlimits**](OutboundApi.html#get_outbound_attemptlimits) | Query attempt limits list|
|[**get_outbound_callabletimeset**](OutboundApi.html#get_outbound_callabletimeset) | Get callable time set|
|[**get_outbound_callabletimesets**](OutboundApi.html#get_outbound_callabletimesets) | Query callable time set list|
|[**get_outbound_callanalysisresponseset**](OutboundApi.html#get_outbound_callanalysisresponseset) | Get a dialer call analysis response set.|
|[**get_outbound_callanalysisresponsesets**](OutboundApi.html#get_outbound_callanalysisresponsesets) | Query a list of dialer call analysis response sets.|
|[**get_outbound_campaign**](OutboundApi.html#get_outbound_campaign) | Get dialer campaign.|
|[**get_outbound_campaign_agentownedmappingpreview_results**](OutboundApi.html#get_outbound_campaign_agentownedmappingpreview_results) | Get a preview of how agents will be mapped to this campaign&#39;s contact list.|
|[**get_outbound_campaign_diagnostics**](OutboundApi.html#get_outbound_campaign_diagnostics) | Get campaign diagnostics|
|[**get_outbound_campaign_interactions**](OutboundApi.html#get_outbound_campaign_interactions) | Get dialer campaign interactions.|
|[**get_outbound_campaign_progress**](OutboundApi.html#get_outbound_campaign_progress) | Get campaign progress|
|[**get_outbound_campaign_stats**](OutboundApi.html#get_outbound_campaign_stats) | Get statistics about a Dialer Campaign|
|[**get_outbound_campaignrule**](OutboundApi.html#get_outbound_campaignrule) | Get Campaign Rule|
|[**get_outbound_campaignrules**](OutboundApi.html#get_outbound_campaignrules) | Query Campaign Rule list|
|[**get_outbound_campaigns**](OutboundApi.html#get_outbound_campaigns) | Query a list of dialer campaigns.|
|[**get_outbound_campaigns_all**](OutboundApi.html#get_outbound_campaigns_all) | Query across all types of campaigns by division|
|[**get_outbound_campaigns_all_divisionviews**](OutboundApi.html#get_outbound_campaigns_all_divisionviews) | Query across all types of campaigns|
|[**get_outbound_campaigns_divisionview**](OutboundApi.html#get_outbound_campaigns_divisionview) | Get a basic Campaign information object|
|[**get_outbound_campaigns_divisionviews**](OutboundApi.html#get_outbound_campaigns_divisionviews) | Query a list of basic Campaign information objects|
|[**get_outbound_contactlist**](OutboundApi.html#get_outbound_contactlist) | Get a dialer contact list.|
|[**get_outbound_contactlist_contact**](OutboundApi.html#get_outbound_contactlist_contact) | Get a contact.|
|[**get_outbound_contactlist_export**](OutboundApi.html#get_outbound_contactlist_export) | Get the URI of a contact list export.|
|[**get_outbound_contactlist_importstatus**](OutboundApi.html#get_outbound_contactlist_importstatus) | Get dialer contactList import status.|
|[**get_outbound_contactlist_timezonemappingpreview**](OutboundApi.html#get_outbound_contactlist_timezonemappingpreview) | Preview the result of applying Automatic Time Zone Mapping to a contact list|
|[**get_outbound_contactlistfilter**](OutboundApi.html#get_outbound_contactlistfilter) | Get Contact list filter|
|[**get_outbound_contactlistfilters**](OutboundApi.html#get_outbound_contactlistfilters) | Query Contact list filters|
|[**get_outbound_contactlists**](OutboundApi.html#get_outbound_contactlists) | Query a list of contact lists.|
|[**get_outbound_contactlists_divisionview**](OutboundApi.html#get_outbound_contactlists_divisionview) | Get a basic ContactList information object|
|[**get_outbound_contactlists_divisionviews**](OutboundApi.html#get_outbound_contactlists_divisionviews) | Query a list of simplified contact list objects.|
|[**get_outbound_dnclist**](OutboundApi.html#get_outbound_dnclist) | Get dialer DNC list|
|[**get_outbound_dnclist_export**](OutboundApi.html#get_outbound_dnclist_export) | Get the URI of a DNC list export.|
|[**get_outbound_dnclist_importstatus**](OutboundApi.html#get_outbound_dnclist_importstatus) | Get dialer dncList import status.|
|[**get_outbound_dnclists**](OutboundApi.html#get_outbound_dnclists) | Query dialer DNC lists|
|[**get_outbound_dnclists_divisionview**](OutboundApi.html#get_outbound_dnclists_divisionview) | Get a basic DncList information object|
|[**get_outbound_dnclists_divisionviews**](OutboundApi.html#get_outbound_dnclists_divisionviews) | Query a list of simplified dnc list objects.|
|[**get_outbound_event**](OutboundApi.html#get_outbound_event) | Get Dialer Event|
|[**get_outbound_events**](OutboundApi.html#get_outbound_events) | Query Event Logs|
|[**get_outbound_messagingcampaign**](OutboundApi.html#get_outbound_messagingcampaign) | Get an Outbound Messaging Campaign|
|[**get_outbound_messagingcampaign_progress**](OutboundApi.html#get_outbound_messagingcampaign_progress) | Get messaging campaign&#39;s progress|
|[**get_outbound_messagingcampaigns**](OutboundApi.html#get_outbound_messagingcampaigns) | Query a list of Messaging Campaigns|
|[**get_outbound_messagingcampaigns_divisionview**](OutboundApi.html#get_outbound_messagingcampaigns_divisionview) | Get a basic Messaging Campaign information object|
|[**get_outbound_messagingcampaigns_divisionviews**](OutboundApi.html#get_outbound_messagingcampaigns_divisionviews) | Query a list of basic Messaging Campaign information objects|
|[**get_outbound_ruleset**](OutboundApi.html#get_outbound_ruleset) | Get a Rule Set by ID.|
|[**get_outbound_rulesets**](OutboundApi.html#get_outbound_rulesets) | Query a list of Rule Sets.|
|[**get_outbound_schedules_campaign**](OutboundApi.html#get_outbound_schedules_campaign) | Get a dialer campaign schedule.|
|[**get_outbound_schedules_campaigns**](OutboundApi.html#get_outbound_schedules_campaigns) | Query for a list of dialer campaign schedules.|
|[**get_outbound_schedules_sequence**](OutboundApi.html#get_outbound_schedules_sequence) | Get a dialer sequence schedule.|
|[**get_outbound_schedules_sequences**](OutboundApi.html#get_outbound_schedules_sequences) | Query for a list of dialer sequence schedules.|
|[**get_outbound_sequence**](OutboundApi.html#get_outbound_sequence) | Get a dialer campaign sequence.|
|[**get_outbound_sequences**](OutboundApi.html#get_outbound_sequences) | Query a list of dialer campaign sequences.|
|[**get_outbound_settings**](OutboundApi.html#get_outbound_settings) | Get the outbound settings for this organization|
|[**get_outbound_wrapupcodemappings**](OutboundApi.html#get_outbound_wrapupcodemappings) | Get the Dialer wrap up code mapping.|
|[**patch_outbound_settings**](OutboundApi.html#patch_outbound_settings) | Update the outbound settings for this organization|
|[**post_outbound_attemptlimits**](OutboundApi.html#post_outbound_attemptlimits) | Create attempt limits|
|[**post_outbound_audits**](OutboundApi.html#post_outbound_audits) | Retrieves audits for dialer.|
|[**post_outbound_callabletimesets**](OutboundApi.html#post_outbound_callabletimesets) | Create callable time set|
|[**post_outbound_callanalysisresponsesets**](OutboundApi.html#post_outbound_callanalysisresponsesets) | Create a dialer call analysis response set.|
|[**post_outbound_campaign_agentownedmappingpreview**](OutboundApi.html#post_outbound_campaign_agentownedmappingpreview) | Initiate request for a preview of how agents will be mapped to this campaign&#39;s contact list.|
|[**post_outbound_campaign_callback_schedule**](OutboundApi.html#post_outbound_campaign_callback_schedule) | Schedule a Callback for a Dialer Campaign (Deprecated)|
|[**post_outbound_campaignrules**](OutboundApi.html#post_outbound_campaignrules) | Create Campaign Rule|
|[**post_outbound_campaigns**](OutboundApi.html#post_outbound_campaigns) | Create a campaign.|
|[**post_outbound_campaigns_progress**](OutboundApi.html#post_outbound_campaigns_progress) | Get progress for a list of campaigns|
|[**post_outbound_contactlist_clear**](OutboundApi.html#post_outbound_contactlist_clear) | Deletes all contacts out of a list. All outstanding recalls or rule-scheduled callbacks for non-preview campaigns configured with the contactlist will be cancelled.|
|[**post_outbound_contactlist_contacts**](OutboundApi.html#post_outbound_contactlist_contacts) | Add contacts to a contact list.|
|[**post_outbound_contactlist_contacts_bulk**](OutboundApi.html#post_outbound_contactlist_contacts_bulk) | Get contacts from a contact list.|
|[**post_outbound_contactlist_export**](OutboundApi.html#post_outbound_contactlist_export) | Initiate the export of a contact list.|
|[**post_outbound_contactlistfilters**](OutboundApi.html#post_outbound_contactlistfilters) | Create Contact List Filter|
|[**post_outbound_contactlistfilters_preview**](OutboundApi.html#post_outbound_contactlistfilters_preview) | Get a preview of the output of a contact list filter|
|[**post_outbound_contactlists**](OutboundApi.html#post_outbound_contactlists) | Create a contact List.|
|[**post_outbound_conversation_dnc**](OutboundApi.html#post_outbound_conversation_dnc) | Add phone numbers to a Dialer DNC list.|
|[**post_outbound_dnclist_export**](OutboundApi.html#post_outbound_dnclist_export) | Initiate the export of a dnc list.|
|[**post_outbound_dnclist_phonenumbers**](OutboundApi.html#post_outbound_dnclist_phonenumbers) | Add phone numbers to a DNC list.|
|[**post_outbound_dnclists**](OutboundApi.html#post_outbound_dnclists) | Create dialer DNC list|
|[**post_outbound_messagingcampaigns**](OutboundApi.html#post_outbound_messagingcampaigns) | Create a Messaging Campaign|
|[**post_outbound_messagingcampaigns_progress**](OutboundApi.html#post_outbound_messagingcampaigns_progress) | Get progress for a list of messaging campaigns|
|[**post_outbound_rulesets**](OutboundApi.html#post_outbound_rulesets) | Create a Rule Set.|
|[**post_outbound_sequences**](OutboundApi.html#post_outbound_sequences) | Create a new campaign sequence.|
|[**put_outbound_attemptlimit**](OutboundApi.html#put_outbound_attemptlimit) | Update attempt limits|
|[**put_outbound_callabletimeset**](OutboundApi.html#put_outbound_callabletimeset) | Update callable time set|
|[**put_outbound_callanalysisresponseset**](OutboundApi.html#put_outbound_callanalysisresponseset) | Update a dialer call analysis response set.|
|[**put_outbound_campaign**](OutboundApi.html#put_outbound_campaign) | Update a campaign.|
|[**put_outbound_campaign_agent**](OutboundApi.html#put_outbound_campaign_agent) | Send notification that an agent&#39;s state changed |
|[**put_outbound_campaignrule**](OutboundApi.html#put_outbound_campaignrule) | Update Campaign Rule|
|[**put_outbound_contactlist**](OutboundApi.html#put_outbound_contactlist) | Update a contact list.|
|[**put_outbound_contactlist_contact**](OutboundApi.html#put_outbound_contactlist_contact) | Update a contact.|
|[**put_outbound_contactlistfilter**](OutboundApi.html#put_outbound_contactlistfilter) | Update Contact List Filter|
|[**put_outbound_dnclist**](OutboundApi.html#put_outbound_dnclist) | Update dialer DNC list|
|[**put_outbound_messagingcampaign**](OutboundApi.html#put_outbound_messagingcampaign) | Update an Outbound Messaging Campaign|
|[**put_outbound_ruleset**](OutboundApi.html#put_outbound_ruleset) | Update a Rule Set.|
|[**put_outbound_schedules_campaign**](OutboundApi.html#put_outbound_schedules_campaign) | Update a new campaign schedule.|
|[**put_outbound_schedules_sequence**](OutboundApi.html#put_outbound_schedules_sequence) | Update a new sequence schedule.|
|[**put_outbound_sequence**](OutboundApi.html#put_outbound_sequence) | Update a new campaign sequence.|
|[**put_outbound_wrapupcodemappings**](OutboundApi.html#put_outbound_wrapupcodemappings) | Update the Dialer wrap up code mapping.|
{: class="table table-striped"}

<a name="delete_outbound_attemptlimit"></a>

##  delete_outbound_attemptlimit(attempt_limits_id)



Delete attempt limits



Wraps DELETE /api/v2/outbound/attemptlimits/{attemptLimitsId} 

Requires ANY permissions: 

* outbound:attemptLimits:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
attempt_limits_id = 'attempt_limits_id_example' # str | Attempt limits ID

try:
    # Delete attempt limits
    api_instance.delete_outbound_attemptlimit(attempt_limits_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_attemptlimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **attempt_limits_id** | **str**| Attempt limits ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_callabletimeset"></a>

##  delete_outbound_callabletimeset(callable_time_set_id)



Delete callable time set



Wraps DELETE /api/v2/outbound/callabletimesets/{callableTimeSetId} 

Requires ANY permissions: 

* outbound:callableTimeSet:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
callable_time_set_id = 'callable_time_set_id_example' # str | Callable Time Set ID

try:
    # Delete callable time set
    api_instance.delete_outbound_callabletimeset(callable_time_set_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_callabletimeset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **callable_time_set_id** | **str**| Callable Time Set ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_callanalysisresponseset"></a>

##  delete_outbound_callanalysisresponseset(call_analysis_set_id)



Delete a dialer call analysis response set.



Wraps DELETE /api/v2/outbound/callanalysisresponsesets/{callAnalysisSetId} 

Requires ANY permissions: 

* outbound:responseSet:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
call_analysis_set_id = 'call_analysis_set_id_example' # str | Call Analysis Response Set ID

try:
    # Delete a dialer call analysis response set.
    api_instance.delete_outbound_callanalysisresponseset(call_analysis_set_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_callanalysisresponseset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **call_analysis_set_id** | **str**| Call Analysis Response Set ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_campaign"></a>

## [**Campaign**](Campaign.html) delete_outbound_campaign(campaign_id)



Delete a campaign.



Wraps DELETE /api/v2/outbound/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:campaign:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Delete a campaign.
    api_response = api_instance.delete_outbound_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**Campaign**](Campaign.html)

<a name="delete_outbound_campaign_progress"></a>

##  delete_outbound_campaign_progress(campaign_id)



Reset campaign progress and recycle the campaign



Wraps DELETE /api/v2/outbound/campaigns/{campaignId}/progress 

Requires ANY permissions: 

* outbound:campaign:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Reset campaign progress and recycle the campaign
    api_instance.delete_outbound_campaign_progress(campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_campaign_progress: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_campaignrule"></a>

##  delete_outbound_campaignrule(campaign_rule_id)



Delete Campaign Rule



Wraps DELETE /api/v2/outbound/campaignrules/{campaignRuleId} 

Requires ANY permissions: 

* outbound:campaignRule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_rule_id = 'campaign_rule_id_example' # str | Campaign Rule ID

try:
    # Delete Campaign Rule
    api_instance.delete_outbound_campaignrule(campaign_rule_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_campaignrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_rule_id** | **str**| Campaign Rule ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_contactlist"></a>

##  delete_outbound_contactlist(contact_list_id)



Delete a contact list.



Wraps DELETE /api/v2/outbound/contactlists/{contactListId} 

Requires ANY permissions: 

* outbound:contactList:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID

try:
    # Delete a contact list.
    api_instance.delete_outbound_contactlist(contact_list_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_contactlist_contact"></a>

##  delete_outbound_contactlist_contact(contact_list_id, contact_id)



Delete a contact.



Wraps DELETE /api/v2/outbound/contactlists/{contactListId}/contacts/{contactId} 

Requires ANY permissions: 

* outbound:contact:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID
contact_id = 'contact_id_example' # str | Contact ID

try:
    # Delete a contact.
    api_instance.delete_outbound_contactlist_contact(contact_list_id, contact_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlist_contact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **contact_id** | **str**| Contact ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_contactlist_contacts"></a>

##  delete_outbound_contactlist_contacts(contact_list_id, contact_ids)



Delete contacts from a contact list.



Wraps DELETE /api/v2/outbound/contactlists/{contactListId}/contacts 

Requires ANY permissions: 

* outbound:contact:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID
contact_ids = ['contact_ids_example'] # list[str] | ContactIds to delete.

try:
    # Delete contacts from a contact list.
    api_instance.delete_outbound_contactlist_contacts(contact_list_id, contact_ids)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlist_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **contact_ids** | [**list[str]**](str.html)| ContactIds to delete. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_contactlistfilter"></a>

##  delete_outbound_contactlistfilter(contact_list_filter_id)



Delete Contact List Filter



Wraps DELETE /api/v2/outbound/contactlistfilters/{contactListFilterId} 

Requires ANY permissions: 

* outbound:contactListFilter:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_filter_id = 'contact_list_filter_id_example' # str | Contact List Filter ID

try:
    # Delete Contact List Filter
    api_instance.delete_outbound_contactlistfilter(contact_list_filter_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlistfilter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_filter_id** | **str**| Contact List Filter ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_contactlists"></a>

##  delete_outbound_contactlists(id)



Delete multiple contact lists.



Wraps DELETE /api/v2/outbound/contactlists 

Requires ANY permissions: 

* outbound:contactList:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
id = ['id_example'] # list[str] | contact list id(s) to delete

try:
    # Delete multiple contact lists.
    api_instance.delete_outbound_contactlists(id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlists: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| contact list id(s) to delete |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_dnclist"></a>

##  delete_outbound_dnclist(dnc_list_id)



Delete dialer DNC list



Wraps DELETE /api/v2/outbound/dnclists/{dncListId} 

Requires ANY permissions: 

* outbound:dncList:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID

try:
    # Delete dialer DNC list
    api_instance.delete_outbound_dnclist(dnc_list_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_dnclist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_messagingcampaign"></a>

## [**MessagingCampaign**](MessagingCampaign.html) delete_outbound_messagingcampaign(messaging_campaign_id)



Delete an Outbound Messaging Campaign



Wraps DELETE /api/v2/outbound/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:delete
* outbound:emailCampaign:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
messaging_campaign_id = 'messaging_campaign_id_example' # str | The Messaging Campaign ID

try:
    # Delete an Outbound Messaging Campaign
    api_response = api_instance.delete_outbound_messagingcampaign(messaging_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_messagingcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |
{: class="table table-striped"}

### Return type

[**MessagingCampaign**](MessagingCampaign.html)

<a name="delete_outbound_ruleset"></a>

##  delete_outbound_ruleset(rule_set_id)



Delete a Rule Set.



Wraps DELETE /api/v2/outbound/rulesets/{ruleSetId} 

Requires ANY permissions: 

* outbound:ruleSet:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
rule_set_id = 'rule_set_id_example' # str | Rule Set ID

try:
    # Delete a Rule Set.
    api_instance.delete_outbound_ruleset(rule_set_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_ruleset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_set_id** | **str**| Rule Set ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_schedules_campaign"></a>

##  delete_outbound_schedules_campaign(campaign_id)



Delete a dialer campaign schedule.



Wraps DELETE /api/v2/outbound/schedules/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:schedule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Delete a dialer campaign schedule.
    api_instance.delete_outbound_schedules_campaign(campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_schedules_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_schedules_sequence"></a>

##  delete_outbound_schedules_sequence(sequence_id)



Delete a dialer sequence schedule.



Wraps DELETE /api/v2/outbound/schedules/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:schedule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
sequence_id = 'sequence_id_example' # str | Sequence ID

try:
    # Delete a dialer sequence schedule.
    api_instance.delete_outbound_schedules_sequence(sequence_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_schedules_sequence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sequence_id** | **str**| Sequence ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_outbound_sequence"></a>

##  delete_outbound_sequence(sequence_id)



Delete a dialer campaign sequence.



Wraps DELETE /api/v2/outbound/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:campaignSequence:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
sequence_id = 'sequence_id_example' # str | Campaign Sequence ID

try:
    # Delete a dialer campaign sequence.
    api_instance.delete_outbound_sequence(sequence_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_sequence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sequence_id** | **str**| Campaign Sequence ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_outbound_attemptlimit"></a>

## [**AttemptLimits**](AttemptLimits.html) get_outbound_attemptlimit(attempt_limits_id)



Get attempt limits



Wraps GET /api/v2/outbound/attemptlimits/{attemptLimitsId} 

Requires ANY permissions: 

* outbound:attemptLimits:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
attempt_limits_id = 'attempt_limits_id_example' # str | Attempt limits ID

try:
    # Get attempt limits
    api_response = api_instance.get_outbound_attemptlimit(attempt_limits_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_attemptlimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **attempt_limits_id** | **str**| Attempt limits ID |  |
{: class="table table-striped"}

### Return type

[**AttemptLimits**](AttemptLimits.html)

<a name="get_outbound_attemptlimits"></a>

## [**AttemptLimitsEntityListing**](AttemptLimitsEntityListing.html) get_outbound_attemptlimits(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)



Query attempt limits list



Wraps GET /api/v2/outbound/attemptlimits 

Requires ANY permissions: 

* outbound:attemptLimits:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query attempt limits list
    api_response = api_instance.get_outbound_attemptlimits(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_attemptlimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**AttemptLimitsEntityListing**](AttemptLimitsEntityListing.html)

<a name="get_outbound_callabletimeset"></a>

## [**CallableTimeSet**](CallableTimeSet.html) get_outbound_callabletimeset(callable_time_set_id)



Get callable time set



Wraps GET /api/v2/outbound/callabletimesets/{callableTimeSetId} 

Requires ANY permissions: 

* outbound:callableTimeSet:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
callable_time_set_id = 'callable_time_set_id_example' # str | Callable Time Set ID

try:
    # Get callable time set
    api_response = api_instance.get_outbound_callabletimeset(callable_time_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_callabletimeset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **callable_time_set_id** | **str**| Callable Time Set ID |  |
{: class="table table-striped"}

### Return type

[**CallableTimeSet**](CallableTimeSet.html)

<a name="get_outbound_callabletimesets"></a>

## [**CallableTimeSetEntityListing**](CallableTimeSetEntityListing.html) get_outbound_callabletimesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)



Query callable time set list



Wraps GET /api/v2/outbound/callabletimesets 

Requires ANY permissions: 

* outbound:callableTimeSet:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query callable time set list
    api_response = api_instance.get_outbound_callabletimesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_callabletimesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CallableTimeSetEntityListing**](CallableTimeSetEntityListing.html)

<a name="get_outbound_callanalysisresponseset"></a>

## [**ResponseSet**](ResponseSet.html) get_outbound_callanalysisresponseset(call_analysis_set_id)



Get a dialer call analysis response set.



Wraps GET /api/v2/outbound/callanalysisresponsesets/{callAnalysisSetId} 

Requires ANY permissions: 

* outbound:responseSet:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
call_analysis_set_id = 'call_analysis_set_id_example' # str | Call Analysis Response Set ID

try:
    # Get a dialer call analysis response set.
    api_response = api_instance.get_outbound_callanalysisresponseset(call_analysis_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_callanalysisresponseset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **call_analysis_set_id** | **str**| Call Analysis Response Set ID |  |
{: class="table table-striped"}

### Return type

[**ResponseSet**](ResponseSet.html)

<a name="get_outbound_callanalysisresponsesets"></a>

## [**ResponseSetEntityListing**](ResponseSetEntityListing.html) get_outbound_callanalysisresponsesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)



Query a list of dialer call analysis response sets.



Wraps GET /api/v2/outbound/callanalysisresponsesets 

Requires ANY permissions: 

* outbound:responseSet:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of dialer call analysis response sets.
    api_response = api_instance.get_outbound_callanalysisresponsesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_callanalysisresponsesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**ResponseSetEntityListing**](ResponseSetEntityListing.html)

<a name="get_outbound_campaign"></a>

## [**Campaign**](Campaign.html) get_outbound_campaign(campaign_id)



Get dialer campaign.



Wraps GET /api/v2/outbound/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get dialer campaign.
    api_response = api_instance.get_outbound_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**Campaign**](Campaign.html)

<a name="get_outbound_campaign_agentownedmappingpreview_results"></a>

## [**AgentOwnedMappingPreviewListing**](AgentOwnedMappingPreviewListing.html) get_outbound_campaign_agentownedmappingpreview_results(campaign_id)



Get a preview of how agents will be mapped to this campaign's contact list.



Wraps GET /api/v2/outbound/campaigns/{campaignId}/agentownedmappingpreview/results 

Requires ALL permissions: 

* outbound:campaign:view
* outbound:contact:view
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
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get a preview of how agents will be mapped to this campaign's contact list.
    api_response = api_instance.get_outbound_campaign_agentownedmappingpreview_results(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_agentownedmappingpreview_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**AgentOwnedMappingPreviewListing**](AgentOwnedMappingPreviewListing.html)

<a name="get_outbound_campaign_diagnostics"></a>

## [**CampaignDiagnostics**](CampaignDiagnostics.html) get_outbound_campaign_diagnostics(campaign_id)



Get campaign diagnostics



Wraps GET /api/v2/outbound/campaigns/{campaignId}/diagnostics 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get campaign diagnostics
    api_response = api_instance.get_outbound_campaign_diagnostics(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_diagnostics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignDiagnostics**](CampaignDiagnostics.html)

<a name="get_outbound_campaign_interactions"></a>

## [**CampaignInteractions**](CampaignInteractions.html) get_outbound_campaign_interactions(campaign_id)



Get dialer campaign interactions.



Wraps GET /api/v2/outbound/campaigns/{campaignId}/interactions 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get dialer campaign interactions.
    api_response = api_instance.get_outbound_campaign_interactions(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_interactions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignInteractions**](CampaignInteractions.html)

<a name="get_outbound_campaign_progress"></a>

## [**CampaignProgress**](CampaignProgress.html) get_outbound_campaign_progress(campaign_id)



Get campaign progress



Wraps GET /api/v2/outbound/campaigns/{campaignId}/progress 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get campaign progress
    api_response = api_instance.get_outbound_campaign_progress(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_progress: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignProgress**](CampaignProgress.html)

<a name="get_outbound_campaign_stats"></a>

## [**CampaignStats**](CampaignStats.html) get_outbound_campaign_stats(campaign_id)



Get statistics about a Dialer Campaign



Wraps GET /api/v2/outbound/campaigns/{campaignId}/stats 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get statistics about a Dialer Campaign
    api_response = api_instance.get_outbound_campaign_stats(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_stats: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignStats**](CampaignStats.html)

<a name="get_outbound_campaignrule"></a>

## [**CampaignRule**](CampaignRule.html) get_outbound_campaignrule(campaign_rule_id)



Get Campaign Rule



Wraps GET /api/v2/outbound/campaignrules/{campaignRuleId} 

Requires ANY permissions: 

* outbound:campaignRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_rule_id = 'campaign_rule_id_example' # str | Campaign Rule ID

try:
    # Get Campaign Rule
    api_response = api_instance.get_outbound_campaignrule(campaign_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaignrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_rule_id** | **str**| Campaign Rule ID |  |
{: class="table table-striped"}

### Return type

[**CampaignRule**](CampaignRule.html)

<a name="get_outbound_campaignrules"></a>

## [**CampaignRuleEntityListing**](CampaignRuleEntityListing.html) get_outbound_campaignrules(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)



Query Campaign Rule list



Wraps GET /api/v2/outbound/campaignrules 

Requires ANY permissions: 

* outbound:campaignRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query Campaign Rule list
    api_response = api_instance.get_outbound_campaignrules(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaignrules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CampaignRuleEntityListing**](CampaignRuleEntityListing.html)

<a name="get_outbound_campaigns"></a>

## [**CampaignEntityListing**](CampaignEntityListing.html) get_outbound_campaigns(page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, contact_list_id=contact_list_id, dnc_list_ids=dnc_list_ids, distribution_queue_id=distribution_queue_id, edge_group_id=edge_group_id, call_analysis_response_set_id=call_analysis_response_set_id, division_id=division_id, sort_by=sort_by, sort_order=sort_order)



Query a list of dialer campaigns.



Wraps GET /api/v2/outbound/campaigns 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
contact_list_id = 'contact_list_id_example' # str | Contact List ID (optional)
dnc_list_ids = 'dnc_list_ids_example' # str | DNC list ID (optional)
distribution_queue_id = 'distribution_queue_id_example' # str | Distribution queue ID (optional)
edge_group_id = 'edge_group_id_example' # str | Edge group ID (optional)
call_analysis_response_set_id = 'call_analysis_response_set_id_example' # str | Call analysis response set ID (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of dialer campaigns.
    api_response = api_instance.get_outbound_campaigns(page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, contact_list_id=contact_list_id, dnc_list_ids=dnc_list_ids, distribution_queue_id=distribution_queue_id, edge_group_id=edge_group_id, call_analysis_response_set_id=call_analysis_response_set_id, division_id=division_id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaigns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **contact_list_id** | **str**| Contact List ID | [optional]  |
| **dnc_list_ids** | **str**| DNC list ID | [optional]  |
| **distribution_queue_id** | **str**| Distribution queue ID | [optional]  |
| **edge_group_id** | **str**| Edge group ID | [optional]  |
| **call_analysis_response_set_id** | **str**| Call analysis response set ID | [optional]  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CampaignEntityListing**](CampaignEntityListing.html)

<a name="get_outbound_campaigns_all"></a>

## [**CommonCampaignEntityListing**](CommonCampaignEntityListing.html) get_outbound_campaigns_all(page_size=page_size, page_number=page_number, id=id, name=name, division_id=division_id, media_type=media_type, sort_order=sort_order)



Query across all types of campaigns by division



Wraps GET /api/v2/outbound/campaigns/all 

Requires ANY permissions: 

* outbound:campaign:view
* outbound:messagingCampaign:view
* outbound:emailCampaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | Campaign ID(s) (optional)
name = 'name_example' # str | Campaign name(s) (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
media_type = ['media_type_example'] # list[str] | Media type(s) (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query across all types of campaigns by division
    api_response = api_instance.get_outbound_campaigns_all(page_size=page_size, page_number=page_number, id=id, name=name, division_id=division_id, media_type=media_type, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaigns_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| Campaign ID(s) | [optional]  |
| **name** | **str**| Campaign name(s) | [optional]  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
| **media_type** | [**list[str]**](str.html)| Media type(s) | [optional] <br />**Values**: email, sms, voice |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CommonCampaignEntityListing**](CommonCampaignEntityListing.html)

<a name="get_outbound_campaigns_all_divisionviews"></a>

## [**CommonCampaignDivisionViewEntityListing**](CommonCampaignDivisionViewEntityListing.html) get_outbound_campaigns_all_divisionviews(page_size=page_size, page_number=page_number, id=id, name=name, division_id=division_id, media_type=media_type, sort_order=sort_order)



Query across all types of campaigns



Wraps GET /api/v2/outbound/campaigns/all/divisionviews 

Requires ANY permissions: 

* outbound:campaign:search
* outbound:messagingCampaign:search
* outbound:emailCampaign:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | Campaign ID(s) (optional)
name = 'name_example' # str | Campaign name(s) (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
media_type = ['media_type_example'] # list[str] | Media type(s) (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query across all types of campaigns
    api_response = api_instance.get_outbound_campaigns_all_divisionviews(page_size=page_size, page_number=page_number, id=id, name=name, division_id=division_id, media_type=media_type, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaigns_all_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| Campaign ID(s) | [optional]  |
| **name** | **str**| Campaign name(s) | [optional]  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
| **media_type** | [**list[str]**](str.html)| Media type(s) | [optional] <br />**Values**: email, sms, voice |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CommonCampaignDivisionViewEntityListing**](CommonCampaignDivisionViewEntityListing.html)

<a name="get_outbound_campaigns_divisionview"></a>

## [**CampaignDivisionView**](CampaignDivisionView.html) get_outbound_campaigns_divisionview(campaign_id)



Get a basic Campaign information object

This returns a simplified version of a Campaign, consisting of name and division.

Wraps GET /api/v2/outbound/campaigns/divisionviews/{campaignId} 

Requires ALL permissions: 

* outbound:campaign:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get a basic Campaign information object
    api_response = api_instance.get_outbound_campaigns_divisionview(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaigns_divisionview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignDivisionView**](CampaignDivisionView.html)

<a name="get_outbound_campaigns_divisionviews"></a>

## [**CampaignDivisionViewListing**](CampaignDivisionViewListing.html) get_outbound_campaigns_divisionviews(page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, sort_by=sort_by, sort_order=sort_order)



Query a list of basic Campaign information objects

This returns a simplified version of a Campaign, consisting of name and division.

Wraps GET /api/v2/outbound/campaigns/divisionviews 

Requires ALL permissions: 

* outbound:campaign:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of basic Campaign information objects
    api_response = api_instance.get_outbound_campaigns_divisionviews(page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaigns_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CampaignDivisionViewListing**](CampaignDivisionViewListing.html)

<a name="get_outbound_contactlist"></a>

## [**ContactList**](ContactList.html) get_outbound_contactlist(contact_list_id, include_import_status=include_import_status, include_size=include_size)



Get a dialer contact list.



Wraps GET /api/v2/outbound/contactlists/{contactListId} 

Requires ANY permissions: 

* outbound:contactList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID
include_import_status = false # bool | Import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)

try:
    # Get a dialer contact list.
    api_response = api_instance.get_outbound_contactlist(contact_list_id, include_import_status=include_import_status, include_size=include_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
| **include_import_status** | **bool**| Import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**ContactList**](ContactList.html)

<a name="get_outbound_contactlist_contact"></a>

## [**DialerContact**](DialerContact.html) get_outbound_contactlist_contact(contact_list_id, contact_id)



Get a contact.



Wraps GET /api/v2/outbound/contactlists/{contactListId}/contacts/{contactId} 

Requires ANY permissions: 

* outbound:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID
contact_id = 'contact_id_example' # str | Contact ID

try:
    # Get a contact.
    api_response = api_instance.get_outbound_contactlist_contact(contact_list_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist_contact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **contact_id** | **str**| Contact ID |  |
{: class="table table-striped"}

### Return type

[**DialerContact**](DialerContact.html)

<a name="get_outbound_contactlist_export"></a>

## [**ExportUri**](ExportUri.html) get_outbound_contactlist_export(contact_list_id, download=download)



Get the URI of a contact list export.



Wraps GET /api/v2/outbound/contactlists/{contactListId}/export 

Requires ALL permissions: 

* outbound:contact:view
* outbound:contactList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID
download = 'false' # str | Redirect to download uri (optional) (default to false)

try:
    # Get the URI of a contact list export.
    api_response = api_instance.get_outbound_contactlist_export(contact_list_id, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
| **download** | **str**| Redirect to download uri | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**ExportUri**](ExportUri.html)

<a name="get_outbound_contactlist_importstatus"></a>

## [**ImportStatus**](ImportStatus.html) get_outbound_contactlist_importstatus(contact_list_id)



Get dialer contactList import status.



Wraps GET /api/v2/outbound/contactlists/{contactListId}/importstatus 

Requires ANY permissions: 

* outbound:contactList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID

try:
    # Get dialer contactList import status.
    api_response = api_instance.get_outbound_contactlist_importstatus(contact_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist_importstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
{: class="table table-striped"}

### Return type

[**ImportStatus**](ImportStatus.html)

<a name="get_outbound_contactlist_timezonemappingpreview"></a>

## [**TimeZoneMappingPreview**](TimeZoneMappingPreview.html) get_outbound_contactlist_timezonemappingpreview(contact_list_id)



Preview the result of applying Automatic Time Zone Mapping to a contact list



Wraps GET /api/v2/outbound/contactlists/{contactListId}/timezonemappingpreview 

Requires ANY permissions: 

* outbound:contactList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID

try:
    # Preview the result of applying Automatic Time Zone Mapping to a contact list
    api_response = api_instance.get_outbound_contactlist_timezonemappingpreview(contact_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist_timezonemappingpreview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
{: class="table table-striped"}

### Return type

[**TimeZoneMappingPreview**](TimeZoneMappingPreview.html)

<a name="get_outbound_contactlistfilter"></a>

## [**ContactListFilter**](ContactListFilter.html) get_outbound_contactlistfilter(contact_list_filter_id)



Get Contact list filter



Wraps GET /api/v2/outbound/contactlistfilters/{contactListFilterId} 

Requires ANY permissions: 

* outbound:contactListFilter:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_filter_id = 'contact_list_filter_id_example' # str | Contact List Filter ID

try:
    # Get Contact list filter
    api_response = api_instance.get_outbound_contactlistfilter(contact_list_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlistfilter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_filter_id** | **str**| Contact List Filter ID |  |
{: class="table table-striped"}

### Return type

[**ContactListFilter**](ContactListFilter.html)

<a name="get_outbound_contactlistfilters"></a>

## [**ContactListFilterEntityListing**](ContactListFilterEntityListing.html) get_outbound_contactlistfilters(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order, contact_list_id=contact_list_id)



Query Contact list filters



Wraps GET /api/v2/outbound/contactlistfilters 

Requires ANY permissions: 

* outbound:contactListFilter:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)
contact_list_id = 'contact_list_id_example' # str | Contact List ID (optional)

try:
    # Query Contact list filters
    api_response = api_instance.get_outbound_contactlistfilters(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order, contact_list_id=contact_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlistfilters: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
| **contact_list_id** | **str**| Contact List ID | [optional]  |
{: class="table table-striped"}

### Return type

[**ContactListFilterEntityListing**](ContactListFilterEntityListing.html)

<a name="get_outbound_contactlists"></a>

## [**ContactListEntityListing**](ContactListEntityListing.html) get_outbound_contactlists(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, id=id, division_id=division_id, sort_by=sort_by, sort_order=sort_order)



Query a list of contact lists.



Wraps GET /api/v2/outbound/contactlists 

Requires ANY permissions: 

* outbound:contactList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
include_import_status = false # bool | Include import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of contact lists.
    api_response = api_instance.get_outbound_contactlists(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, id=id, division_id=division_id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlists: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_import_status** | **bool**| Include import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**ContactListEntityListing**](ContactListEntityListing.html)

<a name="get_outbound_contactlists_divisionview"></a>

## [**ContactListDivisionView**](ContactListDivisionView.html) get_outbound_contactlists_divisionview(contact_list_id, include_import_status=include_import_status, include_size=include_size)



Get a basic ContactList information object

This returns a simplified version of a ContactList, consisting of the name, division, column names, phone columns, import status, and size.

Wraps GET /api/v2/outbound/contactlists/divisionviews/{contactListId} 

Requires ALL permissions: 

* outbound:contactList:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contactlist ID
include_import_status = false # bool | Include import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)

try:
    # Get a basic ContactList information object
    api_response = api_instance.get_outbound_contactlists_divisionview(contact_list_id, include_import_status=include_import_status, include_size=include_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlists_divisionview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contactlist ID |  |
| **include_import_status** | **bool**| Include import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**ContactListDivisionView**](ContactListDivisionView.html)

<a name="get_outbound_contactlists_divisionviews"></a>

## [**ContactListDivisionViewListing**](ContactListDivisionViewListing.html) get_outbound_contactlists_divisionviews(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, sort_by=sort_by, sort_order=sort_order)



Query a list of simplified contact list objects.

This return a simplified version of contact lists, consisting of the name, division, column names, phone columns, import status, and size.

Wraps GET /api/v2/outbound/contactlists/divisionviews 

Requires ALL permissions: 

* outbound:contactList:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
include_import_status = false # bool | Include import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of simplified contact list objects.
    api_response = api_instance.get_outbound_contactlists_divisionviews(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlists_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_import_status** | **bool**| Include import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**ContactListDivisionViewListing**](ContactListDivisionViewListing.html)

<a name="get_outbound_dnclist"></a>

## [**DncList**](DncList.html) get_outbound_dnclist(dnc_list_id, include_import_status=include_import_status, include_size=include_size)



Get dialer DNC list



Wraps GET /api/v2/outbound/dnclists/{dncListId} 

Requires ANY permissions: 

* outbound:dncList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID
include_import_status = false # bool | Import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)

try:
    # Get dialer DNC list
    api_response = api_instance.get_outbound_dnclist(dnc_list_id, include_import_status=include_import_status, include_size=include_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_dnclist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **include_import_status** | **bool**| Import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**DncList**](DncList.html)

<a name="get_outbound_dnclist_export"></a>

## [**ExportUri**](ExportUri.html) get_outbound_dnclist_export(dnc_list_id, download=download)



Get the URI of a DNC list export.



Wraps GET /api/v2/outbound/dnclists/{dncListId}/export 

Requires ALL permissions: 

* outbound:dnc:view
* outbound:dncList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID
download = 'false' # str | Redirect to download uri (optional) (default to false)

try:
    # Get the URI of a DNC list export.
    api_response = api_instance.get_outbound_dnclist_export(dnc_list_id, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_dnclist_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **download** | **str**| Redirect to download uri | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**ExportUri**](ExportUri.html)

<a name="get_outbound_dnclist_importstatus"></a>

## [**ImportStatus**](ImportStatus.html) get_outbound_dnclist_importstatus(dnc_list_id)



Get dialer dncList import status.



Wraps GET /api/v2/outbound/dnclists/{dncListId}/importstatus 

Requires ANY permissions: 

* outbound:dncList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID

try:
    # Get dialer dncList import status.
    api_response = api_instance.get_outbound_dnclist_importstatus(dnc_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_dnclist_importstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
{: class="table table-striped"}

### Return type

[**ImportStatus**](ImportStatus.html)

<a name="get_outbound_dnclists"></a>

## [**DncListEntityListing**](DncListEntityListing.html) get_outbound_dnclists(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, dnc_source_type=dnc_source_type, division_id=division_id, sort_by=sort_by, sort_order=sort_order)



Query dialer DNC lists



Wraps GET /api/v2/outbound/dnclists 

Requires ANY permissions: 

* outbound:dncList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
include_import_status = false # bool | Import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
dnc_source_type = 'dnc_source_type_example' # str | DncSourceType (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)

try:
    # Query dialer DNC lists
    api_response = api_instance.get_outbound_dnclists(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, dnc_source_type=dnc_source_type, division_id=division_id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_dnclists: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_import_status** | **bool**| Import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **dnc_source_type** | **str**| DncSourceType | [optional] <br />**Values**: rds, dnc.com, gryphon |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] <br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**DncListEntityListing**](DncListEntityListing.html)

<a name="get_outbound_dnclists_divisionview"></a>

## [**DncListDivisionView**](DncListDivisionView.html) get_outbound_dnclists_divisionview(dnc_list_id, include_import_status=include_import_status, include_size=include_size)



Get a basic DncList information object

This returns a simplified version of a DncList, consisting of the name, division, import status, and size.

Wraps GET /api/v2/outbound/dnclists/divisionviews/{dncListId} 

Requires ALL permissions: 

* outbound:dncList:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | Dnclist ID
include_import_status = false # bool | Include import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)

try:
    # Get a basic DncList information object
    api_response = api_instance.get_outbound_dnclists_divisionview(dnc_list_id, include_import_status=include_import_status, include_size=include_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_dnclists_divisionview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| Dnclist ID |  |
| **include_import_status** | **bool**| Include import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**DncListDivisionView**](DncListDivisionView.html)

<a name="get_outbound_dnclists_divisionviews"></a>

## [**DncListDivisionViewListing**](DncListDivisionViewListing.html) get_outbound_dnclists_divisionviews(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, dnc_source_type=dnc_source_type, id=id, sort_by=sort_by, sort_order=sort_order)



Query a list of simplified dnc list objects.

This return a simplified version of dnc lists, consisting of the name, division, import status, and size.

Wraps GET /api/v2/outbound/dnclists/divisionviews 

Requires ALL permissions: 

* outbound:dncList:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
include_import_status = false # bool | Include import status (optional) (default to false)
include_size = false # bool | Include size (optional) (default to false)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
dnc_source_type = 'dnc_source_type_example' # str | DncSourceType (optional)
id = ['id_example'] # list[str] | id (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of simplified dnc list objects.
    api_response = api_instance.get_outbound_dnclists_divisionviews(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, dnc_source_type=dnc_source_type, id=id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_dnclists_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_import_status** | **bool**| Include import status | [optional] [default to false] |
| **include_size** | **bool**| Include size | [optional] [default to false] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **dnc_source_type** | **str**| DncSourceType | [optional] <br />**Values**: rds, dnc.com, gryphon |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**DncListDivisionViewListing**](DncListDivisionViewListing.html)

<a name="get_outbound_event"></a>

## [**EventLog**](EventLog.html) get_outbound_event(event_id)



Get Dialer Event



Wraps GET /api/v2/outbound/events/{eventId} 

Requires ANY permissions: 

* outbound:eventLog:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
event_id = 'event_id_example' # str | Event Log ID

try:
    # Get Dialer Event
    api_response = api_instance.get_outbound_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_event: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **event_id** | **str**| Event Log ID |  |
{: class="table table-striped"}

### Return type

[**EventLog**](EventLog.html)

<a name="get_outbound_events"></a>

## [**DialerEventEntityListing**](DialerEventEntityListing.html) get_outbound_events(page_size=page_size, page_number=page_number, filter_type=filter_type, category=category, level=level, sort_by=sort_by, sort_order=sort_order)



Query Event Logs



Wraps GET /api/v2/outbound/events 

Requires ANY permissions: 

* outbound:eventLog:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
category = 'category_example' # str | Category (optional)
level = 'level_example' # str | Level (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query Event Logs
    api_response = api_instance.get_outbound_events(page_size=page_size, page_number=page_number, filter_type=filter_type, category=category, level=level, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_events: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **category** | **str**| Category | [optional]  |
| **level** | **str**| Level | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**DialerEventEntityListing**](DialerEventEntityListing.html)

<a name="get_outbound_messagingcampaign"></a>

## [**MessagingCampaign**](MessagingCampaign.html) get_outbound_messagingcampaign(messaging_campaign_id)



Get an Outbound Messaging Campaign



Wraps GET /api/v2/outbound/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
messaging_campaign_id = 'messaging_campaign_id_example' # str | The Messaging Campaign ID

try:
    # Get an Outbound Messaging Campaign
    api_response = api_instance.get_outbound_messagingcampaign(messaging_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |
{: class="table table-striped"}

### Return type

[**MessagingCampaign**](MessagingCampaign.html)

<a name="get_outbound_messagingcampaign_progress"></a>

## [**CampaignProgress**](CampaignProgress.html) get_outbound_messagingcampaign_progress(messaging_campaign_id)



Get messaging campaign's progress



Wraps GET /api/v2/outbound/messagingcampaigns/{messagingCampaignId}/progress 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
messaging_campaign_id = 'messaging_campaign_id_example' # str | The Messaging Campaign ID

try:
    # Get messaging campaign's progress
    api_response = api_instance.get_outbound_messagingcampaign_progress(messaging_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaign_progress: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignProgress**](CampaignProgress.html)

<a name="get_outbound_messagingcampaigns"></a>

## [**MessagingCampaignEntityListing**](MessagingCampaignEntityListing.html) get_outbound_messagingcampaigns(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, contact_list_id=contact_list_id, division_id=division_id, type=type, sender_sms_phone_number=sender_sms_phone_number, id=id)



Query a list of Messaging Campaigns



Wraps GET /api/v2/outbound/messagingcampaigns 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'name' # str | The field to sort by (optional) (default to name)
sort_order = 'ascending' # str | The direction to sort (optional) (default to ascending)
name = 'name_example' # str | Name (optional)
contact_list_id = 'contact_list_id_example' # str | Contact List ID (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
type = 'type_example' # str | Campaign Type (optional)
sender_sms_phone_number = 'sender_sms_phone_number_example' # str | Sender SMS Phone Number (optional)
id = ['id_example'] # list[str] | A list of messaging campaign ids to bulk fetch (optional)

try:
    # Query a list of Messaging Campaigns
    api_response = api_instance.get_outbound_messagingcampaigns(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, contact_list_id=contact_list_id, division_id=division_id, type=type, sender_sms_phone_number=sender_sms_phone_number, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaigns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| The field to sort by | [optional] [default to name]<br />**Values**: campaignStatus, name, type |
| **sort_order** | **str**| The direction to sort | [optional] [default to ascending]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
| **contact_list_id** | **str**| Contact List ID | [optional]  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
| **type** | **str**| Campaign Type | [optional] <br />**Values**: EMAIL, SMS |
| **sender_sms_phone_number** | **str**| Sender SMS Phone Number | [optional]  |
| **id** | [**list[str]**](str.html)| A list of messaging campaign ids to bulk fetch | [optional]  |
{: class="table table-striped"}

### Return type

[**MessagingCampaignEntityListing**](MessagingCampaignEntityListing.html)

<a name="get_outbound_messagingcampaigns_divisionview"></a>

## [**MessagingCampaignDivisionView**](MessagingCampaignDivisionView.html) get_outbound_messagingcampaigns_divisionview(messaging_campaign_id)



Get a basic Messaging Campaign information object

This returns a simplified version of a Messaging Campaign, consisting of id, name, and division.

Wraps GET /api/v2/outbound/messagingcampaigns/divisionviews/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:search
* outbound:emailCampaign:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
messaging_campaign_id = 'messaging_campaign_id_example' # str | The Messaging Campaign ID

try:
    # Get a basic Messaging Campaign information object
    api_response = api_instance.get_outbound_messagingcampaigns_divisionview(messaging_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaigns_divisionview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |
{: class="table table-striped"}

### Return type

[**MessagingCampaignDivisionView**](MessagingCampaignDivisionView.html)

<a name="get_outbound_messagingcampaigns_divisionviews"></a>

## [**MessagingCampaignDivisionViewEntityListing**](MessagingCampaignDivisionViewEntityListing.html) get_outbound_messagingcampaigns_divisionviews(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, type=type, id=id, sender_sms_phone_number=sender_sms_phone_number)



Query a list of basic Messaging Campaign information objects

This returns a listing of simplified Messaging Campaigns, each consisting of id, name, and division.

Wraps GET /api/v2/outbound/messagingcampaigns/divisionviews 

Requires ANY permissions: 

* outbound:messagingCampaign:search
* outbound:emailCampaign:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'a' # str | The direction to sort (optional) (default to a)
name = 'name_example' # str | Name (optional)
type = 'type_example' # str | Campaign Type (optional)
id = ['id_example'] # list[str] | id (optional)
sender_sms_phone_number = 'sender_sms_phone_number_example' # str | Sender SMS Phone Number (optional)

try:
    # Query a list of basic Messaging Campaign information objects
    api_response = api_instance.get_outbound_messagingcampaigns_divisionviews(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, type=type, id=id, sender_sms_phone_number=sender_sms_phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaigns_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| The direction to sort | [optional] [default to a]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
| **type** | **str**| Campaign Type | [optional] <br />**Values**: EMAIL, SMS |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **sender_sms_phone_number** | **str**| Sender SMS Phone Number | [optional]  |
{: class="table table-striped"}

### Return type

[**MessagingCampaignDivisionViewEntityListing**](MessagingCampaignDivisionViewEntityListing.html)

<a name="get_outbound_ruleset"></a>

## [**RuleSet**](RuleSet.html) get_outbound_ruleset(rule_set_id)



Get a Rule Set by ID.



Wraps GET /api/v2/outbound/rulesets/{ruleSetId} 

Requires ANY permissions: 

* outbound:ruleSet:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
rule_set_id = 'rule_set_id_example' # str | Rule Set ID

try:
    # Get a Rule Set by ID.
    api_response = api_instance.get_outbound_ruleset(rule_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_ruleset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_set_id** | **str**| Rule Set ID |  |
{: class="table table-striped"}

### Return type

[**RuleSet**](RuleSet.html)

<a name="get_outbound_rulesets"></a>

## [**RuleSetEntityListing**](RuleSetEntityListing.html) get_outbound_rulesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)



Query a list of Rule Sets.



Wraps GET /api/v2/outbound/rulesets 

Requires ANY permissions: 

* outbound:ruleSet:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of Rule Sets.
    api_response = api_instance.get_outbound_rulesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_rulesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**RuleSetEntityListing**](RuleSetEntityListing.html)

<a name="get_outbound_schedules_campaign"></a>

## [**CampaignSchedule**](CampaignSchedule.html) get_outbound_schedules_campaign(campaign_id)



Get a dialer campaign schedule.



Wraps GET /api/v2/outbound/schedules/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Get a dialer campaign schedule.
    api_response = api_instance.get_outbound_schedules_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**CampaignSchedule**](CampaignSchedule.html)

<a name="get_outbound_schedules_campaigns"></a>

## [**list[CampaignSchedule]**](CampaignSchedule.html) get_outbound_schedules_campaigns()



Query for a list of dialer campaign schedules.



Wraps GET /api/v2/outbound/schedules/campaigns 

Requires ANY permissions: 

* outbound:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()

try:
    # Query for a list of dialer campaign schedules.
    api_response = api_instance.get_outbound_schedules_campaigns()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_campaigns: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**list[CampaignSchedule]**](CampaignSchedule.html)

<a name="get_outbound_schedules_sequence"></a>

## [**SequenceSchedule**](SequenceSchedule.html) get_outbound_schedules_sequence(sequence_id)



Get a dialer sequence schedule.



Wraps GET /api/v2/outbound/schedules/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
sequence_id = 'sequence_id_example' # str | Sequence ID

try:
    # Get a dialer sequence schedule.
    api_response = api_instance.get_outbound_schedules_sequence(sequence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_sequence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sequence_id** | **str**| Sequence ID |  |
{: class="table table-striped"}

### Return type

[**SequenceSchedule**](SequenceSchedule.html)

<a name="get_outbound_schedules_sequences"></a>

## [**list[SequenceSchedule]**](SequenceSchedule.html) get_outbound_schedules_sequences()



Query for a list of dialer sequence schedules.



Wraps GET /api/v2/outbound/schedules/sequences 

Requires ANY permissions: 

* outbound:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()

try:
    # Query for a list of dialer sequence schedules.
    api_response = api_instance.get_outbound_schedules_sequences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_sequences: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**list[SequenceSchedule]**](SequenceSchedule.html)

<a name="get_outbound_sequence"></a>

## [**CampaignSequence**](CampaignSequence.html) get_outbound_sequence(sequence_id)



Get a dialer campaign sequence.



Wraps GET /api/v2/outbound/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:campaignSequence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
sequence_id = 'sequence_id_example' # str | Campaign Sequence ID

try:
    # Get a dialer campaign sequence.
    api_response = api_instance.get_outbound_sequence(sequence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_sequence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sequence_id** | **str**| Campaign Sequence ID |  |
{: class="table table-striped"}

### Return type

[**CampaignSequence**](CampaignSequence.html)

<a name="get_outbound_sequences"></a>

## [**CampaignSequenceEntityListing**](CampaignSequenceEntityListing.html) get_outbound_sequences(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)



Query a list of dialer campaign sequences.



Wraps GET /api/v2/outbound/sequences 

Requires ANY permissions: 

* outbound:campaignSequence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = false # bool | Whether to return an empty page when there are no results for that page (optional) (default to false)
filter_type = 'Prefix' # str | Filter type (optional) (default to Prefix)
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = 'a' # str | Sort order (optional) (default to a)

try:
    # Query a list of dialer campaign sequences.
    api_response = api_instance.get_outbound_sequences(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_sequences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to false] |
| **filter_type** | **str**| Filter type | [optional] [default to Prefix]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to a]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**CampaignSequenceEntityListing**](CampaignSequenceEntityListing.html)

<a name="get_outbound_settings"></a>

## [**OutboundSettings**](OutboundSettings.html) get_outbound_settings()



Get the outbound settings for this organization



Wraps GET /api/v2/outbound/settings 

Requires ANY permissions: 

* outbound:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()

try:
    # Get the outbound settings for this organization
    api_response = api_instance.get_outbound_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**OutboundSettings**](OutboundSettings.html)

<a name="get_outbound_wrapupcodemappings"></a>

## [**WrapUpCodeMapping**](WrapUpCodeMapping.html) get_outbound_wrapupcodemappings()



Get the Dialer wrap up code mapping.



Wraps GET /api/v2/outbound/wrapupcodemappings 

Requires ANY permissions: 

* outbound:wrapUpCodeMapping:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()

try:
    # Get the Dialer wrap up code mapping.
    api_response = api_instance.get_outbound_wrapupcodemappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_wrapupcodemappings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**WrapUpCodeMapping**](WrapUpCodeMapping.html)

<a name="patch_outbound_settings"></a>

##  patch_outbound_settings(body)



Update the outbound settings for this organization



Wraps PATCH /api/v2/outbound/settings 

Requires ANY permissions: 

* outbound:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.OutboundSettings() # OutboundSettings | outboundSettings

try:
    # Update the outbound settings for this organization
    api_instance.patch_outbound_settings(body)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutboundSettings**](OutboundSettings.html)| outboundSettings |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_outbound_attemptlimits"></a>

## [**AttemptLimits**](AttemptLimits.html) post_outbound_attemptlimits(body)



Create attempt limits



Wraps POST /api/v2/outbound/attemptlimits 

Requires ANY permissions: 

* outbound:attemptLimits:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.AttemptLimits() # AttemptLimits | AttemptLimits

try:
    # Create attempt limits
    api_response = api_instance.post_outbound_attemptlimits(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_attemptlimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AttemptLimits**](AttemptLimits.html)| AttemptLimits |  |
{: class="table table-striped"}

### Return type

[**AttemptLimits**](AttemptLimits.html)

<a name="post_outbound_audits"></a>

## [**AuditSearchResult**](AuditSearchResult.html) post_outbound_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, facets_only=facets_only)



Retrieves audits for dialer.



Wraps POST /api/v2/outbound/audits 

Requires ANY permissions: 

* outbound:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.DialerAuditRequest() # DialerAuditRequest | AuditSearch
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'entity.name' # str | Sort by (optional) (default to entity.name)
sort_order = 'ascending' # str | Sort order (optional) (default to ascending)
facets_only = false # bool | Facets only (optional) (default to false)

try:
    # Retrieves audits for dialer.
    api_response = api_instance.post_outbound_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, facets_only=facets_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_audits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DialerAuditRequest**](DialerAuditRequest.html)| AuditSearch |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to entity.name] |
| **sort_order** | **str**| Sort order | [optional] [default to ascending] |
| **facets_only** | **bool**| Facets only | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AuditSearchResult**](AuditSearchResult.html)

<a name="post_outbound_callabletimesets"></a>

## [**CallableTimeSet**](CallableTimeSet.html) post_outbound_callabletimesets(body)



Create callable time set



Wraps POST /api/v2/outbound/callabletimesets 

Requires ANY permissions: 

* outbound:callableTimeSet:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.CallableTimeSet() # CallableTimeSet | DialerCallableTimeSet

try:
    # Create callable time set
    api_response = api_instance.post_outbound_callabletimesets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_callabletimesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CallableTimeSet**](CallableTimeSet.html)| DialerCallableTimeSet |  |
{: class="table table-striped"}

### Return type

[**CallableTimeSet**](CallableTimeSet.html)

<a name="post_outbound_callanalysisresponsesets"></a>

## [**ResponseSet**](ResponseSet.html) post_outbound_callanalysisresponsesets(body)



Create a dialer call analysis response set.



Wraps POST /api/v2/outbound/callanalysisresponsesets 

Requires ANY permissions: 

* outbound:responseSet:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.ResponseSet() # ResponseSet | ResponseSet

try:
    # Create a dialer call analysis response set.
    api_response = api_instance.post_outbound_callanalysisresponsesets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_callanalysisresponsesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ResponseSet**](ResponseSet.html)| ResponseSet |  |
{: class="table table-striped"}

### Return type

[**ResponseSet**](ResponseSet.html)

<a name="post_outbound_campaign_agentownedmappingpreview"></a>

## [**Empty**](Empty.html) post_outbound_campaign_agentownedmappingpreview(campaign_id)



Initiate request for a preview of how agents will be mapped to this campaign's contact list.



Wraps POST /api/v2/outbound/campaigns/{campaignId}/agentownedmappingpreview 

Requires ALL permissions: 

* outbound:campaign:view
* outbound:contact:view
* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID

try:
    # Initiate request for a preview of how agents will be mapped to this campaign's contact list.
    api_response = api_instance.post_outbound_campaign_agentownedmappingpreview(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaign_agentownedmappingpreview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="post_outbound_campaign_callback_schedule"></a>

## [**ContactCallbackRequest**](ContactCallbackRequest.html) post_outbound_campaign_callback_schedule(campaign_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Schedule a Callback for a Dialer Campaign (Deprecated)

This endpoint is deprecated and may have unexpected results. Please use \"/conversations/{conversationId}/participants/{participantId}/callbacks instead.\"

Wraps POST /api/v2/outbound/campaigns/{campaignId}/callback/schedule 

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
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID
body = PureCloudPlatformClientV2.ContactCallbackRequest() # ContactCallbackRequest | ContactCallbackRequest

try:
    # Schedule a Callback for a Dialer Campaign (Deprecated)
    api_response = api_instance.post_outbound_campaign_callback_schedule(campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaign_callback_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **body** | [**ContactCallbackRequest**](ContactCallbackRequest.html)| ContactCallbackRequest |  |
{: class="table table-striped"}

### Return type

[**ContactCallbackRequest**](ContactCallbackRequest.html)

<a name="post_outbound_campaignrules"></a>

## [**CampaignRule**](CampaignRule.html) post_outbound_campaignrules(body)



Create Campaign Rule



Wraps POST /api/v2/outbound/campaignrules 

Requires ANY permissions: 

* outbound:campaignRule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.CampaignRule() # CampaignRule | CampaignRule

try:
    # Create Campaign Rule
    api_response = api_instance.post_outbound_campaignrules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaignrules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CampaignRule**](CampaignRule.html)| CampaignRule |  |
{: class="table table-striped"}

### Return type

[**CampaignRule**](CampaignRule.html)

<a name="post_outbound_campaigns"></a>

## [**Campaign**](Campaign.html) post_outbound_campaigns(body)



Create a campaign.



Wraps POST /api/v2/outbound/campaigns 

Requires ANY permissions: 

* outbound:campaign:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.Campaign() # Campaign | Campaign

try:
    # Create a campaign.
    api_response = api_instance.post_outbound_campaigns(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaigns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Campaign**](Campaign.html)| Campaign |  |
{: class="table table-striped"}

### Return type

[**Campaign**](Campaign.html)

<a name="post_outbound_campaigns_progress"></a>

## [**list[CampaignProgress]**](CampaignProgress.html) post_outbound_campaigns_progress(body)



Get progress for a list of campaigns



Wraps POST /api/v2/outbound/campaigns/progress 

Requires ANY permissions: 

* outbound:campaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Campaign IDs

try:
    # Get progress for a list of campaigns
    api_response = api_instance.post_outbound_campaigns_progress(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaigns_progress: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **list[str]**| Campaign IDs |  |
{: class="table table-striped"}

### Return type

[**list[CampaignProgress]**](CampaignProgress.html)

<a name="post_outbound_contactlist_clear"></a>

##  post_outbound_contactlist_clear(contact_list_id)



Deletes all contacts out of a list. All outstanding recalls or rule-scheduled callbacks for non-preview campaigns configured with the contactlist will be cancelled.



Wraps POST /api/v2/outbound/contactlists/{contactListId}/clear 

Requires ANY permissions: 

* outbound:contact:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID

try:
    # Deletes all contacts out of a list. All outstanding recalls or rule-scheduled callbacks for non-preview campaigns configured with the contactlist will be cancelled.
    api_instance.post_outbound_contactlist_clear(contact_list_id)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_clear: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_outbound_contactlist_contacts"></a>

## [**list[DialerContact]**](DialerContact.html) post_outbound_contactlist_contacts(contact_list_id, body, priority=priority, clear_system_data=clear_system_data, do_not_queue=do_not_queue)



Add contacts to a contact list.



Wraps POST /api/v2/outbound/contactlists/{contactListId}/contacts 

Requires ANY permissions: 

* outbound:contact:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID
body = [PureCloudPlatformClientV2.WritableDialerContact()] # list[WritableDialerContact] | Contact
priority = true # bool | Contact priority. True means the contact(s) will be dialed next; false means the contact will go to the end of the contact queue. (optional)
clear_system_data = true # bool | Clear system data. True means the system columns (attempts, callable status, etc) stored on the contact will be cleared if the contact already exists; false means they won't. (optional)
do_not_queue = true # bool | Do not queue. True means that updated contacts will not have their positions in the queue altered, so contacts that have already been dialed will not be redialed. For new contacts, this parameter has no effect; False means that updated contacts will be re-queued, according to the 'priority' parameter. (optional)

try:
    # Add contacts to a contact list.
    api_response = api_instance.post_outbound_contactlist_contacts(contact_list_id, body, priority=priority, clear_system_data=clear_system_data, do_not_queue=do_not_queue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **body** | [**list[WritableDialerContact]**](WritableDialerContact.html)| Contact |  |
| **priority** | **bool**| Contact priority. True means the contact(s) will be dialed next; false means the contact will go to the end of the contact queue. | [optional]  |
| **clear_system_data** | **bool**| Clear system data. True means the system columns (attempts, callable status, etc) stored on the contact will be cleared if the contact already exists; false means they won&#39;t. | [optional]  |
| **do_not_queue** | **bool**| Do not queue. True means that updated contacts will not have their positions in the queue altered, so contacts that have already been dialed will not be redialed. For new contacts, this parameter has no effect; False means that updated contacts will be re-queued, according to the &#39;priority&#39; parameter. | [optional]  |
{: class="table table-striped"}

### Return type

[**list[DialerContact]**](DialerContact.html)

<a name="post_outbound_contactlist_contacts_bulk"></a>

## [**list[DialerContact]**](DialerContact.html) post_outbound_contactlist_contacts_bulk(contact_list_id, body)



Get contacts from a contact list.



Wraps POST /api/v2/outbound/contactlists/{contactListId}/contacts/bulk 

Requires ANY permissions: 

* outbound:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | ContactIds to get.

try:
    # Get contacts from a contact list.
    api_response = api_instance.post_outbound_contactlist_contacts_bulk(contact_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_contacts_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **body** | **list[str]**| ContactIds to get. |  |
{: class="table table-striped"}

### Return type

[**list[DialerContact]**](DialerContact.html)

<a name="post_outbound_contactlist_export"></a>

## [**DomainEntityRef**](DomainEntityRef.html) post_outbound_contactlist_export(contact_list_id)



Initiate the export of a contact list.

Returns 200 if received OK.

Wraps POST /api/v2/outbound/contactlists/{contactListId}/export 

Requires ALL permissions: 

* outbound:contact:view
* outbound:contactList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID

try:
    # Initiate the export of a contact list.
    api_response = api_instance.post_outbound_contactlist_export(contact_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
{: class="table table-striped"}

### Return type

[**DomainEntityRef**](DomainEntityRef.html)

<a name="post_outbound_contactlistfilters"></a>

## [**ContactListFilter**](ContactListFilter.html) post_outbound_contactlistfilters(body)



Create Contact List Filter



Wraps POST /api/v2/outbound/contactlistfilters 

Requires ANY permissions: 

* outbound:contactListFilter:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.ContactListFilter() # ContactListFilter | ContactListFilter

try:
    # Create Contact List Filter
    api_response = api_instance.post_outbound_contactlistfilters(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlistfilters: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactListFilter**](ContactListFilter.html)| ContactListFilter |  |
{: class="table table-striped"}

### Return type

[**ContactListFilter**](ContactListFilter.html)

<a name="post_outbound_contactlistfilters_preview"></a>

## [**FilterPreviewResponse**](FilterPreviewResponse.html) post_outbound_contactlistfilters_preview(body)



Get a preview of the output of a contact list filter



Wraps POST /api/v2/outbound/contactlistfilters/preview 

Requires ANY permissions: 

* outbound:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.ContactListFilter() # ContactListFilter | ContactListFilter

try:
    # Get a preview of the output of a contact list filter
    api_response = api_instance.post_outbound_contactlistfilters_preview(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlistfilters_preview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactListFilter**](ContactListFilter.html)| ContactListFilter |  |
{: class="table table-striped"}

### Return type

[**FilterPreviewResponse**](FilterPreviewResponse.html)

<a name="post_outbound_contactlists"></a>

## [**ContactList**](ContactList.html) post_outbound_contactlists(body)



Create a contact List.



Wraps POST /api/v2/outbound/contactlists 

Requires ANY permissions: 

* outbound:contactList:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.ContactList() # ContactList | ContactList

try:
    # Create a contact List.
    api_response = api_instance.post_outbound_contactlists(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlists: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactList**](ContactList.html)| ContactList |  |
{: class="table table-striped"}

### Return type

[**ContactList**](ContactList.html)

<a name="post_outbound_conversation_dnc"></a>

##  post_outbound_conversation_dnc(conversation_id)



Add phone numbers to a Dialer DNC list.



Wraps POST /api/v2/outbound/conversations/{conversationId}/dnc 

Requires ANY permissions: 

* outbound:dnc:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
conversation_id = 'conversation_id_example' # str | Conversation ID

try:
    # Add phone numbers to a Dialer DNC list.
    api_instance.post_outbound_conversation_dnc(conversation_id)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_conversation_dnc: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_outbound_dnclist_export"></a>

## [**DomainEntityRef**](DomainEntityRef.html) post_outbound_dnclist_export(dnc_list_id)



Initiate the export of a dnc list.

Returns 200 if received OK.

Wraps POST /api/v2/outbound/dnclists/{dncListId}/export 

Requires ALL permissions: 

* outbound:dnc:view
* outbound:dncList:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID

try:
    # Initiate the export of a dnc list.
    api_response = api_instance.post_outbound_dnclist_export(dnc_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_dnclist_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
{: class="table table-striped"}

### Return type

[**DomainEntityRef**](DomainEntityRef.html)

<a name="post_outbound_dnclist_phonenumbers"></a>

##  post_outbound_dnclist_phonenumbers(dnc_list_id, body, expiration_date_time=expiration_date_time)



Add phone numbers to a DNC list.

Only Internal DNC lists may be appended to

Wraps POST /api/v2/outbound/dnclists/{dncListId}/phonenumbers 

Requires ANY permissions: 

* outbound:dnc:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | DNC Phone Numbers
expiration_date_time = 'expiration_date_time_example' # str | Expiration date for DNC phone numbers in yyyy-MM-ddTHH:mmZ format (optional)

try:
    # Add phone numbers to a DNC list.
    api_instance.post_outbound_dnclist_phonenumbers(dnc_list_id, body, expiration_date_time=expiration_date_time)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_dnclist_phonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | **list[str]**| DNC Phone Numbers |  |
| **expiration_date_time** | **str**| Expiration date for DNC phone numbers in yyyy-MM-ddTHH:mmZ format | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_outbound_dnclists"></a>

## [**DncList**](DncList.html) post_outbound_dnclists(body)



Create dialer DNC list



Wraps POST /api/v2/outbound/dnclists 

Requires ANY permissions: 

* outbound:dncList:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.DncListCreate() # DncListCreate | DncList

try:
    # Create dialer DNC list
    api_response = api_instance.post_outbound_dnclists(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_dnclists: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DncListCreate**](DncListCreate.html)| DncList |  |
{: class="table table-striped"}

### Return type

[**DncList**](DncList.html)

<a name="post_outbound_messagingcampaigns"></a>

## [**MessagingCampaign**](MessagingCampaign.html) post_outbound_messagingcampaigns(body)



Create a Messaging Campaign



Wraps POST /api/v2/outbound/messagingcampaigns 

Requires ANY permissions: 

* outbound:messagingCampaign:add
* outbound:emailCampaign:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.MessagingCampaign() # MessagingCampaign | Messaging Campaign

try:
    # Create a Messaging Campaign
    api_response = api_instance.post_outbound_messagingcampaigns(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_messagingcampaigns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MessagingCampaign**](MessagingCampaign.html)| Messaging Campaign |  |
{: class="table table-striped"}

### Return type

[**MessagingCampaign**](MessagingCampaign.html)

<a name="post_outbound_messagingcampaigns_progress"></a>

## [**list[CampaignProgress]**](CampaignProgress.html) post_outbound_messagingcampaigns_progress(body)



Get progress for a list of messaging campaigns



Wraps POST /api/v2/outbound/messagingcampaigns/progress 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Messaging Campaign IDs

try:
    # Get progress for a list of messaging campaigns
    api_response = api_instance.post_outbound_messagingcampaigns_progress(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_messagingcampaigns_progress: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **list[str]**| Messaging Campaign IDs |  |
{: class="table table-striped"}

### Return type

[**list[CampaignProgress]**](CampaignProgress.html)

<a name="post_outbound_rulesets"></a>

## [**RuleSet**](RuleSet.html) post_outbound_rulesets(body)



Create a Rule Set.



Wraps POST /api/v2/outbound/rulesets 

Requires ANY permissions: 

* outbound:ruleSet:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.RuleSet() # RuleSet | RuleSet

try:
    # Create a Rule Set.
    api_response = api_instance.post_outbound_rulesets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_rulesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RuleSet**](RuleSet.html)| RuleSet |  |
{: class="table table-striped"}

### Return type

[**RuleSet**](RuleSet.html)

<a name="post_outbound_sequences"></a>

## [**CampaignSequence**](CampaignSequence.html) post_outbound_sequences(body)



Create a new campaign sequence.



Wraps POST /api/v2/outbound/sequences 

Requires ANY permissions: 

* outbound:campaignSequence:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.CampaignSequence() # CampaignSequence | Organization

try:
    # Create a new campaign sequence.
    api_response = api_instance.post_outbound_sequences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_sequences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CampaignSequence**](CampaignSequence.html)| Organization |  |
{: class="table table-striped"}

### Return type

[**CampaignSequence**](CampaignSequence.html)

<a name="put_outbound_attemptlimit"></a>

## [**AttemptLimits**](AttemptLimits.html) put_outbound_attemptlimit(attempt_limits_id, body)



Update attempt limits



Wraps PUT /api/v2/outbound/attemptlimits/{attemptLimitsId} 

Requires ANY permissions: 

* outbound:attemptLimits:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
attempt_limits_id = 'attempt_limits_id_example' # str | Attempt limits ID
body = PureCloudPlatformClientV2.AttemptLimits() # AttemptLimits | AttemptLimits

try:
    # Update attempt limits
    api_response = api_instance.put_outbound_attemptlimit(attempt_limits_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_attemptlimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **attempt_limits_id** | **str**| Attempt limits ID |  |
| **body** | [**AttemptLimits**](AttemptLimits.html)| AttemptLimits |  |
{: class="table table-striped"}

### Return type

[**AttemptLimits**](AttemptLimits.html)

<a name="put_outbound_callabletimeset"></a>

## [**CallableTimeSet**](CallableTimeSet.html) put_outbound_callabletimeset(callable_time_set_id, body)



Update callable time set



Wraps PUT /api/v2/outbound/callabletimesets/{callableTimeSetId} 

Requires ANY permissions: 

* outbound:callableTimeSet:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
callable_time_set_id = 'callable_time_set_id_example' # str | Callable Time Set ID
body = PureCloudPlatformClientV2.CallableTimeSet() # CallableTimeSet | DialerCallableTimeSet

try:
    # Update callable time set
    api_response = api_instance.put_outbound_callabletimeset(callable_time_set_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_callabletimeset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **callable_time_set_id** | **str**| Callable Time Set ID |  |
| **body** | [**CallableTimeSet**](CallableTimeSet.html)| DialerCallableTimeSet |  |
{: class="table table-striped"}

### Return type

[**CallableTimeSet**](CallableTimeSet.html)

<a name="put_outbound_callanalysisresponseset"></a>

## [**ResponseSet**](ResponseSet.html) put_outbound_callanalysisresponseset(call_analysis_set_id, body)



Update a dialer call analysis response set.



Wraps PUT /api/v2/outbound/callanalysisresponsesets/{callAnalysisSetId} 

Requires ANY permissions: 

* outbound:responseSet:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
call_analysis_set_id = 'call_analysis_set_id_example' # str | Call Analysis Response Set ID
body = PureCloudPlatformClientV2.ResponseSet() # ResponseSet | ResponseSet

try:
    # Update a dialer call analysis response set.
    api_response = api_instance.put_outbound_callanalysisresponseset(call_analysis_set_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_callanalysisresponseset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **call_analysis_set_id** | **str**| Call Analysis Response Set ID |  |
| **body** | [**ResponseSet**](ResponseSet.html)| ResponseSet |  |
{: class="table table-striped"}

### Return type

[**ResponseSet**](ResponseSet.html)

<a name="put_outbound_campaign"></a>

## [**Campaign**](Campaign.html) put_outbound_campaign(campaign_id, body)



Update a campaign.



Wraps PUT /api/v2/outbound/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:campaign:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID
body = PureCloudPlatformClientV2.Campaign() # Campaign | Campaign

try:
    # Update a campaign.
    api_response = api_instance.put_outbound_campaign(campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **body** | [**Campaign**](Campaign.html)| Campaign |  |
{: class="table table-striped"}

### Return type

[**Campaign**](Campaign.html)

<a name="put_outbound_campaign_agent"></a>

## str** put_outbound_campaign_agent(campaign_id, user_id, body)



Send notification that an agent's state changed 

New agent state.

Wraps PUT /api/v2/outbound/campaigns/{campaignId}/agents/{userId} 

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
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID
user_id = 'user_id_example' # str | Agent's user ID
body = PureCloudPlatformClientV2.Agent() # Agent | agent

try:
    # Send notification that an agent's state changed 
    api_response = api_instance.put_outbound_campaign_agent(campaign_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_campaign_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **user_id** | **str**| Agent&#39;s user ID |  |
| **body** | [**Agent**](Agent.html)| agent |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_outbound_campaignrule"></a>

## [**CampaignRule**](CampaignRule.html) put_outbound_campaignrule(campaign_rule_id, body)



Update Campaign Rule



Wraps PUT /api/v2/outbound/campaignrules/{campaignRuleId} 

Requires ANY permissions: 

* outbound:campaignRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_rule_id = 'campaign_rule_id_example' # str | Campaign Rule ID
body = PureCloudPlatformClientV2.CampaignRule() # CampaignRule | CampaignRule

try:
    # Update Campaign Rule
    api_response = api_instance.put_outbound_campaignrule(campaign_rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_campaignrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_rule_id** | **str**| Campaign Rule ID |  |
| **body** | [**CampaignRule**](CampaignRule.html)| CampaignRule |  |
{: class="table table-striped"}

### Return type

[**CampaignRule**](CampaignRule.html)

<a name="put_outbound_contactlist"></a>

## [**ContactList**](ContactList.html) put_outbound_contactlist(contact_list_id, body)



Update a contact list.



Wraps PUT /api/v2/outbound/contactlists/{contactListId} 

Requires ANY permissions: 

* outbound:contactList:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | ContactList ID
body = PureCloudPlatformClientV2.ContactList() # ContactList | ContactList

try:
    # Update a contact list.
    api_response = api_instance.put_outbound_contactlist(contact_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_contactlist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
| **body** | [**ContactList**](ContactList.html)| ContactList |  |
{: class="table table-striped"}

### Return type

[**ContactList**](ContactList.html)

<a name="put_outbound_contactlist_contact"></a>

## [**DialerContact**](DialerContact.html) put_outbound_contactlist_contact(contact_list_id, contact_id, body)



Update a contact.



Wraps PUT /api/v2/outbound/contactlists/{contactListId}/contacts/{contactId} 

Requires ANY permissions: 

* outbound:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_id = 'contact_list_id_example' # str | Contact List ID
contact_id = 'contact_id_example' # str | Contact ID
body = PureCloudPlatformClientV2.DialerContact() # DialerContact | Contact

try:
    # Update a contact.
    api_response = api_instance.put_outbound_contactlist_contact(contact_list_id, contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_contactlist_contact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **contact_id** | **str**| Contact ID |  |
| **body** | [**DialerContact**](DialerContact.html)| Contact |  |
{: class="table table-striped"}

### Return type

[**DialerContact**](DialerContact.html)

<a name="put_outbound_contactlistfilter"></a>

## [**ContactListFilter**](ContactListFilter.html) put_outbound_contactlistfilter(contact_list_filter_id, body)



Update Contact List Filter



Wraps PUT /api/v2/outbound/contactlistfilters/{contactListFilterId} 

Requires ANY permissions: 

* outbound:contactListFilter:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
contact_list_filter_id = 'contact_list_filter_id_example' # str | Contact List Filter ID
body = PureCloudPlatformClientV2.ContactListFilter() # ContactListFilter | ContactListFilter

try:
    # Update Contact List Filter
    api_response = api_instance.put_outbound_contactlistfilter(contact_list_filter_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_contactlistfilter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_filter_id** | **str**| Contact List Filter ID |  |
| **body** | [**ContactListFilter**](ContactListFilter.html)| ContactListFilter |  |
{: class="table table-striped"}

### Return type

[**ContactListFilter**](ContactListFilter.html)

<a name="put_outbound_dnclist"></a>

## [**DncList**](DncList.html) put_outbound_dnclist(dnc_list_id, body)



Update dialer DNC list



Wraps PUT /api/v2/outbound/dnclists/{dncListId} 

Requires ANY permissions: 

* outbound:dncList:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
dnc_list_id = 'dnc_list_id_example' # str | DncList ID
body = PureCloudPlatformClientV2.DncList() # DncList | DncList

try:
    # Update dialer DNC list
    api_response = api_instance.put_outbound_dnclist(dnc_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_dnclist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | [**DncList**](DncList.html)| DncList |  |
{: class="table table-striped"}

### Return type

[**DncList**](DncList.html)

<a name="put_outbound_messagingcampaign"></a>

## [**MessagingCampaign**](MessagingCampaign.html) put_outbound_messagingcampaign(messaging_campaign_id, body)



Update an Outbound Messaging Campaign



Wraps PUT /api/v2/outbound/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:edit
* outbound:emailCampaign:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
messaging_campaign_id = 'messaging_campaign_id_example' # str | The Messaging Campaign ID
body = PureCloudPlatformClientV2.MessagingCampaign() # MessagingCampaign | MessagingCampaign

try:
    # Update an Outbound Messaging Campaign
    api_response = api_instance.put_outbound_messagingcampaign(messaging_campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_messagingcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |
| **body** | [**MessagingCampaign**](MessagingCampaign.html)| MessagingCampaign |  |
{: class="table table-striped"}

### Return type

[**MessagingCampaign**](MessagingCampaign.html)

<a name="put_outbound_ruleset"></a>

## [**RuleSet**](RuleSet.html) put_outbound_ruleset(rule_set_id, body)



Update a Rule Set.



Wraps PUT /api/v2/outbound/rulesets/{ruleSetId} 

Requires ANY permissions: 

* outbound:ruleSet:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
rule_set_id = 'rule_set_id_example' # str | Rule Set ID
body = PureCloudPlatformClientV2.RuleSet() # RuleSet | RuleSet

try:
    # Update a Rule Set.
    api_response = api_instance.put_outbound_ruleset(rule_set_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_ruleset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_set_id** | **str**| Rule Set ID |  |
| **body** | [**RuleSet**](RuleSet.html)| RuleSet |  |
{: class="table table-striped"}

### Return type

[**RuleSet**](RuleSet.html)

<a name="put_outbound_schedules_campaign"></a>

## [**CampaignSchedule**](CampaignSchedule.html) put_outbound_schedules_campaign(campaign_id, body)



Update a new campaign schedule.



Wraps PUT /api/v2/outbound/schedules/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
campaign_id = 'campaign_id_example' # str | Campaign ID
body = PureCloudPlatformClientV2.CampaignSchedule() # CampaignSchedule | CampaignSchedule

try:
    # Update a new campaign schedule.
    api_response = api_instance.put_outbound_schedules_campaign(campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_schedules_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **body** | [**CampaignSchedule**](CampaignSchedule.html)| CampaignSchedule |  |
{: class="table table-striped"}

### Return type

[**CampaignSchedule**](CampaignSchedule.html)

<a name="put_outbound_schedules_sequence"></a>

## [**SequenceSchedule**](SequenceSchedule.html) put_outbound_schedules_sequence(sequence_id, body)



Update a new sequence schedule.



Wraps PUT /api/v2/outbound/schedules/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
sequence_id = 'sequence_id_example' # str | Sequence ID
body = PureCloudPlatformClientV2.SequenceSchedule() # SequenceSchedule | SequenceSchedule

try:
    # Update a new sequence schedule.
    api_response = api_instance.put_outbound_schedules_sequence(sequence_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_schedules_sequence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sequence_id** | **str**| Sequence ID |  |
| **body** | [**SequenceSchedule**](SequenceSchedule.html)| SequenceSchedule |  |
{: class="table table-striped"}

### Return type

[**SequenceSchedule**](SequenceSchedule.html)

<a name="put_outbound_sequence"></a>

## [**CampaignSequence**](CampaignSequence.html) put_outbound_sequence(sequence_id, body)



Update a new campaign sequence.



Wraps PUT /api/v2/outbound/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:campaignSequence:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
sequence_id = 'sequence_id_example' # str | Campaign Sequence ID
body = PureCloudPlatformClientV2.CampaignSequence() # CampaignSequence | Organization

try:
    # Update a new campaign sequence.
    api_response = api_instance.put_outbound_sequence(sequence_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_sequence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sequence_id** | **str**| Campaign Sequence ID |  |
| **body** | [**CampaignSequence**](CampaignSequence.html)| Organization |  |
{: class="table table-striped"}

### Return type

[**CampaignSequence**](CampaignSequence.html)

<a name="put_outbound_wrapupcodemappings"></a>

## [**WrapUpCodeMapping**](WrapUpCodeMapping.html) put_outbound_wrapupcodemappings(body)



Update the Dialer wrap up code mapping.



Wraps PUT /api/v2/outbound/wrapupcodemappings 

Requires ANY permissions: 

* outbound:wrapUpCodeMapping:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OutboundApi()
body = PureCloudPlatformClientV2.WrapUpCodeMapping() # WrapUpCodeMapping | wrapUpCodeMapping

try:
    # Update the Dialer wrap up code mapping.
    api_response = api_instance.put_outbound_wrapupcodemappings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_wrapupcodemappings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WrapUpCodeMapping**](WrapUpCodeMapping.html)| wrapUpCodeMapping |  |
{: class="table table-striped"}

### Return type

[**WrapUpCodeMapping**](WrapUpCodeMapping.html)

