---
title: Campaign
---
## Campaign

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [**UriReference**](UriReference.html) | identifier of the contact list for the campaign | |
| **queue** | [**UriReference**](UriReference.html) | identifier of the agent assignment queue, required for all dialing modes other than agentless | |
| **dialing_mode** | **str** | dialing mode of the campaign | |
| **script** | [**UriReference**](UriReference.html) | identifier of the campaign script, required for all dialing modes other than agentless | |
| **edge_group** | [**UriReference**](UriReference.html) | identifier of the edge group, required for all dialing modes other than preview | |
| **campaign_status** | **str** | status of the campaign; can be set to &#39;on&#39; or &#39;off&#39; | |
| **phone_columns** | [**list[PhoneColumn]**](PhoneColumn.html) | the contact list phone columns to be called for the campaign | |
| **abandon_rate** | **float** | the targeted abandon rate percentage | [optional] |
| **dnc_lists** | [**list[UriReference]**](UriReference.html) | identifiers of the do not call lists | [optional] |
| **callable_time_set** | [**UriReference**](UriReference.html) | the identifier of the callable time set | [optional] |
| **call_analysis_response_set** | [**UriReference**](UriReference.html) | the identifier of the call analysis response set, required for all dialing modes other than preview | |
| **errors** | [**list[RestErrorDetail]**](RestErrorDetail.html) | a list of current error conditions associated with the campaign | [optional] |
| **caller_name** | **str** | caller id name to be displayed on the outbound call | [optional] |
| **caller_address** | **str** | caller id phone number to be displayed on the outbound call | [optional] |
| **outbound_line_count** | **int** | for agentless campaigns, the number of outbound lines to be concurrently dialed | [optional] |
| **rule_sets** | [**list[UriReference]**](UriReference.html) | identifiers of the rule sets | [optional] |
| **skip_preview_disabled** | **bool** | for preview campaigns, indicator of whether the agent can skip a preview without placing a call | [optional] |
| **preview_time_out_seconds** | **int** | for preview campaigns, number of seconds before a call will be automatically placed. A value of 0 indicates no automatic placement of calls | [optional] |
| **contact_sort** | [**ContactSort**](ContactSort.html) | information determining the order in which the contacts will be dialed | [optional] |
| **contact_sorts** | [**list[ContactSort]**](ContactSort.html) | column prioritized information determining the order in which the contacts will be dialed | [optional] |
| **no_answer_timeout** | **int** | for non-preview campaigns, how long to wait before dispositioning as &#39;no-answer&#39;, default 30 seconds | [optional] |
| **call_analysis_language** | **str** | The language the edge will use to analyse the call | [optional] |
| **priority** | **int** | The priority of this campaign relative to other campaigns | [optional] |
| **contact_list_filters** | [**list[UriReference]**](UriReference.html) | Filter defining a subset of contacts from the contact list to be dialed | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


