---
title: CampaignSequence
---
## CampaignSequence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **campaigns** | [**list[DomainEntityRef]**](DomainEntityRef.html) | The ordered list of Campaigns that this CampaignSequence will run. | |
| **current_campaign** | **int** | A zero-based index indicating which Campaign this CampaignSequence is currently on. | |
| **status** | **str** | The current status of the CampaignSequence. A CampaignSequence can be turned &#39;on&#39; or &#39;off&#39;. | |
| **stop_message** | **str** | A message indicating if and why a CampaignSequence has stopped unexpectedly. | [optional] |
| **repeat** | **bool** | Indicates if a sequence should repeat from the beginning after the last campaign completes. Default is false. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


