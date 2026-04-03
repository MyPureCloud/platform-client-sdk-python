# V3SynchronizationUploadUrlRequest

## V3SynchronizationUploadUrlRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **file_name** | str | Name of the file to upload. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%&#x60;]\&quot;&gt;[~&lt;#| | |
| **content_md5** | str | Content MD5 of the file to upload encoded in base64, example: \&quot;f8VicOenD6gaWTW3Lqy+KQ&#x3D;&#x3D;\&quot;. Not the hexadecimal representation as \&quot;7fc56270e7a70fa81a5935b72eacbe29\&quot;. | [optional] |
| **content_type** | str | The content type of the file to upload | [optional] |
| **content_length** | int | The length of the file to upload in bytes | [optional] |
| **metadata** | [V3SynchronizationUploadMetadata](V3SynchronizationUploadMetadata) | The metadata of the file to upload | [optional] |



_PureCloudPlatformClientV2 255.0.0_
