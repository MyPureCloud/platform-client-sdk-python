# WfmUserNotification

## WfmUserNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The immutable globally unique identifier for the object. | |
| **mutable_group_id** | str | The group ID of the notification (mutable, may change  on update) | |
| **timestamp** | datetime | The timestamp for this notification. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **type** | str | The type of this notification | [optional] |
| **shift_trade** | [ShiftTradeNotification](ShiftTradeNotification) | A shift trade notification.  Only set if type &#x3D;&#x3D; ShiftTrade | [optional] |
| **time_off_request** | [TimeOffRequestNotification](TimeOffRequestNotification) | A time off request notification.  Only set if type &#x3D;&#x3D; TimeOffRequest | [optional] |
| **adherence_explanation** | [AdherenceExplanationNotification](AdherenceExplanationNotification) | An adherence explanation notification.  Only set if type &#x3D;&#x3D; AdherenceExplanation | [optional] |
| **alternative_shift** | [AlternativeShiftNotification](AlternativeShiftNotification) | An alternative shift trade notification.  Only set if type &#x3D;&#x3D; AlternativeShift | [optional] |
| **marked_as_read** | bool | Whether this notification has been marked \&quot;read\&quot; | |
| **agent_notification** | bool | Whether this notification is for an agent | [optional] |
| **other_notification_ids_in_group** | list[str] | Other notification IDs in group.  This field is only populated in real-time notifications | [optional] |



_PureCloudPlatformClientV2 211.1.0_
