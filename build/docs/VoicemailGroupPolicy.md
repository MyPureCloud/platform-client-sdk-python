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
| **rotate_calls_secs** | **int** | How many seconds to ring before rotating to the next member in the group | [optional] |
| **stop_ringing_after_rotations** | **int** | How many rotations to go through | [optional] |
{: class="table table-striped"}


