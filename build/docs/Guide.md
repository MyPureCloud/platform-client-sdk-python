# Guide

## Guide

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the guide. | [optional] |
| **status** | str | The status of the guide. | [optional] |
| **source** | str | Indicates how the guide content was generated. | [optional] |
| **date_created** | datetime | The date and time the guide was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date and time the guide was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **latest_saved_version** | [GuideVersionRef](GuideVersionRef) | The latest saved version of the guide. | [optional] |
| **latest_production_ready_version** | [GuideVersionRef](GuideVersionRef) | The latest production ready version of the guide. | [optional] |



_PureCloudPlatformClientV2 237.0.0_
