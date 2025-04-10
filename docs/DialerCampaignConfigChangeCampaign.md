# DialerCampaignConfigChangeCampaign

## DialerCampaignConfigChangeCampaign

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **contact_list** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) |  | [optional] |
| **queue** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **dialing_mode** | str | dialing mode of the campaign | [optional] |
| **script** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **edge_group** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **site** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **campaign_status** | str |  | [optional] |
| **phone_columns** | [list[DialerCampaignConfigChangePhoneColumn]](DialerCampaignConfigChangePhoneColumn) | the contact list phone columns to be called for the campaign | [optional] |
| **abandon_rate** | float | the targeted abandon rate percentage | [optional] |
| **dnc_lists** | [list[DialerCampaignConfigChangeUriReference]](DialerCampaignConfigChangeUriReference) | identifiers of the do not call lists | [optional] |
| **callable_time_set** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **call_analysis_response_set** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **caller_name** | str | caller id name to be displayed on the outbound call | [optional] |
| **caller_address** | str | caller id phone number to be displayed on the outbound call | [optional] |
| **outbound_line_count** | int | for agentless campaigns, the number of outbound lines to be concurrently dialed | [optional] |
| **errors** | [list[DialerCampaignConfigChangeRestErrorDetail]](DialerCampaignConfigChangeRestErrorDetail) | a list of current error conditions associated with the campaign | [optional] |
| **rule_sets** | [list[DialerCampaignConfigChangeUriReference]](DialerCampaignConfigChangeUriReference) | identifiers of the rule sets | [optional] |
| **skip_preview_disabled** | bool | for preview campaigns, indicator of whether the agent can skip a preview without placing a call | [optional] |
| **preview_time_out_seconds** | int | for preview campaigns, number of seconds before a call will be automatically placed. A value of 0 indicates no automatic placement of calls | [optional] |
| **single_number_preview** | bool | for preview campaigns with multiple phone columns, indicator if one (true) or multiple (false) phone numbers will be available to call for each preview | [optional] |
| **contact_sort** | [DialerCampaignConfigChangeContactSort](DialerCampaignConfigChangeContactSort) |  | [optional] |
| **contact_sorts** | [list[DialerCampaignConfigChangeContactSort]](DialerCampaignConfigChangeContactSort) | List of contact sort objects. | [optional] |
| **no_answer_timeout** | int | for non-preview campaigns, how long to wait before dispositioning as &#39;no-answer&#39;, default 30 seconds | [optional] |
| **call_analysis_language** | str | The language the edge will use to analyze the call | [optional] |
| **priority** | int | The priority of this campaign relative to other campaigns | [optional] |
| **contact_list_filters** | [list[DialerCampaignConfigChangeUriReference]](DialerCampaignConfigChangeUriReference) | List of contact filters | [optional] |
| **division** | [DialerCampaignConfigChangeUriReference](DialerCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **agent_owned_column** | str | For Preview Campaigns. Name of the contact column in the contact list containing the userIds of agents to assign specific contact records to. | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 225.0.0_
