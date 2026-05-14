# MediaParticipantRequest

## MediaParticipantRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **wrapup** | [WrapupInput](WrapupInput) | Wrap-up to assign to this participant. | [optional] |
| **state** | str | The state to update to set for this participant&#39;s communications.  Possible values are: &#39;connected&#39; and &#39;disconnected&#39;. | [optional] |
| **recording** | bool | True to enable ad-hoc recording of this participant, otherwise false to disable recording. | [optional] |
| **muted** | bool | True to mute this conversation participant. | [optional] |
| **confined** | bool | True to confine this conversation participant.  Should only be used for ad-hoc conferences | [optional] |
| **held** | bool | True to hold this conversation participant. | [optional] |
| **wrapup_skipped** | bool | True to skip wrap-up for this participant. | [optional] |
| **resume_time** | datetime | Time to resume parked communication. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 257.1.0_
