# AgentIntegrationsResponse

## AgentIntegrationsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **agent** | [UserReference](UserReference) | The user associated with the integrations | |
| **selected_integration** | [WfmIntegrationReference](WfmIntegrationReference) | The integration selected for the agent. If not set, no integration will be used for the agent | [optional] |
| **user_selected** | bool | Whether the integration association has been manually selected | [optional] |
| **associated_integrations** | [list[AgentIntegrationAssociationResponse]](AgentIntegrationAssociationResponse) | The list of integrations associated with the agent | |



_PureCloudPlatformClientV2 229.0.0_
