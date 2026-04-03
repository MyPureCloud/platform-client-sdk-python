# V3SourceCreateRequest

## V3SourceCreateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the source. | |
| **type** | str | The type of the source. Required if connectionId is not specified, inherits the connection type otherwise. | [optional] |
| **connection_id** | str | The id of the connection related to the source. Required if type is Sharepoint. | [optional] |
| **trigger_type** | str | The trigger type of the source. Default is Manual. | [optional] |
| **schedule_settings** | [V3SourceScheduleSettings](V3SourceScheduleSettings) | Settings that determine when the source starts a sync. Required if triggerType is Scheduled. | [optional] |
| **filters** | [V3SourceFilter](V3SourceFilter) | Filters that determine what documents are synced. | [optional] |



_PureCloudPlatformClientV2 255.0.0_
