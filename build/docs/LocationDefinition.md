---
title: LocationDefinition
---
## LocationDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the Location. | |
| **contact_user** | [**AddressableEntityRef**](AddressableEntityRef.html) | Site contact for the location | [optional] |
| **emergency_number** | [**LocationEmergencyNumber**](LocationEmergencyNumber.html) |  | [optional] |
| **address** | [**LocationAddress**](LocationAddress.html) |  | [optional] |
| **address_verified** | **bool** |  | [optional] |
| **state** | **str** | Current activity status of the location. | [optional] |
| **notes** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |
| **path** | **list[str]** | A list of ancestor IDs in order | [optional] |
| **profile_image** | [**list[LocationImage]**](LocationImage.html) | Profile image set for the location | [optional] |
| **floorplan_image** | [**list[LocationImage]**](LocationImage.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


