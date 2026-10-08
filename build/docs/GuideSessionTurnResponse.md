# GuideSessionTurnResponse

## GuideSessionTurnResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **response** | [GuideSessionTurnResponseData](GuideSessionTurnResponseData) | The response content for this turn. | [optional] |
| **status** | str | The status of the turn. | [optional] |
| **result** | str | The result of the turn. | [optional] |
| **output_variables** | [list[GuideSessionVariable]](GuideSessionVariable) | The output variables for this turn. | [optional] |
| **invocation_id** | str | Invocation ID for this turn. | [optional] |
| **invocations** | [list[GuideSessionTurnInvocationResponse]](GuideSessionTurnInvocationResponse) | The invocations for this turn. | [optional] |
| **context** | [GuideSessionTurnResponseContext](GuideSessionTurnResponseContext) | The context for this turn, including conversation custom attribute updates. | [optional] |



_PureCloudPlatformClientV2 269.0.0_
