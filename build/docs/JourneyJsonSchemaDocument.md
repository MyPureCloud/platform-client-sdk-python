# JourneyJsonSchemaDocument

## JourneyJsonSchemaDocument

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schema** | str | The JSON Schema specification link. The only value currently supported is \&quot;http://json-schema.org/draft-04/schema#\&quot;. | |
| **title** | str | The title of the schema. Must be unique across all enabled External Event schemas. | |
| **description** | str | The schema description. | [optional] |
| **required** | list[str] | The list of required schema properties. All fields are optional unless listed. Optional fields can&#39;t be changed to required after the schema is saved. | [optional] |
| **properties** | dict(str, object) | The map of schema properties and their limits. | [optional] |



_PureCloudPlatformClientV2 257.1.0_
