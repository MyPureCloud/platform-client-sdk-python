# Queue

## Queue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **description** | str | The queue description. | [optional] |
| **date_created** | datetime | The date the queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date of the last modification to the queue. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | str | The ID of the user that last modified the queue. | [optional] |
| **created_by** | str | The ID of the user that created the queue. | [optional] |
| **member_count** | int | The total number of members in the queue. | [optional] |
| **user_member_count** | int | The number of user members (i.e., non-group members) in the queue. | [optional] |
| **joined_member_count** | int | The number of joined members in the queue. | [optional] |
| **media_settings** | [QueueMediaSettings](QueueMediaSettings) | The media settings for the queue. | [optional] |
| **routing_rules** | [list[RoutingRule]](RoutingRule) | The routing rules for the queue, used for Preferred Agent Routing. | [optional] |
| **conditional_group_routing** | [ConditionalGroupRouting](ConditionalGroupRouting) | The Conditional Group Routing settings for the queue. | [optional] |
| **bullseye** | [Bullseye](Bullseye) | The bullseye settings for the queue. | [optional] |
| **scoring_method** | str | The Scoring Method for the queue. | [optional] |
| **last_agent_routing_mode** | str | The Last Agent Routing Mode for the queue. | [optional] |
| **acw_settings** | [AcwSettings](AcwSettings) | The ACW settings for the queue. | [optional] |
| **skill_evaluation_method** | str | The skill evaluation method to use when routing conversations. | [optional] |
| **member_groups** | [list[MemberGroup]](MemberGroup) | The groups of agents associated with the queue, if any.  Queue membership will update to match group membership changes. | [optional] |
| **queue_flow** | [DomainEntityRef](DomainEntityRef) | The in-queue flow to use for call conversations waiting in queue. | [optional] |
| **email_in_queue_flow** | [DomainEntityRef](DomainEntityRef) | The in-queue flow to use for email conversations waiting in queue. | [optional] |
| **message_in_queue_flow** | [DomainEntityRef](DomainEntityRef) | The in-queue flow to use for message conversations waiting in queue. | [optional] |
| **whisper_prompt** | [DomainEntityRef](DomainEntityRef) | The prompt used for whisper on the queue, if configured. | [optional] |
| **on_hold_prompt** | [DomainEntityRef](DomainEntityRef) | The audio to be played when calls on this queue are on hold. If not configured, the default on-hold music will play. | [optional] |
| **auto_answer_only** | bool | Specifies whether the configured whisper should play for all ACD calls, or only for those which are auto-answered. | [optional] |
| **canned_response_libraries** | [CannedResponseLibraries](CannedResponseLibraries) | Canned response library IDs and mode with which they are associated with the queue | [optional] |
| **enable_transcription** | bool | Indicates whether voice transcription is enabled for this queue. | [optional] |
| **enable_audio_monitoring** | bool | Indicates whether audio monitoring is enabled for this queue. | [optional] |
| **enable_manual_assignment** | bool | Indicates whether manual assignment is enabled for this queue. | [optional] |
| **agent_owned_routing** | [AgentOwnedRouting](AgentOwnedRouting) | The Agent Owned Routing settings for the queue | [optional] |
| **direct_routing** | [DirectRouting](DirectRouting) | The Direct Routing settings for the queue | [optional] |
| **calling_party_name** | str | The name to use for caller identification for outbound calls from this queue. | [optional] |
| **calling_party_number** | str | The phone number to use for caller identification for outbound calls from this queue. | [optional] |
| **default_scripts** | [dict(str, Script)](Script) | The default script Ids for the communication types. | [optional] |
| **outbound_messaging_addresses** | [QueueMessagingAddresses](QueueMessagingAddresses) | The messaging addresses for the queue. | [optional] |
| **outbound_email_address** | [QueueEmailAddress](QueueEmailAddress) | The default email address to use for outbound email from this queue. | [optional] |
| **peer_id** | str | The ID of an associated external queue. | [optional] |
| **suppress_in_queue_call_recording** | bool | Indicates whether recording in-queue calls is suppressed for this queue. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
