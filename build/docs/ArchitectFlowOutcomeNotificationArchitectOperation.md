# ArchitectFlowOutcomeNotificationArchitectOperation

## ArchitectFlowOutcomeNotificationArchitectOperation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique identifier for this operation, as generated by the initiating client | [optional] |
| **complete** | bool | Indicates if the operation is complete | [optional] |
| **user** | [ArchitectFlowOutcomeNotificationUser](ArchitectFlowOutcomeNotificationUser) |  | [optional] |
| **client** | [ArchitectFlowOutcomeNotificationClient](ArchitectFlowOutcomeNotificationClient) |  | [optional] |
| **action_name** | str | The action being performed | [optional] |
| **action_status** | str | The action status | [optional] |
| **error_message** | str | The error message, if the action failed | [optional] |
| **error_code** | str | The error code, if the action failed | [optional] |
| **error_message_params** | [ArchitectFlowOutcomeNotificationErrorMessageParams](ArchitectFlowOutcomeNotificationErrorMessageParams) |  | [optional] |
| **error_details** | [list[ArchitectFlowOutcomeNotificationErrorDetail]](ArchitectFlowOutcomeNotificationErrorDetail) | The error details, if the action failed | [optional] |



_PureCloudPlatformClientV2 233.0.0_
