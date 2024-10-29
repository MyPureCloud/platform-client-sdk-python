# Trustor

## Trustor

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Organization Id for this trust. | [optional] |
| **enabled** | bool | If disabled no trustee user will have access, even if they were previously added. | |
| **date_created** | datetime | Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [OrgUser](OrgUser) | User that created trust. | [optional] |
| **organization** | [Organization](Organization) | Organization associated with this trust. | [optional] |
| **authorization** | [TrusteeAuthorization](TrusteeAuthorization) | Authorization for the trustee user has in this trustor organization | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 215.0.0_
