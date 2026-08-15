# AgenticVirtualAgentRepetitionCheck

## AgenticVirtualAgentRepetitionCheck

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | Whether this check looks for repetition in user messages or agent responses. | |
| **messages** | int | The number of prior messages of the specified type to compare for repetition. | |
| **similarity** | str | The similarity category compared to the Levenshtein result that triggers this check&#39;s instruction. | |
| **instruction** | str | The instruction added to the virtual agent&#39;s turn when message similarity matches the configured category. | |



_PureCloudPlatformClientV2 264.0.0_
