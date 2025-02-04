# ResponseSet

## ResponseSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the ResponseSet. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **responses** | [dict(str, Reaction)](Reaction) | Map of disposition identifiers to reactions. For example: {\&quot;disposition.classification.callable.person\&quot;: {\&quot;reactionType\&quot;: \&quot;transfer\&quot;}}. | |
| **beep_detection_enabled** | bool | Whether to enable answering machine beep detection | [optional] |
| **amd_speech_distinguish_enabled** | bool | Whether to enable answering machine detection | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
