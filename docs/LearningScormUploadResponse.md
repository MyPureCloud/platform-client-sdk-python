# LearningScormUploadResponse

## LearningScormUploadResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str | The status of the SCORM package | [optional] |
| **upload_url** | str | The pre-signed URL. Use it with headers below to upload file to S3 | [optional] |
| **headers** | dict(str, str) | The additional headers that need to be included in the upload request | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
