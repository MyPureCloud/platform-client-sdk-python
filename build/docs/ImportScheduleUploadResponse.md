---
title: ImportScheduleUploadResponse
---
## ImportScheduleUploadResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **upload_key** | **str** | The key to pass to the secondary request to start processing of the upload | [optional] |
| **url** | **str** | The url to which to PUT the upload body | [optional] |
| **headers** | **dict(str, str)** | Required headers for the PUT request to the url | [optional] |
| **upload_body_schema** | [**ImportScheduleUploadSchema**](ImportScheduleUploadSchema.html) | Always null. Defines the schema of the json body to be PUT to the url. The json body should be gzip encoded before uploading | [optional] |
{: class="table table-striped"}


