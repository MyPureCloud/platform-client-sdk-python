# NuanceBot

## NuanceBot

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Nuance bot Id | |
| **name** | str | Nuance bot name | |
| **integration_id** | str | The Integration Id for this bot | |
| **nuance_organization** | [NuanceOrganization](NuanceOrganization) | The Nuance Organization for this bot | |
| **application** | [NuanceApplication](NuanceApplication) | The Application for this bot | |
| **nuance_environment** | [NuanceEnvironment](NuanceEnvironment) | The environment of the Nuance bot | |
| **geography** | [NuanceGeography](NuanceGeography) | The Geography of the Nuance bot | |
| **credentials** | [list[NuanceBotCredentials]](NuanceBotCredentials) | client ID/Secret objects for the credentials that execute this Nuance bot | [optional] |
| **variables** | [list[NuanceBotVariable]](NuanceBotVariable) | List of available variables in this Nuance bot.  When querying, use the &#39;expand&#x3D;variables&#39; query param to populate this value | [optional] |
| **transfer_nodes** | [list[NuanceBotTransferNode]](NuanceBotTransferNode) | List of transferNodes in this Nuance bot.  When querying, use the &#39;expand&#x3D;transferNodes&#39; query param to populate this value | [optional] |
| **locales** | list[str] | List of locales associated with this Nuance bot.  Generally in the ISO format such as &#39;en-US&#39; | [optional] |
| **channels** | [list[NuanceChannel]](NuanceChannel) | List of channels associated with this Nuance bot. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
