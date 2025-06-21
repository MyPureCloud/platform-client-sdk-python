# DIDNumber

## DIDNumber

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **number** | str | The number of the DID formatted as E164. | [optional] |
| **assigned** | bool | True if this DID is assigned to an entity.  False otherwise. | [optional] |
| **did_pool** | [AddressableEntityRef](AddressableEntityRef) | A Uri reference to the DID Pool this DID is a part of. | [optional] |
| **owner** | [DomainEntityRef](DomainEntityRef) | A Uri reference to the owner of this DID.  The owner&#39;s type can be found in ownerType.  If the DID is unassigned, this will be NULL. | [optional] |
| **owner_type** | str | The type of the entity that owns this DID.  If the DID is unassigned, this will be NULL. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 231.0.0_
