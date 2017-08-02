---
title: TrustRequest
---
## TrustRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **created_by** | [**OrgUser**](OrgUser.html) | User who created this request. | [optional] |
| **date_created** | **datetime** | Date request was created. There is a 48 hour expiration on all requests. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **trustee** | [**Organization**](Organization.html) | Trustee organization who generated this request. | |
| **users** | [**list[OrgUser]**](OrgUser.html) | The list of trustee users that are requesting access. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


