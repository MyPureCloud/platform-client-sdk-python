# ImportStatus

## ImportStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | current status of the import | |
| **total_records** | int | total number of records to be imported | |
| **completed_records** | int | number of records finished importing | |
| **percent_complete** | int | percentage of records finished importing | |
| **failure_reason** | str | if the import has failed, the reason for the failure | [optional] |
| **target_contact_list_ids** | list[str] | The contact list Ids for target contact lists. | [optional] |
| **list_name_prefix** | str | The prefix for the contact list name | [optional] |



_PureCloudPlatformClientV2 223.0.0_
