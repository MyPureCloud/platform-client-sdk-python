# AggregatedExportSnapshotJobRequest

## AggregatedExportSnapshotJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **granularity** | str | Granularity of the exported data, defaults to day | [optional] |
| **time_zone** | str | The requested time zone of the exported data, in Olson format. Defaults to business unit time zone | [optional] |
| **delimiter** | str | The delimiter to use between fields in the export, defaults to comma | [optional] |
| **planning_group_ids** | list[str] | The IDs of the planning groups to include in the export, defaults to all planning groups in the business unit | [optional] |
| **date_start** | datetime | Start date-time of the export range in ISO-8601 format | [optional] |
| **date_end** | datetime | End date-time of the export range in ISO-8601 format | [optional] |
| **snapshot_id** | str | The ID of the snapshot to export | |



_PureCloudPlatformClientV2 265.0.0_
