# HistoricalImportDeleteFilesJobResponse

## HistoricalImportDeleteFilesJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The Job Id Request | [optional] |
| **state** | str | Property denoting the state of the remove request | [optional] |
| **entities** | [list[HistoricalDataDeleteEntity]](HistoricalDataDeleteEntity) | The request entities that got deleted | [optional] |
| **disallowed_entities** | [list[HistoricalDataDisallowedDeleteEntity]](HistoricalDataDisallowedDeleteEntity) | The request entities that were disallowed to be deleted | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 228.0.0_
