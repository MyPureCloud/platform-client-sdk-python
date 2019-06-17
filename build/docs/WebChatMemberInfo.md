---
title: WebChatMemberInfo
---
## WebChatMemberInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The communicationId of this member. | [optional] |
| **display_name** | **str** | The display name of the member. | [optional] |
| **avatar_image_url** | **str** | The url to the avatar image of the member. | [optional] |
| **role** | **str** | The role of the member, one of [agent, customer, acd, workflow] | |
| **join_date** | **datetime** | The time the member joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **leave_date** | **datetime** | The time the member left the conversation, or null if the member is still active in the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **authenticated_guest** | **bool** | If true, the guest member is an authenticated guest. | [optional] |
| **custom_fields** | **dict(str, str)** | Any custom fields of information pertaining to this member. | [optional] |
| **state** | **str** | The connection state of this member. | [optional] |
{: class="table table-striped"}


