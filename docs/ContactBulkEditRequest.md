# ContactBulkEditRequest

## ContactBulkEditRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **contact_list_filter_id** | str | Contact List Filter ID. | [optional] |
| **criteria** | [ContactBulkSearchCriteria](ContactBulkSearchCriteria) | Criteria to filter the contacts by. | [optional] |
| **contact_ids** | list[str] | Contact IDs to be bulk edited. | [optional] |
| **contact** | [DialerContact](DialerContact) | Contact object with details of fields used for patching. | [optional] |
| **generate_download_uri** | bool | Whether to do backup export as part of Bulk Operation or not. Default: true. | [optional] |



_PureCloudPlatformClientV2 230.0.0_
