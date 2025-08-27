# ResponseAsset

## ResponseAsset

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **content_length** | int | response asset size in bytes | [optional] |
| **content_location** | str | response asset location. | [optional] |
| **content_type** | str | MIME type of response asset | [optional] |
| **date_created** | datetime | Created date of the response asset. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User who created the response asset | [optional] |
| **date_modified** | datetime | Last modified date of the response asset. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User who last modified the response asset | [optional] |
| **responses** | [list[DomainEntityRef]](DomainEntityRef) | Canned responses actively using this asset | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 236.0.0_
