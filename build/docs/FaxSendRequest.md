# FaxSendRequest

## FaxSendRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **addresses** | list[str] | A list of outbound fax dialing addresses. E.g. +13175555555 or 3175555555 | |
| **document_id** | str | DocumentId of Content Management artifact. If Content Management document is not used for faxing, documentId should be null | [optional] |
| **content_type** | str | The content type that is going to be uploaded. If Content Management document is used for faxing, contentType will be ignored | [optional] |
| **workspace** | [Workspace](Workspace) | Workspace in which the document should be stored. If Content Management document is used for faxing, workspace will be ignored | [optional] |
| **cover_sheet** | [CoverSheet](CoverSheet) | Data for coversheet generation. | [optional] |
| **time_zone_offset_minutes** | int | Time zone offset minutes from GMT | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_
