# WebChatMemberInfo

## WebChatMemberInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The communicationId of this member. | [optional] |
| **display_name** | str | The display name of the member. | [optional] |
| **first_name** | str | The first name of the member. | [optional] |
| **last_name** | str | The last name of the member. | [optional] |
| **email** | str | The email address of the member. | [optional] |
| **phone_number** | str | The phone number of the member. | [optional] |
| **avatar_image_url** | str | The url to the avatar image of the member. | [optional] |
| **role** | str | The role of the member, one of [agent, customer, acd, workflow] | |
| **join_date** | datetime | The time the member joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **leave_date** | datetime | The time the member left the conversation, or null if the member is still active in the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **authenticated_guest** | bool | If true, the guest member is an authenticated guest. | [optional] |
| **custom_fields** | dict(str, str) | Any custom fields of information pertaining to this member. | [optional] |
| **state** | str | The connection state of this member. | [optional] |



_PureCloudPlatformClientV2 211.0.0_
