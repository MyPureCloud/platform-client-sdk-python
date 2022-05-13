---
title: LocationDefinition
---
## LocationDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **contact_user** | [**AddressableEntityRef**](AddressableEntityRef.html) | Site contact for the location entity | [optional] |
| **emergency_number** | [**LocationEmergencyNumber**](LocationEmergencyNumber.html) | Emergency number for the location entity | [optional] |
| **address** | [**LocationAddress**](LocationAddress.html) |  | [optional] |
| **state** | **str** | Current state of the location entity | [optional] |
| **notes** | **str** | Notes for the location entity | [optional] |
| **version** | **int** | Current version of the location entity, value to be supplied should be retrieved by a GET or on create/update response | [optional] |
| **path** | **list[str]** | A list of ancestor IDs in order | [optional] |
| **profile_image** | [**list[LocationImage]**](LocationImage.html) | Profile image of the location entity, retrieved with ?expand&#x3D;images query parameter | [optional] |
| **floorplan_image** | [**list[LocationImage]**](LocationImage.html) | Floorplan images of the location entity, retrieved with ?expand&#x3D;images query parameter | [optional] |
| **address_verification_details** | [**LocationAddressVerificationDetails**](LocationAddressVerificationDetails.html) | Address verification information, retrieve dwith the ?expand&#x3D;addressVerificationDetails query parameter | [optional] |
| **address_verified** | **bool** | Boolean field which states if the address has been verified as an actual address | [optional] |
| **address_stored** | **bool** | Boolean field which states if the address has been stored for E911 | [optional] |
| **images** | **str** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


