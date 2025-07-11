# PhoneStatus

## PhoneStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **operational_status** | str | The Operational Status of this phone | [optional] |
| **edges_status** | str | The status of the primary or secondary Edges assigned to the phone lines. | [optional] |
| **event_creation_time** | str | Event Creation Time represents an ISO-8601 string. For example: UTC, UTC+01:00, or Europe/London | [optional] |
| **provision** | [ProvisionInfo](ProvisionInfo) | Provision information for this phone | [optional] |
| **line_statuses** | [list[LineStatus]](LineStatus) | A list of LineStatus information for each of the lines of this phone | [optional] |
| **phone_assignment_to_edge_type** | str | The phone status&#39;s edge assignment type. | [optional] |
| **edge** | [DomainEntityRef](DomainEntityRef) | The URI of the edge that provided this status information. | [optional] |
| **self_uri** | str | The URI for this object. Deprecated. Do not use. | [optional] |



_PureCloudPlatformClientV2 233.0.0_
