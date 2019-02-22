---
title: EmailMediaParticipant
---
## EmailMediaParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The unique participant ID. | [optional] |
| **name** | **str** | The display friendly name of the participant. | [optional] |
| **address** | **str** | The participant address. | [optional] |
| **start_time** | **datetime** | The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The time when this participant went connected for this media (eg: video connected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **end_time** | **datetime** | The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **start_hold_time** | **datetime** | The time when this participant&#39;s hold started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **purpose** | **str** | The participant&#39;s purpose.  Values can be: &#39;agent&#39;, &#39;user&#39;, &#39;customer&#39;, &#39;external&#39;, &#39;acd&#39;, &#39;ivr | [optional] |
| **state** | **str** | The participant&#39;s state.  Values can be: &#39;alerting&#39;, &#39;connected&#39;, &#39;disconnected&#39;, &#39;dialing&#39;, &#39;contacting | [optional] |
| **direction** | **str** | The participant&#39;s direction.  Values can be: &#39;inbound&#39; or &#39;outbound&#39; | [optional] |
| **disconnect_type** | **str** | The reason the participant was disconnected from the conversation. | [optional] |
| **held** | **bool** | Value is true when the participant is on hold. | [optional] |
| **wrapup_required** | **bool** | Value is true when the participant requires wrap-up. | [optional] |
| **wrapup_prompt** | **str** | The wrap-up prompt indicating the type of wrap-up to be performed. | [optional] |
| **user** | [**UriReference**](UriReference.html) | The PureCloud user for this participant. | [optional] |
| **queue** | [**UriReference**](UriReference.html) | The PureCloud queue for this participant. | [optional] |
| **attributes** | **dict(str, str)** | A list of ad-hoc attributes for the participant. | [optional] |
| **error_info** | [**ErrorBody**](ErrorBody.html) | If the conversation ends in error, contains additional error details. | [optional] |
| **script** | [**UriReference**](UriReference.html) | The Engage script that should be used by this participant. | [optional] |
| **wrapup_timeout_ms** | **int** | The amount of time the participant has to complete wrap-up. | [optional] |
| **wrapup_skipped** | **bool** | Value is true when the participant has skipped wrap-up. | [optional] |
| **alerting_timeout_ms** | **int** | Specifies how long the agent has to answer an interaction before being marked as not responding. | [optional] |
| **provider** | **str** | The source provider for the communication. | [optional] |
| **external_contact** | [**UriReference**](UriReference.html) | If this participant represents an external contact, then this will be the reference for the external contact. | [optional] |
| **external_organization** | [**UriReference**](UriReference.html) | If this participant represents an external org, then this will be the reference for the external org. | [optional] |
| **wrapup** | [**Wrapup**](Wrapup.html) | Wrapup for this participant, if it has been applied. | [optional] |
| **peer** | **str** | The peer communication corresponding to a matching leg for this communication. | [optional] |
| **flagged_reason** | **str** | The reason specifying why participant flagged the conversation. | [optional] |
| **journey_context** | [**JourneyContext**](JourneyContext.html) | Journey System data/context that is applicable to this communication.  When used for historical purposes, the context should be immutable.  When null, there is no applicable Journey System context. | [optional] |
| **subject** | **str** | The subject of the email. | [optional] |
| **messages_sent** | **int** | The number of messages that have been sent in this email conversation. | [optional] |
| **auto_generated** | **bool** | Indicates that the email was auto-generated like an Out of Office reply. | [optional] |
| **draft_attachments** | [**list[Attachment]**](Attachment.html) | A list of uploaded attachments on the email draft. | [optional] |
{: class="table table-striped"}


