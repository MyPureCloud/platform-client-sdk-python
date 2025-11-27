# UcUserPresence

## UcUserPresence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **user_id** | str | User ID of the associated Genesys Cloud user. | [optional] |
| **source** | str | Deprecated - The sourceID field should be used as a replacement. | [optional] |
| **source_id** | str | The registered source ID from where the presence was set | [optional] |
| **presence_definition** | [PresenceDefinition](PresenceDefinition) |  | [optional] |
| **message** | str |  | [optional] |
| **modified_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 245.0.0_
