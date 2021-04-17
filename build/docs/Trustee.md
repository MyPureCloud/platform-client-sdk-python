---
title: Trustee
---
## Trustee

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Organization Id for this trust. | [optional] |
| **enabled** | **bool** | If disabled no trustee user will have access, even if they were previously added. | |
| **uses_default_role** | **bool** | Denotes if trustee uses admin role by default. | [optional] |
| **date_created** | **datetime** | Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**OrgUser**](OrgUser.html) | User that created trust. | [optional] |
| **organization** | [**Organization**](Organization.html) | Organization associated with this trust. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


