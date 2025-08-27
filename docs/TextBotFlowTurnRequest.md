# TextBotFlowTurnRequest

## TextBotFlowTurnRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **previous_turn** | [TextBotTurnReference](TextBotTurnReference) | The reference to a previous turn if appropriate, used to avoid race conditions. | [optional] |
| **input_event_type** | str | Indicates the type of input event being requested. If appropriate, fill out the matching user input object details on this request. | |
| **input_event_user_input** | [TextBotUserInputEvent](TextBotUserInputEvent) | The data for the input event of this turn if it is a user input event. Only one inputEvent may be set. | [optional] |
| **input_event_error** | [TextBotErrorInputEvent](TextBotErrorInputEvent) | The data for the input event of this turn if it is an error event. Only one inputEvent may be set. | [optional] |



_PureCloudPlatformClientV2 236.0.0_
