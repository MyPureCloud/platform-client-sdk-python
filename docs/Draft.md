# Draft

## Draft

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Draft name | |
| **miner** | [Miner](Miner) | Miner to which the draft belongs. | [optional] |
| **intents** | [list[DraftIntents]](DraftIntents) | Draft intent object. | [optional] |
| **topics** | [list[DraftTopics]](DraftTopics) | Draft topic object. | [optional] |
| **date_created** | datetime | Date when the draft was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the draft was updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 217.0.0_
