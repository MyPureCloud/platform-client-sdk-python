# LearningAssignmentStep

## LearningAssignmentStep

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the learning assignment step | [optional] |
| **module_step** | [LearningModuleInformStep](LearningModuleInformStep) | The module step data for this step | [optional] |
| **structure** | [list[LearningAssignmentStepScoStructure]](LearningAssignmentStepScoStructure) | The structure for any SCO associated with this step | [optional] |
| **success_status** | str | The success status of this step | [optional] |
| **completion_status** | str | The completion status of the assignment step | [optional] |
| **completion_percentage** | float | The completion percentage for this step | [optional] |
| **percentage_score** | float | The percentage score for this step | [optional] |
| **shareable_content_object** | [LearningShareableContentObject](LearningShareableContentObject) | The SCO (Shareable Content Object) data | [optional] |
| **signed_cookie** | [LearningAssignmentStepSignedCookie](LearningAssignmentStepSignedCookie) | The signed cookie information needed to access the content of this step (if required) | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 223.0.0_
