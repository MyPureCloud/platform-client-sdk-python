# Policy

## Policy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **modified_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **order** | int |  | [optional] |
| **description** | str |  | [optional] |
| **enabled** | bool |  | [optional] |
| **media_policies** | [MediaPolicies](MediaPolicies) | Conditions and actions per media type | [optional] |
| **conditions** | [PolicyConditions](PolicyConditions) | Conditions | [optional] |
| **actions** | [PolicyActions](PolicyActions) | Actions | [optional] |
| **policy_errors** | [PolicyErrors](PolicyErrors) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_
