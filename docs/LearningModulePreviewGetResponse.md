# LearningModulePreviewGetResponse

## LearningModulePreviewGetResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of learning module | |
| **description** | str | The description of learning module | [optional] |
| **cover_art** | [LearningModuleCoverArtResponse](LearningModuleCoverArtResponse) | The cover art for the learning module | [optional] |
| **enforce_content_order** | bool | If true, learning module content should be viewed one by one in order | [optional] |
| **review_assessment_results** | [ReviewAssessmentResults](ReviewAssessmentResults) | Allows to view Assessment results in detail | [optional] |
| **assessment_form** | [AssessmentForm](AssessmentForm) | The assessment form for learning module | [optional] |
| **assignment** | [LearningModulePreviewGetResponseAssignment](LearningModulePreviewGetResponseAssignment) | the assignment preview | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 241.0.0_
