# ResponseDivisionView

## ResponseDivisionView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **response_type** | str | The response type represented by the response. | [optional] |
| **libraries** | [list[LibraryDivisionView]](LibraryDivisionView) | One or more libraries response is associated with. | [optional] |
| **substitutions** | [list[ResponseSubstitution]](ResponseSubstitution) | Details about any text substitutions used in the texts for this response. | [optional] |
| **substitutions_schema** | [JsonSchemaDocument](JsonSchemaDocument) | Metadata about the text substitutions in json schema format. | [optional] |
| **messaging_template** | [MessagingTemplate](MessagingTemplate) | An optional messaging template definition for responseType.MessagingTemplate. | [optional] |
| **form** | [Form](Form) | Form template definition for responseType.Form. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 265.0.0_
