---
title: PolicyActions
---
## PolicyActions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **retain_recording** | **bool** | true to retain the recording associated with the conversation. Default = true | [optional] |
| **delete_recording** | **bool** | true to delete the recording associated with the conversation. If retainRecording = true, this will be ignored. Default = false | [optional] |
| **always_delete** | **bool** | true to delete the recording associated with the conversation regardless of the values of retainRecording or deleteRecording. Default = false | [optional] |
| **assign_evaluations** | [**list[EvaluationAssignment]**](EvaluationAssignment.html) |  | [optional] |
| **assign_metered_evaluations** | [**list[MeteredEvaluationAssignment]**](MeteredEvaluationAssignment.html) |  | [optional] |
| **assign_metered_assignment_by_agent** | [**list[MeteredAssignmentByAgent]**](MeteredAssignmentByAgent.html) |  | [optional] |
| **assign_calibrations** | [**list[CalibrationAssignment]**](CalibrationAssignment.html) |  | [optional] |
| **assign_surveys** | [**list[SurveyAssignment]**](SurveyAssignment.html) |  | [optional] |
| **retention_duration** | [**RetentionDuration**](RetentionDuration.html) |  | [optional] |
| **initiate_screen_recording** | [**InitiateScreenRecording**](InitiateScreenRecording.html) |  | [optional] |
| **media_transcriptions** | [**list[MediaTranscription]**](MediaTranscription.html) |  | [optional] |
| **integration_export** | [**IntegrationExport**](IntegrationExport.html) | Policy action for exporting recordings using an integration to 3rd party s3. | [optional] |
{: class="table table-striped"}


