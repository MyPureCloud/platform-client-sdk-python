---
title: UnifiedCommunicationsIntegration
---
## UnifiedCommunicationsIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **uc_integration_key** | [**AddressableEntityRef**](AddressableEntityRef.html) | ucIntegrationKey | |
| **integration_presence_source** | **str** | integrationPresenceType | |
| **pbx_permission** | **str** | pbxPermission | |
| **icon** | [**UCIcon**](UCIcon.html) | icon | |
| **badge_icons** | [**dict(str, UCIcon)**](UCIcon.html) | badgeIcon | |
| **i10n** | [**dict(str, UCI10n)**](UCI10n.html) | i10n | |
| **polled_presence** | **bool** | polledPresence | |
| **poll_interval_sec** | **int** | pollIntervalSec | [optional] |
| **user_permissions** | **list[str]** | userPermissions | |
| **oauth_scopes** | **list[str]** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


