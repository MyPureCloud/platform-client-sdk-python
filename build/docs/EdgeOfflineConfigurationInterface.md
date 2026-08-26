# EdgeOfflineConfigurationInterface

## EdgeOfflineConfigurationInterface

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **routes** | [list[DomainNetworkRoute]](DomainNetworkRoute) | The list of routes assigned to this interface. | [optional] |
| **addresses** | [list[DomainNetworkAddress]](DomainNetworkAddress) | The list of IP addresses on this interface.  Priority of dns addresses are based on order in the list. | [optional] |
| **ipv4_capabilities** | [DomainCapabilities](DomainCapabilities) | IPv4 interface settings. | [optional] |
| **ipv6_capabilities** | [DomainCapabilities](DomainCapabilities) | IPv6 interface settings. | [optional] |



_PureCloudPlatformClientV2 265.0.0_
