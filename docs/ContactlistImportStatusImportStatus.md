# ContactlistImportStatusImportStatus

## ContactlistImportStatusImportStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **import_state** | str | current status of the import | [optional] |
| **total_records** | int | total number of records to be imported | [optional] |
| **completed_records** | int | number of records finished importing | [optional] |
| **percentage_complete** | int | percentage of records finished importing | [optional] |
| **failure_reason** | str | if the import has failed, the reason for the failure | [optional] |
| **target_contact_list_ids** | list[str] | The ids for target contact lists | [optional] |
| **list_name_prefix** | str | The prefix used for target contact list names | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **get_additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 237.0.0_
