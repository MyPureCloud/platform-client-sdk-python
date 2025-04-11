# AgentDirectRoutingBackupSettings

## AgentDirectRoutingBackupSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | str | ID of queue to be used as backup. If queueId and userId are both specified, queue behaves as secondary backup. | [optional] |
| **user_id** | str | ID of user to be used as backup. If queueId and userId are both specified, user behaves as primary backup. | [optional] |
| **wait_for_agent** | bool | Flag indicating if Direct Routing interactions should wait for Direct Routing agent or go immediately to selected backup. | [optional] |
| **agent_wait_seconds** | int | Time (in seconds) that a Direct Routing interaction will wait for Direct Routing agent before going to selected backup. Valid range [60, 864000]. | [optional] |
| **backed_up_users** | list[str] | Set of users that this user is a backup for. | [optional] |



_PureCloudPlatformClientV2 226.0.0_
