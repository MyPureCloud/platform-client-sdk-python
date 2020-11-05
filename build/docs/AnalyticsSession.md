---
title: AnalyticsSession
---
## AnalyticsSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_type** | **str** | The session media type | [optional] |
| **session_id** | **str** | The unique identifier of this session | [optional] |
| **address_other** | **str** |  | [optional] |
| **address_self** | **str** |  | [optional] |
| **address_from** | **str** |  | [optional] |
| **address_to** | **str** |  | [optional] |
| **message_type** | **str** | Message type for messaging services such as sms | [optional] |
| **ani** | **str** | Automatic Number Identification (caller&#39;s number) | [optional] |
| **direction** | **str** | Direction | [optional] |
| **dnis** | **str** | Dialed number identification service (number dialed by the calling party) | [optional] |
| **session_dnis** | **str** | Dialed number for the current session; this can be different from dnis, e.g. if the call was transferred | [optional] |
| **outbound_campaign_id** | **str** | (Dialer) Unique identifier of the outbound campaign | [optional] |
| **outbound_contact_id** | **str** | (Dialer) Unique identifier of the contact | [optional] |
| **outbound_contact_list_id** | **str** | (Dialer) Unique identifier of the contact list that this contact belongs to | [optional] |
| **disposition_analyzer** | **str** | (Dialer) Unique identifier of the contact list that this contact belongs to | [optional] |
| **disposition_name** | **str** | (Dialer) Result of the analysis | [optional] |
| **edge_id** | **str** | Unique identifier of the edge device | [optional] |
| **remote_name_displayable** | **str** |  | [optional] |
| **room_id** | **str** | Unique identifier for the room | [optional] |
| **monitored_session_id** | **str** | The sessionID being monitored | [optional] |
| **monitored_participant_id** | **str** |  | [optional] |
| **callback_user_name** | **str** | The name of the user requesting a call back | [optional] |
| **callback_numbers** | **list[str]** | List of numbers to callback | [optional] |
| **callback_scheduled_time** | **datetime** | Scheduled callback date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **script_id** | **str** | A unique identifier for a script | [optional] |
| **peer_id** | **str** | A unique identifier for a peer | [optional] |
| **skip_enabled** | **bool** | (Dialer) Whether the agent can skip the dialer contact | [optional] |
| **timeout_seconds** | **int** | The number of seconds before PureCloud begins the call for a call back. 0 disables automatic calling | [optional] |
| **cobrowse_role** | **str** | Describe side of the cobrowse (sharer or viewer) | [optional] |
| **cobrowse_room_id** | **str** | A unique identifier for a PureCloud Cobrowse room. | [optional] |
| **media_bridge_id** | **str** |  | [optional] |
| **screen_share_address_self** | **str** | Direct ScreenShare address | [optional] |
| **sharing_screen** | **bool** | Flag determining if screenShare is started or not (true/false) | [optional] |
| **screen_share_room_id** | **str** | A unique identifier for a PureCloud ScreenShare room. | [optional] |
| **video_room_id** | **str** | A unique identifier for a PureCloud video room. | [optional] |
| **video_address_self** | **str** | Direct Video address | [optional] |
| **segments** | [**list[AnalyticsConversationSegment]**](AnalyticsConversationSegment.html) | List of segments for this session | [optional] |
| **metrics** | [**list[AnalyticsSessionMetric]**](AnalyticsSessionMetric.html) | List of metrics for this session | [optional] |
| **flow** | [**AnalyticsFlow**](AnalyticsFlow.html) | IVR flow execution associated with this session | [optional] |
| **media_endpoint_stats** | [**list[AnalyticsMediaEndpointStat]**](AnalyticsMediaEndpointStat.html) | Media endpoint stats associated with this session | [optional] |
| **recording** | **bool** | Flag determining if an audio recording was started or not | [optional] |
| **journey_customer_id** | **str** | ID of the journey customer | [optional] |
| **journey_customer_id_type** | **str** | Type of the journey customer ID | [optional] |
| **journey_customer_session_id** | **str** | ID of the journey customer session | [optional] |
| **journey_customer_session_id_type** | **str** | Type of the journey customer session ID | [optional] |
| **journey_action_id** | **str** | Journey action ID | [optional] |
| **journey_action_map_id** | **str** | Journey action map ID | [optional] |
| **journey_action_map_version** | **str** | Journey action map version | [optional] |
| **protocol_call_id** | **str** | The original voice protocol call ID, e.g. a SIP call ID | [optional] |
| **provider** | **str** | The source provider for the communication | [optional] |
| **remote** | **str** | Name, phone number, or email address of the remote party. | [optional] |
| **media_count** | **int** | Count of any media (images, files, etc) included in this session | [optional] |
| **flow_in_type** | **str** | Type of flow in that occurred, e.g. acd, ivr, etc. | [optional] |
| **flow_out_type** | **str** | Type of flow out that occurred, e.g. voicemail, callback, or acd | [optional] |
| **requested_routings** | **list[str]** | All routing types for requested/attempted routing methods. | [optional] |
| **used_routing** | **str** | Complete routing method | [optional] |
| **selected_agent_id** | **str** | Selected agent id | [optional] |
| **selected_agent_rank** | **int** | Selected agent GPR rank | [optional] |
| **agent_assistant_id** | **str** | Unique identifier of the active virtual agent assistant | [optional] |
| **proposed_agents** | [**list[AnalyticsProposedAgent]**](AnalyticsProposedAgent.html) | Proposed agents | [optional] |
| **assigner_id** | **str** | ID of the user that manually assigned a conversation | [optional] |
| **acw_skipped** | **bool** | Marker for an agent that skipped after call work | [optional] |
{: class="table table-striped"}


