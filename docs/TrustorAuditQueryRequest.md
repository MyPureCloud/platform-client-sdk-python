# TrustorAuditQueryRequest

## TrustorAuditQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **trustor_organization_id** | str | Limit returned audits to this trustor organizationId. | |
| **trustee_user_ids** | list[str] | Limit returned audits to these trustee userIds. | |
| **start_date** | datetime | Starting date/time for the audit search. ISO-8601 formatted date-time, UTC. | [optional] |
| **end_date** | datetime | Ending date/time for the audit search. ISO-8601 formatted date-time, UTC. | [optional] |
| **query_phrase** | str | Word or phrase to look for in audit bodies. | [optional] |
| **facets** | [list[Facet]](Facet) | Facet information to be returned with the query results. | [optional] |
| **filters** | [list[Filter]](Filter) | Additional custom filters to be applied to the query. | [optional] |



_PureCloudPlatformClientV2 238.0.0_
