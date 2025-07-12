# MediaEndpointStatistics

## MediaEndpointStatistics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **trunk** | [MediaStatisticsTrunkInfo](MediaStatisticsTrunkInfo) | Trunk information utilized when creating the media endpoint | [optional] |
| **station** | [NamedEntity](NamedEntity) | Station information associated with media endpoint | [optional] |
| **user** | [NamedEntity](NamedEntity) | User information associated media endpoint | [optional] |
| **ice** | [MediaIceStatistics](MediaIceStatistics) | The ICE protocol statistics and details. Reference: https://www.rfc-editor.org/rfc/rfc5245 | [optional] |
| **rtp** | [MediaRtpStatistics](MediaRtpStatistics) | Statistics of sent and received RTP. Reference: https://www.rfc-editor.org/rfc/rfc3550 | [optional] |
| **reconnect_attempts** | int | Media reconnect attempt count | [optional] |
| **source_type** | str | Source type of media endpoint | [optional] |
| **client_info** | [MediaStatisticsClientInfo](MediaStatisticsClientInfo) | Client information associated with media endpoint | [optional] |



_PureCloudPlatformClientV2 233.0.0_
