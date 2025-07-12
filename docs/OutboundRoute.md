# OutboundRoute

## OutboundRoute

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
| **classification_types** | list[str] | The site associated to the outbound route. | |
| **enabled** | bool |  | [optional] |
| **distribution** | str |  | [optional] |
| **external_trunk_bases** | [list[DomainEntityRef]](DomainEntityRef) | Trunk base settings of trunkType \&quot;EXTERNAL\&quot;.  This base must also be set on an edge logical interface for correct routing. | [optional] |
| **site** | [Site](Site) | The site associated to the outbound route. | [optional] |
| **managed** | bool | Is this outbound route being managed remotely. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
