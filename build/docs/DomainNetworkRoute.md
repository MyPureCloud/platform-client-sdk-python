# DomainNetworkRoute

## DomainNetworkRoute

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **prefix** | str | The IPv4 or IPv6 route prefix in CIDR notation. | [optional] |
| **nexthop** | str | The IPv4 or IPv6 nexthop IP address. | [optional] |
| **persistent** | bool | True if this route will persist on Edge restart.  Routes assigned by DHCP will be returned as false. | [optional] |
| **metric** | int | The metric being used for route. Lower values will have a higher priority. | [optional] |
| **family** | int | The address family for this route. | [optional] |



_PureCloudPlatformClientV2 219.1.0_
