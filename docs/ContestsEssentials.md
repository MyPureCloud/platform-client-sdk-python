# ContestsEssentials

## ContestsEssentials

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **title** | str | The Contest title | |
| **status** | str | The Contest status | [optional] |
| **date_start** | date | Start date of the contest. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **date_end** | date | End date of the contest. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **profile** | [ContestProfile](ContestProfile) | The performance profile | [optional] |
| **participant_count** | int | The Number of participants in the contest | [optional] |
| **date_announced** | datetime | The Contest&#39;s Announcement datetime. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_finalized** | datetime | The Contest&#39;s finalize datetime, returned when a contest is complete. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_cancelled** | datetime | The Contest&#39;s cancelled datetime, returned when a contest is complete. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The Contest&#39;s last modified datetime. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_scores_modified** | datetime | The datetime the contest scores were last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **metrics** | [list[ContestMetrics]](ContestMetrics) | The Contest&#39;s Metrics | |
| **requesting_participant_contest_info** | [ContestRequesingParticipantDailyInfo](ContestRequesingParticipantDailyInfo) | The Most Recent Contest Info for the requesting participant | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 243.0.0_
