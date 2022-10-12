---
title: MessagingCampaign
---
## MessagingCampaign

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **division** | [**DomainEntityRef**](DomainEntityRef.html) | The division this entity belongs to. | [optional] |
| **campaign_status** | **str** | The current status of the messaging campaign. A messaging campaign may be turned &#39;on&#39; or &#39;off&#39;. | [optional] |
| **callable_time_set** | [**DomainEntityRef**](DomainEntityRef.html) | The callable time set for this messaging campaign. | [optional] |
| **contact_list** | [**DomainEntityRef**](DomainEntityRef.html) | The contact list that this messaging campaign will send messages for. | |
| **dnc_lists** | [**list[DomainEntityRef]**](DomainEntityRef.html) | The dnc lists to check before sending a message for this messaging campaign. | [optional] |
| **always_running** | **bool** | Whether this messaging campaign is always running | [optional] |
| **contact_sorts** | [**list[ContactSort]**](ContactSort.html) | The order in which to sort contacts for dialing, based on up to four columns. | [optional] |
| **messages_per_minute** | **int** | How many messages this messaging campaign will send per minute. | |
| **rule_sets** | [**list[DomainEntityRef]**](DomainEntityRef.html) | Rule Sets to be applied while this campaign is sending messages | [optional] |
| **contact_list_filters** | [**list[DomainEntityRef]**](DomainEntityRef.html) | The contact list filter to check before sending a message for this messaging campaign. | [optional] |
| **errors** | [**list[RestErrorDetail]**](RestErrorDetail.html) | A list of current error conditions associated with this messaging campaign. | [optional] |
| **email_config** | [**EmailConfig**](EmailConfig.html) | Configuration for this messaging campaign to send Email messages. | [optional] |
| **sms_config** | [**SmsConfig**](SmsConfig.html) | Configuration for this messaging campaign to send SMS messages. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


