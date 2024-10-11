# LearningModuleRequest

## LearningModuleRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of learning module | |
| **description** | str | The description of learning module | [optional] |
| **completion_time_in_days** | int | The completion time of learning module in days | |
| **inform_steps** | [list[LearningModuleInformStepRequest]](LearningModuleInformStepRequest) | The list of inform steps in a learning module | [optional] |
| **type** | str | The type for the learning module. Informational, AssessedContent and Assessment are deprecated | [optional] |
| **assessment_form** | [AssessmentForm](AssessmentForm) | The assessment form for learning module | [optional] |
| **cover_art** | [LearningModuleCoverArtRequest](LearningModuleCoverArtRequest) | The cover art for the learning module | [optional] |
| **length_in_minutes** | int | The recommended time in minutes to complete the module | [optional] |
| **excluded_from_catalog** | bool | If true, learning module is excluded when retrieving modules for manual assignment | [optional] |
| **external_id** | str | The external ID of the learning module. Maximum length: 50 characters. | [optional] |
| **enforce_content_order** | bool | If true, learning module content should be viewed one by one in order | [optional] |
| **review_assessment_results** | [ReviewAssessmentResults](ReviewAssessmentResults) | Allows to view Assessment results in detail | [optional] |



_PureCloudPlatformClientV2 213.0.0_
