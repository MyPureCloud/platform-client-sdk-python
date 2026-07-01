# V3SynchronizationUploadUrlResponse

## V3SynchronizationUploadUrlResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **file_id** | str | The unique identifier for the upload object. | [optional] |
| **file_name** | str | Name of the uploaded file. | [optional] |
| **metadata** | [V3SynchronizationUploadMetadata](V3SynchronizationUploadMetadata) | The metadata of the uploaded file | [optional] |
| **synchronization** | [V3SynchronizationRef](V3SynchronizationRef) | The synchronization of the file upload. | [optional] |
| **url** | str | Pre-signed URL to PUT the file to. | [optional] |
| **headers** | dict(str, str) | Required headers when uploading a file through PUT request to the URL. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 261.0.0_
