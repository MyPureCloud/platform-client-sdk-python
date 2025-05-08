# CreateShareResponse

## CreateShareResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **shared_entity_type** | str |  | [optional] |
| **shared_entity** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **member_type** | str |  | [optional] |
| **member** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **shared_by** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **workspace** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **succeeded** | [list[Share]](Share) |  | [optional] |
| **failed** | [list[Share]](Share) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_
