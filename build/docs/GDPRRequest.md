# GDPRRequest

## GDPRRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | The user that created this request | |
| **replacement_terms** | [list[ReplacementTerm]](ReplacementTerm) | The replacement terms for the provided search terms, in the case of a GDPR_UPDATE request | [optional] |
| **request_type** | str | The type of GDPR request | |
| **created_date** | datetime | When the request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **status** | str | The status of the request | |
| **subject** | [GDPRSubject](GDPRSubject) | The subject of the GDPR request | |
| **results_url** | str | The location where the results of the request can be retrieved | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.0.0_
