# UploadAttachmentRequest

## UploadAttachmentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Name of the attachment file to upload. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%&#x60;]\&quot;&gt;[~&lt;#| | |
| **content_length_bytes** | int | The length of the file to upload in bytes | |
| **content_md5** | str | Content MD5 of the file to upload | [optional] |
| **inline_image** | bool | Whether or not the attachment should be attached inline | [optional] |



_PureCloudPlatformClientV2 265.0.0_
