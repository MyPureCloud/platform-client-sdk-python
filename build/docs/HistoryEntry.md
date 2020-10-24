---
title: HistoryEntry
---
## HistoryEntry

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **action** | **str** | The action performed | [optional] |
| **resource** | **str** | For actions performed not on the item itself, but on a sub-item, this field identifies the sub-item by name.  For example, for actions performed on prompt resources, this will be the prompt resource name. | [optional] |
| **timestamp** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **user** | [**User**](User.html) | User associated with this entry. | [optional] |
| **client** | [**DomainEntityRef**](DomainEntityRef.html) | OAuth client associated with this entry. | [optional] |
| **version** | **str** |  | [optional] |
| **secure** | **bool** |  | [optional] |
{: class="table table-striped"}


