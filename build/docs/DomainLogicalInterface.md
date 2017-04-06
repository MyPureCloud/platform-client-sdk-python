---
title: DomainLogicalInterface
---
## DomainLogicalInterface

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** |  | [optional] |
| **created_by** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **modified_by_app** | **str** |  | [optional] |
| **created_by_app** | **str** |  | [optional] |
| **edge_uri** | **str** |  | [optional] |
| **edge_assigned_id** | **str** |  | [optional] |
| **friendly_name** | **str** | Friendly Name | |
| **vlan_tag_id** | **int** |  | [optional] |
| **hardware_address** | **str** | Hardware Address | |
| **physical_adapter_id** | **str** | Physical Adapter Id | |
| **if_status** | **str** |  | [optional] |
| **interface_type** | **str** | The type of this network interface. | [optional] |
| **routes** | [**list[DomainNetworkRoute]**](DomainNetworkRoute.html) | The list of routes assigned to this interface. | [optional] |
| **addresses** | [**list[DomainNetworkAddress]**](DomainNetworkAddress.html) | The list of IP addresses on this interface.  Priority of dns addresses are based on order in the list. | [optional] |
| **ipv4_capabilities** | [**DomainCapabilities**](DomainCapabilities.html) | IPv4 interface settings. | [optional] |
| **ipv6_capabilities** | [**DomainCapabilities**](DomainCapabilities.html) | IPv6 interface settings. | [optional] |
| **current_state** | **str** |  | [optional] |
| **last_modified_user_id** | **str** |  | [optional] |
| **last_modified_correlation_id** | **str** |  | [optional] |
| **command_responses** | [**list[DomainNetworkCommandResponse]**](DomainNetworkCommandResponse.html) |  | [optional] |
| **inherit_phone_trunk_bases_i_pv4** | **bool** | The IPv4 phone trunk base assignment will be inherited from the Edge Group. | [optional] |
| **inherit_phone_trunk_bases_i_pv6** | **bool** | The IPv6 phone trunk base assignment will be inherited from the Edge Group. | [optional] |
| **use_for_internal_edge_communication** | **bool** | This interface will be used for all internal edge-to-edge communication using settings from the edgeTrunkBaseAssignment on the Edge Group. | [optional] |
| **external_trunk_base_assignments** | [**list[TrunkBaseAssignment]**](TrunkBaseAssignment.html) | External trunk base settings to use for external communication from this interface. | [optional] |
| **phone_trunk_base_assignments** | [**list[TrunkBaseAssignment]**](TrunkBaseAssignment.html) | Phone trunk base settings to use for phone communication from this interface.  These settings will be ignored when \&quot;inheritPhoneTrunkBases\&quot; is true. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


