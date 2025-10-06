# SupportCenterSettings

## SupportCenterSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether or not knowledge portal (previously support center) is enabled | |
| **knowledge_base** | [AddressableEntityRef](AddressableEntityRef) | The knowledge base for knowledge portal (previously support center) | |
| **custom_messages** | [list[SupportCenterCustomMessage]](SupportCenterCustomMessage) | Customizable display texts for knowledge portal (previously support center) | [optional] |
| **router_type** | str | Router type for knowledge portal (previously support center) | [optional] |
| **screens** | [list[SupportCenterScreen]](SupportCenterScreen) | Available screens for the knowledge portal (previously support center) with its modules | |
| **enabled_categories** | [list[SupportCenterCategory]](SupportCenterCategory) | Featured categories for knowledge portal (previously support center) home screen | |
| **label_filter** | [SupportCenterLabelFilter](SupportCenterLabelFilter) | Document label filter. If set, only documents having at least one of the specified labels will be returned by knowledge document query operations. | [optional] |
| **style_setting** | [SupportCenterStyleSetting](SupportCenterStyleSetting) | Style attributes for knowledge portal (previously support center) | |
| **feedback** | [SupportCenterFeedbackSettings](SupportCenterFeedbackSettings) | Customer feedback settings | [optional] |



_PureCloudPlatformClientV2 240.0.0_
