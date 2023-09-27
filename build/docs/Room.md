---
title: Room
---
## Room

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The jid of the room | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Room&#39;s created time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **room_type** | **str** | The type of room | [optional] |
| **description** | **str** | Room&#39;s description | [optional] |
| **subject** | **str** | Room&#39;s subject | [optional] |
| **participant_limit** | **int** | Room&#39;s size limit | [optional] |
| **owners** | [**list[UserReference]**](UserReference.html) | Room&#39;s owners | [optional] |
| **pinned_messages** | [**list[AddressableEntityRef]**](AddressableEntityRef.html) | Room&#39;s pinned messages | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


