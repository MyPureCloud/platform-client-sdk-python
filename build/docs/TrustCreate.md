---
title: TrustCreate
---
## TrustCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **pairing_id** | **str** | The pairing Id created by the trustee. This is required to prove that the trustee agrees to the relationship. | |
| **enabled** | **bool** | If disabled no trustee user will have access, even if they were previously added. | |
| **users** | [**list[TrustMemberCreate]**](TrustMemberCreate.html) | The list of users and their roles to which access will be granted. The users are from the trustee and the roles are from the trustor. If no users are specified, at least one group is required. | [optional] |
| **groups** | [**list[TrustMemberCreate]**](TrustMemberCreate.html) | The list of groups and their roles to which access will be granted. The groups are from the trustee and the roles are from the trustor. If no groups are specified, at least one user is required. | [optional] |
{: class="table table-striped"}


