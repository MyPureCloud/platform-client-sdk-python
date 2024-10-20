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
| **time_zone** | str | The time zone for this CampaignSchedule. For example, Africa/Abidjan. | |
| **campaign** | [DomainEntityRef](DomainEntityRef) | The Campaign that this CampaignSchedule is for. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 214.0.0_
