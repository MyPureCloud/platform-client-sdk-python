# DialerCampaignScheduleConfigChangeCampaignSchedule

## DialerCampaignScheduleConfigChangeCampaignSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **intervals** | [list[DialerCampaignScheduleConfigChangeScheduleInterval]](DialerCampaignScheduleConfigChangeScheduleInterval) | a list of start and end times | [optional] |
| **recurrences** | [list[DialerCampaignScheduleConfigChangeScheduleRecurrence]](DialerCampaignScheduleConfigChangeScheduleRecurrence) | a list of recurrences for a schedule | [optional] |
| **time_zone** | str | time zone identifier to be applied to the intervals; for example Africa/Abidjan | [optional] |
| **campaign** | [DialerCampaignScheduleConfigChangeUriReference](DialerCampaignScheduleConfigChangeUriReference) |  | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 217.0.0_