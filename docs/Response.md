# Response

## Response

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **version** | int | Version number required for updates. | [optional] |
| **libraries** | [list[DomainEntityRef]](DomainEntityRef) | One or more libraries response is associated with. | |
| **texts** | [list[ResponseText]](ResponseText) | One or more texts associated with the response. | |
| **created_by** | [User](User) | User that created the response | [optional] |
| **date_created** | datetime | The date and time the response was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **interaction_type** | str | The interaction type for this response. | [optional] |
| **substitutions** | [list[ResponseSubstitution]](ResponseSubstitution) | Details about any text substitutions used in the texts for this response. | [optional] |
| **substitutions_schema** | [JsonSchemaDocument](JsonSchemaDocument) | Metadata about the text substitutions in json schema format. | [optional] |
| **response_type** | str | The response type represented by the response. | [optional] |
| **messaging_template** | [MessagingTemplate](MessagingTemplate) | An optional messaging template definition for responseType.MessagingTemplate. | [optional] |
| **assets** | [list[AddressableEntityRef]](AddressableEntityRef) | Assets used in the response | [optional] |
| **footer** | [FooterTemplate](FooterTemplate) | Footer template definition for responseType.Footer. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 243.0.0_
