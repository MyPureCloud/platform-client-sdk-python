# Edge

## Edge

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
| **interfaces** | [list[EdgeInterface]](EdgeInterface) | The list of interfaces for the edge. (Deprecated) Replaced by configuring trunks/ip info on the logical interface instead | [optional] |
| **make** | str |  | [optional] |
| **model** | str |  | [optional] |
| **api_version** | str |  | [optional] |
| **software_version** | str |  | [optional] |
| **software_version_timestamp** | str |  | [optional] |
| **software_version_platform** | str |  | [optional] |
| **software_version_configuration** | str |  | [optional] |
| **full_software_version** | str |  | [optional] |
| **pairing_id** | str | The pairing Id for a hardware Edge in the format: 00000-00000-00000-00000-00000. This field is only required when creating an Edge with a deployment type of HARDWARE. | [optional] |
| **fingerprint** | str |  | [optional] |
| **fingerprint_hint** | str |  | [optional] |
| **current_version** | str |  | [optional] |
| **staged_version** | str |  | [optional] |
| **patch** | str |  | [optional] |
| **status_code** | str | The current status of the Edge. | [optional] |
| **edge_group** | [EdgeGroup](EdgeGroup) |  | [optional] |
| **site** | [Site](Site) | The Site to which the Edge is assigned. | [optional] |
| **software_status** | [DomainEdgeSoftwareUpdateDto](DomainEdgeSoftwareUpdateDto) | Details about an in-progress or recently in-progress Edge software upgrade. This node appears only if a software upgrade was recently initiated for this Edge. | [optional] |
| **online_status** | str |  | [optional] |
| **serial_number** | str |  | [optional] |
| **physical_edge** | bool |  | [optional] |
| **managed** | bool |  | [optional] |
| **edge_deployment_type** | str |  | [optional] |
| **cert_type** | str | The type of certificate used to communicate with edge-proxy. | [optional] |
| **call_draining_state** | str | The current state of the Edge&#39;s call draining process before it can be safely rebooted or updated. | [optional] |
| **conversation_count** | int | The remaining number of conversations the Edge has to drain before it can be safely rebooted or updated. When an Edge is not draining conversations, this will be NULL or 0. | [optional] |
| **proxy** | str | Edge HTTP proxy configuration for the WAN port. The field can be a hostname, FQDN, IPv4 or IPv6 address. If port is not included, port 80 is assumed. | [optional] |
| **offline_config_called** | bool | True if the offline edge configuration endpoint has been called for this edge. | [optional] |
| **os_name** | str | The name provided by the operating system of the Edge. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
