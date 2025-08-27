# ContestsCreateRequest

## ContestsCreateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division** | [WritableDivision](WritableDivision) | The division for this performance profile associate to. Only set for DEFAULT profile. | [optional] |
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
| **profile_id** | str | The Contest profile | |
| **participant_ids** | list[str] | The Contest&#39;s participants | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 236.0.0_
