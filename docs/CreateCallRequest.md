# CreateCallRequest

## CreateCallRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **phone_number** | str | The phone number to dial. | [optional] |
| **caller_id** | str | The caller id phone number for this outbound call. | [optional] |
| **caller_id_name** | str | The caller id name for this outbound call. | [optional] |
| **call_from_queue_id** | str | The queue ID to call on behalf of. | [optional] |
| **call_queue_id** | str | The queue ID to call. | [optional] |
| **call_user_id** | str | The user ID to call. | [optional] |
| **priority** | int | The priority to assign to this call (if calling a queue). | [optional] |
| **attributes** | dict(str, str) | The list of attributes to associate with the customer participant. | [optional] |
| **language_id** | str | The language skill ID to use for routing this call (if calling a queue). | [optional] |
| **routing_skills_ids** | list[str] | The skill ID&#39;s to use for routing this call (if calling a queue). | [optional] |
| **conversation_ids** | list[str] | The list of existing call conversations to merge into a new ad-hoc conference. | [optional] |
| **participants** | [list[Destination]](Destination) | The list of participants to call to create a new ad-hoc conference. | [optional] |
| **uui_data** | str | User to User Information (UUI) data managed by SIP session application. | [optional] |
| **external_contact_id** | str | The external contact with which to associate the call. | [optional] |
| **label** | str | An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level | [optional] |



_PureCloudPlatformClientV2 213.0.0_
