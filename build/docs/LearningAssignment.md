# LearningAssignment

## LearningAssignment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **assessment** | [LearningAssessment](LearningAssessment) | The assessment associated with this assignment | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the assignment | [optional] |
| **date_created** | datetime | The date when the assignment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who modified the assignment | [optional] |
| **date_modified** | datetime | The date when the assignment was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **is_overdue** | bool | True if the assignment is overdue | [optional] |
| **percentage_score** | float | The user&#39;s percentage score for this assignment | [optional] |
| **assessment_percentage_score** | float | The user&#39;s percentage score for this assignment&#39;s assessment | [optional] |
| **is_rule** | bool | True if this assignment was created by a Rule | [optional] |
| **is_manual** | bool | True if this assignment was created manually | [optional] |
| **is_passed** | bool | True if the assessment was passed | [optional] |
| **is_latest** | bool | True if the assignment is based on latest module | [optional] |
| **assessment_completion_percentage** | float | The assessment completion percentage of assignment | [optional] |
| **completion_percentage** | float | The overall completion percentage of assignment | [optional] |
| **steps** | [list[LearningAssignmentStep]](LearningAssignmentStep) | List of assignment steps | [optional] |
| **next_step** | [LearningAssignmentStep](LearningAssignmentStep) | The next assignment step | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **state** | str | The Learning Assignment state | [optional] |
| **date_recommended_for_completion** | datetime | The recommended completion date of the assignment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | The version of Learning module assigned | [optional] |
| **module** | [LearningModule](LearningModule) | The Learning module object associated with this assignment | [optional] |
| **user** | [UserReference](UserReference) | The user to whom the assignment is assigned | [optional] |
| **assessment_form** | [AssessmentForm](AssessmentForm) | The assessment form associated with this assignment | [optional] |
| **length_in_minutes** | int | The length in minutes of the assignment | [optional] |



_PureCloudPlatformClientV2 213.0.0_
