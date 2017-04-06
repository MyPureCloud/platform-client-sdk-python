---
title: RuleSet
---
## RuleSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [**UriReference**](UriReference.html) | The identifier of an example contact list that provides user-interface suggestions for contact-based conditions and actions | [optional] |
| **queue** | [**UriReference**](UriReference.html) | The identifier of an example queue that provides user-interface suggestions for wrap-up associated conditions | [optional] |
| **rules** | [**list[DialerRule]**](DialerRule.html) | The list of rules | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


