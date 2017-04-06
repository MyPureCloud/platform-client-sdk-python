---
title: EncryptionKey
---
## EncryptionKey

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **create_date** | **datetime** | create date of the key pair. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **keydata_summary** | **str** | key data summary (base 64 encoded public key) | [optional] |
| **user** | [**User**](User.html) | user that requested generation of public key | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


