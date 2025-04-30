# ContactEnrichRequest

## ContactEnrichRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A user-specified tracker string, only useful in the Bulk-Enrich API. If one Bulk-Enrich operation in a request fails, the requested operation will be repeated in the Bulk API response, including this id field, allowing associating of request and response operations. | [optional] |
| **division** | [WritableStarrableDivision](WritableStarrableDivision) | The division to which this entity belongs. | [optional] |
| **matching_identifiers** | [list[ContactIdentifier]](ContactIdentifier) | An ordered list of one or more Identifiers which might each be claimed by a Contact. &#x60;action&#x60; describes what to do with any possibly matching Contacts. Identifier lookups will occur in the order specified here. | |
| **action** | str | The action that should be taken based on any Contacts found by &#x60;matchingIdentifiers&#x60;. | |
| **contact** | [ExternalContact](ExternalContact) | Data to be added, either as an update to an existing Contact or the body of a new Contact. Omitting a field in this contract means that it will be treated as null in the &#x60;fieldRules&#x60; logic. | [optional] |
| **field_rules** | [EnrichFieldRules](EnrichFieldRules) | Logic describing how to combine data from the submitted request with data found in the database. | [optional] |
| **options** | [ContactEnrichOptions](ContactEnrichOptions) | Additional options modifying the behavior of the API operation. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
