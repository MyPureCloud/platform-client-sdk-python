# GamificationContestPrizeImageUploadUrlRequest

## GamificationContestPrizeImageUploadUrlRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **file_name** | str | Name of the file to upload. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%&#x60;]\&quot;&gt;[~&lt;#| | [optional] |
| **content_md5** | str | Content MD5 of the file to upload | [optional] |
| **signed_url_timeout_seconds** | int | The number of seconds the presigned URL is valid for (from 1 to 604800 seconds). If none provided, defaults to 600 seconds | [optional] |
| **content_type** | str | The content type of the file to upload. | |
| **content_length** | int | The size of the file to upload. | |
| **server_side_encryption** | str |  | [optional] |



_PureCloudPlatformClientV2 235.0.0_
