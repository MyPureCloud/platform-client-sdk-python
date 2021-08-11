---
title: LearningAssignment
---
## LearningAssignment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **assessment** | [**LearningAssessment**](LearningAssessment.html) | The assessment associated with this assignment | [optional] |
| **created_by** | [**UserReference**](UserReference.html) | The user who created the assignment | [optional] |
| **date_created** | **datetime** | The date when the assignment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The user who modified the assignment | [optional] |
| **date_modified** | **datetime** | The date when the assignment was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **is_overdue** | **bool** | True if the assignment is overdue | [optional] |
| **percentage_score** | **float** | The user&#39;s percentage score for this assignment | [optional] |
| **is_rule** | **bool** | True if this assignment was created by a Rule | [optional] |
| **is_manual** | **bool** | True if this assignment was created manually | [optional] |
| **is_passed** | **bool** | True if the assessment was passed | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **state** | **str** | The Learning Assignment state | [optional] |
| **date_recommended_for_completion** | **datetime** | The recommended completion date of the assignment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | The version of Learning module assigned | [optional] |
| **module** | [**LearningModule**](LearningModule.html) | The Learning module object associated with this assignment | [optional] |
| **user** | [**UserReference**](UserReference.html) | The user to whom the assignment is assigned | [optional] |
| **assessment_form** | [**AssessmentForm**](AssessmentForm.html) | The assessment form associated with this assignment | [optional] |
{: class="table table-striped"}


