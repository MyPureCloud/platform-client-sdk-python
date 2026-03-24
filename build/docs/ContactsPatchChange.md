# ContactsPatchChange

## ContactsPatchChange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **field** | str | A JSONPath string, whose syntax is a strict subset of the JSONPath RFC 9535.  The root of the field string must be \&quot;$.\&quot; indicating a path from the root of the entity. You may only use dot-notation to access named fields. Examples: To select the &#x60;firstName&#x60; field of a Contact, use: \&quot;$.firstName\&quot;.To access object fields, use the top level object field name: \&quot;$.address\&quot;. To access nested field names, use the nested field name: \&quot;$.address.city\&quot;. Note: trying to patch both nested fields and their parent field is not allowed and will result in a 409 error response. | |
| **value** | object | The value which is applied to the selected field for the patch. Acceptable types are String, Integer, Boolean, Array, Map. | [optional] |
| **action** | str | The action of the operation.UpdateIfEmpty: Update if and only if the current value is emptyUpdate: Update the field unconditionally.UpdateIfExists: Update the field if and only if the existing field is not empty.AppendToCollection: Add new items to a collection, preserving existing data.Remove: Remove the current value unconditionally.RemoveFromCollection: Remove specified value from a collection. | |



_PureCloudPlatformClientV2 254.0.0_
