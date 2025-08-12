# Trunk

## Trunk

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the entity. | |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **description** | str | The resource&#39;s description. | [optional] |
| **version** | int | The current version of the resource. | [optional] |
| **date_created** | datetime | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | str | The ID of the user that last modified the resource. | [optional] |
| **created_by** | str | The ID of the user that created the resource. | [optional] |
| **state** | str | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | str | The application that last modified the resource. | [optional] |
| **created_by_app** | str | The application that created the resource. | [optional] |
| **trunk_type** | str | The type of this trunk. | [optional] |
| **edge** | [DomainEntityRef](DomainEntityRef) | The Edge using this trunk. | [optional] |
| **trunk_base** | [DomainEntityRef](DomainEntityRef) | The trunk base configuration used on this trunk. | [optional] |
| **trunk_metabase** | [DomainEntityRef](DomainEntityRef) | The metabase used to create this trunk. | [optional] |
| **edge_group** | [DomainEntityRef](DomainEntityRef) | The edge group associated with this trunk. | [optional] |
| **in_service** | bool | True if this trunk is in-service.  This comes from the trunk_enabled property of the referenced trunk base. | [optional] |
| **enabled** | bool | True if the Edge used by this trunk is in-service | [optional] |
| **logical_interface** | [DomainEntityRef](DomainEntityRef) | The Logical Interface on the Edge to which the trunk is assigned. | [optional] |
| **connected_status** | [TrunkConnectedStatus](TrunkConnectedStatus) | The connected status of the trunk | [optional] |
| **options_status** | [list[TrunkMetricsOptions]](TrunkMetricsOptions) | The trunk optionsStatus | [optional] |
| **registers_status** | [list[TrunkMetricsRegisters]](TrunkMetricsRegisters) | The trunk registersStatus | [optional] |
| **ip_status** | [TrunkMetricsNetworkTypeIp](TrunkMetricsNetworkTypeIp) | The trunk ipStatus | [optional] |
| **options_enabled_status** | str | Returns Enabled when the trunk base supports the availability interval and it has a value greater than 0. | [optional] |
| **registers_enabled_status** | str | Returns Enabled when the trunk base supports the registration interval and it has a value greater than 0. | [optional] |
| **family** | int | The IP Network Family of the trunk | [optional] |
| **proxy_address_list** | list[str] | The list of proxy addresses (ports if provided) for the trunk | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.0.0_
