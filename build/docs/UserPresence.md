---
title: UserPresence
---
## UserPresence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **source** | **str** | Represents the source where the Presence was set. Some examples are: PURECLOUD, LYNC, OUTLOOK, etc. | [optional] |
| **primary** | **bool** | A boolean used to tell whether or not to set this presence source as the primary on a PATCH | [optional] |
| **presence_definition** | [**PresenceDefinition**](PresenceDefinition.html) |  | [optional] |
| **message** | **str** |  | [optional] |
| **modified_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


