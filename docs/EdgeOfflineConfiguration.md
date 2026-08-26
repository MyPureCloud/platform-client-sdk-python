# EdgeOfflineConfiguration

## EdgeOfflineConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **pairing_id** | str | The pairingId for your hardware Edge in the format: 00000-00000-00000-00000-00000. | |
| **network** | [EdgeOfflineConfigurationNetwork](EdgeOfflineConfigurationNetwork) | Network settings for your hardware Edge. | |
| **use_verification_code** | bool | Boolean to know if the verification code will be used to provision the Edge. Only used if the Edge is being provisioned. | [optional] |
| **cert_type** | str | The type of Certificate Authority this Edge will use. Defaults to NotRequested if the Edge is already provisioned. PureCloud signed CA is recommended. Public CA signed by a trusted third party. China CA must be used if the Site&#39;s Location is in China. | [optional] |
| **site** | [DomainEntityRef](DomainEntityRef) | The Site that will be associated to the Edge. Required if the Edge is being provisioned. | [optional] |
| **proxy** | str | Edge HTTP proxy configuration for the WAN port. The field can be a hostname, FQDN, IPv4 or IPv6 address. If port is not included, port 80 is assumed. | [optional] |



_PureCloudPlatformClientV2 265.0.0_
