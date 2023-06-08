---
title: WorkbinVersion
---
## WorkbinVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Workbin name | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **description** | **str** | Workbin description | [optional] |
| **date_created** | **datetime** | The creation date of the Workbin. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | The modified date of the Workbin. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The id of the User who modified the Workbin. | [optional] |
| **version** | **int** | Version | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


