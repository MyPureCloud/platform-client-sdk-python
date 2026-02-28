# CustomAttributes

## CustomAttributes

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The id of the Custom Attributes record. | [optional] |
| **name** | str |  | [optional] |
| **conversation_id** | str | The id of the conversation. | [optional] |
| **divisions** | list[str] | The list of division ids that the record is visible in. If [], the record is visible to all divisions (Unassigned Division). | [optional] |
| **schema** | [ConversationDataSchema](ConversationDataSchema) | The schema that dictates which attributes can be included. | [optional] |
| **custom_attributes** | dict(str, object) | The map of attribute values. | [optional] |
| **custom_attributes_timestamps** | dict(str, str) | The map of timestamps for when each attribute was last updated. | [optional] |
| **version** | int | The latest version of the Custom Attributes record. | [optional] |
| **date_created** | datetime | The date the record was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date the record was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 252.0.0_
