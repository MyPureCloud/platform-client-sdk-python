# OutboundFaxStatus

## OutboundFaxStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **initiating_user** | [AddressableEntityRef](AddressableEntityRef) | The user who sent the fax. | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **audit_transaction_id** | str |  | [optional] |
| **expiration_time** | int |  | [optional] |
| **status_code** | str | Lifecycle status of the outbound fax send (e.g. UPLOADING, TRANSMITTING, COMPLETE, TERMINATED). | [optional] |
| **result** | str | Transmission result of the fax. Does NOT indicate successful arrival to a workspace&#39;s inbox. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 265.0.0_
