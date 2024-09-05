# Miner

## Miner

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Chat Corpus Name. | |
| **language** | str | Language Localization code. | [optional] |
| **miner_type** | str | Type of the miner, intent or topic. | [optional] |
| **date_created** | datetime | Date when the miner was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | Status of the miner. | [optional] |
| **conversations_date_range_start** | date | Date from which the conversations need to be taken for mining. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **conversations_date_range_end** | date | Date till which the conversations need to be taken for mining. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_completed** | datetime | Date when the mining process was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **message** | str | Mining message if present. | [optional] |
| **error_info** | [MinerErrorInfo](MinerErrorInfo) | Error Information | [optional] |
| **warning_info** | [MinerErrorInfo](MinerErrorInfo) | Warning Information | [optional] |
| **conversation_data_uploaded** | bool | Flag to indicate whether data file to be mined was uploaded. | [optional] |
| **media_type** | str | Media type for filtering conversations. | [optional] |
| **participant_type** | str | Type of the participant, either agent, customer or both. | [optional] |
| **queue_ids** | list[str] | List of queue IDs for filtering conversations. | [optional] |
| **date_triggered** | datetime | Date when the miner started execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the miner was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **latest_draft_version** | [Draft](Draft) | Latest draft details of the miner. | [optional] |
| **conversations_fetched_count** | int | Number of conversations/transcripts fetched. | [optional] |
| **conversations_valid_count** | int | Number of conversations/recordings/transcripts that were found valid for mining purposes. | [optional] |
| **getmined_item_count** | int | Number of intents or topics based on the miner type. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 210.0.0_
