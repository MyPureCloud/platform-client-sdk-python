# ContestsResponse

## ContestsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division** | [WritableDivision](WritableDivision) | The division for this performance profile associate to | [optional] |
| **title** | str | The Contest title | |
| **description** | str | The Contest description | |
| **date_start** | date | Start date of the contest. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **date_end** | date | End date of the contest. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **winning_criteria** | str | The Contest winning criteria | |
| **date_announced** | datetime | The Contest&#39;s Announcement Datetime. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **announcement_timezone** | str | The Contest&#39;s Announcement Timezone. Valid values are strings of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London | |
| **anonymization** | str | The Contest anonymization | |
| **metrics** | [list[ContestMetrics]](ContestMetrics) | The Contest&#39;s Metrics | |
| **prizes** | [list[ContestPrizes]](ContestPrizes) | The Contest Prizes | |
| **version** | int | The Contest Version | [optional] |
| **created_by** | [UserReference](UserReference) | The creator of the contest | [optional] |
| **profile** | [ContestProfile](ContestProfile) | The performance profile | [optional] |
| **participants** | [list[UserReference]](UserReference) | The Contest&#39;s participants | [optional] |
| **status** | str | The Contest status | [optional] |
| **participant_count** | int | The Number of participants in the contest | [optional] |
| **date_finalized** | datetime | The Contest&#39;s finalize datetime, returned when a contest is complete. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_cancelled** | datetime | The Contest&#39;s cancelled datetime, returned when a contest is complete. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The Contest&#39;s last modified datetime. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_scores_modified** | datetime | The datetime the contest scores were last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **winners** | [list[ContestWinners]](ContestWinners) | The Contest Winners | [optional] |
| **disqualified_agents** | [list[ContestDisqualifiedAgents]](ContestDisqualifiedAgents) | The Contest&#39;s disqualified agents, returned when a contest is complete | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 238.0.0_
