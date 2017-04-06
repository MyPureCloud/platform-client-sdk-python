---
title: CampaignSequence
---
## CampaignSequence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **campaigns** | [**list[UriReference]**](UriReference.html) | the ordered list of campaign identifiers | |
| **current_campaign** | **int** | the zero-based index of the current campaign in the campaigns list | |
| **status** | **str** | status of the sequence | |
| **stop_message** | **str** | if a sequence has unexpectedly stopped, this message provides the reason | [optional] |
| **repeat** | **bool** | indicates if a sequence is to repeat from the beginning after the last campaign completes; default is false | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


