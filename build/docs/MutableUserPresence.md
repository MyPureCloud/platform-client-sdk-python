# MutableUserPresence

## MutableUserPresence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The user&#39;s id | [optional] |
| **name** | str |  | [optional] |
| **source** | str | Deprecated - The sourceID field should be used as a replacement. | [optional] |
| **source_id** | str | Represents the ID of a registered source | [optional] |
| **primary** | bool | A boolean used to tell whether or not to set this presence source as the primary on a PATCH | [optional] |
| **presence_definition** | [PresenceDefinition](PresenceDefinition) |  | [optional] |
| **message** | str |  | [optional] |
| **modified_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
