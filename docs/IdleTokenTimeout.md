# IdleTokenTimeout

## IdleTokenTimeout

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **idle_token_timeout_seconds** | int | Token timeout length in seconds. Must be at least 5 minutes and 8 hours or less (if HIPAA is disabled) or 15 minutes or less (if HIPAA is enabled). | [optional] |
| **enable_idle_token_timeout** | bool | Indicates whether the Token Timeout should be enabled or disabled. | [optional] |
| **inactivity_timeout_unit** | str | The unit for the inactivity timeout (MINUTES or HOURS). | [optional] |
| **inactivity_timeout_groups_enabled** | bool | Indicates whether inactivity timeout groups are enabled. | [optional] |
| **inactivity_timeout_group_bundles** | [list[InactivityTimeoutGroupBundle]](InactivityTimeoutGroupBundle) | Group bundle configuration for inactivity timeout. | [optional] |



_PureCloudPlatformClientV2 252.0.0_
