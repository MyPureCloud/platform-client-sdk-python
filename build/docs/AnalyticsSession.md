---
title: AnalyticsSession
---
## AnalyticsSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **active_skill_ids** | **list[str]** | ID(s) of Skill(s) that are active on the conversation | [optional] |
| **acw_skipped** | **bool** | Marker for an agent that skipped after call work | [optional] |
| **address_from** | **str** | The address that initiated an action | [optional] |
| **address_other** | **str** | The email address for the participant on the other side of the email conversation | [optional] |
| **address_self** | **str** | The email address for the participant on this side of the email conversation | [optional] |
| **address_to** | **str** | The address receiving an action | [optional] |
| **agent_assistant_id** | **str** | Unique identifier of the active virtual agent assistant | [optional] |
| **agent_bullseye_ring** | **int** | Bullseye ring of the targeted agent | [optional] |
| **agent_owned** | **bool** | Flag indicating an agent-owned callback | [optional] |
| **ani** | **str** | Automatic Number Identification (caller&#39;s number) | [optional] |
| **assigner_id** | **str** | ID of the user that manually assigned a conversation | [optional] |
| **authenticated** | **bool** | Flag that indicates that the identity of the customer has been asserted as verified by the provider. | [optional] |
| **callback_numbers** | **list[str]** | Callback phone number(s) | [optional] |
| **callback_scheduled_time** | **datetime** | Scheduled callback date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **callback_user_name** | **str** | The name of the user requesting a call back | [optional] |
| **coached_participant_id** | **str** | The participantId being coached (if someone (e.g. an agent) is being coached, this would correspond to one of the other participantIds present in the conversation) | [optional] |
| **cobrowse_role** | **str** | Describes side of the cobrowse (sharer or viewer) | [optional] |
| **cobrowse_room_id** | **str** | A unique identifier for a PureCloud cobrowse room | [optional] |
| **delivery_status** | **str** | The email delivery status | [optional] |
| **delivery_status_change_date** | **datetime** | Date and time of the most recent delivery status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **destination_addresses** | **list[str]** | Destination address(es) of transfers or consults | [optional] |
| **direction** | **str** | The direction of the communication | [optional] |
| **disposition_analyzer** | **str** | (Dialer) Analyzer (for example speech.person) | [optional] |
| **disposition_name** | **str** | (Dialer) Result of the analysis (for example disposition.classification.callable.machine) | [optional] |
| **dnis** | **str** | Dialed number identification service (number dialed by the calling party) | [optional] |
| **edge_id** | **str** | Unique identifier of the edge device | [optional] |
| **eligible_agent_counts** | **list[int]** | Number of eligible agents for each predictive routing attempt | [optional] |
| **flow_in_type** | **str** | Type of flow in that occurred when entering ACD. | [optional] |
| **flow_out_type** | **str** | Type of flow out that occurred when emitting tFlowOut. | [optional] |
| **journey_action_id** | **str** | Identifier of the journey action. | [optional] |
| **journey_action_map_id** | **str** | Identifier of the journey action map that triggered the action. | [optional] |
| **journey_action_map_version** | **int** | Version of the journey action map that triggered the action. | [optional] |
| **journey_customer_id** | **str** | Primary identifier of the journey customer in the source where the activities originate from. | [optional] |
| **journey_customer_id_type** | **str** | Type of primary identifier of the journey customer (e.g. cookie). | [optional] |
| **journey_customer_session_id** | **str** | Unique identifier of the journey session. | [optional] |
| **journey_customer_session_id_type** | **str** | Type or category of journey sessions (e.g. web, ticket, delivery, atm). | [optional] |
| **media_bridge_id** | **str** | Media bridge ID for the conference session consistent across all participants | [optional] |
| **media_count** | **int** | Count of any media (images, files, etc) included in this session | [optional] |
| **media_type** | **str** | The session media type | [optional] |
| **message_type** | **str** | Message type for messaging services. E.g.: sms, facebook, twitter, line | [optional] |
| **monitored_participant_id** | **str** | The participantId being monitored (if someone (e.g. an agent) is being monitored, this would correspond to one of the other participantIds present in the conversation) | [optional] |
| **outbound_campaign_id** | **str** | (Dialer) Unique identifier of the outbound campaign | [optional] |
| **outbound_contact_id** | **str** | (Dialer) Unique identifier of the contact | [optional] |
| **outbound_contact_list_id** | **str** | (Dialer) Unique identifier of the contact list that this contact belongs to | [optional] |
| **peer_id** | **str** | This identifies pairs of related sessions on a conversation. E.g. an external session’s peerId will be the session that the call originally connected to, e.g. if an IVR was dialed, the IVR session, which will also have the external session’s ID as its peer. After that point, any transfers of that session to other internal components (acd, agent, etc.) will all spawn new sessions whose peerIds point back to that original external session. | [optional] |
| **protocol_call_id** | **str** | The original voice protocol call ID, e.g. a SIP call ID | [optional] |
| **provider** | **str** | The source provider for the communication. | [optional] |
| **recording** | **bool** | Flag determining if an audio recording was started or not | [optional] |
| **remote** | **str** | Name, phone number, or email address of the remote party. | [optional] |
| **remote_name_displayable** | **str** | Unique identifier for the remote party | [optional] |
| **removed_skill_ids** | **list[str]** | ID(s) of Skill(s) that have been removed by bullseye routing | [optional] |
| **requested_routings** | **list[str]** | Routing type(s) for requested/attempted routing methods. | [optional] |
| **room_id** | **str** | Unique identifier for the room | [optional] |
| **routing_ring** | **int** | Routing ring for bullseye or preferred agent routing | [optional] |
| **screen_share_address_self** | **str** | Direct ScreenShare address | [optional] |
| **screen_share_room_id** | **str** | A unique identifier for a PureCloud ScreenShare room | [optional] |
| **script_id** | **str** | A unique identifier for a script | [optional] |
| **selected_agent_id** | **str** | Selected agent ID | [optional] |
| **selected_agent_rank** | **int** | Selected agent GPR rank | [optional] |
| **session_dnis** | **str** | Dialed number for the current session; this can be different from dnis, e.g. if the call was transferred | [optional] |
| **session_id** | **str** | The unique identifier of this session | [optional] |
| **sharing_screen** | **bool** | Flag determining if screenShare is started or not (true/false) | [optional] |
| **skip_enabled** | **bool** | (Dialer) Whether the agent can skip the dialer contact | [optional] |
| **timeout_seconds** | **int** | The number of seconds before PureCloud begins the call for a call back (0 disables automatic calling) | [optional] |
| **used_routing** | **str** | Complete routing method | [optional] |
| **video_address_self** | **str** | Direct Video address | [optional] |
| **video_room_id** | **str** | A unique identifier for a PureCloud video room | [optional] |
| **waiting_interaction_counts** | **list[int]** | Number of waiting interactions for each predictive routing attempt | [optional] |
| **proposed_agents** | [**list[AnalyticsProposedAgent]**](AnalyticsProposedAgent.html) | Proposed agents | [optional] |
| **media_endpoint_stats** | [**list[AnalyticsMediaEndpointStat]**](AnalyticsMediaEndpointStat.html) | MediaEndpointStats associated with this session | [optional] |
| **flow** | [**AnalyticsFlow**](AnalyticsFlow.html) | IVR flow execution associated with this session | [optional] |
| **metrics** | [**list[AnalyticsSessionMetric]**](AnalyticsSessionMetric.html) | List of metrics for this session | [optional] |
| **segments** | [**list[AnalyticsConversationSegment]**](AnalyticsConversationSegment.html) | List of segments for this session | [optional] |
{: class="table table-striped"}


