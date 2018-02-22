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
| **dnis** | **str** | Automatic Number Identification (caller&#39;s number) | [optional] |
| **outbound_campaign_id** | **str** | (Dialer) Unique identifier of the outbound campaign | [optional] |
| **outbound_contact_id** | **str** | (Dialer) Unique identifier of the contact | [optional] |
| **outbound_contact_list_id** | **str** | (Dialer) Unique identifier of the contact list that this contact belongs to | [optional] |
| **disposition_analyzer** | **str** | (Dialer) Unique identifier of the contact list that this contact belongs to | [optional] |
| **disposition_name** | **str** | (Dialer) Result of the analysis (for example disposition.classification.callable.machine)  | [optional] |
| **edge_id** | **str** | Unique identifier of the edge device | [optional] |
| **remote_name_displayable** | **str** |  | [optional] |
| **room_id** | **str** | Unique identifier for the room | [optional] |
| **monitored_session_id** | **str** | The sessionID being monitored | [optional] |
| **monitored_participant_id** | **str** |  | [optional] |
| **callback_user_name** | **str** | The name of the user requesting a call back | [optional] |
| **callback_numbers** | **list[str]** | List of numbers to callback | [optional] |
| **callback_scheduled_time** | **datetime** | Scheduled callback date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **script_id** | **str** | Scheduled callback date/time, Date time is represented as an ISO-8601 string.  | [optional] |
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
{: class="table table-striped"}


