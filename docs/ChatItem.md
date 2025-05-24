# ChatItem

## ChatItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **open** | bool | If the chat is open | |
| **favorite** | [ChatFavorite](ChatFavorite) | The favorite entity for the chat, only appears if the chat is favorited | [optional] |
| **images** | [list[Image]](Image) | Avatar images for the chat | [optional] |
| **date_last_message** | datetime | The date of the last message. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_closed** | datetime | The date the chat was closed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **user** | [ChatUserRef](ChatUserRef) | The other 1on1 user | [optional] |
| **room** | [Room](Room) | The room of the chat | [optional] |
| **chat_type** | str | The type of chat | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
