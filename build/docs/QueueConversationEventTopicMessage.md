---
title: QueueConversationEventTopicMessage
---
## QueueConversationEventTopicMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **state** | **str** |  | [optional] |
| **initial_state** | **str** |  | [optional] |
| **direction** | **str** | Whether a message is inbound or outbound. | [optional] |
| **held** | **bool** | True if this call is held and the person on this side hears silence. | [optional] |
| **error_info** | [**QueueConversationEventTopicErrorDetails**](QueueConversationEventTopicErrorDetails.html) | Detailed information about an error response. | [optional] |
| **provider** | **str** | The source provider of the email. | [optional] |
| **script_id** | **str** | The UUID of the script to use. | [optional] |
| **peer_id** | **str** | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | **datetime** | The timestamp the email was placed on hold in the cloud clock if the email is currently on hold. | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **to_address** | [**QueueConversationEventTopicAddress**](QueueConversationEventTopicAddress.html) | Address and name data for a call endpoint. | [optional] |
| **from_address** | [**QueueConversationEventTopicAddress**](QueueConversationEventTopicAddress.html) | Address and name data for a call endpoint. | [optional] |
| **messages** | [**list[QueueConversationEventTopicMessageDetails]**](QueueConversationEventTopicMessageDetails.html) | The messages sent on this communication channel. | [optional] |
| **messages_transcript_uri** | **str** | the messages transcript file uri. | [optional] |
| **type** | **str** | Indicates the type of message platform from which the message originated. | [optional] |
| **recipient_country** | **str** | Indicates the country where the recipient is associated in ISO 3166-1 alpha-2 format. | [optional] |
| **recipient_type** | **str** | The type of the recipient. Eg: Provisioned phoneNumber is the recipient for sms message type. | [optional] |
| **journey_context** | [**QueueConversationEventTopicJourneyContext**](QueueConversationEventTopicJourneyContext.html) | A subset of the Journey System&#39;s data relevant to a part of a conversation (for external linkage and internal usage/context). | [optional] |
| **wrapup** | [**QueueConversationEventTopicWrapup**](QueueConversationEventTopicWrapup.html) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [**QueueConversationEventTopicAfterCallWork**](QueueConversationEventTopicAfterCallWork.html) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | **bool** | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **agent_assistant_id** | **str** | UUID of virtual agent assistant that provide suggestions to the agent participant during the conversation. | [optional] |
| **byo_sms_integration_id** | **str** |  | [optional] |
| **queue_media_settings** | [**QueueConversationEventTopicQueueMediaSettings**](QueueConversationEventTopicQueueMediaSettings.html) | Represents the queue setting for this media. | [optional] |
{: class="table table-striped"}


