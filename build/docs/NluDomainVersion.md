# NluDomainVersion

## NluDomainVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **domain** | [NluDomain](NluDomain) | The NLU domain of the version. | [optional] |
| **description** | str | The description of the NLU domain version. | [optional] |
| **language** | str | The language that the NLU domain version supports. | |
| **published** | bool | Whether this NLU domain version has been published. | [optional] |
| **date_created** | datetime | The date when the NLU domain version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date when the NLU domain version was updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_trained** | datetime | The date when the NLU domain version was trained. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_published** | datetime | The date when the NLU domain version was published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **training_status** | str | The training status of the NLU domain version. | [optional] |
| **evaluation_status** | str | The evaluation status of the NLU domain version. | [optional] |
| **intents** | [list[IntentDefinition]](IntentDefinition) | The intents defined for this NLU domain version. | [optional] |
| **entity_types** | [list[NamedEntityTypeDefinition]](NamedEntityTypeDefinition) | The entity types defined for this NLU domain version. | [optional] |
| **entities** | [list[NamedEntityDefinition]](NamedEntityDefinition) | The entities defined for this NLU domain version.This field is mutually exclusive with entityTypeBindings | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 223.0.0_
