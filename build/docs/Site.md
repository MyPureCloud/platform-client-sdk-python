# Site

## Site

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
| **primary_sites** | [list[DomainEntityRef]](DomainEntityRef) |  | [optional] |
| **secondary_sites** | [list[DomainEntityRef]](DomainEntityRef) |  | [optional] |
| **primary_edges** | [list[Edge]](Edge) |  | [optional] |
| **secondary_edges** | [list[Edge]](Edge) |  | [optional] |
| **addresses** | [list[Contact]](Contact) |  | [optional] |
| **edges** | [list[Edge]](Edge) |  | [optional] |
| **edge_auto_update_config** | [EdgeAutoUpdateConfig](EdgeAutoUpdateConfig) | Recurrance rule, time zone, and start/end settings for automatic edge updates for this site | [optional] |
| **media_regions_use_latency_based** | bool |  | [optional] |
| **location** | [LocationDefinition](LocationDefinition) | Location | |
| **managed** | bool |  | [optional] |
| **ntp_settings** | [NTPSettings](NTPSettings) | Network Time Protocol settings for the site | [optional] |
| **media_model** | str | Media model for the site | [optional] |
| **core_site** | bool | Is this site a core site | [optional] |
| **site_connections** | [list[SiteConnection]](SiteConnection) | The site connections | [optional] |
| **media_regions** | list[str] | The ordered list of AWS regions through which media can stream. | [optional] |
| **caller_id** | str | The caller ID value for the site. | [optional] |
| **caller_name** | str | The caller name for the site. | [optional] |
| **cloud_proxy_force_turn** | bool | Enables premises Edge Force Turn  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 218.0.0_
