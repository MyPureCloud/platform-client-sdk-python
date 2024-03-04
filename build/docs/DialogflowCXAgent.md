---
title: DialogflowCXAgent
---
## DialogflowCXAgent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **project** | [**DialogflowCXProject**](DialogflowCXProject.html) | The project this Dialogflow CX agent belongs to. | [optional] |
| **languages** | **list[str]** | The supported languages of the Dialogflow CX agent.  Each value will be a language code in the country-locale format. e.g. en-us, es-us, fr-ca, etc. | [optional] |
| **environments** | [**list[DialogflowCXEnvironment]**](DialogflowCXEnvironment.html) | Available environments for this CX agent. | [optional] |
| **integration** | [**DomainEntityRef**](DomainEntityRef.html) | The Integration this Dialogflow CX agent was referenced from. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


