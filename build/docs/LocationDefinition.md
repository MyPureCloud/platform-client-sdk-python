---
title: LocationDefinition
---
## LocationDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the Location. | |
| **address** | [**LocationAddress**](LocationAddress.html) |  | [optional] |
| **address_verified** | **bool** |  | [optional] |
| **emergency_number** | [**LocationEmergencyNumber**](LocationEmergencyNumber.html) |  | [optional] |
| **state** | **str** | Current activity status of the location. | [optional] |
| **version** | **int** |  | [optional] |
| **path** | **list[str]** |  | [optional] |
| **notes** | **str** |  | [optional] |
| **profile_image** | [**list[LocationImage]**](LocationImage.html) | Profile image set for the location | [optional] |
| **floorplan_image** | [**list[LocationImage]**](LocationImage.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


