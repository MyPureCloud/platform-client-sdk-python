# DomainLogicalInterface

## DomainLogicalInterface

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
| **edge_uri** | str |  | [optional] |
| **edge_assigned_id** | str |  | [optional] |
| **friendly_name** | str | Friendly Name | |
| **vlan_tag_id** | int |  | [optional] |
| **hardware_address** | str | Hardware Address | |
| **physical_adapter_id** | str | Physical Adapter Id | |
| **if_status** | str |  | [optional] |
| **interface_type** | str | The type of this network interface. | [optional] |
| **public_nat_address_ip_v4** | str | IPv4 NENT IP Address | [optional] |
| **public_nat_address_ip_v6** | str | IPv6 NENT IP Address | [optional] |
| **routes** | [list[DomainNetworkRoute]](DomainNetworkRoute) | The list of routes assigned to this interface. | [optional] |
| **addresses** | [list[DomainNetworkAddress]](DomainNetworkAddress) | The list of IP addresses on this interface.  Priority of dns addresses are based on order in the list. | [optional] |
| **ipv4_capabilities** | [DomainCapabilities](DomainCapabilities) | IPv4 interface settings. | [optional] |
| **ipv6_capabilities** | [DomainCapabilities](DomainCapabilities) | IPv6 interface settings. | [optional] |
| **current_state** | str |  | [optional] |
| **last_modified_user_id** | str |  | [optional] |
| **last_modified_correlation_id** | str |  | [optional] |
| **command_responses** | [list[DomainNetworkCommandResponse]](DomainNetworkCommandResponse) |  | [optional] |
| **inherit_phone_trunk_bases_ipv4** | bool | The IPv4 phone trunk base assignment will be inherited from the Edge Group. | [optional] |
| **inherit_phone_trunk_bases_ipv6** | bool | The IPv6 phone trunk base assignment will be inherited from the Edge Group. | [optional] |
| **use_for_internal_edge_communication** | bool | This interface will be used for all internal edge-to-edge communication using settings from the edgeTrunkBaseAssignment on the Edge Group. | [optional] |
| **use_for_indirect_edge_communication** | bool | Site Interconnects using the \&quot;Indirect\&quot; method will communicate using the Public IP Address specified on the interface. Use this option when a NAT enabled firewall is between the Edge and the far end. | [optional] |
| **use_for_cloud_proxy_edge_communication** | bool | Site Interconnects using the \&quot;Cloud Proxy\&quot; method will broker the connection between them with a Cloud Proxy. This method is required for connections between one or more Sites using Cloud Media, but can optionally be used between two premises Sites if Direct or Indirect are not an option. | [optional] |
| **use_for_wan_interface** | bool | This interface will be used for all communication with the internet. | [optional] |
| **external_trunk_base_assignments** | [list[TrunkBaseAssignment]](TrunkBaseAssignment) | External trunk base settings to use for external communication from this interface. | [optional] |
| **phone_trunk_base_assignments** | [list[TrunkBaseAssignment]](TrunkBaseAssignment) | Phone trunk base settings to use for phone communication from this interface.  These settings will be ignored when \&quot;inheritPhoneTrunkBases\&quot; is true. | [optional] |
| **trace_enabled** | bool |  | [optional] |
| **start_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 215.0.0_
