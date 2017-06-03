---
title: ContactListFilter
---
## ContactListFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [**UriReference**](UriReference.html) | The contact list the filter is based on | |
| **clauses** | [**list[ContactListFilterClause]**](ContactListFilterClause.html) |  | [optional] |
| **filter_type** | **str** | The filter type tells the api how to compare between clauses | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


