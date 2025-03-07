# CampaignSchedule

## CampaignSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **intervals** | [list[ScheduleInterval]](ScheduleInterval) | A list of intervals during which to run the associated Campaign. | |
| **recurrences** | [list[Reoccurrence]](Reoccurrence) | Recurring schedules of the campaign | [optional] |
| **time_zone** | str | The time zone for this CampaignSchedule. Defaults to UTC if empty or not provided. See here for a list of valid time zones https://www.iana.org/time-zones | [optional] |
| **campaign** | [DivisionedDomainEntityRef](DivisionedDomainEntityRef) | The Campaign that this CampaignSchedule is for. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 223.0.0_
