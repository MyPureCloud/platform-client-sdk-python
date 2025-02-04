# CachedMediaItem

## CachedMediaItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The unique identifier for the cached media. | [optional] |
| **url** | str | The URL that represents the external media that has been cached | [optional] |
| **download_url** | str | A URL to fetch the cached media | [optional] |
| **media_type** | str | The media type for the URL | [optional] |
| **content_length_bytes** | int | The content length of the media represented by the URL, in bytes. | [optional] |
| **date_created** | datetime | The date the cached item was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_expires** | datetime | The date the cached item expires and will be removed from the cache. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
