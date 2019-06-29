---
title: ManagementUnit
---
## ManagementUnit

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **business_unit** | [**BusinessUnitReference**](BusinessUnitReference.html) | The business unit to which this management unit belongs | [optional] |
| **start_day_of_week** | **str** | Start day of week for scheduling and forecasting purposes | [optional] |
| **time_zone** | **str** | The time zone for the management unit in standard Olson Format (See https://en.wikipedia.org/wiki/Tz_database) | [optional] |
| **settings** | [**ManagementUnitSettings**](ManagementUnitSettings.html) | The configuration settings for this management unit | [optional] |
| **version** | **int** | The version of the underlying entity.  Deprecated, use metadata field instead | |
| **date_modified** | **datetime** | The date and time at which this entity was last modified.  Deprecated, use metadata field instead. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The user who last modified this entity.  Deprecated, use metadata field instead | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version info metadata for this management unit | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


