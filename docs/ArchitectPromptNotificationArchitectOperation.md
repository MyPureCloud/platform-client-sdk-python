# ArchitectPromptNotificationArchitectOperation

## ArchitectPromptNotificationArchitectOperation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique identifier for this operation, as generated by the initiating client | [optional] |
| **complete** | bool | Indicates if the operation is complete | [optional] |
| **user** | [ArchitectPromptNotificationUser](ArchitectPromptNotificationUser) |  | [optional] |
| **client** | [ArchitectPromptNotificationClient](ArchitectPromptNotificationClient) |  | [optional] |
| **action_name** | str | The action being performed | [optional] |
| **action_status** | str | The action status | [optional] |
| **error_message** | str | The error message, if the action failed | [optional] |
| **error_code** | str | The error code, if the action failed | [optional] |
| **error_message_params** | [ArchitectPromptNotificationErrorMessageParams](ArchitectPromptNotificationErrorMessageParams) |  | [optional] |
| **error_details** | [list[ArchitectPromptNotificationErrorDetail]](ArchitectPromptNotificationErrorDetail) | The error details, if the action failed | [optional] |



_PureCloudPlatformClientV2 217.0.0_