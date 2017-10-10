---
title: CampaignNotification
---
## CampaignNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** |  | [optional] |
| **date_modified** | **datetime** |  | [optional] |
| **version** | **int** |  | [optional] |
| **contact_list** | [**DocumentDataV2NotificationCreatedBy**](DocumentDataV2NotificationCreatedBy.html) |  | [optional] |
| **queue** | [**CampaignNotificationUriReference**](CampaignNotificationUriReference.html) |  | [optional] |
| **dialing_mode** | **str** |  | [optional] |
| **script** | [**CampaignNotificationUriReference**](CampaignNotificationUriReference.html) |  | [optional] |
| **edge_group** | [**CampaignNotificationUriReference**](CampaignNotificationUriReference.html) |  | [optional] |
| **site** | [**CampaignNotificationUriReference**](CampaignNotificationUriReference.html) |  | [optional] |
| **campaign_status** | **str** |  | [optional] |
| **phone_columns** | [**list[CampaignNotificationPhoneColumns]**](CampaignNotificationPhoneColumns.html) |  | [optional] |
| **abandon_rate** | **float** |  | [optional] |
| **dnc_lists** | [**list[CampaignNotificationUriReference]**](CampaignNotificationUriReference.html) |  | [optional] |
| **callable_time_set** | [**CampaignNotificationUriReference**](CampaignNotificationUriReference.html) |  | [optional] |
| **call_analysis_response_set** | [**CampaignNotificationUriReference**](CampaignNotificationUriReference.html) |  | [optional] |
| **caller_name** | **str** |  | [optional] |
| **caller_address** | **str** |  | [optional] |
| **outbound_line_count** | **int** |  | [optional] |
| **errors** | [**list[CampaignNotificationErrors]**](CampaignNotificationErrors.html) |  | [optional] |
| **rule_sets** | [**list[CampaignNotificationUriReference]**](CampaignNotificationUriReference.html) |  | [optional] |
| **skip_preview_disabled** | **bool** |  | [optional] |
| **preview_time_out_seconds** | **int** |  | [optional] |
| **single_number_preview** | **bool** |  | [optional] |
| **contact_sort** | [**CampaignNotificationContactSort**](CampaignNotificationContactSort.html) |  | [optional] |
| **contact_sorts** | [**list[CampaignNotificationContactSort]**](CampaignNotificationContactSort.html) |  | [optional] |
| **no_answer_timeout** | **int** |  | [optional] |
| **call_analysis_language** | **str** |  | [optional] |
| **priority** | **int** |  | [optional] |
| **contact_list_filters** | [**list[CampaignNotificationUriReference]**](CampaignNotificationUriReference.html) |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


