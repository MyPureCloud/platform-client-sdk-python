# LocationDefinition

## LocationDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **contact_user** | [AddressableEntityRef](AddressableEntityRef) | Site contact for the location entity | [optional] |
| **emergency_number** | [LocationEmergencyNumber](LocationEmergencyNumber) | Emergency number for the location entity | [optional] |
| **address** | [LocationAddress](LocationAddress) |  | [optional] |
| **state** | str | Current state of the location entity | [optional] |
| **notes** | str | Notes for the location entity | [optional] |
| **version** | int | Current version of the location entity, value to be supplied should be retrieved by a GET or on create/update response | [optional] |
| **path** | list[str] | A list of ancestor IDs in order | [optional] |
| **profile_image** | [list[LocationImage]](LocationImage) | Profile image of the location entity, retrieved with ?expand&#x3D;images query parameter | [optional] |
| **floorplan_image** | [list[LocationImage]](LocationImage) | Floorplan images of the location entity, retrieved with ?expand&#x3D;images query parameter | [optional] |
| **address_verification_details** | [LocationAddressVerificationDetails](LocationAddressVerificationDetails) | Address verification information, retrieve dwith the ?expand&#x3D;addressVerificationDetails query parameter | [optional] |
| **address_verified** | bool | Boolean field which states if the address has been verified as an actual address | [optional] |
| **address_stored** | bool | Boolean field which states if the address has been stored for E911 | [optional] |
| **images** | str |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
