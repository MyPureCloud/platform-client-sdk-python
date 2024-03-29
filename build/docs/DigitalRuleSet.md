---
title: DigitalRuleSet
---
## DigitalRuleSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [**DomainEntityRef**](DomainEntityRef.html) | A ContactList to provide suggestions for contact columns on relevant conditions and actions. | [optional] |
| **rules** | [**list[DigitalRule]**](DigitalRule.html) | The list of rules. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


