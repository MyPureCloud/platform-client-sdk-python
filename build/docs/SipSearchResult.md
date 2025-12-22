# SipSearchResult

## SipSearchResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | int | Status of the search request | [optional] |
| **sid** | str | Session id associated to the search request | [optional] |
| **auth** | str | Auth token used for this search request | [optional] |
| **message** | str | Any messages returned from homer as part of the response | [optional] |
| **data** | [list[HomerRecord]](HomerRecord) | Homer search data that is returned | [optional] |
| **count** | int | Number of records returned | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
