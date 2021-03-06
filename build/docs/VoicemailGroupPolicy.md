---
title: VoicemailGroupPolicy
---
## VoicemailGroupPolicy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** |  | [optional] |
| **group** | [**Group**](Group.html) | The group associated with the policy | [optional] |
| **enabled** | **bool** | Whether voicemail is enabled for the group | [optional] |
| **send_email_notifications** | **bool** | Whether email notifications are sent to group members when a new voicemail is received | [optional] |
| **disable_email_pii** | **bool** | Removes any PII from group emails. This is overridden by the analogous organization configuration value. This is always true if HIPAA is enabled or unknown for an organization. | [optional] |
| **rotate_calls_secs** | **int** | How many seconds to ring before rotating to the next member in the group | [optional] |
| **stop_ringing_after_rotations** | **int** | How many rotations to go through | [optional] |
| **overflow_group_id** | **str** |  A fallback group to contact when all of the members in this group did not answer the call. | [optional] |
| **group_alert_type** | **str** | Specifies if the members in this group should be contacted randomly, in a specific order, or by round-robin. | [optional] |
{: class="table table-striped"}


