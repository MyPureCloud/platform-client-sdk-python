---
title: Trustor
---
## Trustor

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Organization Id for this trust. | [optional] |
| **enabled** | **bool** | If disabled no trustee user will have access, even if they were previously added. | |
| **date_created** | **datetime** | Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **created_by** | [**OrgUser**](OrgUser.html) | User that created trust. | [optional] |
| **organization** | [**Organization**](Organization.html) | Organization associated with this trust. | [optional] |
| **authorization** | [**TrusteeAuthorization**](TrusteeAuthorization.html) | Authorization for the trustee user has in this trustor organization | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


