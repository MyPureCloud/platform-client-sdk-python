# ConversationJsonSchemaRequest

## ConversationJsonSchemaRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schema** | str | The JSON Schema specification link. The only value currently supported is \&quot;http://json-schema.org/draft-04/schema#\&quot;. | |
| **title** | str | The title of the schema. Must be unique across all enabled Custom Attributes schemas. | |
| **description** | str | The schema description. | [optional] |
| **required** | list[str] | The list of required schema properties. All fields are optional unless listed. New fields added after initial schema creation must be optional before being able to update to required. | [optional] |
| **properties** | dict(str, object) | The map of schema properties and their limits. | |



_PureCloudPlatformClientV2 254.0.0_
