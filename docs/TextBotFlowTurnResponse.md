# TextBotFlowTurnResponse

## TextBotFlowTurnResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the bot flow turn. If additional turns are needed, supply this ID as the previous turn in your next turn request. | |
| **previous_turn** | [TextBotTurnReference](TextBotTurnReference) | The reference to a previous turn, if applicable. | [optional] |
| **prompts** | [TextBotOutputPrompts](TextBotOutputPrompts) | The output prompts for this turn. | [optional] |
| **next_action_type** | str | Indicates the suggested next action. If appropriate, the matching output event object includes additional information. | |
| **next_action_disconnect** | [TextBotDisconnectAction](TextBotDisconnectAction) | The next action directive for this turn if it is a Disconnect type. | [optional] |
| **next_action_wait_for_input** | [TextBotWaitForInputAction](TextBotWaitForInputAction) | The next action directive for this turn if it is a WaitForInput type. | [optional] |
| **next_action_exit** | [TextBotExitAction](TextBotExitAction) | The next action directive for this turn if it is an Exit type. | [optional] |



_PureCloudPlatformClientV2 213.0.0_
