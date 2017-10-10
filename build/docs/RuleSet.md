---
title: RuleSet
---
## RuleSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the RuleSet. | |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [**UriReference**](UriReference.html) | A ContactList to provide user-interface suggestions for contact columns on relevant conditions and actions. | [optional] |
| **queue** | [**UriReference**](UriReference.html) | A Queue to provide user-interface suggestions for wrap-up codes on relevant conditions and actions. | [optional] |
| **rules** | [**list[DialerRule]**](DialerRule.html) | The list of rules. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


