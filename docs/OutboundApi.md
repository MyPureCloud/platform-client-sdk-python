# OutboundApi

## PureCloudPlatformClientV2.OutboundApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_outbound_attemptlimit**](#delete_outbound_attemptlimit) | Delete attempt limits|
|[**delete_outbound_callabletimeset**](#delete_outbound_callabletimeset) | Delete callable time set|
|[**delete_outbound_callanalysisresponseset**](#delete_outbound_callanalysisresponseset) | Delete a dialer call analysis response set.|
|[**delete_outbound_campaign**](#delete_outbound_campaign) | Delete a campaign.|
|[**delete_outbound_campaign_progress**](#delete_outbound_campaign_progress) | Reset campaign progress and recycle the campaign|
|[**delete_outbound_campaignrule**](#delete_outbound_campaignrule) | Delete Campaign Rule|
|[**delete_outbound_contactlist**](#delete_outbound_contactlist) | Delete a contact list.|
|[**delete_outbound_contactlist_contact**](#delete_outbound_contactlist_contact) | Delete a contact.|
|[**delete_outbound_contactlist_contacts**](#delete_outbound_contactlist_contacts) | Delete contacts from a contact list.|
|[**delete_outbound_contactlistfilter**](#delete_outbound_contactlistfilter) | Delete Contact List Filter|
|[**delete_outbound_contactlists**](#delete_outbound_contactlists) | Delete multiple contact lists.|
|[**delete_outbound_contactlisttemplate**](#delete_outbound_contactlisttemplate) | Delete Contact List Template|
|[**delete_outbound_contactlisttemplates**](#delete_outbound_contactlisttemplates) | Delete multiple contact list templates.|
|[**delete_outbound_digitalruleset**](#delete_outbound_digitalruleset) | Delete an Outbound Digital Rule Set|
|[**delete_outbound_dnclist**](#delete_outbound_dnclist) | Delete dialer DNC list|
|[**delete_outbound_dnclist_customexclusioncolumns**](#delete_outbound_dnclist_customexclusioncolumns) | Deletes all or expired custom exclusion column entries from a DNC list.|
|[**delete_outbound_dnclist_emailaddresses**](#delete_outbound_dnclist_emailaddresses) | Deletes all or expired email addresses from a DNC list.|
|[**delete_outbound_dnclist_phonenumbers**](#delete_outbound_dnclist_phonenumbers) | Deletes all or expired phone numbers from a DNC list.|
|[**delete_outbound_dnclist_whatsappnumbers**](#delete_outbound_dnclist_whatsappnumbers) | Deletes all or expired whatsApp numbers from a DNC list.|
|[**delete_outbound_filespecificationtemplate**](#delete_outbound_filespecificationtemplate) | Delete File Specification Template|
|[**delete_outbound_filespecificationtemplates_bulk**](#delete_outbound_filespecificationtemplates_bulk) | Delete multiple file specification templates.|
|[**delete_outbound_importtemplate**](#delete_outbound_importtemplate) | Delete Import Template|
|[**delete_outbound_importtemplates**](#delete_outbound_importtemplates) | Delete multiple import templates.|
|[**delete_outbound_messagingcampaign**](#delete_outbound_messagingcampaign) | Delete an Outbound Messaging Campaign|
|[**delete_outbound_messagingcampaign_progress**](#delete_outbound_messagingcampaign_progress) | Reset messaging campaign progress and recycle the messaging campaign|
|[**delete_outbound_ruleset**](#delete_outbound_ruleset) | Delete a Rule Set.|
|[**delete_outbound_schedules_campaign**](#delete_outbound_schedules_campaign) | Delete a dialer campaign schedule.|
|[**delete_outbound_schedules_emailcampaign**](#delete_outbound_schedules_emailcampaign) | Delete an email campaign schedule.|
|[**delete_outbound_schedules_messagingcampaign**](#delete_outbound_schedules_messagingcampaign) | Delete a messaging campaign schedule.|
|[**delete_outbound_schedules_sequence**](#delete_outbound_schedules_sequence) | Delete a dialer sequence schedule.|
|[**delete_outbound_schedules_whatsappcampaign**](#delete_outbound_schedules_whatsappcampaign) | Delete a WhatsApp campaign schedule.|
|[**delete_outbound_sequence**](#delete_outbound_sequence) | Delete a dialer campaign sequence.|
|[**get_outbound_attemptlimit**](#get_outbound_attemptlimit) | Get attempt limits|
|[**get_outbound_attemptlimits**](#get_outbound_attemptlimits) | Query attempt limits list|
|[**get_outbound_callabletimeset**](#get_outbound_callabletimeset) | Get callable time set|
|[**get_outbound_callabletimesets**](#get_outbound_callabletimesets) | Query callable time set list|
|[**get_outbound_callanalysisresponseset**](#get_outbound_callanalysisresponseset) | Get a dialer call analysis response set.|
|[**get_outbound_callanalysisresponsesets**](#get_outbound_callanalysisresponsesets) | Query a list of dialer call analysis response sets.|
|[**get_outbound_campaign**](#get_outbound_campaign) | Get dialer campaign.|
|[**get_outbound_campaign_agentownedmappingpreview_results**](#get_outbound_campaign_agentownedmappingpreview_results) | Get a preview of how agents will be mapped to this campaign&#39;s contact list.|
|[**get_outbound_campaign_diagnostics**](#get_outbound_campaign_diagnostics) | Get campaign diagnostics|
|[**get_outbound_campaign_interactions**](#get_outbound_campaign_interactions) | Get dialer campaign interactions.|
|[**get_outbound_campaign_linedistribution**](#get_outbound_campaign_linedistribution) | Get line distribution information for campaigns using same Edge Group or Site as given campaign|
|[**get_outbound_campaign_progress**](#get_outbound_campaign_progress) | Get campaign progress|
|[**get_outbound_campaign_skillcombinations**](#get_outbound_campaign_skillcombinations) | Get the remaining and total contact count for each skill combination in a skills campaign|
|[**get_outbound_campaign_stats**](#get_outbound_campaign_stats) | Get statistics about a Dialer Campaign|
|[**get_outbound_campaignrule**](#get_outbound_campaignrule) | Get Campaign Rule|
|[**get_outbound_campaignrules**](#get_outbound_campaignrules) | Query Campaign Rule list|
|[**get_outbound_campaigns**](#get_outbound_campaigns) | Query a list of dialer campaigns.|
|[**get_outbound_campaigns_all**](#get_outbound_campaigns_all) | Query across all types of campaigns by division|
|[**get_outbound_campaigns_all_divisionviews**](#get_outbound_campaigns_all_divisionviews) | Query across all types of campaigns|
|[**get_outbound_campaigns_divisionview**](#get_outbound_campaigns_divisionview) | Get a basic Campaign information object|
|[**get_outbound_campaigns_divisionviews**](#get_outbound_campaigns_divisionviews) | Query a list of basic Campaign information objects|
|[**get_outbound_contactlist**](#get_outbound_contactlist) | Get a dialer contact list.|
|[**get_outbound_contactlist_contact**](#get_outbound_contactlist_contact) | Get a contact.|
|[**get_outbound_contactlist_contacts_bulk_job**](#get_outbound_contactlist_contacts_bulk_job) | Get bulk operation job.|
|[**get_outbound_contactlist_contacts_bulk_jobs**](#get_outbound_contactlist_contacts_bulk_jobs) | Get 10 most recent bulk operation jobs associated with contact list.|
|[**get_outbound_contactlist_export**](#get_outbound_contactlist_export) | Get the URI of a contact list export.|
|[**get_outbound_contactlist_importstatus**](#get_outbound_contactlist_importstatus) | Get dialer contactList import status.|
|[**get_outbound_contactlist_timezonemappingpreview**](#get_outbound_contactlist_timezonemappingpreview) | Preview the result of applying Automatic Time Zone Mapping to a contact list|
|[**get_outbound_contactlistfilter**](#get_outbound_contactlistfilter) | Get Contact list filter|
|[**get_outbound_contactlistfilters**](#get_outbound_contactlistfilters) | Query Contact list filters|
|[**get_outbound_contactlists**](#get_outbound_contactlists) | Query a list of contact lists.|
|[**get_outbound_contactlists_divisionview**](#get_outbound_contactlists_divisionview) | Get a basic ContactList information object|
|[**get_outbound_contactlists_divisionviews**](#get_outbound_contactlists_divisionviews) | Query a list of simplified contact list objects.|
|[**get_outbound_contactlisttemplate**](#get_outbound_contactlisttemplate) | Get Contact List Template|
|[**get_outbound_contactlisttemplates**](#get_outbound_contactlisttemplates) | Query a list of contact list templates|
|[**get_outbound_digitalruleset**](#get_outbound_digitalruleset) | Get an Outbound Digital Rule Set|
|[**get_outbound_digitalrulesets**](#get_outbound_digitalrulesets) | Query a list of Outbound Digital Rule Sets|
|[**get_outbound_dnclist**](#get_outbound_dnclist) | Get dialer DNC list|
|[**get_outbound_dnclist_export**](#get_outbound_dnclist_export) | Get the URI of a DNC list export.|
|[**get_outbound_dnclist_importstatus**](#get_outbound_dnclist_importstatus) | Get dialer dncList import status.|
|[**get_outbound_dnclists**](#get_outbound_dnclists) | Query dialer DNC lists|
|[**get_outbound_dnclists_divisionview**](#get_outbound_dnclists_divisionview) | Get a basic DncList information object|
|[**get_outbound_dnclists_divisionviews**](#get_outbound_dnclists_divisionviews) | Query a list of simplified dnc list objects.|
|[**get_outbound_event**](#get_outbound_event) | Get Dialer Event|
|[**get_outbound_events**](#get_outbound_events) | Query Event Logs|
|[**get_outbound_filespecificationtemplate**](#get_outbound_filespecificationtemplate) | Get File Specification Template|
|[**get_outbound_filespecificationtemplates**](#get_outbound_filespecificationtemplates) | Query File Specification Templates|
|[**get_outbound_importtemplate**](#get_outbound_importtemplate) | Get Import Template|
|[**get_outbound_importtemplate_importstatus**](#get_outbound_importtemplate_importstatus) | Get the import status for an import template.|
|[**get_outbound_importtemplates**](#get_outbound_importtemplates) | Query Import Templates|
|[**get_outbound_messagingcampaign**](#get_outbound_messagingcampaign) | Get an Outbound Messaging Campaign|
|[**get_outbound_messagingcampaign_diagnostics**](#get_outbound_messagingcampaign_diagnostics) | Get messaging campaign diagnostics|
|[**get_outbound_messagingcampaign_progress**](#get_outbound_messagingcampaign_progress) | Get messaging campaign&#39;s progress|
|[**get_outbound_messagingcampaigns**](#get_outbound_messagingcampaigns) | Query a list of Messaging Campaigns|
|[**get_outbound_messagingcampaigns_divisionview**](#get_outbound_messagingcampaigns_divisionview) | Get a basic Messaging Campaign information object|
|[**get_outbound_messagingcampaigns_divisionviews**](#get_outbound_messagingcampaigns_divisionviews) | Query a list of basic Messaging Campaign information objects|
|[**get_outbound_ruleset**](#get_outbound_ruleset) | Get a Rule Set by ID.|
|[**get_outbound_rulesets**](#get_outbound_rulesets) | Query a list of Rule Sets.|
|[**get_outbound_schedules_campaign**](#get_outbound_schedules_campaign) | Get a dialer campaign schedule.|
|[**get_outbound_schedules_campaigns**](#get_outbound_schedules_campaigns) | Query for a list of dialer campaign schedules.|
|[**get_outbound_schedules_emailcampaign**](#get_outbound_schedules_emailcampaign) | Get an email campaign schedule.|
|[**get_outbound_schedules_emailcampaigns**](#get_outbound_schedules_emailcampaigns) | Query for a list of email campaign schedules.|
|[**get_outbound_schedules_messagingcampaign**](#get_outbound_schedules_messagingcampaign) | Get a messaging campaign schedule.|
|[**get_outbound_schedules_messagingcampaigns**](#get_outbound_schedules_messagingcampaigns) | Query for a list of messaging campaign schedules.|
|[**get_outbound_schedules_sequence**](#get_outbound_schedules_sequence) | Get a dialer sequence schedule.|
|[**get_outbound_schedules_sequences**](#get_outbound_schedules_sequences) | Query for a list of dialer sequence schedules.|
|[**get_outbound_schedules_whatsappcampaign**](#get_outbound_schedules_whatsappcampaign) | Get a WhatsApp campaign schedule.|
|[**get_outbound_schedules_whatsappcampaigns**](#get_outbound_schedules_whatsappcampaigns) | Query for a list of WhatsApp campaign schedules.|
|[**get_outbound_sequence**](#get_outbound_sequence) | Get a dialer campaign sequence.|
|[**get_outbound_sequences**](#get_outbound_sequences) | Query a list of dialer campaign sequences.|
|[**get_outbound_settings**](#get_outbound_settings) | Get the outbound settings for this organization|
|[**get_outbound_wrapupcodemappings**](#get_outbound_wrapupcodemappings) | Get the Dialer wrap up code mapping.|
|[**patch_outbound_campaign**](#patch_outbound_campaign) | Update a campaign.|
|[**patch_outbound_dnclist_customexclusioncolumns**](#patch_outbound_dnclist_customexclusioncolumns) | Add entries to or delete entries from a DNC list.|
|[**patch_outbound_dnclist_emailaddresses**](#patch_outbound_dnclist_emailaddresses) | Add emails to or Delete emails from a DNC list.|
|[**patch_outbound_dnclist_phonenumbers**](#patch_outbound_dnclist_phonenumbers) | Add numbers to or delete numbers from a DNC list.|
|[**patch_outbound_dnclist_whatsappnumbers**](#patch_outbound_dnclist_whatsappnumbers) | Add entries to or delete entries from a DNC list.|
|[**patch_outbound_settings**](#patch_outbound_settings) | Update the outbound settings for this organization|
|[**post_outbound_attemptlimits**](#post_outbound_attemptlimits) | Create attempt limits|
|[**post_outbound_callabletimesets**](#post_outbound_callabletimesets) | Create callable time set|
|[**post_outbound_callanalysisresponsesets**](#post_outbound_callanalysisresponsesets) | Create a dialer call analysis response set.|
|[**post_outbound_campaign_agentownedmappingpreview**](#post_outbound_campaign_agentownedmappingpreview) | Initiate request for a preview of how agents will be mapped to this campaign&#39;s contact list.|
|[**post_outbound_campaign_callback_schedule**](#post_outbound_campaign_callback_schedule) | Schedule a Callback for a Dialer Campaign (Deprecated)|
|[**post_outbound_campaign_start**](#post_outbound_campaign_start) | Start the campaign|
|[**post_outbound_campaign_stop**](#post_outbound_campaign_stop) | Stop the campaign|
|[**post_outbound_campaignrules**](#post_outbound_campaignrules) | Create Campaign Rule|
|[**post_outbound_campaigns**](#post_outbound_campaigns) | Create a campaign.|
|[**post_outbound_campaigns_progress**](#post_outbound_campaigns_progress) | Get progress for a list of campaigns|
|[**post_outbound_contactlist_clear**](#post_outbound_contactlist_clear) | Deletes all contacts out of a list. All outstanding recalls or rule-scheduled callbacks for non-preview campaigns configured with the contactlist will be cancelled.|
|[**post_outbound_contactlist_contacts**](#post_outbound_contactlist_contacts) | Add contacts to a contact list.|
|[**post_outbound_contactlist_contacts_bulk**](#post_outbound_contactlist_contacts_bulk) | Get contacts from a contact list.|
|[**post_outbound_contactlist_contacts_bulk_remove**](#post_outbound_contactlist_contacts_bulk_remove) | Start an async job to delete contacts using a filter.|
|[**post_outbound_contactlist_contacts_bulk_update**](#post_outbound_contactlist_contacts_bulk_update) | Start an async job to bulk edit contacts.|
|[**post_outbound_contactlist_contacts_search**](#post_outbound_contactlist_contacts_search) | Query contacts from a contact list.|
|[**post_outbound_contactlist_export**](#post_outbound_contactlist_export) | Initiate the export of a contact list.|
|[**post_outbound_contactlistfilters**](#post_outbound_contactlistfilters) | Create Contact List Filter|
|[**post_outbound_contactlistfilters_bulk_retrieve**](#post_outbound_contactlistfilters_bulk_retrieve) | Retrieve multiple contact list filters|
|[**post_outbound_contactlistfilters_preview**](#post_outbound_contactlistfilters_preview) | Get a preview of the output of a contact list filter|
|[**post_outbound_contactlists**](#post_outbound_contactlists) | Create a contact List.|
|[**post_outbound_contactlisttemplates**](#post_outbound_contactlisttemplates) | Create Contact List Template|
|[**post_outbound_contactlisttemplates_bulk_add**](#post_outbound_contactlisttemplates_bulk_add) | Add multiple contact list templates|
|[**post_outbound_contactlisttemplates_bulk_retrieve**](#post_outbound_contactlisttemplates_bulk_retrieve) | Get multiple contact list templates|
|[**post_outbound_conversation_dnc**](#post_outbound_conversation_dnc) | Add phone numbers to a Dialer DNC list.|
|[**post_outbound_digitalrulesets**](#post_outbound_digitalrulesets) | Create an Outbound Digital Rule Set|
|[**post_outbound_dnclist_emailaddresses**](#post_outbound_dnclist_emailaddresses) | Add email addresses to a DNC list.|
|[**post_outbound_dnclist_export**](#post_outbound_dnclist_export) | Initiate the export of a dnc list.|
|[**post_outbound_dnclist_phonenumbers**](#post_outbound_dnclist_phonenumbers) | Add phone numbers to a DNC list.|
|[**post_outbound_dnclists**](#post_outbound_dnclists) | Create dialer DNC list|
|[**post_outbound_filespecificationtemplates**](#post_outbound_filespecificationtemplates) | Create File Specification Template|
|[**post_outbound_importtemplates**](#post_outbound_importtemplates) | Create Import Template|
|[**post_outbound_importtemplates_bulk_add**](#post_outbound_importtemplates_bulk_add) | Add multiple import templates|
|[**post_outbound_messagingcampaign_start**](#post_outbound_messagingcampaign_start) | Start the campaign|
|[**post_outbound_messagingcampaign_stop**](#post_outbound_messagingcampaign_stop) | Stop the campaign|
|[**post_outbound_messagingcampaigns**](#post_outbound_messagingcampaigns) | Create a Messaging Campaign|
|[**post_outbound_messagingcampaigns_progress**](#post_outbound_messagingcampaigns_progress) | Get progress for a list of messaging campaigns|
|[**post_outbound_rulesets**](#post_outbound_rulesets) | Create a Rule Set.|
|[**post_outbound_sequences**](#post_outbound_sequences) | Create a new campaign sequence.|
|[**put_outbound_attemptlimit**](#put_outbound_attemptlimit) | Update attempt limits|
|[**put_outbound_callabletimeset**](#put_outbound_callabletimeset) | Update callable time set|
|[**put_outbound_callanalysisresponseset**](#put_outbound_callanalysisresponseset) | Update a dialer call analysis response set.|
|[**put_outbound_campaign**](#put_outbound_campaign) | Update a campaign.|
|[**put_outbound_campaign_agent**](#put_outbound_campaign_agent) | Send notification that an agent&#39;s state changed |
|[**put_outbound_campaignrule**](#put_outbound_campaignrule) | Update Campaign Rule|
|[**put_outbound_contactlist**](#put_outbound_contactlist) | Update a contact list.|
|[**put_outbound_contactlist_contact**](#put_outbound_contactlist_contact) | Update a contact.|
|[**put_outbound_contactlistfilter**](#put_outbound_contactlistfilter) | Update Contact List Filter|
|[**put_outbound_contactlisttemplate**](#put_outbound_contactlisttemplate) | Update a contact list template.|
|[**put_outbound_digitalruleset**](#put_outbound_digitalruleset) | Update an Outbound Digital Rule Set|
|[**put_outbound_dnclist**](#put_outbound_dnclist) | Update dialer DNC list|
|[**put_outbound_filespecificationtemplate**](#put_outbound_filespecificationtemplate) | Update File Specification Template|
|[**put_outbound_importtemplate**](#put_outbound_importtemplate) | Update Import Template|
|[**put_outbound_messagingcampaign**](#put_outbound_messagingcampaign) | Update an Outbound Messaging Campaign|
|[**put_outbound_ruleset**](#put_outbound_ruleset) | Update a Rule Set.|
|[**put_outbound_schedules_campaign**](#put_outbound_schedules_campaign) | Update a new campaign schedule.|
|[**put_outbound_schedules_emailcampaign**](#put_outbound_schedules_emailcampaign) | Update an email campaign schedule.|
|[**put_outbound_schedules_messagingcampaign**](#put_outbound_schedules_messagingcampaign) | Update a new messaging campaign schedule.|
|[**put_outbound_schedules_sequence**](#put_outbound_schedules_sequence) | Update a new sequence schedule.|
|[**put_outbound_schedules_whatsappcampaign**](#put_outbound_schedules_whatsappcampaign) | Update a WhatsApp campaign schedule.|
|[**put_outbound_sequence**](#put_outbound_sequence) | Update a new campaign sequence.|
|[**put_outbound_wrapupcodemappings**](#put_outbound_wrapupcodemappings) | Update the Dialer wrap up code mapping.|



## delete_outbound_attemptlimit

>  delete_outbound_attemptlimit(attempt_limits_id)


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

### Return type

void (empty response body)


## delete_outbound_callabletimeset

>  delete_outbound_callabletimeset(callable_time_set_id)


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

### Return type

void (empty response body)


## delete_outbound_callanalysisresponseset

>  delete_outbound_callanalysisresponseset(call_analysis_set_id)


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

### Return type

void (empty response body)


## delete_outbound_campaign

> [**Campaign**](Campaign) delete_outbound_campaign(campaign_id)


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

### Return type

[**Campaign**](Campaign)


## delete_outbound_campaign_progress

>  delete_outbound_campaign_progress(campaign_id)


Reset campaign progress and recycle the campaign

Wraps DELETE /api/v2/outbound/campaigns/{campaignId}/progress 

Requires ANY permissions: 

* outbound:campaign:edit
* outbound:campaign:recycle

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

### Return type

void (empty response body)


## delete_outbound_campaignrule

>  delete_outbound_campaignrule(campaign_rule_id)


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

### Return type

void (empty response body)


## delete_outbound_contactlist

>  delete_outbound_contactlist(contact_list_id)


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

### Return type

void (empty response body)


## delete_outbound_contactlist_contact

>  delete_outbound_contactlist_contact(contact_list_id, contact_id)


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

### Return type

void (empty response body)


## delete_outbound_contactlist_contacts

>  delete_outbound_contactlist_contacts(contact_list_id, contact_ids)


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
| **contact_ids** | [**list[str]**](str)| ContactIds to delete. |  |

### Return type

void (empty response body)


## delete_outbound_contactlistfilter

>  delete_outbound_contactlistfilter(contact_list_filter_id)


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

### Return type

void (empty response body)


## delete_outbound_contactlists

>  delete_outbound_contactlists(id)


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
| **id** | [**list[str]**](str)| contact list id(s) to delete |  |

### Return type

void (empty response body)


## delete_outbound_contactlisttemplate

>  delete_outbound_contactlisttemplate(contact_list_template_id)


Delete Contact List Template

Wraps DELETE /api/v2/outbound/contactlisttemplates/{contactListTemplateId} 

Requires ANY permissions: 

* outbound:contactListTemplate:delete

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
contact_list_template_id = 'contact_list_template_id_example' # str | ContactListTemplate ID

try:
    # Delete Contact List Template
    api_instance.delete_outbound_contactlisttemplate(contact_list_template_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlisttemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_template_id** | **str**| ContactListTemplate ID |  |

### Return type

void (empty response body)


## delete_outbound_contactlisttemplates

>  delete_outbound_contactlisttemplates(id)


Delete multiple contact list templates.

Wraps DELETE /api/v2/outbound/contactlisttemplates 

Requires ANY permissions: 

* outbound:contactListTemplate:delete

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
id = ['id_example'] # list[str] | contact list template id(s) to delete

try:
    # Delete multiple contact list templates.
    api_instance.delete_outbound_contactlisttemplates(id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_contactlisttemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| contact list template id(s) to delete |  |

### Return type

void (empty response body)


## delete_outbound_digitalruleset

>  delete_outbound_digitalruleset(digital_rule_set_id)


Delete an Outbound Digital Rule Set

Wraps DELETE /api/v2/outbound/digitalrulesets/{digitalRuleSetId} 

Requires ANY permissions: 

* outbound:digitalRuleSet:delete

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
digital_rule_set_id = 'digital_rule_set_id_example' # str | The Digital Rule Set ID

try:
    # Delete an Outbound Digital Rule Set
    api_instance.delete_outbound_digitalruleset(digital_rule_set_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_digitalruleset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **digital_rule_set_id** | **str**| The Digital Rule Set ID |  |

### Return type

void (empty response body)


## delete_outbound_dnclist

>  delete_outbound_dnclist(dnc_list_id)


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

### Return type

void (empty response body)


## delete_outbound_dnclist_customexclusioncolumns

>  delete_outbound_dnclist_customexclusioncolumns(dnc_list_id, expired_only=expired_only)


Deletes all or expired custom exclusion column entries from a DNC list.

This operation is only for Internal DNC lists of custom exclusion column entries

Wraps DELETE /api/v2/outbound/dnclists/{dncListId}/customexclusioncolumns 

Requires ANY permissions: 

* outbound:dnc:delete

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
expired_only = False # bool | Set to true to only remove DNC entries that are expired (optional) (default to False)

try:
    # Deletes all or expired custom exclusion column entries from a DNC list.
    api_instance.delete_outbound_dnclist_customexclusioncolumns(dnc_list_id, expired_only=expired_only)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_dnclist_customexclusioncolumns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **expired_only** | **bool**| Set to true to only remove DNC entries that are expired | [optional] [default to False] |

### Return type

void (empty response body)


## delete_outbound_dnclist_emailaddresses

>  delete_outbound_dnclist_emailaddresses(dnc_list_id, expired_only=expired_only)


Deletes all or expired email addresses from a DNC list.

This operation is Only for Internal DNC lists of email addresses

Wraps DELETE /api/v2/outbound/dnclists/{dncListId}/emailaddresses 

Requires ANY permissions: 

* outbound:dnc:delete

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
expired_only = False # bool | Set to true to only remove DNC entries that are expired (optional) (default to False)

try:
    # Deletes all or expired email addresses from a DNC list.
    api_instance.delete_outbound_dnclist_emailaddresses(dnc_list_id, expired_only=expired_only)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_dnclist_emailaddresses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **expired_only** | **bool**| Set to true to only remove DNC entries that are expired | [optional] [default to False] |

### Return type

void (empty response body)


## delete_outbound_dnclist_phonenumbers

>  delete_outbound_dnclist_phonenumbers(dnc_list_id, expired_only=expired_only)


Deletes all or expired phone numbers from a DNC list.

This operation is Only for Internal DNC lists of phone numbers

Wraps DELETE /api/v2/outbound/dnclists/{dncListId}/phonenumbers 

Requires ANY permissions: 

* outbound:dnc:delete

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
expired_only = False # bool | Set to true to only remove DNC entries that are expired (optional) (default to False)

try:
    # Deletes all or expired phone numbers from a DNC list.
    api_instance.delete_outbound_dnclist_phonenumbers(dnc_list_id, expired_only=expired_only)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_dnclist_phonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **expired_only** | **bool**| Set to true to only remove DNC entries that are expired | [optional] [default to False] |

### Return type

void (empty response body)


## delete_outbound_dnclist_whatsappnumbers

>  delete_outbound_dnclist_whatsappnumbers(dnc_list_id, expired_only=expired_only)


Deletes all or expired whatsApp numbers from a DNC list.

This operation is only for Internal DNC lists of whatsApp numbers

Wraps DELETE /api/v2/outbound/dnclists/{dncListId}/whatsappnumbers 

Requires ANY permissions: 

* outbound:dnc:delete

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
expired_only = False # bool | Set to true to only remove DNC whatsApp numbers that are expired (optional) (default to False)

try:
    # Deletes all or expired whatsApp numbers from a DNC list.
    api_instance.delete_outbound_dnclist_whatsappnumbers(dnc_list_id, expired_only=expired_only)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_dnclist_whatsappnumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **expired_only** | **bool**| Set to true to only remove DNC whatsApp numbers that are expired | [optional] [default to False] |

### Return type

void (empty response body)


## delete_outbound_filespecificationtemplate

>  delete_outbound_filespecificationtemplate(file_specification_template_id)


Delete File Specification Template

Wraps DELETE /api/v2/outbound/filespecificationtemplates/{fileSpecificationTemplateId} 

Requires ANY permissions: 

* outbound:fileSpecificationTemplate:delete

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
file_specification_template_id = 'file_specification_template_id_example' # str | File Specification Template ID

try:
    # Delete File Specification Template
    api_instance.delete_outbound_filespecificationtemplate(file_specification_template_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_filespecificationtemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **file_specification_template_id** | **str**| File Specification Template ID |  |

### Return type

void (empty response body)


## delete_outbound_filespecificationtemplates_bulk

>  delete_outbound_filespecificationtemplates_bulk(id)


Delete multiple file specification templates.

Wraps DELETE /api/v2/outbound/filespecificationtemplates/bulk 

Requires ANY permissions: 

* outbound:fileSpecificationTemplate:delete

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
id = ['id_example'] # list[str] | File Specification template id(s) to delete

try:
    # Delete multiple file specification templates.
    api_instance.delete_outbound_filespecificationtemplates_bulk(id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_filespecificationtemplates_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| File Specification template id(s) to delete |  |

### Return type

void (empty response body)


## delete_outbound_importtemplate

>  delete_outbound_importtemplate(import_template_id)


Delete Import Template

Wraps DELETE /api/v2/outbound/importtemplates/{importTemplateId} 

Requires ANY permissions: 

* outbound:importTemplate:delete

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
import_template_id = 'import_template_id_example' # str | Import Template ID

try:
    # Delete Import Template
    api_instance.delete_outbound_importtemplate(import_template_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_importtemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **import_template_id** | **str**| Import Template ID |  |

### Return type

void (empty response body)


## delete_outbound_importtemplates

>  delete_outbound_importtemplates(id)


Delete multiple import templates.

Wraps DELETE /api/v2/outbound/importtemplates 

Requires ANY permissions: 

* outbound:importTemplate:delete

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
id = ['id_example'] # list[str] | import template id(s) to delete

try:
    # Delete multiple import templates.
    api_instance.delete_outbound_importtemplates(id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_importtemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| import template id(s) to delete |  |

### Return type

void (empty response body)


## delete_outbound_messagingcampaign

> [**MessagingCampaign**](MessagingCampaign) delete_outbound_messagingcampaign(messaging_campaign_id)


Delete an Outbound Messaging Campaign

Wraps DELETE /api/v2/outbound/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:delete
* outbound:emailCampaign:delete
* outbound:whatsAppCampaign:delete

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

### Return type

[**MessagingCampaign**](MessagingCampaign)


## delete_outbound_messagingcampaign_progress

>  delete_outbound_messagingcampaign_progress(messaging_campaign_id)


Reset messaging campaign progress and recycle the messaging campaign

Documented permissions are applicable based on campaign type.

Wraps DELETE /api/v2/outbound/messagingcampaigns/{messagingCampaignId}/progress 

Requires ANY permissions: 

* outbound:messagingCampaign:edit
* outbound:messagingCampaign:recycle
* outbound:emailCampaign:edit
* outbound:emailCampaign:recycle
* outbound:whatsAppCampaign:edit
* outbound:whatsAppCampaign:recycle

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
    # Reset messaging campaign progress and recycle the messaging campaign
    api_instance.delete_outbound_messagingcampaign_progress(messaging_campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_messagingcampaign_progress: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |

### Return type

void (empty response body)


## delete_outbound_ruleset

>  delete_outbound_ruleset(rule_set_id)


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

### Return type

void (empty response body)


## delete_outbound_schedules_campaign

>  delete_outbound_schedules_campaign(campaign_id)


Delete a dialer campaign schedule.

Wraps DELETE /api/v2/outbound/schedules/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:schedule:delete
* outbound:campaign:deleteSchedule

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

### Return type

void (empty response body)


## delete_outbound_schedules_emailcampaign

>  delete_outbound_schedules_emailcampaign(email_campaign_id)


Delete an email campaign schedule.

Wraps DELETE /api/v2/outbound/schedules/emailcampaigns/{emailCampaignId} 

Requires ANY permissions: 

* outbound:emailCampaignSchedule:delete
* outbound:emailCampaign:deleteSchedule

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
email_campaign_id = 'email_campaign_id_example' # str | Email Campaign ID

try:
    # Delete an email campaign schedule.
    api_instance.delete_outbound_schedules_emailcampaign(email_campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_schedules_emailcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **email_campaign_id** | **str**| Email Campaign ID |  |

### Return type

void (empty response body)


## delete_outbound_schedules_messagingcampaign

>  delete_outbound_schedules_messagingcampaign(messaging_campaign_id)


Delete a messaging campaign schedule.

Wraps DELETE /api/v2/outbound/schedules/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaignSchedule:delete
* outbound:messagingCampaign:deleteSchedule

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
messaging_campaign_id = 'messaging_campaign_id_example' # str | Messaging Campaign ID

try:
    # Delete a messaging campaign schedule.
    api_instance.delete_outbound_schedules_messagingcampaign(messaging_campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_schedules_messagingcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| Messaging Campaign ID |  |

### Return type

void (empty response body)


## delete_outbound_schedules_sequence

>  delete_outbound_schedules_sequence(sequence_id)


Delete a dialer sequence schedule.

Wraps DELETE /api/v2/outbound/schedules/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:schedule:delete
* outbound:campaignSequenceSchedule:delete

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

### Return type

void (empty response body)


## delete_outbound_schedules_whatsappcampaign

>  delete_outbound_schedules_whatsappcampaign(whats_app_campaign_id)


Delete a WhatsApp campaign schedule.

Wraps DELETE /api/v2/outbound/schedules/whatsappcampaigns/{whatsAppCampaignId} 

Requires ANY permissions: 

* outbound:whatsAppCampaignSchedule:delete
* outbound:whatsAppCampaign:deleteSchedule

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
whats_app_campaign_id = 'whats_app_campaign_id_example' # str | WhatsApp Campaign ID

try:
    # Delete a WhatsApp campaign schedule.
    api_instance.delete_outbound_schedules_whatsappcampaign(whats_app_campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->delete_outbound_schedules_whatsappcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **whats_app_campaign_id** | **str**| WhatsApp Campaign ID |  |

### Return type

void (empty response body)


## delete_outbound_sequence

>  delete_outbound_sequence(sequence_id)


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

### Return type

void (empty response body)


## get_outbound_attemptlimit

> [**AttemptLimits**](AttemptLimits) get_outbound_attemptlimit(attempt_limits_id)


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

### Return type

[**AttemptLimits**](AttemptLimits)


## get_outbound_attemptlimits

> [**AttemptLimitsEntityListing**](AttemptLimitsEntityListing) get_outbound_attemptlimits(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**AttemptLimitsEntityListing**](AttemptLimitsEntityListing)


## get_outbound_callabletimeset

> [**CallableTimeSet**](CallableTimeSet) get_outbound_callabletimeset(callable_time_set_id)


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

### Return type

[**CallableTimeSet**](CallableTimeSet)


## get_outbound_callabletimesets

> [**CallableTimeSetEntityListing**](CallableTimeSetEntityListing) get_outbound_callabletimesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CallableTimeSetEntityListing**](CallableTimeSetEntityListing)


## get_outbound_callanalysisresponseset

> [**ResponseSet**](ResponseSet) get_outbound_callanalysisresponseset(call_analysis_set_id)


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

### Return type

[**ResponseSet**](ResponseSet)


## get_outbound_callanalysisresponsesets

> [**ResponseSetEntityListing**](ResponseSetEntityListing) get_outbound_callanalysisresponsesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**ResponseSetEntityListing**](ResponseSetEntityListing)


## get_outbound_campaign

> [**Campaign**](Campaign) get_outbound_campaign(campaign_id)


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

### Return type

[**Campaign**](Campaign)


## get_outbound_campaign_agentownedmappingpreview_results

> [**AgentOwnedMappingPreviewListing**](AgentOwnedMappingPreviewListing) get_outbound_campaign_agentownedmappingpreview_results(campaign_id)


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

### Return type

[**AgentOwnedMappingPreviewListing**](AgentOwnedMappingPreviewListing)


## get_outbound_campaign_diagnostics

> [**CampaignDiagnostics**](CampaignDiagnostics) get_outbound_campaign_diagnostics(campaign_id)


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

### Return type

[**CampaignDiagnostics**](CampaignDiagnostics)


## get_outbound_campaign_interactions

> [**CampaignInteractions**](CampaignInteractions) get_outbound_campaign_interactions(campaign_id)


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

### Return type

[**CampaignInteractions**](CampaignInteractions)


## get_outbound_campaign_linedistribution

> [**CampaignOutboundLinesDistribution**](CampaignOutboundLinesDistribution) get_outbound_campaign_linedistribution(campaign_id, include_only_active_campaigns=include_only_active_campaigns, edge_group_id=edge_group_id, site_id=site_id, use_weight=use_weight, relative_weight=relative_weight, outbound_line_count=outbound_line_count)


Get line distribution information for campaigns using same Edge Group or Site as given campaign

Wraps GET /api/v2/outbound/campaigns/{campaignId}/linedistribution 

Requires ANY permissions: 

* outbound:lineDistribution:view

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
include_only_active_campaigns = True # bool | If true will return only active Campaigns (optional) (default to True)
edge_group_id = 'edge_group_id_example' # str | Edge group to be used in line distribution calculations instead of current Campaign's Edge Group. Campaign's Site and Edge Group are mutually exclusive. (optional)
site_id = 'site_id_example' # str | Site to be used in line distribution calculations instead of current Campaign's Site.  Campaign's Site and Edge Group are mutually exclusive. (optional)
use_weight = True # bool | Enable usage of weight, this value overrides current Campaign's setting in line distribution calculations (optional)
relative_weight = 56 # int | Relative weight to be used in line distribution calculations instead of current Campaign's relative weight (optional)
outbound_line_count = 56 # int | The number of outbound lines to be used in line distribution calculations, instead of current Campaign's Outbound Lines Count (optional)

try:
    # Get line distribution information for campaigns using same Edge Group or Site as given campaign
    api_response = api_instance.get_outbound_campaign_linedistribution(campaign_id, include_only_active_campaigns=include_only_active_campaigns, edge_group_id=edge_group_id, site_id=site_id, use_weight=use_weight, relative_weight=relative_weight, outbound_line_count=outbound_line_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_linedistribution: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **include_only_active_campaigns** | **bool**| If true will return only active Campaigns | [optional] [default to True] |
| **edge_group_id** | **str**| Edge group to be used in line distribution calculations instead of current Campaign&#39;s Edge Group. Campaign&#39;s Site and Edge Group are mutually exclusive. | [optional]  |
| **site_id** | **str**| Site to be used in line distribution calculations instead of current Campaign&#39;s Site.  Campaign&#39;s Site and Edge Group are mutually exclusive. | [optional]  |
| **use_weight** | **bool**| Enable usage of weight, this value overrides current Campaign&#39;s setting in line distribution calculations | [optional]  |
| **relative_weight** | **int**| Relative weight to be used in line distribution calculations instead of current Campaign&#39;s relative weight | [optional]  |
| **outbound_line_count** | **int**| The number of outbound lines to be used in line distribution calculations, instead of current Campaign&#39;s Outbound Lines Count | [optional]  |

### Return type

[**CampaignOutboundLinesDistribution**](CampaignOutboundLinesDistribution)


## get_outbound_campaign_progress

> [**CampaignProgress**](CampaignProgress) get_outbound_campaign_progress(campaign_id)


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

### Return type

[**CampaignProgress**](CampaignProgress)


## get_outbound_campaign_skillcombinations

> [**PagedSkillCombinationListing**](PagedSkillCombinationListing) get_outbound_campaign_skillcombinations(campaign_id, page_number=page_number, page_size=page_size)


Get the remaining and total contact count for each skill combination in a skills campaign

Wraps GET /api/v2/outbound/campaigns/{campaignId}/skillcombinations 

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
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get the remaining and total contact count for each skill combination in a skills campaign
    api_response = api_instance.get_outbound_campaign_skillcombinations(campaign_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_campaign_skillcombinations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**PagedSkillCombinationListing**](PagedSkillCombinationListing)


## get_outbound_campaign_stats

> [**CampaignStats**](CampaignStats) get_outbound_campaign_stats(campaign_id)


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

### Return type

[**CampaignStats**](CampaignStats)


## get_outbound_campaignrule

> [**CampaignRule**](CampaignRule) get_outbound_campaignrule(campaign_rule_id)


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

### Return type

[**CampaignRule**](CampaignRule)


## get_outbound_campaignrules

> [**CampaignRuleEntityListing**](CampaignRuleEntityListing) get_outbound_campaignrules(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CampaignRuleEntityListing**](CampaignRuleEntityListing)


## get_outbound_campaigns

> [**CampaignEntityListing**](CampaignEntityListing) get_outbound_campaigns(page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, contact_list_id=contact_list_id, dnc_list_ids=dnc_list_ids, distribution_queue_id=distribution_queue_id, edge_group_id=edge_group_id, call_analysis_response_set_id=call_analysis_response_set_id, division_id=division_id, sort_by=sort_by, sort_order=sort_order)


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
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
contact_list_id = 'contact_list_id_example' # str | Contact List ID (optional)
dnc_list_ids = 'dnc_list_ids_example' # str | DNC list ID (optional)
distribution_queue_id = 'distribution_queue_id_example' # str | Distribution queue ID (optional)
edge_group_id = 'edge_group_id_example' # str | Edge group ID (optional)
call_analysis_response_set_id = 'call_analysis_response_set_id_example' # str | Call analysis response set ID (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str)| id | [optional]  |
| **contact_list_id** | **str**| Contact List ID | [optional]  |
| **dnc_list_ids** | **str**| DNC list ID | [optional]  |
| **distribution_queue_id** | **str**| Distribution queue ID | [optional]  |
| **edge_group_id** | **str**| Edge group ID | [optional]  |
| **call_analysis_response_set_id** | **str**| Call analysis response set ID | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CampaignEntityListing**](CampaignEntityListing)


## get_outbound_campaigns_all

> [**CommonCampaignEntityListing**](CommonCampaignEntityListing) get_outbound_campaigns_all(page_size=page_size, page_number=page_number, id=id, name=name, division_id=division_id, media_type=media_type, sort_order=sort_order)


Query across all types of campaigns by division

Wraps GET /api/v2/outbound/campaigns/all 

Requires ANY permissions: 

* outbound:campaign:view
* outbound:messagingCampaign:view
* outbound:emailCampaign:view
* outbound:whatsAppCampaign:view

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
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **id** | [**list[str]**](str)| Campaign ID(s) | [optional]  |
| **name** | **str**| Campaign name(s) | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **media_type** | [**list[str]**](str)| Media type(s) | [optional] <br />**Values**: email, sms, voice, whatsapp |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CommonCampaignEntityListing**](CommonCampaignEntityListing)


## get_outbound_campaigns_all_divisionviews

> [**CommonCampaignDivisionViewEntityListing**](CommonCampaignDivisionViewEntityListing) get_outbound_campaigns_all_divisionviews(page_size=page_size, page_number=page_number, id=id, name=name, division_id=division_id, media_type=media_type, sort_order=sort_order)


Query across all types of campaigns

Wraps GET /api/v2/outbound/campaigns/all/divisionviews 

Requires ANY permissions: 

* outbound:campaign:search
* outbound:messagingCampaign:search
* outbound:emailCampaign:search
* outbound:whatsAppCampaign:search

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
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **id** | [**list[str]**](str)| Campaign ID(s) | [optional]  |
| **name** | **str**| Campaign name(s) | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **media_type** | [**list[str]**](str)| Media type(s) | [optional] <br />**Values**: email, sms, voice, whatsapp |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CommonCampaignDivisionViewEntityListing**](CommonCampaignDivisionViewEntityListing)


## get_outbound_campaigns_divisionview

> [**CampaignDivisionView**](CampaignDivisionView) get_outbound_campaigns_divisionview(campaign_id)


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

### Return type

[**CampaignDivisionView**](CampaignDivisionView)


## get_outbound_campaigns_divisionviews

> [**CampaignDivisionViewListing**](CampaignDivisionViewListing) get_outbound_campaigns_divisionviews(page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, sort_by=sort_by, sort_order=sort_order)


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
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str)| id | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CampaignDivisionViewListing**](CampaignDivisionViewListing)


## get_outbound_contactlist

> [**ContactList**](ContactList) get_outbound_contactlist(contact_list_id, include_import_status=include_import_status, include_size=include_size)


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
include_import_status = False # bool | Import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)

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
| **include_import_status** | **bool**| Import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |

### Return type

[**ContactList**](ContactList)


## get_outbound_contactlist_contact

> [**DialerContact**](DialerContact) get_outbound_contactlist_contact(contact_list_id, contact_id)


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

### Return type

[**DialerContact**](DialerContact)


## get_outbound_contactlist_contacts_bulk_job

> [**ContactsBulkOperationJob**](ContactsBulkOperationJob) get_outbound_contactlist_contacts_bulk_job(contact_list_id, job_id)


Get bulk operation job.

Wraps GET /api/v2/outbound/contactlists/{contactListId}/contacts/bulk/jobs/{jobId} 

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
contact_list_id = 'contact_list_id_example' # str | Contact List ID
job_id = 'job_id_example' # str | Job ID

try:
    # Get bulk operation job.
    api_response = api_instance.get_outbound_contactlist_contacts_bulk_job(contact_list_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist_contacts_bulk_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **job_id** | **str**| Job ID |  |

### Return type

[**ContactsBulkOperationJob**](ContactsBulkOperationJob)


## get_outbound_contactlist_contacts_bulk_jobs

> [**ContactsBulkOperationJobListing**](ContactsBulkOperationJobListing) get_outbound_contactlist_contacts_bulk_jobs(contact_list_id)


Get 10 most recent bulk operation jobs associated with contact list.

Wraps GET /api/v2/outbound/contactlists/{contactListId}/contacts/bulk/jobs 

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
contact_list_id = 'contact_list_id_example' # str | Contact List ID

try:
    # Get 10 most recent bulk operation jobs associated with contact list.
    api_response = api_instance.get_outbound_contactlist_contacts_bulk_jobs(contact_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlist_contacts_bulk_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |

### Return type

[**ContactsBulkOperationJobListing**](ContactsBulkOperationJobListing)


## get_outbound_contactlist_export

> [**ExportUri**](ExportUri) get_outbound_contactlist_export(contact_list_id, download=download)


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
download = ''false'' # str | Redirect to download uri (optional) (default to 'false')

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
| **download** | **str**| Redirect to download uri | [optional] [default to &#39;false&#39;] |

### Return type

[**ExportUri**](ExportUri)


## get_outbound_contactlist_importstatus

> [**ImportStatus**](ImportStatus) get_outbound_contactlist_importstatus(contact_list_id)


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

### Return type

[**ImportStatus**](ImportStatus)


## get_outbound_contactlist_timezonemappingpreview

> [**TimeZoneMappingPreview**](TimeZoneMappingPreview) get_outbound_contactlist_timezonemappingpreview(contact_list_id)


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

### Return type

[**TimeZoneMappingPreview**](TimeZoneMappingPreview)


## get_outbound_contactlistfilter

> [**ContactListFilter**](ContactListFilter) get_outbound_contactlistfilter(contact_list_filter_id)


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

### Return type

[**ContactListFilter**](ContactListFilter)


## get_outbound_contactlistfilters

> [**ContactListFilterEntityListing**](ContactListFilterEntityListing) get_outbound_contactlistfilters(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order, contact_list_id=contact_list_id)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')
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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |
| **contact_list_id** | **str**| Contact List ID | [optional]  |

### Return type

[**ContactListFilterEntityListing**](ContactListFilterEntityListing)


## get_outbound_contactlists

> [**ContactListEntityListing**](ContactListEntityListing) get_outbound_contactlists(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, id=id, division_id=division_id, sort_by=sort_by, sort_order=sort_order)


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
include_import_status = False # bool | Include import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **include_import_status** | **bool**| Include import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str)| id | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**ContactListEntityListing**](ContactListEntityListing)


## get_outbound_contactlists_divisionview

> [**ContactListDivisionView**](ContactListDivisionView) get_outbound_contactlists_divisionview(contact_list_id, include_import_status=include_import_status, include_size=include_size)


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
include_import_status = False # bool | Include import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)

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
| **include_import_status** | **bool**| Include import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |

### Return type

[**ContactListDivisionView**](ContactListDivisionView)


## get_outbound_contactlists_divisionviews

> [**ContactListDivisionViewListing**](ContactListDivisionViewListing) get_outbound_contactlists_divisionviews(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, id=id, sort_by=sort_by, sort_order=sort_order)


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
include_import_status = False # bool | Include import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | id (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **include_import_status** | **bool**| Include import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str)| id | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**ContactListDivisionViewListing**](ContactListDivisionViewListing)


## get_outbound_contactlisttemplate

> [**ContactListTemplate**](ContactListTemplate) get_outbound_contactlisttemplate(contact_list_template_id)


Get Contact List Template

Wraps GET /api/v2/outbound/contactlisttemplates/{contactListTemplateId} 

Requires ANY permissions: 

* outbound:contactListTemplate:view

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
contact_list_template_id = 'contact_list_template_id_example' # str | ContactListTemplate ID

try:
    # Get Contact List Template
    api_response = api_instance.get_outbound_contactlisttemplate(contact_list_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlisttemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_template_id** | **str**| ContactListTemplate ID |  |

### Return type

[**ContactListTemplate**](ContactListTemplate)


## get_outbound_contactlisttemplates

> [**ContactListTemplateEntityListing**](ContactListTemplateEntityListing) get_outbound_contactlisttemplates(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


Query a list of contact list templates

Wraps GET /api/v2/outbound/contactlisttemplates 

Requires ANY permissions: 

* outbound:contactListTemplate:view

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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

try:
    # Query a list of contact list templates
    api_response = api_instance.get_outbound_contactlisttemplates(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_contactlisttemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**ContactListTemplateEntityListing**](ContactListTemplateEntityListing)


## get_outbound_digitalruleset

> [**DigitalRuleSet**](DigitalRuleSet) get_outbound_digitalruleset(digital_rule_set_id)


Get an Outbound Digital Rule Set

Wraps GET /api/v2/outbound/digitalrulesets/{digitalRuleSetId} 

Requires ANY permissions: 

* outbound:digitalRuleSet:view

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
digital_rule_set_id = 'digital_rule_set_id_example' # str | The Digital Rule Set ID

try:
    # Get an Outbound Digital Rule Set
    api_response = api_instance.get_outbound_digitalruleset(digital_rule_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_digitalruleset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **digital_rule_set_id** | **str**| The Digital Rule Set ID |  |

### Return type

[**DigitalRuleSet**](DigitalRuleSet)


## get_outbound_digitalrulesets

> [**DigitalRuleSetEntityListing**](DigitalRuleSetEntityListing) get_outbound_digitalrulesets(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id)


Query a list of Outbound Digital Rule Sets

Wraps GET /api/v2/outbound/digitalrulesets 

Requires ANY permissions: 

* outbound:digitalRuleSet:view

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
sort_by = ''name'' # str | The field to sort by (optional) (default to 'name')
sort_order = ''ascending'' # str | The direction to sort (optional) (default to 'ascending')
name = 'name_example' # str | Name (optional)
id = ['id_example'] # list[str] | A list of digital rule set ids to bulk fetch (optional)

try:
    # Query a list of Outbound Digital Rule Sets
    api_response = api_instance.get_outbound_digitalrulesets(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_digitalrulesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| The field to sort by | [optional] [default to &#39;name&#39;]<br />**Values**: name |
| **sort_order** | **str**| The direction to sort | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
| **id** | [**list[str]**](str)| A list of digital rule set ids to bulk fetch | [optional]  |

### Return type

[**DigitalRuleSetEntityListing**](DigitalRuleSetEntityListing)


## get_outbound_dnclist

> [**DncList**](DncList) get_outbound_dnclist(dnc_list_id, include_import_status=include_import_status, include_size=include_size)


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
include_import_status = False # bool | Import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)

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
| **include_import_status** | **bool**| Import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |

### Return type

[**DncList**](DncList)


## get_outbound_dnclist_export

> [**ExportUri**](ExportUri) get_outbound_dnclist_export(dnc_list_id, download=download)


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
download = ''false'' # str | Redirect to download uri (optional) (default to 'false')

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
| **download** | **str**| Redirect to download uri | [optional] [default to &#39;false&#39;] |

### Return type

[**ExportUri**](ExportUri)


## get_outbound_dnclist_importstatus

> [**ImportStatus**](ImportStatus) get_outbound_dnclist_importstatus(dnc_list_id)


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

### Return type

[**ImportStatus**](ImportStatus)


## get_outbound_dnclists

> [**DncListEntityListing**](DncListEntityListing) get_outbound_dnclists(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, dnc_source_type=dnc_source_type, division_id=division_id, sort_by=sort_by, sort_order=sort_order)


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
include_import_status = False # bool | Import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
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
| **include_import_status** | **bool**| Import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **dnc_source_type** | **str**| DncSourceType | [optional] <br />**Values**: rds, rds_custom, dnc.com, gryphon |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] <br />**Values**: ascending, descending |

### Return type

[**DncListEntityListing**](DncListEntityListing)


## get_outbound_dnclists_divisionview

> [**DncListDivisionView**](DncListDivisionView) get_outbound_dnclists_divisionview(dnc_list_id, include_import_status=include_import_status, include_size=include_size)


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
include_import_status = False # bool | Include import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)

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
| **include_import_status** | **bool**| Include import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |

### Return type

[**DncListDivisionView**](DncListDivisionView)


## get_outbound_dnclists_divisionviews

> [**DncListDivisionViewListing**](DncListDivisionViewListing) get_outbound_dnclists_divisionviews(include_import_status=include_import_status, include_size=include_size, page_size=page_size, page_number=page_number, filter_type=filter_type, name=name, dnc_source_type=dnc_source_type, id=id, sort_by=sort_by, sort_order=sort_order)


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
include_import_status = False # bool | Include import status (optional) (default to False)
include_size = False # bool | Include size (optional) (default to False)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
dnc_source_type = 'dnc_source_type_example' # str | DncSourceType (optional)
id = ['id_example'] # list[str] | id (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **include_import_status** | **bool**| Include import status | [optional] [default to False] |
| **include_size** | **bool**| Include size | [optional] [default to False] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **dnc_source_type** | **str**| DncSourceType | [optional] <br />**Values**: rds, rds_custom, dnc.com, gryphon |
| **id** | [**list[str]**](str)| id | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**DncListDivisionViewListing**](DncListDivisionViewListing)


## get_outbound_event

> [**EventLog**](EventLog) get_outbound_event(event_id)


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

### Return type

[**EventLog**](EventLog)


## get_outbound_events

> [**DialerEventEntityListing**](DialerEventEntityListing) get_outbound_events(page_size=page_size, page_number=page_number, filter_type=filter_type, category=category, level=level, sort_by=sort_by, sort_order=sort_order)


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
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
category = 'category_example' # str | Category (optional)
level = 'level_example' # str | Level (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **category** | **str**| Category | [optional]  |
| **level** | **str**| Level | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**DialerEventEntityListing**](DialerEventEntityListing)


## get_outbound_filespecificationtemplate

> [**FileSpecificationTemplate**](FileSpecificationTemplate) get_outbound_filespecificationtemplate(file_specification_template_id)


Get File Specification Template

Wraps GET /api/v2/outbound/filespecificationtemplates/{fileSpecificationTemplateId} 

Requires ANY permissions: 

* outbound:fileSpecificationTemplate:view

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
file_specification_template_id = 'file_specification_template_id_example' # str | File Specification Template ID

try:
    # Get File Specification Template
    api_response = api_instance.get_outbound_filespecificationtemplate(file_specification_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_filespecificationtemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **file_specification_template_id** | **str**| File Specification Template ID |  |

### Return type

[**FileSpecificationTemplate**](FileSpecificationTemplate)


## get_outbound_filespecificationtemplates

> [**FileSpecificationTemplateEntityListing**](FileSpecificationTemplateEntityListing) get_outbound_filespecificationtemplates(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


Query File Specification Templates

Wraps GET /api/v2/outbound/filespecificationtemplates 

Requires ANY permissions: 

* outbound:fileSpecificationTemplate:view

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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

try:
    # Query File Specification Templates
    api_response = api_instance.get_outbound_filespecificationtemplates(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_filespecificationtemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**FileSpecificationTemplateEntityListing**](FileSpecificationTemplateEntityListing)


## get_outbound_importtemplate

> [**ImportTemplate**](ImportTemplate) get_outbound_importtemplate(import_template_id, include_import_status=include_import_status)


Get Import Template

Wraps GET /api/v2/outbound/importtemplates/{importTemplateId} 

Requires ANY permissions: 

* outbound:importTemplate:view

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
import_template_id = 'import_template_id_example' # str | Import Template ID
include_import_status = False # bool | Import status (optional) (default to False)

try:
    # Get Import Template
    api_response = api_instance.get_outbound_importtemplate(import_template_id, include_import_status=include_import_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_importtemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **import_template_id** | **str**| Import Template ID |  |
| **include_import_status** | **bool**| Import status | [optional] [default to False] |

### Return type

[**ImportTemplate**](ImportTemplate)


## get_outbound_importtemplate_importstatus

> [**ImportStatus**](ImportStatus) get_outbound_importtemplate_importstatus(import_template_id, list_name_prefix=list_name_prefix)


Get the import status for an import template.

Wraps GET /api/v2/outbound/importtemplates/{importTemplateId}/importstatus 

Requires ANY permissions: 

* outbound:importTemplate:view

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
import_template_id = 'import_template_id_example' # str | importTemplateId
list_name_prefix = 'list_name_prefix_example' # str | listNamePrefix (optional)

try:
    # Get the import status for an import template.
    api_response = api_instance.get_outbound_importtemplate_importstatus(import_template_id, list_name_prefix=list_name_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_importtemplate_importstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **import_template_id** | **str**| importTemplateId |  |
| **list_name_prefix** | **str**| listNamePrefix | [optional]  |

### Return type

[**ImportStatus**](ImportStatus)


## get_outbound_importtemplates

> [**ImportTemplateEntityListing**](ImportTemplateEntityListing) get_outbound_importtemplates(include_import_status=include_import_status, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order, contact_list_template_id=contact_list_template_id)


Query Import Templates

Wraps GET /api/v2/outbound/importtemplates 

Requires ANY permissions: 

* outbound:importTemplate:view

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
include_import_status = False # bool | Import status (optional) (default to False)
page_size = 25 # int | Page size. The max that will be returned is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')
contact_list_template_id = 'contact_list_template_id_example' # str | Contact List Template ID (optional)

try:
    # Query Import Templates
    api_response = api_instance.get_outbound_importtemplates(include_import_status=include_import_status, page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order, contact_list_template_id=contact_list_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_importtemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_import_status** | **bool**| Import status | [optional] [default to False] |
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |
| **contact_list_template_id** | **str**| Contact List Template ID | [optional]  |

### Return type

[**ImportTemplateEntityListing**](ImportTemplateEntityListing)


## get_outbound_messagingcampaign

> [**MessagingCampaign**](MessagingCampaign) get_outbound_messagingcampaign(messaging_campaign_id)


Get an Outbound Messaging Campaign

Wraps GET /api/v2/outbound/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view
* outbound:whatsAppCampaign:view

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

### Return type

[**MessagingCampaign**](MessagingCampaign)


## get_outbound_messagingcampaign_diagnostics

> [**MessagingCampaignDiagnostics**](MessagingCampaignDiagnostics) get_outbound_messagingcampaign_diagnostics(messaging_campaign_id)


Get messaging campaign diagnostics

Wraps GET /api/v2/outbound/messagingcampaigns/{messagingCampaignId}/diagnostics 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view
* outbound:whatsAppCampaign:view

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
    # Get messaging campaign diagnostics
    api_response = api_instance.get_outbound_messagingcampaign_diagnostics(messaging_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaign_diagnostics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |

### Return type

[**MessagingCampaignDiagnostics**](MessagingCampaignDiagnostics)


## get_outbound_messagingcampaign_progress

> [**CampaignProgress**](CampaignProgress) get_outbound_messagingcampaign_progress(messaging_campaign_id)


Get messaging campaign's progress

Wraps GET /api/v2/outbound/messagingcampaigns/{messagingCampaignId}/progress 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view
* outbound:whatsAppCampaign:view

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

### Return type

[**CampaignProgress**](CampaignProgress)


## get_outbound_messagingcampaigns

> [**MessagingCampaignEntityListing**](MessagingCampaignEntityListing) get_outbound_messagingcampaigns(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, contact_list_id=contact_list_id, division_id=division_id, type=type, sender_sms_phone_number=sender_sms_phone_number, id=id, content_template_id=content_template_id, campaign_status=campaign_status)


Query a list of Messaging Campaigns

Wraps GET /api/v2/outbound/messagingcampaigns 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view
* outbound:whatsAppCampaign:view

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
sort_by = ''name'' # str | The field to sort by (optional) (default to 'name')
sort_order = ''ascending'' # str | The direction to sort (optional) (default to 'ascending')
name = 'name_example' # str | Name (optional)
contact_list_id = 'contact_list_id_example' # str | Contact List ID (optional)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)
type = 'type_example' # str | Campaign Type (optional)
sender_sms_phone_number = 'sender_sms_phone_number_example' # str | Sender SMS Phone Number (optional)
id = ['id_example'] # list[str] | A list of messaging campaign ids to bulk fetch (optional)
content_template_id = 'content_template_id_example' # str | Content template ID (optional)
campaign_status = 'campaign_status_example' # str | Campaign Status (optional)

try:
    # Query a list of Messaging Campaigns
    api_response = api_instance.get_outbound_messagingcampaigns(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, contact_list_id=contact_list_id, division_id=division_id, type=type, sender_sms_phone_number=sender_sms_phone_number, id=id, content_template_id=content_template_id, campaign_status=campaign_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaigns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| The field to sort by | [optional] [default to &#39;name&#39;]<br />**Values**: campaignStatus, name, type |
| **sort_order** | **str**| The direction to sort | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
| **contact_list_id** | **str**| Contact List ID | [optional]  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |
| **type** | **str**| Campaign Type | [optional] <br />**Values**: EMAIL, SMS, WHATSAPP |
| **sender_sms_phone_number** | **str**| Sender SMS Phone Number | [optional]  |
| **id** | [**list[str]**](str)| A list of messaging campaign ids to bulk fetch | [optional]  |
| **content_template_id** | **str**| Content template ID | [optional]  |
| **campaign_status** | **str**| Campaign Status | [optional] <br />**Values**: on, stopping, off, complete, invalid, forced_off, forced_stopping |

### Return type

[**MessagingCampaignEntityListing**](MessagingCampaignEntityListing)


## get_outbound_messagingcampaigns_divisionview

> [**MessagingCampaignDivisionView**](MessagingCampaignDivisionView) get_outbound_messagingcampaigns_divisionview(messaging_campaign_id)


Get a basic Messaging Campaign information object

This returns a simplified version of a Messaging Campaign, consisting of id, name, and division.

Wraps GET /api/v2/outbound/messagingcampaigns/divisionviews/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:search
* outbound:emailCampaign:search
* outbound:whatsAppCampaign:search

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

### Return type

[**MessagingCampaignDivisionView**](MessagingCampaignDivisionView)


## get_outbound_messagingcampaigns_divisionviews

> [**MessagingCampaignDivisionViewEntityListing**](MessagingCampaignDivisionViewEntityListing) get_outbound_messagingcampaigns_divisionviews(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, type=type, id=id, sender_sms_phone_number=sender_sms_phone_number, content_template_id=content_template_id, campaign_status=campaign_status)


Query a list of basic Messaging Campaign information objects

This returns a listing of simplified Messaging Campaigns, each consisting of id, name, and division.

Wraps GET /api/v2/outbound/messagingcampaigns/divisionviews 

Requires ANY permissions: 

* outbound:messagingCampaign:search
* outbound:emailCampaign:search
* outbound:whatsAppCampaign:search

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
sort_order = ''a'' # str | The direction to sort (optional) (default to 'a')
name = 'name_example' # str | Name (optional)
type = 'type_example' # str | Campaign Type (optional)
id = ['id_example'] # list[str] | id (optional)
sender_sms_phone_number = 'sender_sms_phone_number_example' # str | Sender SMS Phone Number (optional)
content_template_id = 'content_template_id_example' # str | Content template ID (optional)
campaign_status = 'campaign_status_example' # str | Campaign Status (optional)

try:
    # Query a list of basic Messaging Campaign information objects
    api_response = api_instance.get_outbound_messagingcampaigns_divisionviews(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name, type=type, id=id, sender_sms_phone_number=sender_sms_phone_number, content_template_id=content_template_id, campaign_status=campaign_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_messagingcampaigns_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size. The max that will be returned is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| The direction to sort | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |
| **type** | **str**| Campaign Type | [optional] <br />**Values**: EMAIL, SMS, WHATSAPP |
| **id** | [**list[str]**](str)| id | [optional]  |
| **sender_sms_phone_number** | **str**| Sender SMS Phone Number | [optional]  |
| **content_template_id** | **str**| Content template ID | [optional]  |
| **campaign_status** | **str**| Campaign Status | [optional] <br />**Values**: on, stopping, off, complete, invalid, forced_off, forced_stopping |

### Return type

[**MessagingCampaignDivisionViewEntityListing**](MessagingCampaignDivisionViewEntityListing)


## get_outbound_ruleset

> [**RuleSet**](RuleSet) get_outbound_ruleset(rule_set_id)


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

### Return type

[**RuleSet**](RuleSet)


## get_outbound_rulesets

> [**RuleSetEntityListing**](RuleSetEntityListing) get_outbound_rulesets(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**RuleSetEntityListing**](RuleSetEntityListing)


## get_outbound_schedules_campaign

> [**CampaignSchedule**](CampaignSchedule) get_outbound_schedules_campaign(campaign_id)


Get a dialer campaign schedule.

Wraps GET /api/v2/outbound/schedules/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:schedule:view
* outbound:campaign:viewSchedule

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

### Return type

[**CampaignSchedule**](CampaignSchedule)


## get_outbound_schedules_campaigns

> [**list[CampaignSchedule]**](CampaignSchedule) get_outbound_schedules_campaigns()


Query for a list of dialer campaign schedules.

Wraps GET /api/v2/outbound/schedules/campaigns 

Requires ANY permissions: 

* outbound:schedule:view
* outbound:campaign:viewSchedule

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

[**list[CampaignSchedule]**](CampaignSchedule)


## get_outbound_schedules_emailcampaign

> [**EmailCampaignSchedule**](EmailCampaignSchedule) get_outbound_schedules_emailcampaign(email_campaign_id)


Get an email campaign schedule.

Wraps GET /api/v2/outbound/schedules/emailcampaigns/{emailCampaignId} 

Requires ANY permissions: 

* outbound:emailCampaignSchedule:view
* outbound:emailCampaign:viewSchedule

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
email_campaign_id = 'email_campaign_id_example' # str | Email Campaign ID

try:
    # Get an email campaign schedule.
    api_response = api_instance.get_outbound_schedules_emailcampaign(email_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_emailcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **email_campaign_id** | **str**| Email Campaign ID |  |

### Return type

[**EmailCampaignSchedule**](EmailCampaignSchedule)


## get_outbound_schedules_emailcampaigns

> [**EmailCampaignScheduleEntityListing**](EmailCampaignScheduleEntityListing) get_outbound_schedules_emailcampaigns()


Query for a list of email campaign schedules.

Wraps GET /api/v2/outbound/schedules/emailcampaigns 

Requires ANY permissions: 

* outbound:emailCampaignSchedule:view
* outbound:emailCampaign:viewSchedule

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
    # Query for a list of email campaign schedules.
    api_response = api_instance.get_outbound_schedules_emailcampaigns()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_emailcampaigns: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**EmailCampaignScheduleEntityListing**](EmailCampaignScheduleEntityListing)


## get_outbound_schedules_messagingcampaign

> [**MessagingCampaignSchedule**](MessagingCampaignSchedule) get_outbound_schedules_messagingcampaign(messaging_campaign_id)


Get a messaging campaign schedule.

Wraps GET /api/v2/outbound/schedules/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaignSchedule:view
* outbound:messagingCampaign:viewSchedule

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
messaging_campaign_id = 'messaging_campaign_id_example' # str | Messaging Campaign ID

try:
    # Get a messaging campaign schedule.
    api_response = api_instance.get_outbound_schedules_messagingcampaign(messaging_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_messagingcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| Messaging Campaign ID |  |

### Return type

[**MessagingCampaignSchedule**](MessagingCampaignSchedule)


## get_outbound_schedules_messagingcampaigns

> [**MessagingCampaignScheduleEntityListing**](MessagingCampaignScheduleEntityListing) get_outbound_schedules_messagingcampaigns()


Query for a list of messaging campaign schedules.

Wraps GET /api/v2/outbound/schedules/messagingcampaigns 

Requires ANY permissions: 

* outbound:messagingCampaignSchedule:view
* outbound:messagingCampaign:viewSchedule

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
    # Query for a list of messaging campaign schedules.
    api_response = api_instance.get_outbound_schedules_messagingcampaigns()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_messagingcampaigns: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**MessagingCampaignScheduleEntityListing**](MessagingCampaignScheduleEntityListing)


## get_outbound_schedules_sequence

> [**SequenceSchedule**](SequenceSchedule) get_outbound_schedules_sequence(sequence_id)


Get a dialer sequence schedule.

Wraps GET /api/v2/outbound/schedules/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:schedule:view
* outbound:campaignSequenceSchedule:view

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

### Return type

[**SequenceSchedule**](SequenceSchedule)


## get_outbound_schedules_sequences

> [**list[SequenceSchedule]**](SequenceSchedule) get_outbound_schedules_sequences()


Query for a list of dialer sequence schedules.

Wraps GET /api/v2/outbound/schedules/sequences 

Requires ANY permissions: 

* outbound:schedule:view
* outbound:campaignSequenceSchedule:view

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

[**list[SequenceSchedule]**](SequenceSchedule)


## get_outbound_schedules_whatsappcampaign

> [**WhatsAppCampaignSchedule**](WhatsAppCampaignSchedule) get_outbound_schedules_whatsappcampaign(whats_app_campaign_id)


Get a WhatsApp campaign schedule.

Wraps GET /api/v2/outbound/schedules/whatsappcampaigns/{whatsAppCampaignId} 

Requires ANY permissions: 

* outbound:whatsAppCampaignSchedule:view
* outbound:whatsAppCampaign:viewSchedule

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
whats_app_campaign_id = 'whats_app_campaign_id_example' # str | WhatsApp Campaign ID

try:
    # Get a WhatsApp campaign schedule.
    api_response = api_instance.get_outbound_schedules_whatsappcampaign(whats_app_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_whatsappcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **whats_app_campaign_id** | **str**| WhatsApp Campaign ID |  |

### Return type

[**WhatsAppCampaignSchedule**](WhatsAppCampaignSchedule)


## get_outbound_schedules_whatsappcampaigns

> [**WhatsAppCampaignScheduleEntityListing**](WhatsAppCampaignScheduleEntityListing) get_outbound_schedules_whatsappcampaigns()


Query for a list of WhatsApp campaign schedules.

Wraps GET /api/v2/outbound/schedules/whatsappcampaigns 

Requires ANY permissions: 

* outbound:whatsAppCampaignSchedule:view
* outbound:whatsAppCampaign:viewSchedule

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
    # Query for a list of WhatsApp campaign schedules.
    api_response = api_instance.get_outbound_schedules_whatsappcampaigns()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->get_outbound_schedules_whatsappcampaigns: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**WhatsAppCampaignScheduleEntityListing**](WhatsAppCampaignScheduleEntityListing)


## get_outbound_sequence

> [**CampaignSequence**](CampaignSequence) get_outbound_sequence(sequence_id)


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

### Return type

[**CampaignSequence**](CampaignSequence)


## get_outbound_sequences

> [**CampaignSequenceEntityListing**](CampaignSequenceEntityListing) get_outbound_sequences(page_size=page_size, page_number=page_number, allow_empty_result=allow_empty_result, filter_type=filter_type, name=name, sort_by=sort_by, sort_order=sort_order)


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
allow_empty_result = False # bool | Whether to return an empty page when there are no results for that page (optional) (default to False)
filter_type = ''Prefix'' # str | Filter type (optional) (default to 'Prefix')
name = 'name_example' # str | Name (optional)
sort_by = 'sort_by_example' # str | Sort by (optional)
sort_order = ''a'' # str | Sort order (optional) (default to 'a')

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
| **allow_empty_result** | **bool**| Whether to return an empty page when there are no results for that page | [optional] [default to False] |
| **filter_type** | **str**| Filter type | [optional] [default to &#39;Prefix&#39;]<br />**Values**: Equals, RegEx, Contains, Prefix, LessThan, LessThanEqualTo, GreaterThan, GreaterThanEqualTo, BeginsWith, EndsWith |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;a&#39;]<br />**Values**: ascending, descending |

### Return type

[**CampaignSequenceEntityListing**](CampaignSequenceEntityListing)


## get_outbound_settings

> [**OutboundSettings**](OutboundSettings) get_outbound_settings()


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

[**OutboundSettings**](OutboundSettings)


## get_outbound_wrapupcodemappings

> [**WrapUpCodeMapping**](WrapUpCodeMapping) get_outbound_wrapupcodemappings()


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

[**WrapUpCodeMapping**](WrapUpCodeMapping)


## patch_outbound_campaign

>  patch_outbound_campaign(campaign_id, body)


Update a campaign.

Wraps PATCH /api/v2/outbound/campaigns/{campaignId} 

Requires ALL permissions: 

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
body = PureCloudPlatformClientV2.CampaignPatchRequest() # CampaignPatchRequest | CampaignPatchRequest

try:
    # Update a campaign.
    api_instance.patch_outbound_campaign(campaign_id, body)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **body** | [**CampaignPatchRequest**](CampaignPatchRequest)| CampaignPatchRequest |  |

### Return type

void (empty response body)


## patch_outbound_dnclist_customexclusioncolumns

>  patch_outbound_dnclist_customexclusioncolumns(dnc_list_id, body)


Add entries to or delete entries from a DNC list.

Only Internal DNC lists may be deleted from

Wraps PATCH /api/v2/outbound/dnclists/{dncListId}/customexclusioncolumns 

Requires ANY permissions: 

* outbound:dnc:edit

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
body = PureCloudPlatformClientV2.DncPatchCustomExclusionColumnsRequest() # DncPatchCustomExclusionColumnsRequest | DNC Custom exclusion column entries

try:
    # Add entries to or delete entries from a DNC list.
    api_instance.patch_outbound_dnclist_customexclusioncolumns(dnc_list_id, body)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_dnclist_customexclusioncolumns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | [**DncPatchCustomExclusionColumnsRequest**](DncPatchCustomExclusionColumnsRequest)| DNC Custom exclusion column entries |  |

### Return type

void (empty response body)


## patch_outbound_dnclist_emailaddresses

>  patch_outbound_dnclist_emailaddresses(dnc_list_id, body)


Add emails to or Delete emails from a DNC list.

Only Internal DNC lists may be added to or deleted from

Wraps PATCH /api/v2/outbound/dnclists/{dncListId}/emailaddresses 

Requires ANY permissions: 

* outbound:dnc:edit

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
body = PureCloudPlatformClientV2.DncPatchEmailsRequest() # DncPatchEmailsRequest | DNC Emails

try:
    # Add emails to or Delete emails from a DNC list.
    api_instance.patch_outbound_dnclist_emailaddresses(dnc_list_id, body)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_dnclist_emailaddresses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | [**DncPatchEmailsRequest**](DncPatchEmailsRequest)| DNC Emails |  |

### Return type

void (empty response body)


## patch_outbound_dnclist_phonenumbers

>  patch_outbound_dnclist_phonenumbers(dnc_list_id, body)


Add numbers to or delete numbers from a DNC list.

Only Internal DNC lists may be added to deleted from

Wraps PATCH /api/v2/outbound/dnclists/{dncListId}/phonenumbers 

Requires ANY permissions: 

* outbound:dnc:edit

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
body = PureCloudPlatformClientV2.DncPatchPhoneNumbersRequest() # DncPatchPhoneNumbersRequest | DNC Phone Numbers

try:
    # Add numbers to or delete numbers from a DNC list.
    api_instance.patch_outbound_dnclist_phonenumbers(dnc_list_id, body)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_dnclist_phonenumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | [**DncPatchPhoneNumbersRequest**](DncPatchPhoneNumbersRequest)| DNC Phone Numbers |  |

### Return type

void (empty response body)


## patch_outbound_dnclist_whatsappnumbers

>  patch_outbound_dnclist_whatsappnumbers(dnc_list_id, body)


Add entries to or delete entries from a DNC list.

Only Internal DNC lists may be deleted from

Wraps PATCH /api/v2/outbound/dnclists/{dncListId}/whatsappnumbers 

Requires ANY permissions: 

* outbound:dnc:edit

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
body = PureCloudPlatformClientV2.DncPatchWhatsAppNumbersRequest() # DncPatchWhatsAppNumbersRequest | DNC whatsApp numbers

try:
    # Add entries to or delete entries from a DNC list.
    api_instance.patch_outbound_dnclist_whatsappnumbers(dnc_list_id, body)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_dnclist_whatsappnumbers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | [**DncPatchWhatsAppNumbersRequest**](DncPatchWhatsAppNumbersRequest)| DNC whatsApp numbers |  |

### Return type

void (empty response body)


## patch_outbound_settings

>  patch_outbound_settings(body, use_max_calls_per_agent_decimal=use_max_calls_per_agent_decimal)


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
use_max_calls_per_agent_decimal = True # bool | Use maxCallsPerAgent with decimal precision (optional)

try:
    # Update the outbound settings for this organization
    api_instance.patch_outbound_settings(body, use_max_calls_per_agent_decimal=use_max_calls_per_agent_decimal)
except ApiException as e:
    print("Exception when calling OutboundApi->patch_outbound_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutboundSettings**](OutboundSettings)| outboundSettings |  |
| **use_max_calls_per_agent_decimal** | **bool**| Use maxCallsPerAgent with decimal precision | [optional] <br />**Values**: true, false |

### Return type

void (empty response body)


## post_outbound_attemptlimits

> [**AttemptLimits**](AttemptLimits) post_outbound_attemptlimits(body)


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
| **body** | [**AttemptLimits**](AttemptLimits)| AttemptLimits |  |

### Return type

[**AttemptLimits**](AttemptLimits)


## post_outbound_callabletimesets

> [**CallableTimeSet**](CallableTimeSet) post_outbound_callabletimesets(body)


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
| **body** | [**CallableTimeSet**](CallableTimeSet)| DialerCallableTimeSet |  |

### Return type

[**CallableTimeSet**](CallableTimeSet)


## post_outbound_callanalysisresponsesets

> [**ResponseSet**](ResponseSet) post_outbound_callanalysisresponsesets(body)


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
| **body** | [**ResponseSet**](ResponseSet)| ResponseSet |  |

### Return type

[**ResponseSet**](ResponseSet)


## post_outbound_campaign_agentownedmappingpreview

> object** post_outbound_campaign_agentownedmappingpreview(campaign_id)


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

### Return type

**object**


## post_outbound_campaign_callback_schedule

> [**ContactCallbackRequest**](ContactCallbackRequest) post_outbound_campaign_callback_schedule(campaign_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Schedule a Callback for a Dialer Campaign (Deprecated)

This endpoint is deprecated and may have unexpected results. Please use \"/conversations/{conversationId}/participants/{participantId}/callbacks instead.\"

Wraps POST /api/v2/outbound/campaigns/{campaignId}/callback/schedule 

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
| **body** | [**ContactCallbackRequest**](ContactCallbackRequest)| ContactCallbackRequest |  |

### Return type

[**ContactCallbackRequest**](ContactCallbackRequest)


## post_outbound_campaign_start

>  post_outbound_campaign_start(campaign_id)


Start the campaign

Wraps POST /api/v2/outbound/campaigns/{campaignId}/start 

Requires ANY permissions: 

* outbound:campaign:start

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
    # Start the campaign
    api_instance.post_outbound_campaign_start(campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaign_start: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |

### Return type

void (empty response body)


## post_outbound_campaign_stop

>  post_outbound_campaign_stop(campaign_id)


Stop the campaign

Wraps POST /api/v2/outbound/campaigns/{campaignId}/stop 

Requires ANY permissions: 

* outbound:campaign:stop

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
    # Stop the campaign
    api_instance.post_outbound_campaign_stop(campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaign_stop: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |

### Return type

void (empty response body)


## post_outbound_campaignrules

> [**CampaignRule**](CampaignRule) post_outbound_campaignrules(body)


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
| **body** | [**CampaignRule**](CampaignRule)| CampaignRule |  |

### Return type

[**CampaignRule**](CampaignRule)


## post_outbound_campaigns

> [**Campaign**](Campaign) post_outbound_campaigns(body, use_max_calls_per_agent_decimal=use_max_calls_per_agent_decimal)


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
use_max_calls_per_agent_decimal = True # bool | Use maxCallsPerAgent with decimal precision (optional)

try:
    # Create a campaign.
    api_response = api_instance.post_outbound_campaigns(body, use_max_calls_per_agent_decimal=use_max_calls_per_agent_decimal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_campaigns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Campaign**](Campaign)| Campaign |  |
| **use_max_calls_per_agent_decimal** | **bool**| Use maxCallsPerAgent with decimal precision | [optional] <br />**Values**: true, false |

### Return type

[**Campaign**](Campaign)


## post_outbound_campaigns_progress

> [**list[CampaignProgress]**](CampaignProgress) post_outbound_campaigns_progress(body)


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
body = ['body_example'] # list[str] | Campaign IDs

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
| **body** | [**list[str]**](str)| Campaign IDs |  |

### Return type

[**list[CampaignProgress]**](CampaignProgress)


## post_outbound_contactlist_clear

>  post_outbound_contactlist_clear(contact_list_id)


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

### Return type

void (empty response body)


## post_outbound_contactlist_contacts

> [**list[DialerContact]**](DialerContact) post_outbound_contactlist_contacts(contact_list_id, body, priority=priority, clear_system_data=clear_system_data, do_not_queue=do_not_queue)


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
priority = True # bool | Contact priority. True means the contact(s) will be dialed next; false means the contact will go to the end of the contact queue. (optional)
clear_system_data = True # bool | Clear system data. True means the system columns (attempts, callable status, etc) stored on the contact will be cleared if the contact already exists; false means they won't. (optional)
do_not_queue = True # bool | Do not queue. True means that updated contacts will not have their positions in the queue altered, so contacts that have already been dialed will not be redialed. For new contacts, this parameter has no effect; False means that updated contacts will be re-queued, according to the 'priority' parameter. (optional)

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
| **body** | [**list[WritableDialerContact]**](WritableDialerContact)| Contact |  |
| **priority** | **bool**| Contact priority. True means the contact(s) will be dialed next; false means the contact will go to the end of the contact queue. | [optional]  |
| **clear_system_data** | **bool**| Clear system data. True means the system columns (attempts, callable status, etc) stored on the contact will be cleared if the contact already exists; false means they won&#39;t. | [optional]  |
| **do_not_queue** | **bool**| Do not queue. True means that updated contacts will not have their positions in the queue altered, so contacts that have already been dialed will not be redialed. For new contacts, this parameter has no effect; False means that updated contacts will be re-queued, according to the &#39;priority&#39; parameter. | [optional]  |

### Return type

[**list[DialerContact]**](DialerContact)


## post_outbound_contactlist_contacts_bulk

> [**list[DialerContact]**](DialerContact) post_outbound_contactlist_contacts_bulk(contact_list_id, body)


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
body = ['body_example'] # list[str] | ContactIds to get.

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
| **body** | [**list[str]**](str)| ContactIds to get. |  |

### Return type

[**list[DialerContact]**](DialerContact)


## post_outbound_contactlist_contacts_bulk_remove

> [**ContactsBulkOperationJob**](ContactsBulkOperationJob) post_outbound_contactlist_contacts_bulk_remove(contact_list_id, body)


Start an async job to delete contacts using a filter.

Wraps POST /api/v2/outbound/contactlists/{contactListId}/contacts/bulk/remove 

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
body = PureCloudPlatformClientV2.ContactBulkSearchParameters() # ContactBulkSearchParameters | Contact filter information.

try:
    # Start an async job to delete contacts using a filter.
    api_response = api_instance.post_outbound_contactlist_contacts_bulk_remove(contact_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_contacts_bulk_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **body** | [**ContactBulkSearchParameters**](ContactBulkSearchParameters)| Contact filter information. |  |

### Return type

[**ContactsBulkOperationJob**](ContactsBulkOperationJob)


## post_outbound_contactlist_contacts_bulk_update

> [**ContactsBulkOperationJob**](ContactsBulkOperationJob) post_outbound_contactlist_contacts_bulk_update(contact_list_id, body)


Start an async job to bulk edit contacts.

Wraps POST /api/v2/outbound/contactlists/{contactListId}/contacts/bulk/update 

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
body = PureCloudPlatformClientV2.ContactBulkEditRequest() # ContactBulkEditRequest | Contact bulk edit request information.

try:
    # Start an async job to bulk edit contacts.
    api_response = api_instance.post_outbound_contactlist_contacts_bulk_update(contact_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_contacts_bulk_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **body** | [**ContactBulkEditRequest**](ContactBulkEditRequest)| Contact bulk edit request information. |  |

### Return type

[**ContactsBulkOperationJob**](ContactsBulkOperationJob)


## post_outbound_contactlist_contacts_search

> [**ContactListingResponse**](ContactListingResponse) post_outbound_contactlist_contacts_search(contact_list_id, body)


Query contacts from a contact list.

Wraps POST /api/v2/outbound/contactlists/{contactListId}/contacts/search 

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
body = PureCloudPlatformClientV2.ContactListingRequest() # ContactListingRequest | Contact search parameters.

try:
    # Query contacts from a contact list.
    api_response = api_instance.post_outbound_contactlist_contacts_search(contact_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_contacts_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| Contact List ID |  |
| **body** | [**ContactListingRequest**](ContactListingRequest)| Contact search parameters. |  |

### Return type

[**ContactListingResponse**](ContactListingResponse)


## post_outbound_contactlist_export

> [**DomainEntityRef**](DomainEntityRef) post_outbound_contactlist_export(contact_list_id, body=body)


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
body = PureCloudPlatformClientV2.ContactsExportRequest() # ContactsExportRequest | Export information to get (optional)

try:
    # Initiate the export of a contact list.
    api_response = api_instance.post_outbound_contactlist_export(contact_list_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlist_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_id** | **str**| ContactList ID |  |
| **body** | [**ContactsExportRequest**](ContactsExportRequest)| Export information to get | [optional]  |

### Return type

[**DomainEntityRef**](DomainEntityRef)


## post_outbound_contactlistfilters

> [**ContactListFilter**](ContactListFilter) post_outbound_contactlistfilters(body)


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
| **body** | [**ContactListFilter**](ContactListFilter)| ContactListFilter |  |

### Return type

[**ContactListFilter**](ContactListFilter)


## post_outbound_contactlistfilters_bulk_retrieve

> [**ContactListFilterEntityListing**](ContactListFilterEntityListing) post_outbound_contactlistfilters_bulk_retrieve(body)


Retrieve multiple contact list filters

Wraps POST /api/v2/outbound/contactlistfilters/bulk/retrieve 

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
body = PureCloudPlatformClientV2.ContactListFilterBulkRetrieveBody() # ContactListFilterBulkRetrieveBody | The contact list filters to retrieve

try:
    # Retrieve multiple contact list filters
    api_response = api_instance.post_outbound_contactlistfilters_bulk_retrieve(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlistfilters_bulk_retrieve: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactListFilterBulkRetrieveBody**](ContactListFilterBulkRetrieveBody)| The contact list filters to retrieve |  |

### Return type

[**ContactListFilterEntityListing**](ContactListFilterEntityListing)


## post_outbound_contactlistfilters_preview

> [**FilterPreviewResponse**](FilterPreviewResponse) post_outbound_contactlistfilters_preview(body)


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
| **body** | [**ContactListFilter**](ContactListFilter)| ContactListFilter |  |

### Return type

[**FilterPreviewResponse**](FilterPreviewResponse)


## post_outbound_contactlists

> [**ContactList**](ContactList) post_outbound_contactlists(body)


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
| **body** | [**ContactList**](ContactList)| ContactList |  |

### Return type

[**ContactList**](ContactList)


## post_outbound_contactlisttemplates

> [**ContactListTemplate**](ContactListTemplate) post_outbound_contactlisttemplates(body)


Create Contact List Template

Wraps POST /api/v2/outbound/contactlisttemplates 

Requires ANY permissions: 

* outbound:contactListTemplate:add

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
body = PureCloudPlatformClientV2.ContactListTemplate() # ContactListTemplate | ContactListTemplate

try:
    # Create Contact List Template
    api_response = api_instance.post_outbound_contactlisttemplates(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlisttemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactListTemplate**](ContactListTemplate)| ContactListTemplate |  |

### Return type

[**ContactListTemplate**](ContactListTemplate)


## post_outbound_contactlisttemplates_bulk_add

> [**ContactListTemplateEntityListing**](ContactListTemplateEntityListing) post_outbound_contactlisttemplates_bulk_add(body)


Add multiple contact list templates

Wraps POST /api/v2/outbound/contactlisttemplates/bulk/add 

Requires ANY permissions: 

* outbound:contactListTemplate:add

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
body = [PureCloudPlatformClientV2.ContactListTemplate()] # list[ContactListTemplate] | contact list template(s) to add

try:
    # Add multiple contact list templates
    api_response = api_instance.post_outbound_contactlisttemplates_bulk_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlisttemplates_bulk_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[ContactListTemplate]**](ContactListTemplate)| contact list template(s) to add |  |

### Return type

[**ContactListTemplateEntityListing**](ContactListTemplateEntityListing)


## post_outbound_contactlisttemplates_bulk_retrieve

> [**ContactListTemplateEntityListing**](ContactListTemplateEntityListing) post_outbound_contactlisttemplates_bulk_retrieve(body)


Get multiple contact list templates

Wraps POST /api/v2/outbound/contactlisttemplates/bulk/retrieve 

Requires ANY permissions: 

* outbound:contactListTemplate:view

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
body = PureCloudPlatformClientV2.ContactListTemplateBulkRetrieveBody() # ContactListTemplateBulkRetrieveBody | contact list templates to get

try:
    # Get multiple contact list templates
    api_response = api_instance.post_outbound_contactlisttemplates_bulk_retrieve(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_contactlisttemplates_bulk_retrieve: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactListTemplateBulkRetrieveBody**](ContactListTemplateBulkRetrieveBody)| contact list templates to get |  |

### Return type

[**ContactListTemplateEntityListing**](ContactListTemplateEntityListing)


## post_outbound_conversation_dnc

>  post_outbound_conversation_dnc(conversation_id)


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

### Return type

void (empty response body)


## post_outbound_digitalrulesets

> [**DigitalRuleSet**](DigitalRuleSet) post_outbound_digitalrulesets(body)


Create an Outbound Digital Rule Set

Wraps POST /api/v2/outbound/digitalrulesets 

Requires ANY permissions: 

* outbound:digitalRuleSet:add

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
body = PureCloudPlatformClientV2.DigitalRuleSet() # DigitalRuleSet | Digital Rule Set

try:
    # Create an Outbound Digital Rule Set
    api_response = api_instance.post_outbound_digitalrulesets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_digitalrulesets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DigitalRuleSet**](DigitalRuleSet)| Digital Rule Set |  |

### Return type

[**DigitalRuleSet**](DigitalRuleSet)


## post_outbound_dnclist_emailaddresses

>  post_outbound_dnclist_emailaddresses(dnc_list_id, body)


Add email addresses to a DNC list.

Only Internal DNC lists may be appended to

Wraps POST /api/v2/outbound/dnclists/{dncListId}/emailaddresses 

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
body = ['body_example'] # list[str] | DNC email addresses

try:
    # Add email addresses to a DNC list.
    api_instance.post_outbound_dnclist_emailaddresses(dnc_list_id, body)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_dnclist_emailaddresses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dnc_list_id** | **str**| DncList ID |  |
| **body** | [**list[str]**](str)| DNC email addresses |  |

### Return type

void (empty response body)


## post_outbound_dnclist_export

> [**DomainEntityRef**](DomainEntityRef) post_outbound_dnclist_export(dnc_list_id)


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

### Return type

[**DomainEntityRef**](DomainEntityRef)


## post_outbound_dnclist_phonenumbers

>  post_outbound_dnclist_phonenumbers(dnc_list_id, body, expiration_date_time=expiration_date_time)


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
body = ['body_example'] # list[str] | DNC Phone Numbers
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
| **body** | [**list[str]**](str)| DNC Phone Numbers |  |
| **expiration_date_time** | **str**| Expiration date for DNC phone numbers in yyyy-MM-ddTHH:mmZ format | [optional]  |

### Return type

void (empty response body)


## post_outbound_dnclists

> [**DncList**](DncList) post_outbound_dnclists(body)


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
| **body** | [**DncListCreate**](DncListCreate)| DncList |  |

### Return type

[**DncList**](DncList)


## post_outbound_filespecificationtemplates

> [**FileSpecificationTemplate**](FileSpecificationTemplate) post_outbound_filespecificationtemplates(body)


Create File Specification Template

Wraps POST /api/v2/outbound/filespecificationtemplates 

Requires ANY permissions: 

* outbound:fileSpecificationTemplate:add

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
body = PureCloudPlatformClientV2.FileSpecificationTemplate() # FileSpecificationTemplate | FileSpecificationTemplate

try:
    # Create File Specification Template
    api_response = api_instance.post_outbound_filespecificationtemplates(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_filespecificationtemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FileSpecificationTemplate**](FileSpecificationTemplate)| FileSpecificationTemplate |  |

### Return type

[**FileSpecificationTemplate**](FileSpecificationTemplate)


## post_outbound_importtemplates

> [**ImportTemplate**](ImportTemplate) post_outbound_importtemplates(body)


Create Import Template

Wraps POST /api/v2/outbound/importtemplates 

Requires ANY permissions: 

* outbound:importTemplate:add

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
body = PureCloudPlatformClientV2.ImportTemplate() # ImportTemplate | ImportTemplate

try:
    # Create Import Template
    api_response = api_instance.post_outbound_importtemplates(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_importtemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ImportTemplate**](ImportTemplate)| ImportTemplate |  |

### Return type

[**ImportTemplate**](ImportTemplate)


## post_outbound_importtemplates_bulk_add

> [**ImportTemplateEntityListing**](ImportTemplateEntityListing) post_outbound_importtemplates_bulk_add(body)


Add multiple import templates

Wraps POST /api/v2/outbound/importtemplates/bulk/add 

Requires ANY permissions: 

* outbound:importTemplate:add

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
body = [PureCloudPlatformClientV2.ImportTemplate()] # list[ImportTemplate] | import template(s) to add

try:
    # Add multiple import templates
    api_response = api_instance.post_outbound_importtemplates_bulk_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_importtemplates_bulk_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[ImportTemplate]**](ImportTemplate)| import template(s) to add |  |

### Return type

[**ImportTemplateEntityListing**](ImportTemplateEntityListing)


## post_outbound_messagingcampaign_start

>  post_outbound_messagingcampaign_start(messaging_campaign_id)


Start the campaign

Documented permissions are applicable based on campaign type.

Wraps POST /api/v2/outbound/messagingcampaigns/{messagingCampaignId}/start 

Requires ANY permissions: 

* outbound:messagingCampaign:start
* outbound:emailCampaign:start
* outbound:whatsAppCampaign:start

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
    # Start the campaign
    api_instance.post_outbound_messagingcampaign_start(messaging_campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_messagingcampaign_start: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |

### Return type

void (empty response body)


## post_outbound_messagingcampaign_stop

>  post_outbound_messagingcampaign_stop(messaging_campaign_id)


Stop the campaign

Documented permissions are applicable based on campaign type.

Wraps POST /api/v2/outbound/messagingcampaigns/{messagingCampaignId}/stop 

Requires ANY permissions: 

* outbound:messagingCampaign:stop
* outbound:emailCampaign:stop
* outbound:whatsAppCampaign:stop

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
    # Stop the campaign
    api_instance.post_outbound_messagingcampaign_stop(messaging_campaign_id)
except ApiException as e:
    print("Exception when calling OutboundApi->post_outbound_messagingcampaign_stop: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| The Messaging Campaign ID |  |

### Return type

void (empty response body)


## post_outbound_messagingcampaigns

> [**MessagingCampaign**](MessagingCampaign) post_outbound_messagingcampaigns(body)


Create a Messaging Campaign

Wraps POST /api/v2/outbound/messagingcampaigns 

Requires ANY permissions: 

* outbound:messagingCampaign:add
* outbound:emailCampaign:add
* outbound:whatsAppCampaign:add

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
| **body** | [**MessagingCampaign**](MessagingCampaign)| Messaging Campaign |  |

### Return type

[**MessagingCampaign**](MessagingCampaign)


## post_outbound_messagingcampaigns_progress

> [**list[CampaignProgress]**](CampaignProgress) post_outbound_messagingcampaigns_progress(body)


Get progress for a list of messaging campaigns

Wraps POST /api/v2/outbound/messagingcampaigns/progress 

Requires ANY permissions: 

* outbound:messagingCampaign:view
* outbound:emailCampaign:view
* outbound:whatsAppCampaign:view

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
body = ['body_example'] # list[str] | Messaging Campaign IDs

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
| **body** | [**list[str]**](str)| Messaging Campaign IDs |  |

### Return type

[**list[CampaignProgress]**](CampaignProgress)


## post_outbound_rulesets

> [**RuleSet**](RuleSet) post_outbound_rulesets(body)


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
| **body** | [**RuleSet**](RuleSet)| RuleSet |  |

### Return type

[**RuleSet**](RuleSet)


## post_outbound_sequences

> [**CampaignSequence**](CampaignSequence) post_outbound_sequences(body)


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
| **body** | [**CampaignSequence**](CampaignSequence)| Organization |  |

### Return type

[**CampaignSequence**](CampaignSequence)


## put_outbound_attemptlimit

> [**AttemptLimits**](AttemptLimits) put_outbound_attemptlimit(attempt_limits_id, body)


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
| **body** | [**AttemptLimits**](AttemptLimits)| AttemptLimits |  |

### Return type

[**AttemptLimits**](AttemptLimits)


## put_outbound_callabletimeset

> [**CallableTimeSet**](CallableTimeSet) put_outbound_callabletimeset(callable_time_set_id, body)


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
| **body** | [**CallableTimeSet**](CallableTimeSet)| DialerCallableTimeSet |  |

### Return type

[**CallableTimeSet**](CallableTimeSet)


## put_outbound_callanalysisresponseset

> [**ResponseSet**](ResponseSet) put_outbound_callanalysisresponseset(call_analysis_set_id, body)


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
| **body** | [**ResponseSet**](ResponseSet)| ResponseSet |  |

### Return type

[**ResponseSet**](ResponseSet)


## put_outbound_campaign

> [**Campaign**](Campaign) put_outbound_campaign(campaign_id, body, use_max_calls_per_agent_decimal=use_max_calls_per_agent_decimal)


Update a campaign.

Wraps PUT /api/v2/outbound/campaigns/{campaignId} 

Requires ALL permissions: 

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
use_max_calls_per_agent_decimal = True # bool | Use maxCallsPerAgent with decimal precision (optional)

try:
    # Update a campaign.
    api_response = api_instance.put_outbound_campaign(campaign_id, body, use_max_calls_per_agent_decimal=use_max_calls_per_agent_decimal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_campaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **campaign_id** | **str**| Campaign ID |  |
| **body** | [**Campaign**](Campaign)| Campaign |  |
| **use_max_calls_per_agent_decimal** | **bool**| Use maxCallsPerAgent with decimal precision | [optional] <br />**Values**: true, false |

### Return type

[**Campaign**](Campaign)


## put_outbound_campaign_agent

> str** put_outbound_campaign_agent(campaign_id, user_id, body)


Send notification that an agent's state changed 

New agent state.

Wraps PUT /api/v2/outbound/campaigns/{campaignId}/agents/{userId} 

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
| **body** | [**Agent**](Agent)| agent |  |

### Return type

**str**


## put_outbound_campaignrule

> [**CampaignRule**](CampaignRule) put_outbound_campaignrule(campaign_rule_id, body)


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
| **body** | [**CampaignRule**](CampaignRule)| CampaignRule |  |

### Return type

[**CampaignRule**](CampaignRule)


## put_outbound_contactlist

> [**ContactList**](ContactList) put_outbound_contactlist(contact_list_id, body)


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
| **body** | [**ContactList**](ContactList)| ContactList |  |

### Return type

[**ContactList**](ContactList)


## put_outbound_contactlist_contact

> [**DialerContact**](DialerContact) put_outbound_contactlist_contact(contact_list_id, contact_id, body)


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
| **body** | [**DialerContact**](DialerContact)| Contact |  |

### Return type

[**DialerContact**](DialerContact)


## put_outbound_contactlistfilter

> [**ContactListFilter**](ContactListFilter) put_outbound_contactlistfilter(contact_list_filter_id, body)


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
| **body** | [**ContactListFilter**](ContactListFilter)| ContactListFilter |  |

### Return type

[**ContactListFilter**](ContactListFilter)


## put_outbound_contactlisttemplate

> [**ContactListTemplate**](ContactListTemplate) put_outbound_contactlisttemplate(contact_list_template_id, body)


Update a contact list template.

Wraps PUT /api/v2/outbound/contactlisttemplates/{contactListTemplateId} 

Requires ANY permissions: 

* outbound:contactListTemplate:edit

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
contact_list_template_id = 'contact_list_template_id_example' # str | ContactListTemplate ID
body = PureCloudPlatformClientV2.ContactListTemplate() # ContactListTemplate | ContactListTemplate

try:
    # Update a contact list template.
    api_response = api_instance.put_outbound_contactlisttemplate(contact_list_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_contactlisttemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_list_template_id** | **str**| ContactListTemplate ID |  |
| **body** | [**ContactListTemplate**](ContactListTemplate)| ContactListTemplate |  |

### Return type

[**ContactListTemplate**](ContactListTemplate)


## put_outbound_digitalruleset

> [**DigitalRuleSet**](DigitalRuleSet) put_outbound_digitalruleset(digital_rule_set_id, body)


Update an Outbound Digital Rule Set

Wraps PUT /api/v2/outbound/digitalrulesets/{digitalRuleSetId} 

Requires ANY permissions: 

* outbound:digitalRuleSet:edit

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
digital_rule_set_id = 'digital_rule_set_id_example' # str | The Digital Rule Set ID
body = PureCloudPlatformClientV2.DigitalRuleSet() # DigitalRuleSet | Digital Rule Set

try:
    # Update an Outbound Digital Rule Set
    api_response = api_instance.put_outbound_digitalruleset(digital_rule_set_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_digitalruleset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **digital_rule_set_id** | **str**| The Digital Rule Set ID |  |
| **body** | [**DigitalRuleSet**](DigitalRuleSet)| Digital Rule Set |  |

### Return type

[**DigitalRuleSet**](DigitalRuleSet)


## put_outbound_dnclist

> [**DncList**](DncList) put_outbound_dnclist(dnc_list_id, body)


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
| **body** | [**DncList**](DncList)| DncList |  |

### Return type

[**DncList**](DncList)


## put_outbound_filespecificationtemplate

> [**FileSpecificationTemplate**](FileSpecificationTemplate) put_outbound_filespecificationtemplate(file_specification_template_id, body)


Update File Specification Template

Wraps PUT /api/v2/outbound/filespecificationtemplates/{fileSpecificationTemplateId} 

Requires ANY permissions: 

* outbound:fileSpecificationTemplate:edit

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
file_specification_template_id = 'file_specification_template_id_example' # str | File Specification Template ID
body = PureCloudPlatformClientV2.FileSpecificationTemplate() # FileSpecificationTemplate | fileSpecificationTemplate

try:
    # Update File Specification Template
    api_response = api_instance.put_outbound_filespecificationtemplate(file_specification_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_filespecificationtemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **file_specification_template_id** | **str**| File Specification Template ID |  |
| **body** | [**FileSpecificationTemplate**](FileSpecificationTemplate)| fileSpecificationTemplate |  |

### Return type

[**FileSpecificationTemplate**](FileSpecificationTemplate)


## put_outbound_importtemplate

> [**ImportTemplate**](ImportTemplate) put_outbound_importtemplate(import_template_id, body)


Update Import Template

Wraps PUT /api/v2/outbound/importtemplates/{importTemplateId} 

Requires ANY permissions: 

* outbound:importTemplate:edit

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
import_template_id = 'import_template_id_example' # str | Import Template ID
body = PureCloudPlatformClientV2.ImportTemplate() # ImportTemplate | importTemplate

try:
    # Update Import Template
    api_response = api_instance.put_outbound_importtemplate(import_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_importtemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **import_template_id** | **str**| Import Template ID |  |
| **body** | [**ImportTemplate**](ImportTemplate)| importTemplate |  |

### Return type

[**ImportTemplate**](ImportTemplate)


## put_outbound_messagingcampaign

> [**MessagingCampaign**](MessagingCampaign) put_outbound_messagingcampaign(messaging_campaign_id, body)


Update an Outbound Messaging Campaign

Wraps PUT /api/v2/outbound/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaign:edit
* outbound:emailCampaign:edit
* outbound:whatsAppCampaign:edit

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
| **body** | [**MessagingCampaign**](MessagingCampaign)| MessagingCampaign |  |

### Return type

[**MessagingCampaign**](MessagingCampaign)


## put_outbound_ruleset

> [**RuleSet**](RuleSet) put_outbound_ruleset(rule_set_id, body)


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
| **body** | [**RuleSet**](RuleSet)| RuleSet |  |

### Return type

[**RuleSet**](RuleSet)


## put_outbound_schedules_campaign

> [**CampaignSchedule**](CampaignSchedule) put_outbound_schedules_campaign(campaign_id, body)


Update a new campaign schedule.

Wraps PUT /api/v2/outbound/schedules/campaigns/{campaignId} 

Requires ANY permissions: 

* outbound:schedule:edit
* outbound:campaign:editSchedule

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
| **body** | [**CampaignSchedule**](CampaignSchedule)| CampaignSchedule |  |

### Return type

[**CampaignSchedule**](CampaignSchedule)


## put_outbound_schedules_emailcampaign

> [**EmailCampaignSchedule**](EmailCampaignSchedule) put_outbound_schedules_emailcampaign(email_campaign_id, body)


Update an email campaign schedule.

Wraps PUT /api/v2/outbound/schedules/emailcampaigns/{emailCampaignId} 

Requires ANY permissions: 

* outbound:emailCampaignSchedule:edit
* outbound:emailCampaign:editSchedule

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
email_campaign_id = 'email_campaign_id_example' # str | Email Campaign ID
body = PureCloudPlatformClientV2.EmailCampaignSchedule() # EmailCampaignSchedule | EmailCampaignSchedule

try:
    # Update an email campaign schedule.
    api_response = api_instance.put_outbound_schedules_emailcampaign(email_campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_schedules_emailcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **email_campaign_id** | **str**| Email Campaign ID |  |
| **body** | [**EmailCampaignSchedule**](EmailCampaignSchedule)| EmailCampaignSchedule |  |

### Return type

[**EmailCampaignSchedule**](EmailCampaignSchedule)


## put_outbound_schedules_messagingcampaign

> [**MessagingCampaignSchedule**](MessagingCampaignSchedule) put_outbound_schedules_messagingcampaign(messaging_campaign_id, body)


Update a new messaging campaign schedule.

Wraps PUT /api/v2/outbound/schedules/messagingcampaigns/{messagingCampaignId} 

Requires ANY permissions: 

* outbound:messagingCampaignSchedule:edit
* outbound:messagingCampaign:editSchedule

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
messaging_campaign_id = 'messaging_campaign_id_example' # str | Messaging Campaign ID
body = PureCloudPlatformClientV2.MessagingCampaignSchedule() # MessagingCampaignSchedule | MessagingCampaignSchedule

try:
    # Update a new messaging campaign schedule.
    api_response = api_instance.put_outbound_schedules_messagingcampaign(messaging_campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_schedules_messagingcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messaging_campaign_id** | **str**| Messaging Campaign ID |  |
| **body** | [**MessagingCampaignSchedule**](MessagingCampaignSchedule)| MessagingCampaignSchedule |  |

### Return type

[**MessagingCampaignSchedule**](MessagingCampaignSchedule)


## put_outbound_schedules_sequence

> [**SequenceSchedule**](SequenceSchedule) put_outbound_schedules_sequence(sequence_id, body)


Update a new sequence schedule.

Wraps PUT /api/v2/outbound/schedules/sequences/{sequenceId} 

Requires ANY permissions: 

* outbound:schedule:edit
* outbound:campaignSequenceSchedule:edit

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
| **body** | [**SequenceSchedule**](SequenceSchedule)| SequenceSchedule |  |

### Return type

[**SequenceSchedule**](SequenceSchedule)


## put_outbound_schedules_whatsappcampaign

> [**WhatsAppCampaignSchedule**](WhatsAppCampaignSchedule) put_outbound_schedules_whatsappcampaign(whats_app_campaign_id, body)


Update a WhatsApp campaign schedule.

Wraps PUT /api/v2/outbound/schedules/whatsappcampaigns/{whatsAppCampaignId} 

Requires ANY permissions: 

* outbound:whatsAppCampaignSchedule:edit
* outbound:whatsAppCampaign:editSchedule

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
whats_app_campaign_id = 'whats_app_campaign_id_example' # str | WhatsApp Campaign ID
body = PureCloudPlatformClientV2.WhatsAppCampaignSchedule() # WhatsAppCampaignSchedule | WhatsAppCampaignSchedule

try:
    # Update a WhatsApp campaign schedule.
    api_response = api_instance.put_outbound_schedules_whatsappcampaign(whats_app_campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundApi->put_outbound_schedules_whatsappcampaign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **whats_app_campaign_id** | **str**| WhatsApp Campaign ID |  |
| **body** | [**WhatsAppCampaignSchedule**](WhatsAppCampaignSchedule)| WhatsAppCampaignSchedule |  |

### Return type

[**WhatsAppCampaignSchedule**](WhatsAppCampaignSchedule)


## put_outbound_sequence

> [**CampaignSequence**](CampaignSequence) put_outbound_sequence(sequence_id, body)


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
| **body** | [**CampaignSequence**](CampaignSequence)| Organization |  |

### Return type

[**CampaignSequence**](CampaignSequence)


## put_outbound_wrapupcodemappings

> [**WrapUpCodeMapping**](WrapUpCodeMapping) put_outbound_wrapupcodemappings(body)


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
| **body** | [**WrapUpCodeMapping**](WrapUpCodeMapping)| wrapUpCodeMapping |  |

### Return type

[**WrapUpCodeMapping**](WrapUpCodeMapping)


_PureCloudPlatformClientV2 240.0.0_
