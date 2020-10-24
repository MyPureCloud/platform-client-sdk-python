---
title: ActionTarget
---
## ActionTarget

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **user_data** | [**list[KeyValue]**](KeyValue.html) | Additional user data associated with the target in key/value format. | [optional] |
| **supported_media_types** | **list[str]** | Supported media types of the target. | [optional] |
| **state** | **str** | Indicates the state of the target. | [optional] |
| **description** | **str** | Description of the target. | [optional] |
| **service_level** | [**ServiceLevel**](ServiceLevel.html) | Service Level of the action target. Chat offers for the target will be throttled with the aim of achieving this service level. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | The date the target was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_date** | **datetime** | The date the target was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


