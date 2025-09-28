# StaCategory

## StaCategory

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | The description of the category | [optional] |
| **interaction_type** | str | The type of interaction the category will apply to | |
| **criteria** | [Operand](Operand) | A collection of conditions joined together by logical operation to provide more refined filtering of conversations | |
| **created_by** | [AddressableEntityRef](AddressableEntityRef) | The user who created the record | [optional] |
| **date_created** | datetime | The creation date of the record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [AddressableEntityRef](AddressableEntityRef) | The user who last modified the record | [optional] |
| **date_modified** | datetime | The last modified date of the record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 238.0.0_
