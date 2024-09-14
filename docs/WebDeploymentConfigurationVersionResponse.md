# WebDeploymentConfigurationVersionResponse

## WebDeploymentConfigurationVersionResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The configuration version ID | [optional] |
| **name** | str | The configuration version name | |
| **version** | str | The version of the configuration | [optional] |
| **headless_mode** | [WebDeploymentHeadlessMode](WebDeploymentHeadlessMode) | Headless Mode Support which Controls UI components. When enabled, native UI components will be disabled and allows for custom-built UI. | [optional] |
| **description** | str | The description of the configuration | [optional] |
| **languages** | list[str] | A list of languages supported on the configuration required if the messenger is enabled | [optional] |
| **default_language** | str | The default language to use for the configuration required if the messenger is enabled | [optional] |
| **custom_i18n_labels** | [list[CustomI18nLabels]](CustomI18nLabels) | The localization settings for homescreen app | [optional] |
| **messenger** | [MessengerSettings](MessengerSettings) | The settings for messenger | [optional] |
| **position** | [PositionSettings](PositionSettings) | The settings for position | [optional] |
| **support_center** | [SupportCenterSettings](SupportCenterSettings) | The settings for knowledge portal (previously support center) | [optional] |
| **cobrowse** | [CobrowseSettings](CobrowseSettings) | The settings for cobrowse | [optional] |
| **journey_events** | [JourneyEventsSettings](JourneyEventsSettings) | The settings for journey events | [optional] |
| **authentication_settings** | [AuthenticationSettings](AuthenticationSettings) | The settings for authenticated deployments | [optional] |
| **date_created** | datetime | The date the configuration version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date the configuration version was most recently modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_published** | datetime | The date the configuration version was most recently published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **last_modified_user** | [AddressableEntityRef](AddressableEntityRef) | A reference to the user who most recently modified the configuration version | [optional] |
| **created_user** | [AddressableEntityRef](AddressableEntityRef) | A reference to the user who created the configuration version | [optional] |
| **published_user** | [AddressableEntityRef](AddressableEntityRef) | A reference to the user who published the configuration version | [optional] |
| **status** | str | The current status of the configuration version | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 211.1.0_
