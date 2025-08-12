# Station

## Station

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str |  | [optional] |
| **status** | str |  | [optional] |
| **user_id** | str | The Id of the user currently logged in and associated with the station. | [optional] |
| **web_rtc_user_id** | str | The Id of the user configured for the station if it is of type inin_webrtc_softphone. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **primary_edge** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **secondary_edge** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **type** | str |  | [optional] |
| **line_appearance_id** | str |  | [optional] |
| **web_rtc_media_dscp** | int | The default or configured value of media dscp for the station. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **web_rtc_persistent_enabled** | bool | The default or configured value of persistent connection setting for the station. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **web_rtc_force_turn** | bool | Whether the station is configured to require TURN for routing WebRTC calls. Empty if station type is not inin_webrtc_softphone. | [optional] |
| **web_rtc_call_appearances** | int | The number of call appearances on the station. | [optional] |
| **web_rtc_require_media_helper** | bool | True when the media helper required. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.0.0_
