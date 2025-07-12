# ContactsExport

## ContactsExport

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division_ids** | list[str] | Division IDs of entities | [optional] |
| **query_conditions** | [ContactsExportQueryConditions](ContactsExportQueryConditions) | Query conditions to apply on export | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | The user that created this request | [optional] |
| **date_created** | datetime | When the request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | The status of the request | [optional] |
| **download_url** | str | The location where the results of the request can be retrieved | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
