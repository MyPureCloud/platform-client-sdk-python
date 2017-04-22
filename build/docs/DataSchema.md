---
title: DataSchema
---
## DataSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **version** | **int** | The schema&#39;s version. Required for updates. | |
| **applies_to** | **list[str]** | The PureCloud data this schema extends. | [optional] |
| **created_by** | [**UriReference**](UriReference.html) | The user that created this schema. | [optional] |
| **date_created** | **datetime** | The date and time this schema was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **json_schema** | [**JsonSchemaDocument**](JsonSchemaDocument.html) | The JSON schema defining the data extension. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


