# MediaStatisticsPostRequest

## MediaStatisticsPostRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **source_type** | str | Source type of media endpoint | |
| **client_info** | [MediaStatisticsClientInfo](MediaStatisticsClientInfo) | Client information associated with media endpoint | [optional] |
| **rtp** | [MediaRtpStatistics](MediaRtpStatistics) | Statistics of sent and received RTP. Reference: https://www.rfc-editor.org/rfc/rfc3550 | |
| **reconnect_attempts** | int | Media reconnect attempt count | [optional] |
| **date_created** | datetime | Media endpoint statistics creation time. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 242.0.0_
