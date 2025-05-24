# ContactIdentifier

## ContactIdentifier

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division** | [WritableStarrableDivision](WritableStarrableDivision) | The division to which this entity belongs. | [optional] |
| **type** | str | The type of this identifier | |
| **value** | str | The string value of the identifier. Will vary in syntax by type. | |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_source** | [ExternalSource](ExternalSource) | The External Source ID of the identifier | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
