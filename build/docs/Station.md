---
title: Station
---
## Station

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **description** | **str** |  | [optional] |
| **status** | **str** |  | [optional] |
| **user_id** | **str** | The Id of the user currently logged in and associated with the station. | [optional] |
| **web_rtc_user_id** | **str** | The Id of the user configured for the station if it is of type inin_webrtc_softphone. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **primary_edge** | [**UriReference**](UriReference.html) |  | [optional] |
| **secondary_edge** | [**UriReference**](UriReference.html) |  | [optional] |
| **type** | **str** |  | [optional] |
| **line_appearance_id** | **str** |  | [optional] |
| **web_rtc_media_dscp** | **int** | The default or configured value of media dscp for the station. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **web_rtc_persistent_enabled** | **bool** | The default or configured value of persistent connection setting for the station. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


