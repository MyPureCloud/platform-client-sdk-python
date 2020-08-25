---
title: AvailableTopic
---
## AvailableTopic

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | **str** |  | [optional] |
| **id** | **str** |  | [optional] |
| **requires_permissions** | **list[str]** | Permissions required to subscribe to the topic | [optional] |
| **schema** | **dict(str, object)** |  | [optional] |
| **requires_current_user** | **bool** | True if the topic user ID is required to match the subscribing user ID | [optional] |
| **requires_current_user_or_permission** | **bool** | True if permissions are only required when the topic user ID does not match the subscribing user ID | [optional] |
| **transports** | **list[str]** | Transports that support events for the topic | [optional] |
{: class="table table-striped"}


