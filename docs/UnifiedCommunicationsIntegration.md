# UnifiedCommunicationsIntegration

## UnifiedCommunicationsIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **uc_integration_key** | [AddressableEntityRef](AddressableEntityRef) | ucIntegrationKey | |
| **integration_presence_source** | str | integrationPresenceType | |
| **pbx_permission** | str | pbxPermission | |
| **icon** | [UCIcon](UCIcon) | icon | |
| **badge_icons** | [dict(str, UCIcon)](UCIcon) | badgeIcon | |
| **i10n** | [dict(str, UCI10n)](UCI10n) | i10n | |
| **polled_presence** | bool | polledPresence | |
| **poll_interval_sec** | int | pollIntervalSec | [optional] |
| **include_badge** | bool | includeBadge | [optional] |
| **user_permissions** | list[str] | userPermissions | |
| **oauth_scopes** | list[str] |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
