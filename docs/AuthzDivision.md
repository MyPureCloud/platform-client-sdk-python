# AuthzDivision

## AuthzDivision

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | A helpful description for the division. | |
| **home_division** | bool | A flag indicating whether this division is the \&quot;Home\&quot; (default) division. Cannot be modified and any supplied value will be ignored on create or update. | [optional] |
| **object_counts** | dict(str, int) | A count of objects in this division, grouped by type. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 232.0.0_
