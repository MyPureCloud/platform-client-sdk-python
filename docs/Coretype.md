# Coretype

## Coretype

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **version** | int | A positive integer denoting the core type&#39;s version | [optional] |
| **date_created** | datetime | The date the core type was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **schema** | [Schema](Schema) | The core type&#39;s built-in schema | [optional] |
| **current** | bool | A boolean indicating if the core type&#39;s version is the current one in use by the system | [optional] |
| **validation_fields** | list[str] | An array of strings naming the fields of the core type subject to validation.  Validation constraints are specified by a schema author using the core type. | [optional] |
| **validation_limits** | [ValidationLimits](ValidationLimits) | A structure denoting the system-imposed minimum and maximum string length (for text-based core types) or numeric values (for number-based) core types.  For example, the validationLimits for a text-based core type specify the min/max values for a minimum string length (minLength) constraint supplied by a schemaauthor on a text field.  Similarly, the maxLength&#39;s min/max specifies maximum string length constraint supplied by a schema author for the same field. | [optional] |
| **item_validation_fields** | list[str] | Specific to the \&quot;tag\&quot; core type, this is an array of strings naming the tag item fields of the core type subject to validation | [optional] |
| **item_validation_limits** | [ItemValidationLimits](ItemValidationLimits) | A structure denoting the system-imposed minimum and maximum string length for string-array based core types such as \&quot;tag\&quot; and \&quot;enum\&quot;.  Forexample, the validationLimits for a schema field using a tag core type specify the min/max values for a minimum string length (minLength) constraint supplied by a schema author on individual tags.  Similarly, the maxLength&#39;s min/max specifies maximum string length constraint supplied by a schema author for the same field&#39;s tags. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
