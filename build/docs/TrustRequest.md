# TrustRequest

## TrustRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **created_by** | [OrgUser](OrgUser) | User who created this request. | [optional] |
| **date_created** | datetime | Date request was created. There is a 48 hour expiration on all requests. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **trustee** | [Organization](Organization) | Trustee organization who generated this request. | |
| **users** | [list[OrgUser]](OrgUser) | The list of trustee users that are requesting access. | [optional] |
| **groups** | [list[TrustGroup]](TrustGroup) | The list of trustee groups that are requesting access. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 216.0.0_
