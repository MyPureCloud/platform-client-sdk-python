# AnalyticsParticipant

## AnalyticsParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **external_contact_id** | str | External contact identifier | [optional] |
| **external_organization_id** | str | External organization identifier | [optional] |
| **flagged_reason** | str | Reason for which participant flagged conversation | [optional] |
| **participant_id** | str | Unique identifier for the participant | [optional] |
| **participant_name** | str | A human readable name identifying the participant | [optional] |
| **purpose** | str | The participant&#39;s purpose | [optional] |
| **screen_recording** | bool | Flag determining if a screen recording was started or not | [optional] |
| **team_id** | str | The team ID the user is a member of | [optional] |
| **user_id** | str | Unique identifier for the user | [optional] |
| **sessions** | [list[AnalyticsSession]](AnalyticsSession) | List of sessions associated to this participant | [optional] |
| **attributes** | dict(str, str) | List of attributes associated to this participant | [optional] |



_PureCloudPlatformClientV2 217.0.0_
