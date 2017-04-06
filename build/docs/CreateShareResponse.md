---
title: CreateShareResponse
---
## CreateShareResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **shared_entity_type** | **str** |  | [optional] |
| **shared_entity** | [**UriReference**](UriReference.html) |  | [optional] |
| **member_type** | **str** |  | [optional] |
| **member** | [**UriReference**](UriReference.html) |  | [optional] |
| **shared_by** | [**UriReference**](UriReference.html) |  | [optional] |
| **workspace** | [**UriReference**](UriReference.html) |  | [optional] |
| **succeeded** | [**list[Share]**](Share.html) |  | [optional] |
| **failed** | [**list[Share]**](Share.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


