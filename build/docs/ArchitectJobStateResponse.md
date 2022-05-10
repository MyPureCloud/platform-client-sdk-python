---
title: ArchitectJobStateResponse
---
## ArchitectJobStateResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **flow** | [**AddressableEntityRef**](AddressableEntityRef.html) | Flow created from the Architect Job | [optional] |
| **status** | **str** | Status of the Architect Job | [optional] |
| **command** | **str** | The command executed by the Architect Job | [optional] |
| **messages** | [**list[ArchitectJobMessage]**](ArchitectJobMessage.html) | Warnings and Errors messages of the Architect Job | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


