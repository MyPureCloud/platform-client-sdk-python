# MessageMediaParticipant

## MessageMediaParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The unique participant ID. | [optional] |
| **name** | str | The display friendly name of the participant. | [optional] |
| **address** | str | The participant address. | [optional] |
| **start_time** | datetime | The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **connected_time** | datetime | The time when this participant went connected for this media (eg: video connected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_time** | datetime | The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **start_hold_time** | datetime | The time when this participant&#39;s hold started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **purpose** | str | The participant&#39;s purpose.  Values can be: &#39;agent&#39;, &#39;user&#39;, &#39;customer&#39;, &#39;external&#39;, &#39;acd&#39;, &#39;ivr | [optional] |
| **state** | str | The participant&#39;s state.  Values can be: &#39;alerting&#39;, &#39;connected&#39;, &#39;disconnected&#39;, &#39;dialing&#39;, &#39;contacting | [optional] |
| **direction** | str | The participant&#39;s direction.  Values can be: &#39;inbound&#39; or &#39;outbound&#39; | [optional] |
| **disconnect_type** | str | The reason the participant was disconnected from the conversation. | [optional] |
| **held** | bool | Value is true when the participant is on hold. | [optional] |
| **wrapup_required** | bool | Value is true when the participant requires wrap-up. | [optional] |
| **wrapup_prompt** | str | The wrap-up prompt indicating the type of wrap-up to be performed. | [optional] |
| **media_roles** | list[str] | List of roles this participant&#39;s media has had on the conversation, ie monitor, coach, etc | [optional] |
| **user** | [DomainEntityRef](DomainEntityRef) | The PureCloud user for this participant. | [optional] |
| **queue** | [DomainEntityRef](DomainEntityRef) | The PureCloud queue for this participant. | [optional] |
| **team** | [DomainEntityRef](DomainEntityRef) | The PureCloud team for this participant. | [optional] |
| **attributes** | dict(str, str) | A list of ad-hoc attributes for the participant. | [optional] |
| **error_info** | [ErrorInfo](ErrorInfo) | If the conversation ends in error, contains additional error details. | [optional] |
| **script** | [DomainEntityRef](DomainEntityRef) | The Engage script that should be used by this participant. | [optional] |
| **wrapup_timeout_ms** | int | The amount of time the participant has to complete wrap-up. | [optional] |
| **wrapup_skipped** | bool | Value is true when the participant has skipped wrap-up. | [optional] |
| **alerting_timeout_ms** | int | Specifies how long the agent has to answer an interaction before being marked as not responding. | [optional] |
| **provider** | str | The source provider for the communication. | [optional] |
| **external_contact** | [DomainEntityRef](DomainEntityRef) | If this participant represents an external contact, then this will be the reference for the external contact. | [optional] |
| **external_organization** | [DomainEntityRef](DomainEntityRef) | If this participant represents an external org, then this will be the reference for the external org. | [optional] |
| **wrapup** | [Wrapup](Wrapup) | Wrapup for this participant, if it has been applied. | [optional] |
| **peer** | str | The peer communication corresponding to a matching leg for this communication. | [optional] |
| **flagged_reason** | str | The reason specifying why participant flagged the conversation. | [optional] |
| **journey_context** | [JourneyContext](JourneyContext) | Journey System data/context that is applicable to this communication.  When used for historical purposes, the context should be immutable.  When null, there is no applicable Journey System context. | [optional] |
| **conversation_routing_data** | [ConversationRoutingData](ConversationRoutingData) | Information on how a communication should be routed to an agent. | [optional] |
| **start_acw_time** | datetime | The timestamp when this participant started after-call work. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_acw_time** | datetime | The timestamp when this participant ended after-call work. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **park_time** | datetime | The time when this participant&#39;s communication was last parked.  Does not reset on resume. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **to_address** | [Address](Address) | Address for the participant on receiving side of the message conversation. If the address is a phone number, E.164 format is recommended. | [optional] |
| **from_address** | [Address](Address) | Address for the participant on the sending side of the message conversation. If the address is a phone number, E.164 format is recommended. | [optional] |
| **messages** | [list[MessageDetails]](MessageDetails) | Message instance details on the communication. | [optional] |
| **type** | str | Indicates the type of message platform from which the message originated. | [optional] |
| **recipient_country** | str | Indicates the country where the recipient is associated in ISO 3166-1 alpha-2 format. | [optional] |
| **recipient_type** | str | The type of the recipient. Eg: Provisioned phoneNumber is the recipient for sms message type. | [optional] |
| **authenticated** | bool | If true, the participant member is authenticated. | [optional] |
| **monitored_participant_id** | str | The ID of the participant being monitored when performing a message monitor. | [optional] |
| **monitored_participant** | [AddressableEntityRef](AddressableEntityRef) | The participant being monitored when performing a message monitor. | [optional] |



_PureCloudPlatformClientV2 216.0.0_
