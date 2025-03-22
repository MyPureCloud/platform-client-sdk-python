# CobrowseSettings

## CobrowseSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether or not cobrowse is enabled | [optional] |
| **allow_agent_control** | bool | Whether the viewer should have option to request control | [optional] |
| **allow_agent_navigation** | bool | Whether the viewer should have option to request navigation | [optional] |
| **allow_draw** | bool | Should cobrowse draw be enabled | [optional] |
| **mask_selectors** | list[str] | Mask patterns that will apply to pages being shared | [optional] |
| **channels** | list[str] | Cobrowse channels for web messenger | [optional] |
| **readonly_selectors** | list[str] | Readonly patterns that will apply to pages being shared | [optional] |
| **pause_criteria** | [list[PauseCriteria]](PauseCriteria) | Pause criteria that will pause cobrowse if some of them are met in the user&#39;s URL | [optional] |



_PureCloudPlatformClientV2 224.0.0_
