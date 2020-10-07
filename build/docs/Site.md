---
title: Site
---
## Site

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** | The resource&#39;s description. | [optional] |
| **version** | **int** | The current version of the resource. | [optional] |
| **date_created** | **datetime** | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the resource. | [optional] |
| **created_by** | **str** | The ID of the user that created the resource. | [optional] |
| **state** | **str** | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the resource. | [optional] |
| **created_by_app** | **str** | The application that created the resource. | [optional] |
| **primary_sites** | [**list[DomainEntityRef]**](DomainEntityRef.html) |  | [optional] |
| **secondary_sites** | [**list[DomainEntityRef]**](DomainEntityRef.html) |  | [optional] |
| **primary_edges** | [**list[Edge]**](Edge.html) |  | [optional] |
| **secondary_edges** | [**list[Edge]**](Edge.html) |  | [optional] |
| **addresses** | [**list[Contact]**](Contact.html) |  | [optional] |
| **edges** | [**list[Edge]**](Edge.html) |  | [optional] |
| **edge_auto_update_config** | [**EdgeAutoUpdateConfig**](EdgeAutoUpdateConfig.html) | Recurrance rule, time zone, and start/end settings for automatic edge updates for this site | [optional] |
| **media_regions_use_latency_based** | **bool** |  | [optional] |
| **location** | [**LocationDefinition**](LocationDefinition.html) | Location | |
| **managed** | **bool** |  | [optional] |
| **ntp_settings** | [**NTPSettings**](NTPSettings.html) | Network Time Protocol settings for the site | [optional] |
| **core_site** | **bool** | The core site | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


