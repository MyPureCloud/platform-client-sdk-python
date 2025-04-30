# ContactListFilter

## ContactListFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the list. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [DomainEntityRef](DomainEntityRef) | The contact list the filter is based on. Required if sourceType is ContactList | [optional] |
| **contact_list_template** | [DomainEntityRef](DomainEntityRef) | The contact list template the filter is based on. Required if sourceType is ContactListTemplate | [optional] |
| **source_type** | str | The source type the filter is based on. | [optional] |
| **clauses** | [list[ContactListFilterClause]](ContactListFilterClause) | Groups of conditions to filter the contacts by. | [optional] |
| **filter_type** | str | How to join clauses together. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.0.0_
