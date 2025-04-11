# DialerResponsesetConfigChangeResponseSet

## DialerResponsesetConfigChangeResponseSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **responses** | [dict(str, DialerResponsesetConfigChangeReaction)](DialerResponsesetConfigChangeReaction) | Map of disposition identifiers to reactions. For example: {\&quot;disposition.classification.callable.person\&quot;: {\&quot;reactionType\&quot;: \&quot;transfer\&quot;}} | [optional] |
| **beep_detection_enabled** | bool | When beep detection is enabled, answering machine detection will wait for the beep before transferring the call | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 226.0.0_
