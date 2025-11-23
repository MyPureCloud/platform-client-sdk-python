# ArchitectExportJobStateResponse

## ArchitectExportJobStateResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str | Status of the Architect Export Job | [optional] |
| **command** | str | The command executed by the Architect Job | [optional] |
| **download_url** | str | The signed URL for downloading exported Architect data. If more than one flow was exported as part of the job, the URL provides a zipped folder containing all flows. | [optional] |
| **messages** | [list[ArchitectJobMessage]](ArchitectJobMessage) | Warnings and Errors messages of the Architect Job | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 244.0.0_
