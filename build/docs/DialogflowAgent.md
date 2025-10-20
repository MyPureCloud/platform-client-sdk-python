# DialogflowAgent

## DialogflowAgent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **project** | [DialogflowProject](DialogflowProject) | The project this Dialogflow agent belongs to | [optional] |
| **languages** | list[str] | The supported languages of the Dialogflow agent | [optional] |
| **intents** | [list[DialogflowIntent]](DialogflowIntent) | An array of Intents associated with this agent | [optional] |
| **environments** | list[str] | Available environments for this agent | [optional] |
| **integration** | [DomainEntityRef](DomainEntityRef) | The Integration this Dialogflow agent was referenced from. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 241.0.0_
