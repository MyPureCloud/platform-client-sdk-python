# ConversationMetricsTopicConversationMetricRecord

## ConversationMetricsTopicConversationMetricRecord

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metric** | str | Metric name | [optional] |
| **metric_date** | datetime | The date and time of metric creation | [optional] |
| **value** | int | Metric value | [optional] |
| **record_id** | str | Record identifier | [optional] |
| **active_routing** | str | Active routing method | [optional] |
| **active_skill_ids** | list[str] | ID(s) of Skill(s) that are active on the conversation | [optional] |
| **address_from** | str | The address that initiated an action | [optional] |
| **address_to** | str | The address receiving an action | [optional] |
| **agent_assistant_id** | str | Unique identifier of the active virtual agent assistant | [optional] |
| **agent_bullseye_ring** | int | Bullseye ring of the targeted agent | [optional] |
| **agent_owned** | bool | Flag indicating an agent-owned callback | [optional] |
| **ani** | str | Automatic Number Identification (caller&#39;s number) | [optional] |
| **assigner_id** | str | ID of the user that manually assigned a conversation | [optional] |
| **authenticated** | bool | Flag that indicates that the identity of the customer has been asserted as verified by the provider. | [optional] |
| **conversation_id** | str | Unique identifier for the conversation | [optional] |
| **conversation_initiator** | str | Indicates the participant purpose of the participant initiating a message conversation | [optional] |
| **converted_from** | str | Session media type that was converted from in case of a media type conversion | [optional] |
| **converted_to** | str | Session media type that was converted to in case of a media type conversion | [optional] |
| **customer_participation** | bool | Indicates a messaging conversation in which the customer participated by sending at least one message | [optional] |
| **delivery_status** | str | The email or SMS delivery status | [optional] |
| **destination_addresses** | list[str] | Destination address(es) of transfers or consults | [optional] |
| **direction** | str | The direction of the communication | [optional] |
| **disconnect_type** | str | The session disconnect type | [optional] |
| **division_ids** | list[str] | Identifier(s) of division(s) associated with a conversation | [optional] |
| **dnis** | str | Dialed number identification service (number dialed by the calling party) | [optional] |
| **edge_id** | str | Unique identifier of the edge device | [optional] |
| **eligible_agent_counts** | list[int] | Number of eligible agents for each predictive routing attempt | [optional] |
| **error_code** | str | A code corresponding to the error that occurred | [optional] |
| **extended_delivery_status** | str | Extended delivery status | [optional] |
| **external_contact_id** | str | External contact identifier | [optional] |
| **external_media_count** | int | Count of any media (images, files, etc) included on the external session | [optional] |
| **external_organization_id** | str | External organization identifier | [optional] |
| **external_tag** | str | External tag for the conversation | [optional] |
| **first_queue** | bool | Marker that is set if the current queue is the first queue in a conversation | [optional] |
| **flagged_reason** | str | Reason for which participant flagged conversation | [optional] |
| **flow_in_type** | str | Type of flow in that occurred when entering ACD. | [optional] |
| **flow_out_type** | str | Type of flow out that occurred when emitting tFlowOut. | [optional] |
| **group_id** | str | Unique identifier for a Genesys Cloud group | [optional] |
| **interaction_type** | str | The interaction type (enterprise or contactCenter) | [optional] |
| **journey_action_id** | str | Identifier of the journey action. | [optional] |
| **journey_action_map_id** | str | Identifier of the journey action map that triggered the action. | [optional] |
| **journey_action_map_version** | int | Version of the journey action map that triggered the action. | [optional] |
| **journey_customer_id** | str | Primary identifier of the journey customer in the source where the activities originate from. | [optional] |
| **journey_customer_id_type** | str | Type of primary identifier of the journey customer (e.g. cookie). | [optional] |
| **journey_customer_session_id** | str | Unique identifier of the journey session. | [optional] |
| **journey_customer_session_id_type** | str | Type or category of journey sessions (e.g. web, ticket, delivery, atm). | [optional] |
| **knowledge_base_ids** | list[str] | The unique identifier(s) of the knowledge base(s) used | [optional] |
| **media_count** | int | Count of any media (images, files, etc) included in this session | [optional] |
| **media_type** | str | The session media type | [optional] |
| **message_type** | str | Message type for messaging services. E.g.: sms, facebook, twitter, line | [optional] |
| **originating_direction** | str | The original direction of the conversation | [optional] |
| **originating_social_media_public** | bool | Indicates that the conversation originated from a public message on social media | [optional] |
| **outbound_campaign_id** | str | (Dialer) Unique identifier of the outbound campaign | [optional] |
| **outbound_contact_id** | str | (Dialer) Unique identifier of the contact | [optional] |
| **outbound_contact_list_id** | str | (Dialer) Unique identifier of the contact list that this contact belongs to | [optional] |
| **participant_name** | str | A human readable name identifying the participant | [optional] |
| **peer_id** | str | This identifies pairs of related sessions on a conversation. E.g. an external session’s peerId will be the session that the call originally connected to, e.g. if an IVR was dialed, the IVR session, which will also have the external session’s ID as its peer. After that point, any transfers of that session to other internal components (acd, agent, etc.) will all spawn new sessions whose peerIds point back to that original external session. | [optional] |
| **provider** | str | The source provider for the communication. | [optional] |
| **purpose** | str | The participant&#39;s purpose | [optional] |
| **queue_id** | str | Queue identifier | [optional] |
| **remote** | str | Name, phone number, or email address of the remote party. | [optional] |
| **removed_skill_ids** | list[str] | ID(s) of Skill(s) that have been removed by bullseye routing | [optional] |
| **requested_language_id** | str | Unique identifier for the language requested for an interaction | [optional] |
| **requested_routing_skill_ids** | list[str] | Unique identifier(s) for skill(s) requested for an interaction | [optional] |
| **requested_routings** | list[str] | Routing type(s) for requested/attempted routing methods. | [optional] |
| **room_id** | str | Unique identifier for the room | [optional] |
| **routing_priority** | int | Routing priority for the current interaction | [optional] |
| **routing_ring** | int | Routing ring for bullseye or preferred agent routing | [optional] |
| **routing_rule** | str | Routing rule for preferred, conditional and predictive routing type | [optional] |
| **routing_rule_type** | str | Routing rule type | [optional] |
| **selected_agent_id** | str | Selected agent ID | [optional] |
| **selected_agent_rank** | int | Selected agent GPR rank | [optional] |
| **self_served** | bool | Indicates whether all flow sessions were self serviced | [optional] |
| **session_dnis** | str | Dialed number for the current session; this can be different from dnis, e.g. if the call was transferred | [optional] |
| **session_id** | str | The unique identifier of this session | [optional] |
| **station_id** | str | Unique identifier for a phone | [optional] |
| **team_id** | str | The team ID the user is a member of | [optional] |
| **used_routing** | str | Complete routing method | [optional] |
| **user_id** | str | Unique identifier for the user | [optional] |
| **video_present** | bool | Flag indicating if video is present | [optional] |
| **waiting_interaction_counts** | list[int] | Number of waiting interactions for each predictive routing attempt | [optional] |
| **wrap_up_code** | str | Wrap up code | [optional] |
| **proposed_agents** | [list[ConversationMetricsTopicConversationProposedAgent]](ConversationMetricsTopicConversationProposedAgent) | Proposed agents | [optional] |
| **scored_agents** | [list[ConversationMetricsTopicConversationScoredAgent]](ConversationMetricsTopicConversationScoredAgent) | Scored agents | [optional] |



_PureCloudPlatformClientV2 228.0.0_
