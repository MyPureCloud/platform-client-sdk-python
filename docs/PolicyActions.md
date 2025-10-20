# PolicyActions

## PolicyActions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **retain_recording** | bool | true to retain the recording associated with the conversation. Default &#x3D; true | [optional] |
| **delete_recording** | bool | true to delete the recording associated with the conversation. If retainRecording &#x3D; true, this will be ignored. Default &#x3D; false | [optional] |
| **always_delete** | bool | true to delete the recording associated with the conversation regardless of the values of retainRecording or deleteRecording. Default &#x3D; false | [optional] |
| **assign_evaluations** | [list[EvaluationAssignment]](EvaluationAssignment) |  | [optional] |
| **assign_metered_evaluations** | [list[MeteredEvaluationAssignment]](MeteredEvaluationAssignment) |  | [optional] |
| **assign_metered_assignment_by_agent** | [list[MeteredAssignmentByAgent]](MeteredAssignmentByAgent) |  | [optional] |
| **assign_calibrations** | [list[CalibrationAssignment]](CalibrationAssignment) |  | [optional] |
| **assign_surveys** | [list[SurveyAssignment]](SurveyAssignment) |  | [optional] |
| **retention_duration** | [RetentionDuration](RetentionDuration) |  | [optional] |
| **initiate_screen_recording** | [InitiateScreenRecording](InitiateScreenRecording) |  | [optional] |
| **media_transcriptions** | [list[MediaTranscription]](MediaTranscription) |  | [optional] |
| **integration_export** | [IntegrationExport](IntegrationExport) | Policy action for exporting recordings using an integration to 3rd party s3. | [optional] |



_PureCloudPlatformClientV2 241.0.0_
