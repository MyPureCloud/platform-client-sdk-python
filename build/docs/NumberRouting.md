# NumberRouting

## NumberRouting

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **number_id** | str | Phone number Id that has a disaster recovery linking | [optional] |
| **owner_organization_id** | str | Owner organization of numberId | [optional] |
| **carrier_code** | str | Code that indicates which carrier manages the number ie. VERIZON | [optional] |
| **pending_organization_id** | str | OrganizationId where the number will be routed to during a change routing event | [optional] |
| **region** | str | The current region where the number is located | [optional] |
| **status** | str | The current status of the number routing | [optional] |
| **active_organization_id** | str | The orgId where the number is currently routing to | [optional] |
| **linked_organization_ids** | list[str] | List of linked organizations ids | [optional] |



_PureCloudPlatformClientV2 260.0.0_
