# DecisionTableImportRowMetrics

## DecisionTableImportRowMetrics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **total_rows** | int | Total number of rows in the import file (set after parsing completes) | [optional] |
| **rows_parsed** | int | Number of rows successfully parsed so far | [optional] |
| **row_parse_failed** | int | Number of rows that failed to parse | [optional] |
| **rows_created** | int | Number of rows successfully created so far | [optional] |
| **rows_updated** | int | Number of rows successfully updated so far | [optional] |
| **rows_deleted** | int | Number of rows deleted (Replace mode only) | [optional] |
| **row_create_failed** | int | Number of rows that failed during batch create | [optional] |
| **row_update_failed** | int | Number of rows that failed during batch update | [optional] |
| **row_delete_failed** | int | Number of rows that failed during delete | [optional] |



_PureCloudPlatformClientV2 261.0.0_
