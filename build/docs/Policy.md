---
title: Policy
---
## Policy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **modified_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **created_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **order** | **int** |  | [optional] |
| **description** | **str** |  | [optional] |
| **enabled** | **bool** |  | [optional] |
| **media_policies** | [**MediaPolicies**](MediaPolicies.html) | Conditions and actions per media type | [optional] |
| **conditions** | [**PolicyConditions**](PolicyConditions.html) | Conditions | [optional] |
| **actions** | [**PolicyActions**](PolicyActions.html) | Actions | [optional] |
| **policy_errors** | [**PolicyErrors**](PolicyErrors.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


