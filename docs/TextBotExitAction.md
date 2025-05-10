# TextBotExitAction

## TextBotExitAction

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **reason** | str | The reason for the exit. | |
| **reason_extended_info** | str | Extended information related to the reason, if available. | [optional] |
| **active_intent** | str | The active intent at the time of the exit. | [optional] |
| **flow_location** | [TextBotFlowLocation](TextBotFlowLocation) | Describes where in the Bot Flow the user was when the exit occurred. | [optional] |
| **output_data** | [TextBotInputOutputData](TextBotInputOutputData) | The output data for the bot flow. | [optional] |
| **flow_outcomes** | [list[TextBotFlowOutcome]](TextBotFlowOutcome) | The list of Flow Outcomes for the bot flow and their details. | [optional] |



_PureCloudPlatformClientV2 228.0.0_
