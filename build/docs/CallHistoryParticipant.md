# CallHistoryParticipant

## CallHistoryParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The unique participant ID. | [optional] |
| **name** | str | The display friendly name of the participant. | [optional] |
| **address** | str | The participant address. | [optional] |
| **start_time** | datetime | The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_time** | datetime | The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **purpose** | str | The participant&#39;s purpose.  Values can be: &#39;agent&#39;, &#39;user&#39;, &#39;customer&#39;, &#39;external&#39;, &#39;acd&#39;, &#39;ivr | [optional] |
| **direction** | str | The participant&#39;s direction.  Values can be: &#39;inbound&#39; or &#39;outbound&#39; | [optional] |
| **ani** | str | The call ANI. | [optional] |
| **dnis** | str | The call DNIS. | [optional] |
| **user** | [User](User) | The PureCloud user for this participant. | [optional] |
| **queue** | [Queue](Queue) | The PureCloud queue for this participant. | [optional] |
| **group** | [Group](Group) | The group involved in the group ring call. | [optional] |
| **disconnect_type** | str | The reason the participant was disconnected from the conversation. | [optional] |
| **external_contact** | [ExternalContact](ExternalContact) | The PureCloud external contact | [optional] |
| **external_organization** | [ExternalOrganization](ExternalOrganization) | The PureCloud external organization | [optional] |
| **did_interact** | bool | Indicates whether the contact ever connected | [optional] |
| **sip_response_codes** | list[int] | Indicates SIP Response codes associated with the participant | [optional] |
| **flagged_reason** | str | The reason specifying why participant flagged the conversation. | [optional] |
| **outbound_campaign** | [Campaign](Campaign) | The outbound campaign associated with the participant | [optional] |



_PureCloudPlatformClientV2 219.1.0_
