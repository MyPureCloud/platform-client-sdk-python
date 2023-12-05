---
title: SupportCenterSettings
---
## SupportCenterSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** | Whether or not knowledge portal (previously support center) is enabled | [optional] |
| **knowledge_base** | [**AddressableEntityRef**](AddressableEntityRef.html) | The knowledge base for knowledge portal (previously support center) | [optional] |
| **custom_messages** | [**list[SupportCenterCustomMessage]**](SupportCenterCustomMessage.html) | Customizable display texts for knowledge portal (previously support center) | [optional] |
| **router_type** | **str** | Router type for knowledge portal (previously support center) | [optional] |
| **screens** | [**list[SupportCenterScreen]**](SupportCenterScreen.html) | Available screens for the knowledge portal (previously support center) with its modules | [optional] |
| **enabled_categories** | [**list[SupportCenterCategory]**](SupportCenterCategory.html) | Featured categories for knowledge portal (previously support center) home screen | [optional] |
| **style_setting** | [**SupportCenterStyleSetting**](SupportCenterStyleSetting.html) | Style attributes for knowledge portal (previously support center) | [optional] |
| **feedback** | [**SupportCenterFeedbackSettings**](SupportCenterFeedbackSettings.html) | Customer feedback settings | [optional] |
{: class="table table-striped"}


