# Document

## Document

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **change_number** | int |  | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_uploaded** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **content_uri** | str |  | [optional] |
| **workspace** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **uploaded_by** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **sharing_uri** | str |  | [optional] |
| **content_type** | str |  | [optional] |
| **content_length** | int |  | [optional] |
| **system_type** | str |  | [optional] |
| **filename** | str |  | [optional] |
| **page_count** | int |  | [optional] |
| **read** | bool |  | [optional] |
| **caller_address** | str |  | [optional] |
| **receiver_address** | str |  | [optional] |
| **tags** | list[str] |  | [optional] |
| **tag_values** | [list[TagValue]](TagValue) |  | [optional] |
| **attributes** | [list[DocumentAttribute]](DocumentAttribute) |  | [optional] |
| **thumbnails** | [list[DocumentThumbnail]](DocumentThumbnail) |  | [optional] |
| **upload_status** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **upload_destination_uri** | str |  | [optional] |
| **upload_method** | str |  | [optional] |
| **lock_info** | [LockInfo](LockInfo) |  | [optional] |
| **acl** | list[str] | A list of permitted action rights for the user making the request | [optional] |
| **sharing_status** | str |  | [optional] |
| **download_sharing_uri** | str |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 234.0.0_
