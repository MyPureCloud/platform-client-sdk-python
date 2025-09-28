# InstagramIntegration

## InstagramIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique Integration ID. | |
| **name** | str | The name of the Instagram Integration | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingReference](MessagingSettingReference) |  | [optional] |
| **app_id** | str | The App ID from Facebook | |
| **page_id** | str | The Page ID from Instagram messenger | [optional] |
| **instagram_id** | str | The ID from Instagram messenger | [optional] |
| **instagram_username** | str | The Username from Instagram messenger | [optional] |
| **instagram_name** | str | The name from Instagram messenger | [optional] |
| **instagram_profile_image_url** | str | The url of the profile image from Instagram messenger | [optional] |
| **status** | str | The status of the Instagram Integration | [optional] |
| **recipient** | [DomainEntityRef](DomainEntityRef) | The recipient reference associated to the Instagram Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | datetime | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that last modified this Integration | [optional] |
| **version** | int | Version number required for updates. | |
| **create_status** | str | Status of asynchronous create operation | [optional] |
| **create_error** | [ErrorBody](ErrorBody) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 238.0.0_
