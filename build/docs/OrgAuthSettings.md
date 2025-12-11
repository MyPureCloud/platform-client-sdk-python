# OrgAuthSettings

## OrgAuthSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **multifactor_authentication_required** | bool | Indicates whether multi-factor authentication is required. | [optional] |
| **domain_allowlist_enabled** | bool | Indicates whether the domain allowlist is enabled. | [optional] |
| **domain_allowlist** | list[str] | The list of domains that will be allowed to embed Genesys Cloud applications. | [optional] |
| **ip_address_allowlist** | list[str] | The list of IP addresses that will be allowed to authenticate with Genesys Cloud. | [optional] |
| **password_requirements** | [PasswordRequirements](PasswordRequirements) | The password requirements for the organization. | [optional] |
| **inactivity_timeout_exclusions** | list[str] | The list of exempt apis from inactivity timeout. | [optional] |



_PureCloudPlatformClientV2 246.0.0_
