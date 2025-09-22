# CampaignInteraction

## CampaignInteraction

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **campaign** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **agent** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **contact** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **destination_address** | str |  | [optional] |
| **active_preview_call** | bool | Boolean value if there is an active preview call on the interaction | [optional] |
| **last_active_preview_wrapup_time** | datetime | The time when the last preview of the interaction was wrapped up. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **creation_time** | datetime | The time when dialer created the interaction. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **call_placed_time** | datetime | The time when the agent or system places the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **call_routed_time** | datetime | The time when the agent was connected to the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **preview_connected_time** | datetime | The time when the customer and routing participant are connected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **queue** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **script** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **disposition** | str | Describes what happened with call analysis for instance: disposition.classification.callable.person, disposition.classification.callable.noanswer | [optional] |
| **caller_name** | str |  | [optional] |
| **caller_address** | str |  | [optional] |
| **preview_pop_delivered_time** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation** | [ConversationBasic](ConversationBasic) |  | [optional] |
| **dialer_system_participant_id** | str | conversation participant id that is the dialer system participant to monitor the call from dialer perspective | [optional] |
| **dialing_mode** | str |  | [optional] |
| **skills** | [list[DomainEntityRef]](DomainEntityRef) | Any skills that are attached to the call for routing | [optional] |



_PureCloudPlatformClientV2 237.0.0_
