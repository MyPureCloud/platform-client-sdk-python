---
title: UcUserPresence
---
## UcUserPresence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **user_id** | **str** | User ID of the associated Genesys Cloud user. | [optional] |
| **source** | **str** | Represents the source where the Presence was set. Some examples are: PURECLOUD, MICROSOFTTEAMS, ZOOMPHONE, etc. | [optional] |
| **presence_definition** | [**PresenceDefinition**](PresenceDefinition.html) |  | [optional] |
| **message** | **str** |  | [optional] |
| **modified_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


