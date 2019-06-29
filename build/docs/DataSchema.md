---
title: DataSchema
---
## DataSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **version** | **int** | The schema&#39;s version, a positive integer. Required for updates. | |
| **applies_to** | **list[str]** | The PureCloud data this schema extends. | [optional] |
| **enabled** | **bool** | The schema&#39;s current enabled/disabled status. A disabled schema cannot be assigned to any other objects, but the data on those objects from the schemas still exists | [optional] |
| **deleted** | **bool** | The schema&#39;s deleted status. A deleted schema can not be used by any records or updated. All records using a deleted schema will eventually have their schema-based data removed. | [optional] |
| **created_by** | [**UriReference**](UriReference.html) | The user that created this schema. | [optional] |
| **date_created** | **datetime** | The date and time this schema was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **json_schema** | [**JsonSchemaDocument**](JsonSchemaDocument.html) | The JSON schema defining the data extension. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


