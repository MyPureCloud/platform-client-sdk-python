# LearningModulePreviewGetResponseStep

## LearningModulePreviewGetResponseStep

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The id of the step | [optional] |
| **module_step** | [LearningModuleInformStep](LearningModuleInformStep) | The module step data for this step | [optional] |
| **structure** | [list[LearningModulePreviewGetScoStructure]](LearningModulePreviewGetScoStructure) | The structure for any SCO associated with this step | [optional] |
| **success_status** | str | The success status of this step | [optional] |
| **completion_status** | str | The completion status of the assignment step | [optional] |
| **completion_percentage** | float | The completion percentage for this step | [optional] |
| **percentage_score** | float | The percentage score for this step | [optional] |
| **signed_cookie** | [LearningAssignmentStepSignedCookie](LearningAssignmentStepSignedCookie) | The signed cookie information needed to access the content of this step (if required) | [optional] |



_PureCloudPlatformClientV2 222.0.0_
