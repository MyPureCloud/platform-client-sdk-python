---
title: PolicyActions
---
## PolicyActions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **retain_recording** | **bool** | true to retain the recording associated with the conversation. Default &#x3D; true | [optional] |
| **delete_recording** | **bool** | true to delete the recording associated with the conversation. If retainRecording &#x3D; true, this will be ignored. Default &#x3D; false | [optional] |
| **always_delete** | **bool** | true to delete the recording associated with the conversation regardless of the values of retainRecording or deleteRecording. Default &#x3D; false | [optional] |
| **assign_evaluations** | [**list[EvaluationAssignment]**](EvaluationAssignment.html) |  | [optional] |
| **assign_metered_evaluations** | [**list[MeteredEvaluationAssignment]**](MeteredEvaluationAssignment.html) |  | [optional] |
| **assign_calibrations** | [**list[CalibrationAssignment]**](CalibrationAssignment.html) |  | [optional] |
| **retention_duration** | [**RetentionDuration**](RetentionDuration.html) |  | [optional] |
| **initiate_screen_recording** | [**InitiateScreenRecording**](InitiateScreenRecording.html) |  | [optional] |
{: class="table table-striped"}


