---
title: SupportCenterSettings
---
## SupportCenterSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** | Whether or not support center is enabled | [optional] |
| **knowledge_base** | [**AddressableEntityRef**](AddressableEntityRef.html) | The knowledge base for support center | [optional] |
| **custom_messages** | [**list[SupportCenterCustomMessage]**](SupportCenterCustomMessage.html) | Customizable display texts for support center | [optional] |
| **router_type** | **str** | Router type for support center | [optional] |
| **screens** | [**list[SupportCenterScreen]**](SupportCenterScreen.html) | Available screens for the support center with its modules | [optional] |
| **enabled_categories** | [**list[AddressableEntityRef]**](AddressableEntityRef.html) | Enabled article categories for support center | [optional] |
| **style_setting** | [**SupportCenterStyleSetting**](SupportCenterStyleSetting.html) | Style attributes for support center | [optional] |
{: class="table table-striped"}


