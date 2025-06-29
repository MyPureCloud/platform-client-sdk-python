# Geolocation

## Geolocation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **type** | str | A string used to describe the type of client the geolocation is being updated from e.g. ios, android, web, etc. | [optional] |
| **primary** | bool | A boolean used to tell whether or not to set this geolocation client as the primary on a PATCH | [optional] |
| **latitude** | float |  | [optional] |
| **longitude** | float |  | [optional] |
| **country** | str |  | [optional] |
| **region** | str |  | [optional] |
| **city** | str |  | [optional] |
| **locations** | [list[LocationDefinition]](LocationDefinition) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 232.0.0_
