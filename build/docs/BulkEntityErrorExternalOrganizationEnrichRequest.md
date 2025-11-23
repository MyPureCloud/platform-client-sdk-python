# BulkEntityErrorExternalOrganizationEnrichRequest

## BulkEntityErrorExternalOrganizationEnrichRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **code** | str | An error code for the specific error condition. | [optional] |
| **message** | str | A short error message. | [optional] |
| **status** | int | The HTTP Status Code for the error. | [optional] |
| **retryable** | bool | Whether this particular error should be retried. | [optional] |
| **details** | [list[BulkErrorDetail]](BulkErrorDetail) | Additional error details for specific fields. | [optional] |
| **entity** | [ExternalOrganizationEnrichRequest](ExternalOrganizationEnrichRequest) | The entity body specified in the Bulk request operation that caused this error. | [optional] |



_PureCloudPlatformClientV2 244.0.0_
