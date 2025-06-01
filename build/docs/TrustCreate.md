# TrustCreate

## TrustCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **pairing_id** | str | The pairing Id created by the trustee. This is required to prove that the trustee agrees to the relationship.  Not required when creating a default pairing with Customer Care. | [optional] |
| **enabled** | bool | If disabled no trustee user will have access, even if they were previously added. | |
| **users** | [list[TrustMemberCreate]](TrustMemberCreate) | The list of users and their roles to which access will be granted. The users are from the trustee and the roles are from the trustor. If no users are specified, at least one group is required. | [optional] |
| **groups** | [list[TrustMemberCreate]](TrustMemberCreate) | The list of groups and their roles to which access will be granted. The groups are from the trustee and the roles are from the trustor. If no groups are specified, at least one user is required. | [optional] |
| **date_expired** | datetime | The expiration date of the trust. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 230.0.0_
