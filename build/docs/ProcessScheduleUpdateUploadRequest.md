# ProcessScheduleUpdateUploadRequest

## ProcessScheduleUpdateUploadRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **upload_key** | str | The uploadKey provided by the request to get an upload URL | |
| **team_ids** | list[str] | The list of teams to which the users being modified belong. Only required if the requesting user has conditional permission to wfm:schedule:edit | [optional] |
| **management_unit_ids_for_added_team_users** | list[str] | The set of muIds to which agents belong if agents are being newly added to the schedule, if the requesting user has conditional permission to wfm:schedule:edit | [optional] |



_PureCloudPlatformClientV2 222.0.0_
