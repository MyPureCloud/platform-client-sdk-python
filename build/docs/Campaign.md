---
title: Campaign
---
## Campaign

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the Campaign. | |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [**UriReference**](UriReference.html) | The ContactList for this Campaign to dial. | |
| **queue** | [**UriReference**](UriReference.html) | The Queue for this Campaign to route calls to. Required for all dialing modes except agentless. | [optional] |
| **dialing_mode** | **str** | The strategy this Campaign will use for dialing. | |
| **script** | [**UriReference**](UriReference.html) | The Script to be displayed to agents that are handling outbound calls. Required for all dialing modes except agentless. | [optional] |
| **edge_group** | [**UriReference**](UriReference.html) | The EdgeGroup that will place the calls. Required for all dialing modes except preview. | [optional] |
| **site** | [**UriReference**](UriReference.html) | The identifier of the site to be used for dialing; can be set in place of an edge group. | [optional] |
| **campaign_status** | **str** | The current status of the Campaign. A Campaign may be turned &#39;on&#39; or &#39;off&#39;. Required for updates. | [optional] |
| **phone_columns** | [**list[PhoneColumn]**](PhoneColumn.html) | The ContactPhoneNumberColumns on the ContactList that this Campaign should dial. | |
| **abandon_rate** | **float** | The targeted abandon rate percentage. Required for progressive, power, and predictive campaigns. | [optional] |
| **dnc_lists** | [**list[UriReference]**](UriReference.html) | DncLists for this Campaign to check before placing a call. | [optional] |
| **callable_time_set** | [**UriReference**](UriReference.html) | The callable time set for this campaign to check before placing a call. | [optional] |
| **call_analysis_response_set** | [**UriReference**](UriReference.html) | The call analysis response set to handle call analysis results from the edge. Required for all dialing modes except preview. | [optional] |
| **errors** | [**list[RestErrorDetail]**](RestErrorDetail.html) | A list of current error conditions associated with the campaign. | [optional] |
| **caller_name** | **str** | The caller id name to be displayed on the outbound call. | |
| **caller_address** | **str** | The caller id phone number to be displayed on the outbound call. | |
| **outbound_line_count** | **int** | The number of outbound lines to be concurrently dialed. Only applicable to non-preview campaigns; only required for agentless. | [optional] |
| **rule_sets** | [**list[UriReference]**](UriReference.html) | Rule sets to be applied while this campaign is dialing. | [optional] |
| **skip_preview_disabled** | **bool** | Whether or not agents can skip previews without placing a call. Only applicable for preview campaigns. | [optional] |
| **preview_time_out_seconds** | **int** | The number of seconds before a call will be automatically placed on a preview. A value of 0 indicates no automatic placement of calls. Only applicable to preview campaigns. | [optional] |
| **always_running** | **bool** | Indicates (when true) that the campaign will remain on after contacts are depleted, allowing additional contacts to be appended/added to the contact list and processed by the still-running campaign. The campaign can still be turned off manually. | [optional] |
| **contact_sort** | [**ContactSort**](ContactSort.html) | The order in which to sort contacts for dialing, based on a column. | [optional] |
| **contact_sorts** | [**list[ContactSort]**](ContactSort.html) | The order in which to sort contacts for dialing, based on up to four columns. | [optional] |
| **no_answer_timeout** | **int** | How long to wait before dispositioning a call as &#39;no-answer&#39;. Default 30 seconds. Only applicable to non-preview campaigns. | [optional] |
| **call_analysis_language** | **str** | The language the edge will use to analyze the call. | [optional] |
| **priority** | **int** | The priority of this campaign relative to other campaigns that are running on the same queue. 5 is the highest priority, 1 the lowest. | [optional] |
| **contact_list_filters** | [**list[UriReference]**](UriReference.html) | Filter to apply to the contact list before dialing. Currently a campaign can only have one filter applied. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


