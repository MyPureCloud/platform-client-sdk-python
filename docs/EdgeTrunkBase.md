# EdgeTrunkBase

## EdgeTrunkBase

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
| **trunk_metabase** | [DomainEntityRef](DomainEntityRef) | The meta-base this trunk is based on. | |
| **properties** | dict(str, object) |  | [optional] |
| **trunk_type** | str | The type of this trunk base. | |
| **site** | [DomainEntityRef](DomainEntityRef) | Used to determine the media regions for inbound and outbound calls through a trunk. Also determines the dial plan to use for calls that came in on a trunk and have to be sent out on it as well. | [optional] |
| **inbound_site** | [DomainEntityRef](DomainEntityRef) | Allows a customer to set the site to which inbound calls will be routed | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 234.0.0_
