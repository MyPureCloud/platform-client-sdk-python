# MessageMediaData

## MessageMediaData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **url** | str | The location of the media, useful for retrieving it | [optional] |
| **media_type** | str | The detected internet media type of the the media object.  If null then the media type should be dictated by the url. | [optional] |
| **content_length_bytes** | int | The optional content length of the the media object, in bytes. | [optional] |
| **upload_url** | str | The URL returned to upload an attachment | [optional] |
| **status** | str | The status of the media, indicates if the media is in the process of uploading. If the upload fails, the media becomes invalid | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
