# LimitChangeRequestDetails

## LimitChangeRequestDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **key** | str | Limit key to be overridden (see https://developer.mypurecloud.com/api/rest/v2/organization/limits.html#available_limits) | |
| **namespace** | str | Namespace the key belongs to (see https://developer.mypurecloud.com/api/rest/v2/organization/limits.html#available_limits) | |
| **requested_value** | float | Requested limit value for a given key | |
| **description** | str | Description of the need for the limit change request | |
| **support_case_url** | str | The support case url created by Care | |
| **status** | str | Current status of the limit change request | [optional] |
| **current_value** | float | Current limit value for a given key | [optional] |
| **date_created** | datetime | The date of the limit change request creation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status_history** | [list[StatusChange]](StatusChange) | List of statuses that a limit change request has gone through | [optional] |
| **date_completed** | datetime | The date of the limit change request completion (ChangeImplemented, Rejected, or RollbackImplemented. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **reject_reason** | str | The reason for rejecting the limit override request | [optional] |
| **approval_namespaces** | [list[ApprovalNamespace]](ApprovalNamespace) | The approval breakdown for this override request. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 210.0.0_
