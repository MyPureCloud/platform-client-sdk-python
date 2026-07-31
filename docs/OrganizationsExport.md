# OrganizationsExport

## OrganizationsExport

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division_ids** | list[str] | Division IDs of entities | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | The user that created this request | [optional] |
| **date_created** | datetime | When the request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completion** | datetime | When the request reached a terminal state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | The status of the request | [optional] |
| **download_url** | str | The location where the results of the request can be retrieved | [optional] |
| **result_row_count** | int | Number of rows returned by the export query | [optional] |
| **query_conditions** | [OrganizationsExportQueryConditions](OrganizationsExportQueryConditions) | Query conditions to apply on export | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 263.0.0_
