# Recipient

## Recipient

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **flow** | [Flow](Flow) | An automate flow object which defines the set of actions to be taken, when a message is received by this recipient. | [optional] |
| **date_created** | datetime | Date this recipient was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this recipient was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [User](User) | User that created this recipient | [optional] |
| **modified_by** | [User](User) | User that modified this recipient | [optional] |
| **messenger_type** | str | The messenger type for this recipient | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 242.0.0_
