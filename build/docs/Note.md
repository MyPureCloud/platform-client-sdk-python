---
title: Note
---
## Note

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **entity_id** | **str** | The id of the contact or organization to which this note refers. This only needs to be set for input when using the Bulk APIs. | [optional] |
| **entity_type** | **str** | This is only need to be set when using Bulk API. Using any other value than contact or organization will result in null being used. | [optional] |
| **note_text** | **str** |  | [optional] |
| **modify_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **create_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**User**](User.html) | When creating or updating a note, only User.id is required. User object is fully populated when expanding a note. | |
| **external_data_sources** | [**list[ExternalDataSource]**](ExternalDataSource.html) | Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


