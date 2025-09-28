# MessagingSetting

## MessagingSetting

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The messaging Setting unique identifier associated with this integration | |
| **name** | str | The messaging Setting profile name | [optional] |
| **date_created** | datetime | Date this messaging setting was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this messaging setting was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | str | Version number | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Setting | [optional] |
| **updated_by** | [DomainEntityRef](DomainEntityRef) | User reference that modified this Setting | [optional] |
| **content** | [ContentSetting](ContentSetting) | Configuration relating to message contents | [optional] |
| **event** | [EventSetting](EventSetting) | Configuration relating to events which may occur | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 238.0.0_
