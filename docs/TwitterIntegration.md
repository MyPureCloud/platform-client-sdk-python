# TwitterIntegration

## TwitterIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique Integration ID | |
| **name** | str | The name of the Twitter Integration | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingReference](MessagingSettingReference) |  | [optional] |
| **status** | str | The status of the Twitter Integration | [optional] |
| **recipient** | [DomainEntityRef](DomainEntityRef) | The recipient reference associated with the Twitter Integration This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | datetime | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that last modified this Integration | [optional] |
| **version** | int | Version number required for updates | |
| **create_status** | str | Status of asynchronous create operation | [optional] |
| **create_error** | [ErrorBody](ErrorBody) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 226.0.0_
